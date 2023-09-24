import random

user_wins = 0
comp_wins = 0

options = ["daş" , "kağız" , "qayçı"]
while True:
    sec = input("1-ni seç Daş/Kağız/Qayçı, yada çıxmaq üçün q-ya bas: ").lower()
    if sec == "q":
        break
    
    if sec not in options:
        continue

    random_number = random.randint(0, 2)
    # das:0 kagiz:1 qayci:2
    comp_sec = options[random_number]
    print("Kompyuter" , comp_sec , "seçdi")


    if sec == "kağız" and comp_sec == "daş":
        print("Sən qalib gəldin")
        user_wins += 1
        
    elif sec == "qayçı" and comp_sec == "kağız":
        print("Sən qalib gəldin")
        user_wins += 1
        
    elif sec == "daş" and comp_sec == "qayçı":
        print("Sən qalib gəldin")
        user_wins += 1
        
    elif sec == comp_sec:
        print("Bərabər qaldınız")
        user_wins += 1
        comp_wins += 1

    else:
        print("Sən uduzdun! ")
        comp_wins += 1
    

print("Yaxşı sağ ol")
print("Kompyuter", comp_wins, "dəfə qalib gəldi!")
print("Sən" , user_wins, "dəfə qalib gəldin")