"""Real"""
def num1():
    """number input"""
    ans=""
    for _ in range(24):
        status=input()
        if status=="on":
            ans+="1"
        else:
            ans+="0"
    return ans

def tran(binary1):
    """binary"""
    ans=""
    for i in range(0, len(binary1), 8):
        binary_segment=binary1[i:i+8]
        decimal=""
        if binary_segment[:7]=="1111110":
            decimal="0"
        elif binary_segment[:7]=="0110000":
            decimal="1"
        elif binary_segment[:7]=="1101101":
            decimal="2"
        elif binary_segment[:7]=="1111001":
            decimal="3"
        elif binary_segment[:7]=="0110011":
            decimal="4"
        elif binary_segment[:7]=="1011011":
            decimal="5"
        elif binary_segment[:7]=="1011111":
            decimal="6"
        elif binary_segment[:7]=="1110000":
            decimal="7"
        elif binary_segment[:7]=="1111111":
            decimal="8"
        elif binary_segment[:7]=="1111011":
            decimal="9"
        else:
            print("Error")
            return
        if binary_segment[-1] == "1":
            decimal+="."
        ans+=decimal
    if ans:
        print(f"{float(ans.strip()):.2f}")
    else:
        print("Error")
binary1=num1()
tran(binary1)
