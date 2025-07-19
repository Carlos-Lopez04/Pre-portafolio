# Bubble sort

# todo 1 Use a loop to iterate everything
# todo 2 Use a loop to compare adjacent elements in the list
# todo 3 Use a conditional to verify if are in the incorrect order
# todo 4 Inside the conditional swap the elements
# todo 5 Save the actual element in a temporary variable

# * range(len(l) - 1) -> ensures that limits are not exceeded
# * l[j + 1] -> allows access to the next element


def v1():
    l = [5, 3, 8, 1]

    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    print(f"\nLista ordenada 1 -> {l}\n")


def v2():
    l = [5, 3, 8, 1]
    changes = True

    while changes:
        changes = False
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]  # * Direct way to swap elements
                changes = True
    print(f"\nLista ordenada 2 -> {l}\n")


def v3(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == "__main__":
    # v1()
    # print("==============================")
    # v2()
    # print("==============================")
    # Ejemplos de uso:
    lista1 = [64, 34, 25, 12, 22, 11, 90]
    lista2 = [5, 1, 4, 2, 8]
    lista3 = [3, 0, 2, 5, -1, 4, 1]

    # Ordenar y mostrar resultados
    print("Lista 1 (original):", lista1)
    print("Lista 1 (ordenada):", v3(lista1.copy()))
    # Usamos .copy() para no modificar la original
    print("\nLista 2 (original):", lista2)
    print("Lista 2 (ordenada):", v3(lista2.copy()))
    print("\nLista 3 (original):", lista3)
    print("Lista 3 (ordenada):", v3(lista3.copy()))
