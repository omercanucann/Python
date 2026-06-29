def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    print(f"{seed_type} seeds: {quantity} {unit} available")

def main():
    seedtype = str(input("Seed Type: "))
    quant = int(input("Quantity: "))
    unit = str(input("Unit type: "))
    ft_seed_inventory(seedtype, quant, unit)

main()  