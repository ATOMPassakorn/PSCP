"""Filter"""
import json
def answer():
    """find ans"""
    score=json.loads(input())
    want=float(input())
    fil_dic={}
    fil_value=[]
    for i in score:
        if score[i]>=want:
            fil_dic[i]=score[i]
    fil_key=sorted(fil_dic.keys())
    for i in fil_key:
        fil_value.append(fil_dic[i])
    if fil_dic:
        for key,value in zip(fil_key,fil_value):
            print(f"{key}\t{value:.2f}")
    else:
        print("Nope")
answer()
