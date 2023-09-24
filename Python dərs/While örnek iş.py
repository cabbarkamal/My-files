ad = "Mədinə"
par = "1234"

print("Ad 'Mədinə' dır parolu özünüz tapacaqsınız!!")

while(True):
    daxilad = input("Adınızı daxil edin:  ")
    daxilpar = input("Parolunuzu daxil edin:  ")

    if (daxilad == ad) and (daxilpar == par):
        print("Salam Python dərslərinə xoş gəlmişsiniz!!")
        break
    elif (daxilad != ad) and (daxilpar == par):
        print("Adınız səhvdir")
    elif (daxilad == ad) and (daxilpar != par):
        print("Parolunuz səhvdir!")
        print("Parolunu dəyişmək istəyirsiniz? (Hə/Yox):  ")
        cavab = input()
        if (cavab == "Hə"):
              
            ypar = input("Yeni parol daxil edin:  ")
            print("Bir saniyə gözləyin...")
            par = ypar
            print("Parol qeyd edildi!")  
               
    else:
        print("Yenidən yoxlayın")