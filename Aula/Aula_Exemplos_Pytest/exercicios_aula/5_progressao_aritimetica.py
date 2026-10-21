# Escreva um algoritmo que leia um número n (número de termos de uma progressão aritmética), a1 ( o primeiro 
# termo da progressão) e r (a razão da progressão) e escreva os n termos dessa progressão, bem como a soma dos 
# elementos.

n = int(input("\n\nnumero de termos: "))
a1 = int(input("primeiro termo: "))
r = int(input("razao: "))
pa = [a1]
t = a1
s = a1

for i in range (1, n):
    t += r
    s += t
    pa.append(t)

print("\n-----------------------------\n")
print(f"PA = {pa}")
print(f"S = {s}\n")