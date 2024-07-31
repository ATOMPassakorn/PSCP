"""WeightStation"""
def hoklor():
    """WeightStation"""
    average=float(input())
    weight1=float(input())
    weight2=float(input())
    weight3=float(input())
    weight4=average*4-(weight1+weight2+weight3)
    total=weight1+weight2+weight3+weight4
    w1=abs(average-weight1)
    w2=abs(average-weight2)
    w3=abs(average-weight3)
    w4=abs(average-weight4)
    if total>15000:
        print("Overweight")
    elif total<=15000 and \
    (w1<=average/2 and w2<=average/2 \
     and w3<=average/2 and w4<=average/2):
        print(f"Pass {weight4:.2f}")
    elif w1>average/2 or w2>average/2 \
    or w3>average/2 or w4>average/2:
        print("Unbalance")
hoklor()
