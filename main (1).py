import random as r
import turtle as t

 
#m is mine
class board_class():
    def __init__(self, board_size, mine_count, starting_x, starting_y):
        self.board=[[0 for i in range(board_size)] for j in range(board_size)]
        self.board_size=board_size
        self.mine_count=mine_count
        self.t= t.Turtle()
        screen = t.Screen()
        screen.screensize(1200, 1200)
        self.arrow = t.Turtle()
        self.arrow.hideturtle()
        self.arrow.speed(0)
        print(mine_count)
        self.selectAbleSpots=board_size**2-mine_count
        while mine_count!=0:
            x=r.randint(0,board_size-1)
            y=r.randint(0,board_size-1)
            if self.board[y][x]==0:
                if y==starting_y and x==starting_x:
                    continue
                mine_count-=1
                self.board[y][x]="M"
        for i in range(board_size):
            for j in range(board_size):
                if self.board[i][j]!="M":
                    self.add_mines(j, i)

    def __str__(self):
        returnstr=""
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j]==0:
                    returnstr+="_ "
                else:
                    returnstr+=str(self.board[i][j])+" "
            returnstr+="\n"
        return returnstr

    def reveal_tiles(self, x, y, player_board):
        player_board[y][x]=1
        self.selectAbleSpots-=1
        if self.board[y][x]=="M":
            return False
        if self.board[y][x]==0:
            for i in range(x-1,x+2):
                if i>=0 and i<self.board_size:
                    if y-1>=0:
                        reveal_tiles(i, y-1, player_board, self.board, self.board_size)
                    if y+1<self.board_size:
                        reveal_tiles(i, y+1, player_board, self.board, self.board_size)
                if i-1>=0:
                    reveal_tiles(i-1, y, player_board, self.board, self.board_size)
                if i+1<self.board_size:
                    reveal_tiles(i+1, y, player_board, self.board, self.board_size)
            return True 
        else:
            return True   

    def add_mines(self, x, y):
        count=0
        for i in range(x-1,x+2):
            if i<self.board_size and i>=0:
                if y-1>=0 and self.board[y-1][i]=="M":
                    count+=1
                if y+1<self.board_size and self.board[y+1][i]=="M":
                    count+=1
                if self.board[y][i]=="M":
                    count+=1
        self.board[y][x]=count     

    def is_winner(self):
        return self.selectAbleSpots==0

    def draw_square(self, x ,y, text):
        self.arrow.penup()
        self.arrow.goto(x,y)
        self.arrow.pendown()
        side_length=1200/self.board_size
        for i in range(4):
            self.arrow.forward(side_length)
            self.arrow.right(90)
        self.arrow.penup()
        self.arrow.goto(x+side_length/2,y-side_length/2)
        self.arrow.write(text)
        self.arrow.pendown()
        t.done()


def print_grid(grid, player_board):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if player_board[i][j]==0:
                print("_", end="")
            else:
                print(f"{grid[i][j]}", end="")
        print()
 

# def mine_sweeper(mine_count, board_size, starting_x, starting_y):
#     board=[[0 for i in range(board_size)] for j in range(board_size)]
    
#     while mine_count!=0:
#         x=r.randint(0,board_size-1)
#         y=r.randint(0,board_size-1)
#         if board[y][x]==0:
#             if y==starting_y and x==starting_x:
#                 continue
#             mine_count-=1
#             board[y][x]="M"
#     for i in range(x-1,x+2):

#         count=0
#         if y>=0 and y<board_size:
#             if i-1>=0 and board[y][i-1]=="M":
#                 count+=1
#             if i+1<board_size and board[y][i+1]=="M":
#                 count+=1
#         if y-1>=0 and board[y-1][i]=="M":
#             count+=1
#         if y+1<board_size and board[y+1][i]=="M":
#             count+=1
#         board[y][i]=count
    
#     for j in range(board_size):
#         for k in range(board_size):

#     return board        
# """            
        # if i-1>=0 and j-1>=0 and board[i-1][j-1]=="M":
        #     count+=1
        # if  i-1>=0 and board[i-1][j]=="M":
        #     count+=1
        # if i-1>=0 and j+1<board_size and board[i-1][j+1]=="M":
        #     count+=1
        # if j-1>=0 and board[i][j-1]=="M":
        #     count+=1
        # if j+1<board_size and board[i][j+1]=="M":
        #     count+=1        
        # if i+1<board_size and j-1>=0 and board[i+1][j-1]=="M":
        #     count+=1
        # if i+1<board_size and board[i+1][j]=="M":
        #     count+=1    
        # if i+1<board_size and j+1<board_size and board[i+1][j+1]=="M":
        #     count+=1
"""        
        

def reveal_tiles(x, y, player_board, board, board_size):
    player_board[y][x]=1
    if board[y][x]=="M":
        return False
    if board[y][x]==0:
        for i in range(x-1,x+2):
            if i>=0 and i<board_size:
                if y-1>=0:
                    reveal_tiles(i, y-1, player_board, board, board_size)
                if y+1<board_size:
                    reveal_tiles(i, y+1, player_board, board, board_size)
            if i-1>=0:
                reveal_tiles(i-1, y, player_board, board, board_size)
            if i+1<board_size:
                reveal_tiles(i+1, y, player_board, board, board_size)
        return True 
    else:
        return True
"""        



# def main():
#     game_over=False
#     game_win=False
#     board_size=int(input("What board size do you want: "))
#     bombs=int((board_size**2)*0.16)
#     starting_x=int(input("What do you want your starting x-cordinate to be: "))
#     starting_y=int(input("What do you want your starting y-cordinate to be: "))
#     player_board=[[0 for i in range(board_size)] for j in range(board_size)]
    
#     board=mine_sweeper(bombs, board_size, starting_x, starting_y)
#     reveal_tiles(starting_x, starting_y, player_board, board, board_size)
#     print_grid(board, player_board)
#     while not game_over:
#         x=int(input("What x-coordinate to do want to reveal: "))
#         y=int(input("What y-coordinate to do want to reveal: "))
#         reveal_tiles(x,y, player_board, board, board_size)
#         print_grid(board, player_board)
#         print_grid(board, board)
#         if player_board[y][x]=="M":
#             game_state=="Game Over"
    
#     if game_win:
#         print("You win")
#     else:
#         print("You lose")
    
# main()

def main():
    game_over=False
    game_win=False
    board_size=int(input("What board size do you want: "))
    bombs=int((board_size**2)*0.16)
    starting_x=int(input("What do you want your starting x-cordinate to be: "))
    starting_y=int(input("What do you want your starting y-cordinate to be: "))
    board=board_class(board_size, bombs, starting_x, starting_y)
    board.draw_square(0,0, "hi")
    print(board)
main()
