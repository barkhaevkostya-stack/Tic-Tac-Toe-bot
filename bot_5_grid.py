VARIANTS = [[3,7,11,15],[4,8,12,16,20],[9,13,17,21],[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]

def check_risk(board):
    for var in VARIANTS:
        values = [board[i] for i in var]
        if values.count("O") == 3 and values.count("") == 1:
                    return var[values.index("")]
        if values.count("X") == 3 and values.count("") == 1:
            return var[values.index("")]

    return choose_tactics(board)

def choose_tactics(board):
    one,two,free,three = [],[],[],[]
    for variant in VARIANTS:
        values = [board[index] for index in variant]
        if values.count("O") == 3 and values.count("")>=1 and values.count("")<=2:
                    three.append(variant)
        if values.count("O") == 2 and values.count("")>=1 and values.count("")<=3:
            two.append(variant)
        elif values.count("O") == 1 and values.count("") == 2:
            one.append(variant)
        elif values.count("") == 3:
            free.append(variant)
    if three:
            variant = three[0]
            return variant[[board[i] for i in variant].index("")]
    elif two:
        variant = two[0]
        return variant[[board[i] for i in variant].index("")]
    elif one:
        variant = one[0]
        return variant[[board[i] for i in variant].index("")]
    elif free:
        return free[0][0]
    else:
        for i in range(len(board)):
            if board[i] == "":
                return i
    