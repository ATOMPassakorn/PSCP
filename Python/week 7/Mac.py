"""Mac"""
def mac():
    """mac"""
    alpha="ABCDEFabcdef0123456789-:."
    text=input()
    check=True
    first=len(text)==17 and text[2] == "-" and text[5] == "-" and \
text[8] == "-" and text[11] == "-" and text[14] == "-" and text.count("-") == 5
    second=len(text)==17 and text[2] == ":" and text[5] == ":" and \
text[8] == ":" and text[11] == ":" and text[14] == ":" and text.count(":") == 5
    third=len(text)==14 and text[4] == "." and text[9] == "." and text.count(".") == 2 \
and text[:4].isalnum() and text[5:9].isalnum() and text[10:].isalnum()
    for i in text:
        if i not in alpha:
            check=False
            break
    if not (len(text)==17 or len(text)==14):
        check=False
    if check and (first or second or third):
        if first:
            print("VALID 1")
        elif second:
            print("VALID 2")
        if third:
            print("VALID 3")
    else:
        print("ERROR")
mac()
