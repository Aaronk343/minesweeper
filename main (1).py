import random as r
import turtle as t

 
#m is mine
class board_class():
    def __init__(self, board_size, mine_count, starting_x, starting_y):
        self.board=[[0 for i in range(board_size)] for j in range(board_size)]
        self.board_size=board_size
        self.mine_count=mine_count
        self.game_over=False
        self.win=False
        self.t= t.Turtle()
        screen = t.Screen()
        screen.screensize(1000, 1000)
        self.arrow = t.Turtle()
        self.arrow.hideturtle()
        self.arrow.speed(0)
        t.tracer(0)
        print(mine_count)
        self.selectAbleSpots=board_size**2-mine_count
        while mine_count!=0:
            x=r.randint(0,board_size-1)
            y=r.randint(0,board_size-1)
            if self.board[y][x]==0:
                if y==starting_y and x==starting_x:
                    continue
                if y==starting_y-1 and x==starting_x-1:
                    continue
                if y==starting_y-1 and x==starting_x:
                    continue
                if y==starting_y-1 and x==starting_x+1:
                    continue
                if y==starting_y and x==starting_x-1:
                    continue
                if y==starting_y and x==starting_x+1:
                    continue
                if y==starting_y+1 and x==starting_x-1:
                    continue
                if y==starting_y+1 and x==starting_x:
                    continue
                if y==starting_y+1 and x==starting_x+1:
                    continue
                mine_count-=1
                self.board[y][x]="M"

        for i in range(board_size):
            for j in range(board_size):
                if self.board[i][j]!="M":
                    self.add_mines(j, i)
        self.player_board=[[0 for i in range(self.board_size)]for j in range(self.board_size)]
        self.reveal_tiles(starting_x, starting_y)
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

    def reveal_tiles(self, x, y):
        if self.player_board[y][x] == 1:
            return True

        if self.board[y][x] == "M":
            return False

        self.player_board[y][x] = 1
        self.selectAbleSpots -= 1

        if self.board[y][x] == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx = x + dx
                    ny = y + dy

                    if dx == 0 and dy == 0:
                        continue

                    if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                        self.reveal_tiles(nx, ny)

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
        side_length=1000/self.board_size
        
        for i in range(4):
            
            self.arrow.forward(side_length)
            self.arrow.right(90)
        self.arrow.penup()
        self.arrow.goto(x+side_length/2,y-side_length/2)
        self.arrow.write(text)
        self.arrow.pendown()
        t.update()
    
    def draw_board(self):
        side_length=1000/self.board_size
        t.resetscreen()
        for i in range(self.board_size):
            for j in range(self.board_size):
                
                if self.player_board[i][j]==1:
                    self.draw_square((j*side_length)-500, (1000-i*side_length)-500, "" if self.board[i][j]==0 else self.board[i][j] )
                elif self.player_board[i][j]=="F":
                    self.draw_square((j*side_length)-500, (1000-i*side_length)-500, "🚩")
                
                else:
                    self.draw_square((j*side_length)-500, (1000-i*side_length)-500, "")
                    
    
    def handle_click(self, x, y):
        
        print(x,y)
        side_length=1000/self.board_size
        self.arrow.penup()      
        box_x=(x+500)/side_length
        box_y=(500-y)/side_length
        box_x=int(box_x)
        box_y=int(box_y)
        print(box_x, box_y)
        cond=self.reveal_tiles(box_x, box_y)
        self.player_board[box_y][box_x]=1
        if self.board[box_y][box_x]=="M":
            self.handle_game_over()
            return
        elif self.selectAbleSpots==0:
            self.win=True
            self.handle_game_over()
            return
        self.draw_board()
        
    def handle_click_flag(self, x, y):
        
        print(x,y)
        side_length=1000/self.board_size
        self.arrow.penup()      
        box_x=(x+500)/side_length
        box_y=(500-y)/side_length
        box_x=int(box_x)
        box_y=int(box_y)
        print(box_x, box_y)
        if self.player_board[box_y][box_x]==1:
            return
        if self.player_board[box_y][box_x]=="F":
            self.player_board[box_y][box_x]=0
        else:
            self.player_board[box_y][box_x]="F"
        
        self.draw_board()
    def handle_game_over(self):
        self.t.clear()
        self.arrow.penup()
        self.arrow.goto(0,0)
        self.arrow.pendown()
        if self.win==True:
            self.arrow.write("You Win")
        else:
            self.arrow.write("You Lose")

def main():
    
    board_size=int(input("What board size do you want: "))
    bombs=int((board_size**2)*0.16)
    starting_x=int(input("What do you want your starting x-cordinate to be: "))
    starting_y=int(input("What do you want your starting y-cordinate to be: "))
    board=board_class(board_size, bombs, starting_x, starting_y)
    board.draw_board()
    print(board)
    
    board.t.screen.onclick(board.handle_click, btn=1)
    board.t.screen.onclick(board.handle_click_flag, btn=3)
    t.done()

main()
