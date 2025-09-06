#!/usr/bin/env python3
import argparse
import sys
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# We will try to import optional libs; if missing, we handle gracefully.
try:
    import yfinance as yf
except Exception:
    yf = None

try:
    import mplfinance as mpf
except Exception:
    mpf = None

def load_data(ticker: str, start: str, end: str, csv: str | None = None) -> pd.DataFrame:
    """
    Returns a DataFrame indexed by Date with columns: Open, High, Low, Close, Volume.
    Priority: CSV (if provided) -> yfinance (if available) -> synthetic fallback.
    """
    # 1) CSV path provided by user
    if csv:
        df = pd.read_csv(csv, parse_dates=['Date'])
        df = df.set_index('Date').sort_index()
        # Ensure required columns exist
        req = {'Open','High','Low','Close','Volume'}
        if not req.issubset(set(df.columns)):
            raise ValueError(f"CSV must contain columns: {sorted(req)}")
        return df.loc[(df.index >= pd.to_datetime(start)) & (df.index <= pd.to_datetime(end))]

    # 2) Try yfinance
    if yf is not None and ticker:
        try:
            data = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)
            if isinstance(data, pd.DataFrame) and not data.empty:
                # Standardize column names if needed
                cols = {c.lower(): c for c in data.columns}
                # Ensure required
                for req_col in ["Open","High","Low","Close","Volume"]:
                    if req_col not in data.columns:
                        # try case-insensitive
                        cand = [c for c in data.columns if c.lower()==req_col.lower()]
                        if cand:
                            data[req_col] = data[cand[0]]
                        else:
                            raise ValueError("Downloaded data missing required columns.")
                df = data[["Open","High","Low","Close","Volume"]].copy()
                df.index.name = "Date"
                return df
        except Exception as e:
            print(f"[warn] yfinance download failed: {e}", file=sys.stderr)

    # 3) Synthetic fallback (for demo without internet)
    rng = pd.date_range(start=start, end=end, freq="B")  # business days
    if len(rng) == 0:
        rng = pd.date_range(end=pd.Timestamp.today(), periods=100, freq="B")
    # Random walk
    np.random.seed(42)
    price = 100 + np.cumsum(np.random.normal(0, 1, size=len(rng)))
    close = pd.Series(price, index=rng)
    open_ = close.shift(1, fill_value=close.iloc[0])
    high = pd.concat([open_, close], axis=1).max(axis=1) + np.random.rand(len(rng))*0.6
    low = pd.concat([open_, close], axis=1).min(axis=1) - np.random.rand(len(rng))*0.6
    volume = (np.random.randint(100_000, 500_000, size=len(rng))).astype(float)
    df = pd.DataFrame({"Open": open_.values,
                       "High": high.values,
                       "Low": low.values,
                       "Close": close.values,
                       "Volume": volume}, index=rng)
    df.index.name = "Date"
    print("[info] Using synthetic data (no CSV given and download unavailable).")
    return df

def plot_line(df: pd.DataFrame, ticker: str, outdir: Path) -> Path:
    """
    Plots a simple Close price line chart.
    """
    outdir.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df["Close"], label="Close")  # Do not set colors (per requirement)
    ax.set_title(f"{ticker} - Close Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    fig.autofmt_xdate()
    outfile = outdir / f"{ticker}_line.png"
    fig.savefig(outfile, bbox_inches="tight", dpi=150)
    plt.close(fig)
    return outfile

def plot_candlestick(df: pd.DataFrame, ticker: str, outdir: Path) -> Path:
    """
    Plots a candlestick chart with volume using mplfinance if available;
    otherwise falls back to a simple OHLC lines plot with matplotlib.
    """
    outdir.mkdir(parents=True, exist_ok=True)
    outfile = outdir / f"{ticker}_candlestick.png"

    if mpf is not None:
        # mplfinance expects columns Open, High, Low, Close and index as datetime
        mpf.plot(df, type='candle', volume=True, style='classic', savefig=dict(fname=str(outfile), dpi=150, bbox_inches="tight"))
        return outfile

    # Fallback simple OHLC line visualization (not true candles).
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df["Open"], label="Open")
    ax.plot(df.index, df["High"], label="High")
    ax.plot(df.index, df["Low"], label="Low")
    ax.plot(df.index, df["Close"], label="Close")
    ax.set_title(f"{ticker} - OHLC (mplfinance not installed)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    fig.autofmt_xdate()
    fig.savefig(outfile, bbox_inches="tight", dpi=150)
    plt.close(fig)
    return outfile

def main():
    parser = argparse.ArgumentParser(description="Plot stock price charts (line & candlestick).")
    parser.add_argument("--ticker", type=str, default="AAPL", help="Ticker symbol (e.g., AAPL, ASELS.IS, GARAN.IS)")
    parser.add_argument("--start", type=str, default="2024-01-01", help="Start date YYYY-MM-DD")
    parser.add_argument("--end", type=str, default=None, help="End date YYYY-MM-DD (default: today)")
    parser.add_argument("--csv", type=str, default=None, help="Path to CSV with Date,Open,High,Low,Close,Volume")
    parser.add_argument("--outdir", type=str, default="./charts", help="Output directory for images")
    args = parser.parse_args()

    end = args.end or pd.Timestamp.today().strftime("%Y-%m-%d")
    df = load_data(args.ticker, args.start, end, csv=args.csv).copy()
    if df.empty:
        print("No data to plot. Exiting.", file=sys.stderr)
        sys.exit(2)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # Save a copy of the data used
    csv_out = outdir / f"{args.ticker}_prices.csv"
    df.to_csv(csv_out, index=True)

    line_path = plot_line(df, args.ticker, outdir)
    candle_path = plot_candlestick(df, args.ticker, outdir)

    print(f"Saved data: {csv_out}")
    print(f"Saved line chart: {line_path}")
    print(f"Saved candlestick chart: {candle_path}")

if __name__ == "__main__":
    main()
