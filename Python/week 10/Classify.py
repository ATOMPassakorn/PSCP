"""classify"""
def main():
    """classify"""
    list_id = []
    st_num = input()
    current = ""
    while st_num != "END":
        list_id.append(st_num[:4])
        st_num = input()
    copy_list = sorted(list(set(list_id)))
    for i in copy_list:
        if i[:2] != current:
            current = ""
        if not current:
            print(f"{i[:2]} {int(i[2:])} {list_id.count(i)}")
            current = i[:2]
        else:
            print(f"-- {int(i[2:])} {list_id.count(i)}")
main()
