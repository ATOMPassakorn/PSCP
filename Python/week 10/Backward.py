"""backward"""
def backward():
    """backward"""
    text_list = []
    while True:
        text = input()
        if text == "NULL":
            break
        text_list.append(text)
    text_list = text_list[::-1]
    for i in text_list:
        print(i)
backward()
