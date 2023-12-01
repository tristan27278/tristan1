print("latihan 1")
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for baris in matriks:
    for elemen in baris:
        print(elemen)

print("latihan 2")
buku_alamat = [
    ["John Doe", "555-1234"],
    ["Jane Smith", "555-5678"],
    ["Bob Johnson", "555-7890"]
]
for entri in buku_alamat :
    print(f"{entri[0]} - {entri[1]}")

print("latihan 4 ")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i * j, end=' ')
        print()