def multiplicar(x, y):
    r = 0
    i = 0
    while i < x:
        r = r + y
        i = i + 1
    return r

def main():
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    print(multiplicar(x, y))

if __name__ == "__main__":
    main()

