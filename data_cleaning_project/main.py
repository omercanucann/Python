from src.data_loader import load_csv, save_csv
from src.data_cleaner import normalize_column_names, convert_types, handle_missing_values, remove_duplicates
from src.validators import check_unique, check_missing, check_numeric_ranges
from src import config

def main():
    print("Veri Yükleniyor...")
    df = load_csv(config.RAW_DATA_PATH)

    print("Temizleme Başlıyor...")
    df = normalize_column_names(df)
    df = convert_types(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    print("Validasyon yapılıyor...")
    if not check_unique(df, config.ID_COLUMN):
        print("Transaction ID Benzersiz Değil!!!")
    
    print("Eksik veri kontrol ediliyor...")
    print(check_missing(df))

    print("Sayısal alan kontrolleri:")
    print(check_numeric_ranges(df))

    print("Temizlenmiş veri kayıt ediliyor...")
    save_csv(df, config.PROCESSED_DATA_PATH)
    print("Temizleme Tamamlandı")

if __name__ == "__main__":
        main()