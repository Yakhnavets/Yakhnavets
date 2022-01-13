import pygame
import sys
import abc

WIDTH = 600
HEIGHT = 600
SQUARE = 200

COLOR_CIRCLE = (21, 237, 72)
COLOR_CROSS = (11, 33, 230)

LINE_COLOR = (0, 0, 0)
BG_COLOR = (219,226,233)

LINE_WIDTH = 10
PADDING = 55

board = [[0]*3 for i in range(3)]
pygame.init()
screnn = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe Game")
screnn.fill(BG_COLOR)

class Graphic(abc.ABC):

    @abc.abstractclassmethod
    def drawingFigure(self):
        pass

class Board(Graphic):

    def drawingFigure(self):
        Graphic.drawingFigure()
        pygame.draw.line(screnn, LINE_COLOR, (0, SQUARE), (WIDTH, SQUARE), LINE_WIDTH)
        pygame.draw.line(screnn, LINE_COLOR, (0, (2 * SQUARE)), (WIDTH, 2 * SQUARE), LINE_WIDTH)
        pygame.draw.line(screnn, LINE_COLOR, (SQUARE, 0), (SQUARE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screnn, LINE_COLOR, (2 * SQUARE, 0), (2 * SQUARE, HEIGHT), LINE_WIDTH)

    @staticmethod
    def update():
        pygame.display.update()

class Circle(Graphic):

    def __init__(self, radius, lineWidth):
        self.radius = radius
        self.lineWidth = lineWidth

    def drawingFigure(self):
        super().drawingFigure()
        for row in range(3):
            for column in range(3):
                if board[row][column] == 'o':
                    pygame.draw.circle(screnn, COLOR_CIRCLE, (int(column * SQUARE + SQUARE // 2), int(row * SQUARE + SQUARE // 2)), self.radius, self.lineWidth)

class Cross(Graphic):

    def __init__(self, height, lineWidth):
        self.lineWidth = lineWidth

    def drawingFigure(self):
        super().drawingFigure()
        for row in range(3):
            for column in range(3):
                if board[row][column] == 'x':
                    pygame.draw.line(screnn, COLOR_CROSS, (column * SQUARE + PADDING, row * SQUARE + SQUARE - PADDING), (column * SQUARE + SQUARE - PADDING, row*SQUARE + PADDING), self.lineWidth)
                    pygame.draw.line(screnn, COLOR_CROSS, (column * SQUARE + PADDING, row * SQUARE + PADDING), (column * SQUARE + SQUARE - PADDING, row * SQUARE + SQUARE - PADDING), self.lineWidth)

class Game:

    @staticmethod
    def chooseSquare(row, column, team):
        board[row][column] = team

    @staticmethod
    def avaliableMove(row, column):
        if board[row][column] == 0:
            return True
        else:
            return False

    @staticmethod
    def changeTeam(team):
        if team == 'o':
            team = 'x'
            return team
        else:
            team = 'o'
            return team

    @ staticmethod
    def isWin(team):
        flag = False

        if board[0][0] == team and board[1][1] == team and board[2][2] == team:
            flag = True
            print(f"Team {team} win")

        if board[0][2] == team and board[1][1] == team and board[2][0] == team:
            flag = True
            print(f"Team {team} win")

        for i in range(3):
            if all(board[i][j]==team for j in range(3)) or all(board[j][i] == team for j in range(3)):
                flag = True
                print(f"Team {team} win")
                break
        return flag 

    @staticmethod
    def isFull():
        tmp = []
        for i in range(3):
            for j in range(3):
                tmp.append(board[i][j])
        if all(tmp) != 0:
            return True
        else:
            return False

def main():
    node = Board()
    circle = Circle(80, 10)
    cross = Cross(100, 10)
    g = Game()
    node.drawingFigure()
    node.update()

    team = 'o'
    endGame = False
    while True:
        if endGame:
            break
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickRow = int(event.pos[1] // SQUARE)
                    clickColumn = int(event.pos[0] // SQUARE)
                    if g.avaliableMove(clickRow, clickColumn):
                        g.chooseSquare(clickRow, clickColumn, team)

                        if g.isWin(team):
                            node.update()
                            endGame = True

                        if team == 'o':
                            circle.drawingFigure()
                            node.update()

                        if team == 'x':
                            cross.drawingFigure()
                            node.update()

                        team = g.changeTeam(team)
        if g.isFull():
            print(f"Nobody's win")
            break

if __name__ == "__main__":
    main() 