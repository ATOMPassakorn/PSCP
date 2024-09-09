"""almostMean"""
def almostmean(n):
    """almostMean"""
    id_list = []
    score_list = []
    avg = 0
    for _ in range(n):
        text = input()
        text_split=text.split("\t")
        student=text_split[0]
        score=float(text_split[1])
        id_list.append(student)
        score_list.append(score)
    avg=sum(score_list)/len(score_list)
    closed_score=-1
    closed_id=""
    for i in range(n):
        if score_list[i]<=avg and score_list[i]>closed_score:
            closed_score=score_list[i]
            closed_id=id_list[i]
    print(f"{closed_id}\t{closed_score}")
almostmean(int(input()))
