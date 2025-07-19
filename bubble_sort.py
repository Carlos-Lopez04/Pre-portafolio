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


if __name__ == "__main__":
    v1()
    v2()
