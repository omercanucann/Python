from abc import ABC, abstractmethod
# soyut (abstract) sınıflar oluşturmak ve alt sınıfların belirli metotları mutlaka yazmasını zorunlu kılmak için kullanılır.
from typing import Any
# bir fonksiyonun veya değişkenin her türden veri (int, str, list, dict vb.) kabul edebileceğini belirtmek için kullanılan Any tipini içe aktarır.

class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._rank = 0

    @abstractmethod # bir metodun alt sınıflar tarafından mutlaka uygulanmasını zorunlu kılan dekoratördür.
    def validate(self, data: Any) -> bool:
        pass
    # @abstractmethod, "Bu metodu ben yazmıyorum, bunu miras alan sınıflar yazmak zorunda." anlamına gelir.

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]: # fonksiyonun bir tuple döndüreceğini ve bu tuple'ın ilk elemanının int, ikinci elemanının str olacağını gösteren 
        # tip ipucudur (type hint).
        if not self._data:
            raise Exception("No data available") # raise, programda bir hata (exception) oluşturup fırlatmak için kullanılan anahtar kelimedir.
        
        value = self._data.pop(0) # listenin ilk elemanını çıkarır
        rank = self._rank
        self._rank += 1
        return (rank, value)
    
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)): # data değişkeninin int veya float türünde olup olmadığını kontrol eder.
            return True
        
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data) # data listesindeki tüm elemanların int veya float olup olmadığını kontrol eder.
    
    def ingest(self, data: int | float | list[int | float]) -> None: # data parametresinin int, float veya bunlardan oluşan bir liste olabileceğini
        # ve fonksiyonun herhangi bir değer döndürmeyeceğini gösteren tip ipucudur.
        if not self.validate(data): # aynı nesnenin (self) içindeki validate metodunu çağırıp data verisinin geçerli olup olmadığını kontrol ede
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for value in data:
                self._data.append(str(value))
        else:
            self._data.append(str(data))
        
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False
    
    def ingest(self, data: str | list[str]) -> None: # data parametresinin ya tek bir str ya da str'lerden oluşan bir liste olabileceğini belirtir.
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            self._data.extend(data) # data listesindeki bütün elemanları tek tek self._data listesine ekler.
        else:
            self._data.append(data) # data değişkeninin tamamını self._data listesinin sonuna tek bir eleman olarak ekler.

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_dict(d):
            return (
                isinstance(d, dict)
                and all(isinstance(k, str) for k in d.keys())
                and all(isinstance(v, str) for v in d.values())
            ) # "d bir sözlük mü ve bu sözlükteki
            # tüm anahtarlar ile tüm değerler str tipinde mi?" hepsi için tek tek kontrol eder.
        if valid_dict(data):
            True
        if isinstance(data, list):
            return(all(valid_dict(x) for x in data))
        
        return False
    
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        
        if isinstance(data, list):
            logs = data
        else:
            logs = [data]
        
        for log in logs:
            level = log.get("log_level", "")
            message = log.get("log_message", "")
            self._data.append(f"{level}: {message}")
        # logs listesindeki her log sözlüğünü alır, içindeki log_level ve log_message değerlerini okuyup "SEVİYE: Mesaj" formatına çevirerek self._data listesine ekler.
        # .get() bir sözlükten (dict) belirtilen anahtarın değerini güvenli şekilde almak için kullanılır; anahtar yoksa hata vermek yerine varsayılan bir değer döndürür.


print("=== Code Nexus - Data Processor ===\n")

num = NumericProcessor()
print("Testing Numeric Processor...")
print("Trying to validate input '42':", num.validate(42))
print("Trying to validate input 'Hello':", num.validate("Hello"))

print("Test invalid ingestion of string 'foo' without prior validation:")

try:
    num.ingest("foo")
except Exception as e:
    print("Got exception:", e)

print("Processing data:", [1, 2, 3, 4, 5])
num.ingest([1, 2, 3, 4, 5])

print("Extracting 3 values...")
for _ in range(3):
    rank, value = num.output()
    print(f"Numeric value {rank}: {value}")

print()
text = TextProcessor()

print("Testing Text Processor...")
print("Trying to validate input '42':", text.validate(42))

print("Processing data:", ["Hello", "Nexus", "World"])
text.ingest(["Hello", "Nexus", "World"])

print("Extracting 1 value...")
rank, value = text.output()
print(f"Text value {rank}: {value}")

print()

log = LogProcessor()

print("Testing Log Processor...")
print("Trying to validate input 'Hello':", log.validate("Hello"))

logs = [
    {
        "log_level": "NOTICE",
        "log_message": "Connection to server"
    },
    {
        "log_level": "ERROR",
        "log_message": "Unauthorized access!!"
    }
]

print("Processing data:", logs)
log.ingest(logs)

print("Extracting 2 values...")
for _ in range(2):
    rank, value = log.output()
    print(f"Log entry {rank}: {value}")