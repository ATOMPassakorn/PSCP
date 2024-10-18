"""LetterFrequency"""
def main():
    """main"""
    count_letter = {}
    most_used_key = None
    most_value = float('-inf')
    text = input().lower()
    new_text = ""
    for i in text: # purify data
        if i.isalpha():
            new_text += i
    for i in new_text: # create most used alpha
        if i in count_letter:
            count_letter[i] += 1
        else:
            count_letter[i] = 1
    for key, value in count_letter.items(): # find most used alpha
        if value > most_value:
            most_used_key = key
            most_value = value
    print(most_used_key)
main()
