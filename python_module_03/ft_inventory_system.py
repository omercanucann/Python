import sys

print("=== Inventory System Analysis ===")

inventory = {}

for arg in sys.argv[1:]:
    if arg.count(":") != 1:
        print(f"Error - invalid parameter '{arg}'")
        continue
    name, qty_str = arg.split(":", 1) # arg dizgesini ilk : karakterinden itibaren en fazla bir kez böler.
    # Örneğin "sword:5".split(":", 1) sonucu ["sword", "5"] olur. İkinci parametre olan 1, yalnızca ilk iki parçanın elde edilmesini sağlar;
    #  böylece dizgede başka : karakterleri varsa geri kalanı ikinci parçada kalır.

    if not name:
        print(f"Error - invalid parameter '{arg}'")
        continue
    if name in inventory:
        print(f"Reundant item '{name}' - discarding")
        continue
    try:
        qty = int(qty_str)
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")
        continue
    inventory[name] = qty

print(f"Got inventory: {inventory}")
items = list(inventory.keys()) # tüm anahtarlarını gösteren bir görünüm (view) nesnesi döndürür.
# list(inventory.keys()) ise bu görünümü gerçek bir listeye dönüştürür. Örneğin {"sword": 1, "potion": 5} için sonuç ["sword", "potion"] olur.

print(f"Item list: {items}")
total = sum(inventory.values())

print(f"Total quantity of the {len(items)} items: {total}")

if total > 0:
    for item, qty in inventory.items():
        print(f"Item {item} represents {round(qty * 100 / total, 1):.1f}%")

    max_item = next(iter(inventory))
    min_item = next(iter(inventory))

    for item, qty in inventory.items():
        if qty > inventory[max_item]:
            max_item = item
        if qty < inventory[min_item]:
            min_item = item
    
    print(f"Item most abundant: {max_item} with quantity {inventory[max_item]}")
    print(f"Item least abundant: {min_item} with quantity {inventory[min_item]}")

inventory.update({"magic_item": 1}) # sözlüğe "magic_item" anahtarını 1 değeriyle ekler; eğer "magic_item" zaten varsa değerini 1 olarak günceller.
print(f"Updated inventory: {inventory}")