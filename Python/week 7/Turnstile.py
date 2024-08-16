"""Turnstile"""
def turn():
    """Turnstile"""
    status=True
    text=""
    count=0
    while text!="END":
        text=input()
        if text=="C":
            status=False
        if not status and text=="P":
            count+=1
            status=True
    print(count)
turn()
