import os
import numpy as np


def main():
    name = os.environ['NAME']
    prenom = input("Enter votre nom: ")
    print(f"Hello, {prenom} {name}")

    shape = (10, 10)
    arr = np.zeros(shape)
    for i in range(10):
        for j in range(10):
            arr[i][j] = i + j
    print(arr)


if __name__ == '__main__':
    main()
