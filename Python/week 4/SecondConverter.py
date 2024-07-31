"""SecondConverter"""
def main():
    """SecondConverter"""
    k=int(input())
    s=int(input())
    m=int(input())
    h=int(input())
    sec=k%(h*m*s)
    hour=sec//(m*s)
    sec=sec%(m*s)
    minute=sec//s
    sec=sec%s
    print(f"{hour}:{minute}:{sec}")
main()
