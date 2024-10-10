"""Muddled Menu"""
def menu():
    """"Muddled Menu"""
    food=""
    allezcuisine=[]
    while food!="DONE":
        food=input()
        if food=="SOMETHING'S WRONG":
            allezcuisine.clear()
            continue
        if food=="CLOSED":
            allezcuisine.clear()
            break
        if food.startswith("Can't do:"):
            cancel=food.replace("Can't do: ","")
            if cancel in allezcuisine:
                allezcuisine.remove(cancel)
                continue
        if food=="DONE":
            break
        food2=food.split("#")
        if food2[1]=="N":
            allezcuisine.insert(len(allezcuisine),food2[0].strip())
        else:
            allezcuisine.insert(int(food2[1])-1,food2[0].strip())
    enisiuczella=allezcuisine.copy()
    enisiuczella.reverse()
    print(f"Full Course: {allezcuisine} Reversed: {enisiuczella}")
menu()
