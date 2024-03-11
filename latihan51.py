def perkalian(angka1, angka2):
    hasil = 0
    for i in range(angka2):
        hasil += angka1
    return hasil

a = 6
b = 5
hasil_perkalian = perkalian(a, b)
print(f"{a} x {b} = {' + '.join([str(a) for i in range(b)])} = {hasil_perkalian}")

a = 7
b = 10
hasil_perkalian = perkalian(a, b)
print(f"{a} x {b} = {' + '.join([str(a) for i in range(b)])} = {hasil_perkalian}")