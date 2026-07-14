from typing import Generator # tip belirtmek (type hint) için kullanılır.
# Programın çalışması için zorunlu değildir, ancak kodun daha okunabilir olmasını sağlar ve IDE'lerin (VS Code, PyCharm vb.) hata yakalamasına yardımcı olur.
import random

def gen_event() -> Generator[tuple[str, str], None, None]: # -> işareti fonksiyonun ne döndüreceğini belirtir. fonksiyon normal bir değer değil, generator döndürüyor.
    # tuple[str, str] Generator'ın ürettiği (yield ettiği) değerlerin tipidir. Bu bir tuple'dır ve içinde iki tane string vardır.
    # İlk None generator'ın send() metoduyla dışarıdan veri almayacağını belirtir. Son None Generator bittiğinde return ile özel bir değer döndürmeyeceğini belirtir.
    """Endless generator that produces random (player, action) events.""" # bir docstring'dir. Python'da docstring, fonksiyonun,
    # sınıfın veya dosyanın ne yaptığını açıklamak için kullanılan özel bir açıklama metnidir.
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    while True:
        yield (random.choice(players), random.choice(actions)) # yield: Python'da generator (üreteç) oluşturmak için kullanılan bir anahtar kelimedir.
        # Normal bir fonksiyon return ile bir kez değer döndürür ve biter. yield ise değeri döndürür ama fonksiyonu bitirmez.
        #  Kaldığı yerden devam edebilmesi için durumunu hafızasında tutar.
def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    """Randomly removes one event from the list and yields ituntil the list becomes empty."""
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)

def main():
    print("=== Game Data Stream Processor ===")
    stream = gen_event()

    for i in range(1000):
        player, action = next(stream) # next(stream) stream, gen_event() fonksiyonundan oluşturulan generator'dır.
        # player, action = ...Python'da bir tuple'ı değişkenlere ayırmaya unpacking denir.
        print(f"Event {i}: Player {player} did action {action}")
    event_list = [next(stream) for _ in range(10)] # Python'da list comprehension (liste üretme) kullanıyor.
    # stream generator'ından next() ile 10 tane event alıp bunları bir listeye kaydeder.
    print(f"\nBuilt list of events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")

if __name__ == "__main__":
    main()