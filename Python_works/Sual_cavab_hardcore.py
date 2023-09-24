print("Salam Cabbarın oyununa xoş gəlmisən!")
oynamaq_istiyirsen = input("Oynamaq istəyirsən? h/y   ").lower()
xal = 0
if oynamaq_istiyirsen == "h":
    print("Lap yaxşı \nSuallara başlayaq")
    cavab1 = "1993"
    cvb1 = input("Humayın doğum ili (sadəcə ədəd ilə): ").lower()
    if cavab1 == cvb1:
        print("Əla 1-ci sual düz")
        xal += 1
    else:
        print("EEE noldu day bundada çaşma")
    cavab2 = "bakı"
    cvb2 = input("Azərbaycanın paytaxtı ").lower()
    if cavab2 == cvb2:
        print("Əla keçək 3-cü suala")
        xal += 1
    else:
        print("Sənin boinqını yerə soxum")
    cavab3 = "2010"
    cvb3 = input("Cabbarın doğum ili (Sadəcə rəqəm daxil edin!) ").lower()
    if cavab3 == cvb3:
        print("Ağıllı bala afərin!!")
        xal += 1
    else:
        print("Ayıbçıııııı!!!!")
    cavab4 = "1979"
    cvb4 = input("Samirənin doğum ili (Sadəcə rəqəm daxil edin!) ").lower()
    if cavab4 == cvb4:
        print("Əla, ananı tanıyırsan")
        xal += 1
    else:
        print("Sənin boinqını yerə soxum")
    reng = input("En sevdiyin rəng(1 rəng seç) ").lower()
    if reng =="qara" or reng == "ağ":
        print("Mənim də ən sevdiyim!!")
        xal += 1
    else:
        print("Ehh yaxşıdır")
    print("Bu oyunda sənin cavablarına əsasən xallarını topladıq sən",xal ,"xal qazandın! \nTəbriklər gələn dəfə görüşənədək! \nSağ ol")
else:
    print("Niyə burdasan?")
    quit()