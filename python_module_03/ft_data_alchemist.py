import random

print("=== Game Data Alchemist ===")

players = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
]

print("Initial list of players:", players)


capitalized_players = [player.capitalize() for player in players] # players listesindeki her ismin ilk harfini büyütüp yeni bir liste oluşturan bir list comprehension'dır.
# comprehension: Python'da mevcut bir koleksiyondan (liste, sözlük veya küme) tek satırda yeni bir koleksiyon oluşturmayı sağlayan kısa ve okunabilir bir yazım şeklidir.

print("New list with all names capitalized:", capitalized_players)

capitalized_only = [player for player in players if player[0].isupper()] # players listesindeki sadece ilk harfi zaten büyük olan isimleri seçip yeni bir liste
# oluşturan bir list comprehension'dır.

print("New list of capitalized names only: ", capitalized_only)

scores = {
    player: random.randint(0, 1000) # Bir sözlükte (dictionary) player'ı anahtar (key), random.randint(0, 1000) ile üretilen rastgele
     # sayıyı ise değer (value) olarak oluşturur.
    for player in capitalized_players
}

print("Score dict:", scores)

average = sum(scores.values()) / len(scores)

print("Score average is", round(average, 2)) # average değerini virgülden sonra 2 basamak olacak şekilde yuvarlar.

high_scores = {
    player: score
    for player, score in scores.items()
    if score > average
}
 # scores sözlüğündeki ortalamanın üzerinde puana sahip oyuncuları yeni bir sözlükte toplar.

print("High scores:", high_scores)