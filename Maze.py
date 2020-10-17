import Cell, random
import numpy as np

class Maze():
    def __init__(self,rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = []
        self.path=[]

    def generate_maze_sol(self, rows, columns, n_neighbours, movements, movements_id):
        self.rows = rows
        self.columns = columns
        self.n_neighbours = n_neighbours
        self.movements = movements
        self.movements_id = movements_id

    def init_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.columns):
                self.grid[i].append(Cell.Cell(i, j))
    def getMaze(self):
        return self.grid

    def check_maze(self):
        complete=True
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j].visited== False:
                    complete = False
        return complete

    def Choose_Starting_Cell(self):
        initialCellX = random.randint(0, self.columns - 1)
        initialCellY = random.randint(0, self.rows - 1)
        self.grid[initialCellY][initialCellX].setVisited()
        return (initialCellX, initialCellY)

    def Choose_Random_Cell(self):
        choosen=False
        while not choosen:
            self.CurrentCellX = random.randint(0, self.columns - 1)
            self.CurrentCellY = random.randint(0, self.rows - 1)
            if self.grid[self.CurrentCellX][self.CurrentCellY].getVisited() == False:
                self.grid[self.CurrentCellX][self.CurrentCellY].setOnTrace()
                choosen = True

    def randomize_dir(self):
        choosen=False
        while not choosen:
            direction=random.randint(0,3)
            
            if direction==0 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "N" and self.CurrentCellX-1!=-1:
                print("North")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("N")
                self.CurrentCellX-=1
                print("Vamos al Norte. Posición en X= ", self.CurrentCellX, "Posición en Y= ", self.CurrentCellY)
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("S")
                choosen = True
            elif direction==1 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "E" and self.CurrentCellY+1!=self.columns:
                print("east")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("E")
                self.CurrentCellY+=1
                print("Vamos al Este. Posición en X= ", self.CurrentCellX, "Posición en Y= ", self.CurrentCellY)
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("W")
                choosen = True
            elif direction==2 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "S" and self.CurrentCellX+1!=self.rows:
                print("South")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("S")
                self.CurrentCellX+=1
                print("Vamos al Sur. Posición en X= ", self.CurrentCellX, "Posición en Y= ", self.CurrentCellY)
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("N")
                choosen = True
            elif direction==3 and self.grid[self.CurrentCellX][self.CurrentCellY].getDirection() != "W" and self.CurrentCellY-1!=-1:
                print("West")
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("W")
                self.CurrentCellY-=1
                print("Vamos al Oeste. Posición en X= ", self.CurrentCellX, "Posición en Y= ", self.CurrentCellY)
                self.grid[self.CurrentCellX][self.CurrentCellY].setNeighbour("E")
                choosen = True

    def generate_lab(self):
        self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])
        while self.grid[self.CurrentCellX][self.CurrentCellY].getVisited()==False:
            self.randomize_dir()

            self.path.append(self.grid[self.CurrentCellX][self.CurrentCellY])

            if self.grid[self.CurrentCellX][self.CurrentCellY].isOnTrace()==True:
                print("Cicle")
                cellPopped=self.path.pop()
                while cellPopped.getPosition==() != (self.CurrentCellX,self.CurrentCellY):
                    cellPopped.setDefault()
                    cellPopped=path.pop()
            self.grid[self.CurrentCellX][self.CurrentCellY].setOnTrace()
            
            
    def iterate(self):
        self.Choose_Starting_Cell()
        while self.check_maze()==False:
            self.Choose_Random_Cell()
            self.generate_lab()
            for cell in self.path:
                cell.setVisited()

    def printMaze(self):
        for x in self.grid:
            for y in x:
                print(y.getNeigh(), end=" ")
            print()