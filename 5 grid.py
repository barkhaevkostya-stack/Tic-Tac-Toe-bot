import tkinter as tk
from bot_5_grid import choose_tactics,check_risk

GAME_OVER = False
TURN = 0
VARIANTS = [[3,7,11,15],[4,8,12,16,20],[9,13,17,21],[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]
board = ["" for i in range(25)]
TWO = True
print(board)

root = tk.Tk()
root.geometry("400x450")

def choose_one():
    global TWO
    TWO = False
    oneplayer.pack_forget()
    twoplayer.pack_forget()
    desk.pack()
    State.pack()
def two_choose():
    global TWO
    TWO = True
    oneplayer.pack_forget()
    twoplayer.pack_forget()
    desk.pack()
    State.pack()


oneplayer = tk.Button(text="1Player",command=choose_one)
twoplayer = tk.Button(text="2Player",command=two_choose)
oneplayer.pack()
twoplayer.pack()

def place_five(window):
    cells = []
    rows = 0
    columns = 0
    for i in range(25):
        cell = tk.Canvas(desk, width=60, height=60, bd=1,relief="solid",highlightthickness=0)
        cell.grid(column=columns, row=rows,padx=0,pady=0)
        cells.append(cell)

        columns += 1
        if columns > 4:      
            columns = 0
            rows += 1

    return cells

def click(event):
    global TURN
    target = event.widget
    index = cells.index(target)
    if TWO:
        if TURN%2 == 0:
            target.create_text(30, 30, text="X", font=("Arial", 24), fill="blue", tags="text")
            board[index] = "X"
            State.config(text="Enemy's turn", fg="red")
        elif TURN%2 != 0:
            target.create_text(30, 30, text="O", font=("Arial", 24), fill="red", tags="text")
            board[index] = "O"
            State.config(text="Your turn", fg="blue")

        target.unbind("<Button-1>")
        check(board)
        TURN+=1
    elif not TWO:
        if TURN%2 == 0:
            target.create_text(30, 30, text="X", font=("Arial", 24), fill="blue", tags="text")
            board[index] = "X"
            State.config(text="Enemy's turn", fg="red")
            TURN += 1
            target.unbind("<Button-1>")
            check(board)
            root.after(300, bot_move)

def bot_move():
        global TURN
        if GAME_OVER:
            return
        move = check_risk(board)
        cells[move].create_text(30, 30, text="O", font=("Arial", 24), fill="red",tags="text")
        board[move] = "O"
        State.config(text="Your turn", fg="blue") 
        cells[move].unbind("<Button-1>")
        TURN +=1
        check(board)

def end_game():
    global GAME_OVER
    GAME_OVER = True
    for c in cells:
        c.unbind("<Button-1>")

def check(board):
    for variant in VARIANTS:
        values = [board[i] for i in variant]
        if values.count("X") == 4:
            State.config(text="You win", fg="green", font=("Arial", 30))
            end_game()
            return
        if values.count("O") == 4:
            State.config(text="You lose", fg="red", font=("Arial", 30))
            end_game()
            return
    if "" not in board:
        State.config(text="Draw", fg="green")
        end_game()




desk = tk.Frame(root,width=500,height=500)

cells = place_five(root)

State = tk.Label(root,text="Your Turn",fg="blue",font=("Arial",20))

for canvas in cells:
    canvas.bind("<Button-1>", lambda event, c=canvas: click(event))
root.mainloop()