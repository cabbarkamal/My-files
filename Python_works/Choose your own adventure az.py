print("Salam oyunumuza xoş gəlmisən")
name = input("Zəhmət olmasa adını daxil et ")
print("Oyunmuza xoş gəldin" , name)
answer = input("Bizimlə oynamaq istəyirsən? (h/y) ").lower()
if answer == "h":
    print("Yaxşı gəl başlayaq")
else:
    print("Yaxşı gələn dəfə görüşərik! ")
    quit()

print("Ölü sonluğa gəlib çatdın hansı tərəfə getmək istəyirsən? (sağ  / sol) ")
answer = input("Seçimini et: ").lower()
if answer == "sol":
    print("Səhv yolu seçdin və öldün!")
elif answer == "sağ":
    print("Çayın yanına gəldin nə edərsən? üz / yeri ")
    answer = input("Seçimini et: ").lower()
    if answer == "üz":
        print("Açıqcası çayda timsah var idi və səni yedi Allah Rəhmət Etsin!! ^_^")
    elif answer == "yeri":
        print("Çox gəzdin və suyun bitdi Allah Rəhmət Etsin")
    else:
        print("Səhv cavab!!")
else:
    print("Səhv cavab!!")