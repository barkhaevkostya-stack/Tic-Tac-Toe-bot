VARIANTS = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[2,5,8],[0,3,6],[1,4,7],[2,4,6],[0,4,8]]

def check_risk(turns):
    for variant in VARIANTS:
        #checking all the win tactics
        values = [turns[index] for index in variant]
        #checking if we can win
        if values.count("O") == 2 and values.count("") == 1:
                    return variant[values.index("")]
        #checking the risk
        if values.count("X") == 2 and values.count("") == 1:
            return variant[values.index("")]
        
    return choose_tactics(turns)
        

def choose_tactics(board):
    two, one, free = [], [], []
    for variant in VARIANTS:
        values = [board[index] for index in variant]
        if values.count("O") == 2 and values.count("") == 1:
            two.append(variant)
        elif values.count("O") == 1 and values.count("") == 2:
            one.append(variant)
        elif values.count("") == 3:
            free.append(variant)

    if two:
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
    