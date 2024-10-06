"Sciencific Notation"
def to_sci(text) :
    "Change Normal to Sciencific Notation form"
    left_digit = text[:text.find(".")].strip()
    right_digit = text[text.find(".")+1:].strip()
    power = 0

    if 1 <= float(text) < 10 :
        return f"{left_digit}"+f".{right_digit}"*bool(right_digit)+ f" x 10^{power}"

    if float(text) >= 10 :
        power = len(left_digit)-1
        if not right_digit :
            left_digit = str(int(left_digit[::-1]))[::-1]
        left_digit = left_digit.replace(".","")
        return f"{left_digit[0]}"+"."*bool(len(left_digit)>1)+\
            f"{left_digit[1:]}{right_digit} x 10^{power}"

    for i in right_digit :
        power += 1
        if i not in "0" :
            break

    right_digit = str(int(right_digit))
    return f"{right_digit[0]}"+"."*bool(len(right_digit)>1)+f"{right_digit[1:]} x 10^-{power}"

def to_norm(text) :
    "Change Sciencific Notation to Normal form"
    if text.find(".",0,text.find("x")) == -1 :
        text = text[0:text.find("x")].strip() + "." + text[text.find("x"):].strip()
    left_digit = text[:text.find(".")].strip()
    right_digit = text[text.find(".")+1:text.find("x")].strip()
    power = text[text.find("^")+1:].strip()

    if int(power) < 0 :
        left_digit = "0"*abs(int(power)) + left_digit
        return f"{left_digit[0]}.{left_digit[1:]}{right_digit}"

    if int(power) > 0 :
        right_digit = f"{right_digit:<0{int(power)}}"
        return f"{left_digit}{right_digit[:int((power))]}.{right_digit[int(power):]}"

    return left_digit+"."+right_digit

def main() :
    "main"
    text = str(input())
    negative = False
    calculated = None

    if text[0] in "-" :
        negative = True
        text = text[1:]

    if text.count("x") > 0 : #if text is sciencific notation form
        calculated = to_norm(text)

    else : #if text is normal form
        text += "."*(text.count(".") < 1)
        if not float(text) :
            print(0)
            return
        calculated = to_sci(text)

    if not calculated[calculated.find(".")+1:] :
        calculated = calculated.replace(".","")

    print("-"*negative+calculated)
main()
