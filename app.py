# KALKULATOR FPB DAN KPK
# Menggunakan Algoritma Euclid

def hitung_fpb(a, b):
    langkah = []

    while b != 0:
        q = a // b
        r = a % b

        langkah.append(f"{a} = {q} × {b} + {r}")

        a, b = b, r

    return a, langkah


print("=" * 40)
print("     KALKULATOR FPB DAN KPK")
print("=" * 40)

a = int(input("Masukkan bilangan pertama : "))
b = int(input("Masukkan bilangan kedua   : "))

fpb, langkah = hitung_fpb(a, b)

kpk = abs(a * b) // fpb

print("\nLangkah Algoritma Euclid:")
for l in langkah:
    print(l)

print("\nHasil:")
print("FPB =", fpb)
print("KPK =", kpk)
