def multiplicar(n, m):
    r_negativo = (n < 0) != (m < 0)
    n = -n if n < 0 else n
    m = -m if m < 0 else m
    r = 0
    i = 0
    while i < n:
        r = r + m
        i = i + 1
    if r_negativo:
        r = -r
    return r

def main():
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    print(multiplicar(x, y))

if __name__ == "__main__":
    main()