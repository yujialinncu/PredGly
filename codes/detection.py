def detect(frag):
    right_frag=[]
    wrong_frag=[]
    lines = frag
    n=int(len(lines)/2)
    AAs='ACDEFGHIKLMNPQRSTVWYO'
    for i in range(n):
        a=0
        for letter in lines[2*i+1]:
            if letter not in AAs:
                a=1
        if a==1:
            wrong_frag.append(lines[2*i])
            wrong_frag.append(lines[2*i+1])
        else:
            right_frag.append(lines[2*i])
            right_frag.append(lines[2*i+1])
    return right_frag,wrong_frag