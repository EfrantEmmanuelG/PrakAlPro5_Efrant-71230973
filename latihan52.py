def ganjil(bawah, atas):
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                print(i, end=", ")
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                print(i, end=", ")

bawah1, atas1 = 10, 30
print(f"bawah = {bawah1}, atas = {atas1}. Hasil: ", end="")
ganjil(bawah1, atas1)

print("\n")

bawah2, atas2 = 97, 82
print(f"bawah = {bawah2}, atas = {atas2}. Hasil: ", end="")
ganjil(bawah2, atas2)