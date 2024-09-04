"""Real"""
def num1():
    """number input"""
    binary=""
    for _ in range(8):
        status=input()
        if status=="on":
            binary+="1"
        else:
            binary+="0"
    return binary
def tran(binary):
    """binary to decimal"""
    result="Error"
    if binary[:7]=="1111110":
        result = "0"
    if binary[:7]=="0110000":
        result = "1"
    if binary[:7]=="1101101":
        result = "2"
    if binary[:7]=="1111001":
        result = "3"
    if binary[:7]=="0110011":
        result = "4"
    if binary[:7]=="1011011":
        result = "5"
    if binary[:7]=="1011111":
        result = "6"
    if binary[:7]=="1110000":
        result = "7"
    if binary[:7]=="1111111":
        result = "8"
    if binary[:7]=="1111011":
        result = "9"
    return result
def point(binary):
    """point check"""
    if binary[-1] == "1":
        return "."
    return ""
def ans():
    """print result"""
    number=""
    for _ in range(3):
        binary=num1()
        number+=tran(binary)+point(binary)
    if number.count(".")>1 or "Error" in number:
        print("Error")
    else:
        print(f"{float(number):.2f}")
ans()
