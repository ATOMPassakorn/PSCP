"""WordSequence II"""
def main():
    """main"""
    origin = input()
    new_ori = input()
    ori_lst = []
    new_ori_lst = []
    for i in origin: # create two list of new and origin
        ori_lst.append(i)
    for i in new_ori:
        new_ori_lst.append(i)
    for i in range(max(len(ori_lst),len(new_ori_lst))): # make two list equal
        if len(ori_lst) < len(new_ori_lst):
            ori_lst.append("")
        if len(new_ori_lst) < len(ori_lst):
            new_ori_lst.append("")
    print("".join(ori_lst))
    for i, value in enumerate(new_ori_lst):
        if i < len(ori_lst): # condition 2
            ori_lst.pop(i)
        ori_lst.insert(i,value)
        print("".join(ori_lst))
main()
