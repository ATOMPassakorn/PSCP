"""BigFrame"""
def frame():
    """BigFrame"""
    text1=input().strip()
    text2=input().strip()
    text3=input().strip()
    text4=input().strip()
    text5=input().strip()
    lenght=max(len(text1),len(text2),len(text3),len(text4),len(text5))
    print("*"*(lenght+4))
    print(f"* {text1:{lenght}} *")
    print(f"* {text2:{lenght}} *")
    print(f"* {text3:{lenght}} *")
    print(f"* {text4:{lenght}} *")
    print(f"* {text5:{lenght}} *")
    print("*"*(lenght+4))
frame()
