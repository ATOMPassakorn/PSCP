"""Bubble"""
def main():
    """Bubble"""
    bubble_text = input()
    bubble_len = len(bubble_text)
    bubble_clone = bubble_len
    jump = 1
    count = 1
    for _ in range(1,bubble_len+1):
        if bubble_text[count] == " " or count >= bubble_len-1:
            break
        if bubble_text[count] in "o":
            jump += 1
            count += 1
        elif bubble_text[count] in "O":
            if count + 3 >= bubble_len or count + 2 >= bubble_len or count + 1 >= bubble_len:
                jump += 1
                count += (bubble_len - count) - 1
            elif bubble_text[count+3] == "O" or bubble_text[count+3] == "|":
                jump += 1
                count += 3
            elif bubble_text[count+2] == "O" or bubble_text[count+2] == "|":
                jump += 1
                count += 2
            elif bubble_text[count+1] == "O" or bubble_text[count+1] == "|":
                jump += 1
                count += 1
            else:
                for j in (3,2,1):
                    if bubble_text[count+j] == "o":
                        count += j
                        jump += 1
                        break
                    count += 1
                    break
    result = count +1
    return result, bubble_len, bubble_clone, count, jump
result_2, bubble_len_2, bubble_clone_2, count_2, jump_2 = main()
if result_2 < bubble_len_2:
    print("IMPOSSIBLE",bubble_clone_2 - count_2,sep="\n")
else:
    print("POSSIBLE",jump_2,sep="\n")
