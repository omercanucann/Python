def check_unique(df, column):
    return df[column].is_unique

def check_missing(df):
    return df.isnull().sum()

def check_numeric_ranges(df):
    problems = {}
    if "quantity" in df.columns:
        problems["quantity"] = df[df["quantity"] <= 0]
    if "price_per_unit" in df.columns:
        problems["price_per_unit"] = df[df["price_per_unit"] <= 0]
    return problems
