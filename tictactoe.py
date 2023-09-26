from random import randrange
pos=["1","2","3","4","5","6","7","8","9"]

def draw_board(location,sign):
    pos[location-1]=sign

    print("+" + 7 * "-" + "+"+ 7 * "-" + "+" + 7 * "-" + "+")
    print(("|" + " " * 7 + "|" + " "* 7 + "|" + " "* 7 + "|" "\n"),end="")
    print(("|" + " " * 3 + pos[0] + " "*3 + "|" + " "* 3 + pos[1] +" "*3 + "|" + " "* 3 + pos[2] + " "*3 + "|" "\n") , end="")
    print(("|" + " " * 7 + "|" + " "* 7 + "|" + " "* 7 + "|" "\n") , end="")

    print("+" + 7 * "-" + "+"+ 7 * "-" + "+" + 7 * "-" + "+")
    print(("|" + " " * 7 + "|" + " "* 7 + "|" + " "* 7 + "|" "\n") , end="")
    print(("|" + " " * 3 + pos[3] + " "*3 + "|" + " "* 3 + pos[4] +" "*3 + "|" + " "* 3 + pos[5] + " "*3 + "|" "\n") , end="")
    print(("|" + " " * 7 + "|" + " "* 7 + "|" + " "* 7 + "|" "\n") , end="")

    print("+" + 7 * "-" + "+"+ 7 * "-" + "+" + 7 * "-" + "+")
    print(("|" + " " * 7 + "|" + " "* 7 + "|" + " "* 7 + "|" "\n") , end="")
    print(("|" + " " * 3 + pos[6] + " "*3 + "|" + " "* 3 + pos[7] +" "*3 + "|" + " "* 3 + pos[8] + " "*3 + "|" "\n") , end="")
    print(("|" + " " * 7 + "|" + " "* 7 + "|" + " "* 7 + "|" "\n") , end="")
    print("+" + 7 * "-" + "+"+ 7 * "-" + "+" + 7 * "-" + "+")

def computer_run():
    print("COMPUTER_RUN")
    location=randrange(9)
    if check_pos(location,"X"):
        draw_board(location,"X")
    else:
        print("Position Filled")

def user_run():
    location=int(input("USER_RUN : enter location:"))
    if check_pos(location,"0"):
        draw_board(location,"0")
    else:
        print("Position Filled")

def check_pos(location,sign):
    if pos[location-1] == "0" or pos[location-1] == "X":
        return False
    else:
        return True

def check_winner():
    if pos[0]=="0" and pos[1]=="0" and pos[2]=="0":
        return 1
    elif pos[0]=="X" and pos[1]=="X" and pos[2]=="X":
        return 2
    elif pos[3]=="X" and pos[4]=="X" and pos[5]=="X":
        return 2
    elif pos[6]=="0" and pos[7]=="0" and pos[8]=="0":
        return 1
    elif pos[6]=="X" and pos[7]=="X" and pos[8]=="X":
        return 2
    elif pos[0]=="0" and pos[3]=="0" and pos[6]=="0":
        return 1
    elif pos[0]=="X" and pos[3]=="X" and pos[6]=="X":
        return 2
    elif pos[1]=="X" and pos[4]=="X" and pos[7]=="X":
        return 1
    elif pos[2]=="0" and pos[5]=="0" and pos[8]=="0":
        return 1
    elif pos[2]=="X" and pos[5]=="X" and pos[8]=="X":
        return 2
    elif pos[0]=="X" and pos[4]=="X" and pos[8]=="X":
        return 2
    elif pos[2]=="X" and pos[4]=="X" and pos[6]=="X":
        return 2
    
draw_board(5,"X")
while check_winner()==None:        
    computer_run()
    user_run()
else:
    print(pos)
    if check_winner()==1:
        print("THE WINNER IS USER!!!")
    else:
        print("THE WINNER IS COMPUTER!!!") 
