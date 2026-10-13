"""Programa simples que exibe a tabuada de um número de 1 a 10."""


def main():
    numero = int(input())

    for multiplicador in range(1, 11):
        print(f"{numero} * {multiplicador} = {numero * multiplicador}")


if __name__ == "__main__":
    main()
