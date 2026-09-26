import tkinter as tk
from bot import check_risk,VARIANTS

TURN = 0
GAME_OVER = False

window = tk.Tk()
window.geometry("400x450")
window.title("Tic Tac Toe")
window.resizable(False,False)

def restart():
    global TURN,GAME_OVER
    GAME_OVER = False
    TURN = 0
    for i in range(len(board)):
        board[i] = ""
    for canvas in cells:
        canvas.delete("text")
        canvas.bind("<Button-1>", lambda event, c=canvas: click(event))
    State.config(text="Your turn",fg="green")
    restart_button.pack_forget()


def check(desk):
    global GAME_OVER

    for var in VARIANTS:
        if board[var[0]] == board[var[1]] == board[var[2]] and board[var[0]] != "":
            for i in cells:
                i.unbind("<Button-1>")
            GAME_OVER = True
            if (TURN - 1) % 2 == 0:
                State.config(text="You win!", fg="green")
            else:
                State.config(text="You lose!", fg="green")
            restart_button.pack()
            return
    if board.count("") == 0:
        State.config(text="Draw", fg="green")
        restart_button.pack()

board = [""] * 9

def click(event):
    global TURN
    target = event.widget

    index = cells.index(target) 
    if GAME_OVER:
        return
    if board[index]!="":
        return

    target.create_text(30, 30, text="X", font=("Arial", 24), fill="blue",tags="text")
    board[index] = "X" 
    State.config(text="Enemy's turn", fg="red")
    TURN += 1
    target.unbind("<Button-1>") 
    check(board)

    window.after(300,bot_move)

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


desk = tk.Frame(window, width=400, height=400, bg="white")
desk.pack()
left_top = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
left_top.grid(row=0, column=0)

left_top.create_line(60, 0, 60, 60, fill="black", width=2)
left_top.create_line(0, 60, 60, 60, fill="black", width=2)

center_top = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
center_top.grid(row=0, column=1)

center_top.create_line(60, 0, 60, 60, fill="black", width=2)
center_top.create_line(0, 60, 60, 60, fill="black", width=2)

right_top = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
right_top.grid(row=0, column=2)

right_top.create_line(0, 60, 60, 60, fill="black", width=2)

left_center = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
left_center.grid(row=1, column=0)

left_center.create_line(60,0,60,60, fill="black", width=2)
left_center.create_line(0,60,60,60, fill="black", width=2)

center_center = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
center_center.grid(row=1,column=1)
center_center.create_line(60,0,60,60, fill="black", width=2)
center_center.create_line(0,60,60,60, fill="black", width=2)

right_center = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
right_center.grid(row=1,column=2)

right_center.create_line(0,60,60,60, fill="black", width=2)

left_bottom = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
left_bottom.grid(row=2,column=0)

left_bottom.create_line(60,0,60,60, fill="black", width=2)

center_bottom = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
center_bottom.grid(row=2,column=1)

center_bottom.create_line(60,0,60,60, fill="black", width=2)

right_bottom = tk.Canvas(desk, width=60, height=60,border=2,highlightthickness=0, bg="white")
right_bottom.grid(row=2,column=2)

restart_button = tk.Button(text="Restart",command=restart, width=15,height=2,font=("Arial",10))


cells = [left_top, center_top, right_top,
         left_center, center_center, right_center,
         left_bottom, center_bottom, right_bottom]

for canvas in [left_top, center_top, right_top, left_center, center_center, right_center, left_bottom, center_bottom, right_bottom]:
    canvas.bind("<Button-1>", lambda event, c=canvas: click(event))

State = tk.Label(window, text="Your turn", font=("Arial", 20), fg="blue")
State.pack()
window.mainloop()