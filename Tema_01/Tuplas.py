my_list = [1, 2, 3, 4, 5, 6, 7, 12, 8]

def min_max_mid(lista: list) -> tuple:
    return (min(my_list), max(my_list), my_list[len(my_list) // 2])

my_tuple = min_max_mid(my_list)
print(my_tuple)

min, max, mid = min_max_mid(my_list)
print(f"{min}, {max}")