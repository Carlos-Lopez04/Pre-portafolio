# Two sum

# todo Create a list with numbers
# todo The number target need to be the sum of 2 numbers in the list


def v1():
    # * Brute force

    target = int(input("Introduce a number "))

    numbers = [1, 8, 11, 20]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
            print(f"The sum of {numbers[i]} + {numbers[j]} => {target}")


if __name__ == "__main__":
    v1()
    print("==============================")
