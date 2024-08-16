"""Mac"""
def mac():
    """mac"""
    al = "ghijklmnopqrstuvwxyz"
    spec = "!@#$%^&*()+?_=,<>;/\"\\\'"
    ad = input()
    check = True
    for i in ad:
        if i.lower() in al or i in spec:
            check = False
    if check:
        if len(ad) == 17:
            if ad[2] == "-" and ad[5] == "-" and \
                ad[8] == "-" and ad[11] == "-" and ad[14] == "-":
                if ad.count("-") == 5 and not ":" in ad and not "." in ad :
                    print("VALID 1")
                else:
                    print("ERROR")
            elif ad[2] == ":" and ad[5] == ":" and \
                ad[8] == ":" and ad[11] == ":" and ad[14] == ":":
                if ad.count("-") == 5 and not "-" in ad and not "." in ad :
                    print("VALID 2")
                else:
                    print("ERROR")
            else:
                print("ERROR")
        elif len(ad) == 14:
            if ad[4] == "." and ad[9] == "." and ad.count(".") == 2 and not ":" in ad and not "-" in ad :
                print("VALID 3")
            else:
                print("ERROR")
        else:
            print("ERROR")
    else:
        print("ERROR")
mac()
