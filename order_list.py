# Order list

# // 1 Use sort()
# todo 2 Use a function to do the procedure
# todo 3 To have a random list


# * Version 1
def order(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


if __name__ == "__main__":
    lista = [4, 1, 6, 7, 9, 3]
    print(f"\n{order(lista)}\n")
    # print("==============================")
