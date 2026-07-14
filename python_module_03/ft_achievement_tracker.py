import random
# random Python'un rastgele sayı üretme ve rastgele seçim yapma gibi işlemler sağlayan yerleşik random modülünü programınıza dahil eder..

ACHIEVEMENTS = [
    "First Steps",
    "Speed Runner",
    "Treasure Hunter",
    "Master Explorer",
    "Collector Supreme",
    "Boss Slayer",
    "World Savior",
    "Crafting Genius",
    "Strategist",
    "Survivor",
    "Untouchable",
    "Sharp Mind",
    "Hidden Path Finder",
    "Unstoppable",
]

def generate_player_achievements():
    count = random.randint(5,10) # random.randint() ile rastgele bir tam sayı üretebilirsiniz.
    return set(random.sample(ACHIEVEMENTS, count)) # random.sample() ile bir listeden rastgele elemanlar seçebilirsiniz.
    # set: bir küme (set) oluşturan yerleşik yapıcı fonksiyondur. Kümeler sırasızdır ve her elemanı benzersizdir; aynı değerden birden fazla bulunamaz.
    # Örneğin set([1, 2, 2, 3]) sonucu {1, 2, 3} olur. Ayrıca set() argümansız çağrıldığında boş bir küme oluşturur.

def main():
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": generate_player_achievements(),
        "Bob": generate_player_achievements(),
        "Charlie": generate_player_achievements(),
        "Dylan": generate_player_achievements(),
    }

    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    all_achievements = set()
    for ach in players.values():
        all_achievements = all_achievements.union(ach)
        # Bu ifade, ach kümesindeki tüm elemanları all_achievements kümesine ekleyip sonucu tekrar all_achievements değişkenine atar.
        #  Yani iki kümenin birleşimini (tekrarsız olarak) alır. Örneğin {1, 2}.union({2, 3}) sonucu {1, 2, 3} olur.
        # .union kümelerde birleşim işlemidir. İki veya daha fazla kümedeki tüm farklı elemanları tek bir yeni kümede toplar.
        #  Örneğin {1, 2}.union({2, 3}) sonucu {1, 2, 3} olur.
    
    common = all_achievements.copy()
    for ach in players.values():
        common = common.intersection(ach)
        # intersection(ach), bir kümenin ach kümesiyle ortak olan elemanlarını içeren yeni bir küme döndürür.
        #  Yani iki kümenin kesişimini alır. Örneğin {1, 2, 3}.intersection({2, 3, 4}) sonucu {2, 3} olur.

    print(f"\nAll distinct achievements: {all_achievements}")
    print(f"Common achievements: {common}")

    for name, ach in players.items():
        others = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = others.union(other_ach)
        print(f"Only {name} nas: {ach.difference(others)}") # difference() metodu, bir kümenin (set) diğer kümede bulunan elemanlarını
        # çıkararak yalnızca ilk kümeye özgü elemanlardan oluşan yeni bir küme döndürür.
    full_set = set(ACHIEVEMENTS)
    for name, ach in players.items():
        print(f"{name} is missing: {full_set.difference(ach)}")

if __name__ == "__main__":
    main()

