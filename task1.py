import random as rd 
list = ["A","B","C","D","E"]
goal = rd.choice(list)

for i in range(6):
    user = input("pick a word in (A,B,C,D,E)")
    if user.casefold() == goal.casefold():
        print("you win game ")
        break
    else :
        print(f"you lost, you have {5-i} life")
print("game complet")