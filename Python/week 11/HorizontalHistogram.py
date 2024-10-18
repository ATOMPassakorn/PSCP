'''horizontal'''
def main(text):
    '''histrogram'''
    letter = {}
    count = 0
    for i in text:
        if i not in letter:
            letter.update({i:text.count(i)})
    new_dict = sorted(letter,key=str.swapcase)
    for x in new_dict:
        print(f'{x} : ',end="")
        for _ in range(int(letter[x])):
            count += 1
            if count == 6:
                print('|',end="")
                count = 1
            print('-',end="")
        count = 0
        print(end="\n")
main(input())
