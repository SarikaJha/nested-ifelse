day="monday"
breakfast="poorisabzi"
lunch="sambharrice"
dinner="chickenrice"


day="tuesday"
breakfast="poha"
lunch="rajmachawal"
dinner="rotisabzi"
 
day=input("enter the day----")
meal_time=input("enter the meal time----")
if day=="monday":
    if meal_time=="breakfast":
        print("poori sabzi")
    elif meal_time=="lunch":
        print("sambhar rice")
    else:
        print("chicken rice")
elif day=="tuesday":
    if meal_time=="breakfast":
        print("poha")
    elif meal_time=="lunch":
        print("rajma chawal")
    else:
        print("roti sabzi")
else:
    print("you can eat anything")