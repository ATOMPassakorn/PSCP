"""BloodDonation"""
def blood():
    """BloodDonation"""
    age = int(input())
    weight = int(input())
    times = int(input())
    doc=""
    condition=(age > 70 or age < 17) or weight < 45 or (not times and age>55)
    if age==17 or 60<=age<=70:
        doc=input()
        if condition or doc=="False":
            print("No")
        else:
            print("Yes")
    elif condition:
        print("No")
    else:
        print("Yes")
blood()
