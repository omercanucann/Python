def ft_count_harvest_interative(x):
    i = 1
    while i <= x:
        print(f"Day {i}")
        i += 1



def ft_count_harvest_recursive(x):
    i = 1
    while i <= x:
        print(f"Day {i}")
        i += 1


def main():
    x = int(input("Days until harvest: "))
    ft_count_harvest_interative(x)
    print()
    print(f"Days Until Harvest {x}")
    ft_count_harvest_recursive(x)

main()  