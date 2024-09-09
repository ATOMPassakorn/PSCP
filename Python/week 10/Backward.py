"""backward"""
def backward():
    """backward"""
    text_list = []
    text=""
    while text!="NULL":
        text = input()
        if text!="NULL":
            text_list.append(text)
    text_list.reverse()
    for i in text_list:
        print(i)
backward()
