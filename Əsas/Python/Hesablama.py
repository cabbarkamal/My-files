prob = input("Hansı prosesi istəyirsiniz (Birini daxil et: toplama, çıxma, vurma, bölmə) :")

if prob.lower() == "toplama":
    print("İstənilən iki ədədin toplanması")
    a = int(input("Birinci ədədi yaz:"))
    b = int(input("İkinci ədədi yaz:"))
    print(a + b)

elif prob == "çıxma":
    print("İstənilən iki ədədin çıxılması")
    c = int(input("Birinci ədədi yaz:"))
    d = int(input("İkinci ədədi yaz:"))
    print(c - d)

elif prob == "vurma":
    print("İstənilən iki ədədin vurulması")
    e = int(input("Birinci ədədi yaz:"))
    f = int(input("İkinci ədədi yaz:"))
    print(e * f)

elif prob == "bölmə":
    print("İstənilən iki ədədin bölünməsi")
    g = int(input("Birinci ədədi yaz:"))
    h = int(input("İkinci ədədi yaz:"))
    print(g / h)

else:
    print("Proses səhvdir!")