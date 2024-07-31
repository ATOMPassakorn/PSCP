"""FoodGrade I"""
def foodgrade1(num=24,wings=0):
    """FoodGrade I"""
    if not num:
        print(wings)
        return
    c=float(input())
    if 70>=c>=50:
        wings+=1
    foodgrade1(num-1,wings)
foodgrade1()
