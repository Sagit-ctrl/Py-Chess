import pygame, sys, random
from pygame.locals import *
import time

# Tạo sẵn các màu sắc
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0, 100)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
SILVER = (215, 215, 215)
YELLOW = (255, 255, 0, 100)
CYAN = (0, 255, 255, 100)
SILVER = (215, 215, 215)
EMPTY = (0, 0, 0, 0)
# Thông số cơ bản
WIDTH = 70
HEIGHT = 70
NUM_X = 8
NUM_Y = 8
WINDOWWIDTH = WIDTH*NUM_X + WIDTH
WINDOWHEIGHT = HEIGHT*NUM_Y + HEIGHT
EXTRAWIDTH = WIDTH * 4
EXTRAHEIGHT = HEIGHT * 4
# Khởi tạo tham số, GUI game
pygame.init()
FPS = 6
fpsClock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), SRCALPHA, pygame.RESIZABLE)
SCREEN.fill(SILVER)
pygame.display.set_caption('Chess')

background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (WINDOWWIDTH, WINDOWHEIGHT))

b_bishop = pygame.image.load("img/BB.png")
b_king = pygame.image.load("img/BK.png")
b_knight = pygame.image.load("img/BN.png")
b_pawn = pygame.image.load("img/BP.png")
b_queen = pygame.image.load("img/BQ.png")
b_rook = pygame.image.load("img/BR.png")

w_bishop = pygame.image.load("img/WB.png")
w_king = pygame.image.load("img/WK.png")
w_knight = pygame.image.load("img/WN.png")
w_pawn = pygame.image.load("img/WP.png")
w_queen = pygame.image.load("img/WQ.png")
w_rook = pygame.image.load("img/WR.png")

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (WIDTH * 4/5, HEIGHT * 4/5)))

for img in w:
    W.append(pygame.transform.scale(img, (WIDTH * 4/5, HEIGHT * 4/5)))

coreunit = [
            # [id, name, id_type, type, color, row, col, status, move_],
            [0, 'BR1', 5, 'ROOK', 'B', 0, 0, 'T', 0],
            [1, 'BN1', 2, 'KNIGHT', 'B', 0, 1, 'T', 0],
            [2, 'BB1', 0, 'BISHOP', 'B', 0, 2, 'T', 0],
            [3, 'BQ', 4, 'QUEEN', 'B', 0, 3, 'T', 0],
            [4, 'BK', 1, 'KING', 'B', 0, 4, 'T', 0],
            [5, 'BB2', 0, 'BISHOP', 'B', 0, 5, 'T', 0],
            [6, 'BN2', 2, 'KNIGHT', 'B', 0, 6, 'T', 0],
            [7, 'BR2', 5, 'ROOK', 'B', 0, 7, 'T', 0],
            [8, 'BP1', 3, 'PAWN', 'B', 1, 0, 'T', 0],
            [9, 'BP2', 3, 'PAWN', 'B', 1, 1, 'T', 0],
            [10, 'BP3', 3, 'PAWN', 'B', 1, 2, 'T', 0],
            [11, 'BP4', 3, 'PAWN', 'B', 1, 3, 'T', 0],
            [12, 'BP5', 3, 'PAWN', 'B', 1, 4, 'T', 0],
            [13, 'BP6', 3, 'PAWN', 'B', 1, 5, 'T', 0],
            [14, 'BP7', 3, 'PAWN', 'B', 1, 6, 'T', 0],
            [15, 'BP8', 3, 'PAWN', 'B', 1, 7, 'T', 0],
            [16, 'WR1', 5, 'ROOK', 'W', 7, 0, 'T', 0],
            [17, 'WN1', 2, 'KNIGHT', 'W', 7, 1, 'T', 0],
            [18, 'WB1', 0, 'BISHOP', 'W', 7, 2, 'T', 0],
            [19, 'WQ', 4, 'QUEEN', 'W', 7, 3, 'T', 0],
            [20, 'WK', 1, 'KING', 'W', 7, 4, 'T', 0],
            [21, 'WB2', 0, 'BISHOP', 'W', 7, 5, 'T', 0],
            [22, 'WN2', 2, 'KNIGHT', 'W', 7, 6, 'T', 0],
            [23, 'WR2', 5, 'ROOK', 'W', 7, 7, 'T', 0],
            [24, 'WP1', 3, 'PAWN', 'W', 6, 0, 'T', 0],
            [25, 'WP2', 3, 'PAWN', 'W', 6, 1, 'T', 0],
            [26, 'WP3', 3, 'PAWN', 'W', 6, 2, 'T', 0],
            [27, 'WP4', 3, 'PAWN', 'W', 6, 3, 'T', 0],
            [28, 'WP5', 3, 'PAWN', 'W', 6, 4, 'T', 0],
            [29, 'WP6', 3, 'PAWN', 'W', 6, 5, 'T', 0],
            [30, 'WP7', 3, 'PAWN', 'W', 6, 6, 'T', 0],
            [31, 'WP8', 3, 'PAWN', 'W', 6, 7, 'T', 0]]

history_move = [
    # [start move, stop move, kill = False, id_unit = None ],
]
# Các hàm xử lý
def process_mouse_pos(pos):
    if pos[0] >= WIDTH and pos[0] <= WINDOWWIDTH and pos[1] >= HEIGHT and pos[1] <= WINDOWHEIGHT:
        x = int((pos[0] - WIDTH) / WIDTH)
        y = int((pos[1] - HEIGHT) / HEIGHT)
        return [x, y]
    else:
        return [-1, -1]

def find_unit_by_pos(pos):
    for unit in coreunit:
        if unit[7] == "T" and [unit[6], unit[5]] == pos:
            return True, unit[0]
    return False, -1

def find_color_unit(id_unit, mode):
    list_unit = []
    if mode == "S":
        for unit in coreunit:
            if unit[7] == "T" and unit[4] == coreunit[id_unit][4]:
                list_unit.append([unit[6], unit[5]])
        return list_unit
    else:
        for unit in coreunit:
            if unit[7] == "T" and unit[4] != coreunit[id_unit][4]:
                list_unit.append([unit[6], unit[5]])
        return list_unit

def posible_move_straight(id_unit, ls):
    same_color = find_color_unit(id_unit, "S")
    diff_color = find_color_unit(id_unit, "D")
    ls1 = []
    check_find = True
    index = None
    same_or_diff = True
    dif = []
    for unit in ls:
        if unit[0] >= 0 and unit[0] <= 7 and unit[1] >= 0 and unit[1] <=7:
            ls1.append(unit)

    for unit in ls1:
        for same in same_color:
            if unit == same and check_find:
                index = ls1.index(same)
                check_find = False

    for unit in ls1:
        for diff in diff_color:
            if unit == diff and check_find:
                index = ls1.index(diff)
                same_or_diff = False
                check_find = False

    if index != None:
        if not same_or_diff and ls1 != []:
            ls1 = ls1[:index + 1]
            dif = ls1[-1]
        else:
            ls1 = ls1[:index]
    return ls1, dif

def posible_move_around(id_unit, ls):
    same_color = find_color_unit(id_unit, "S")
    diff_color = find_color_unit(id_unit, "D")
    ls1 = []
    diff = []
    move = []

    for unit in ls:
        if unit[0] >= 0 and unit[0] <= 7 and unit[1] >= 0 and unit[1] <=7:
            ls1.append(unit)

    for unit in ls1:
        if same_color.count(unit) == 0 and diff_color.count(unit) == 0:
            move.append(unit)

    for unit in ls1:
        if diff_color.count(unit) != 0:
            diff.append(unit)

    return move, diff

def Bishop_Move_Set(id_unit):
    unit_main = coreunit[id_unit]
    top_left_move = []
    top_right_move = []
    bottom_right_move = []
    bottom_left_move = []
    move = []
    diff = []
    for i in range(1, 9):
        top_left_move.append([unit_main[6] - i, unit_main[5] - i])
        top_right_move.append([unit_main[6] + i, unit_main[5] - i])
        bottom_right_move.append([unit_main[6] + i, unit_main[5] + i])
        bottom_left_move.append([unit_main[6] - i, unit_main[5] + i])

    top_left, top_left_diff = posible_move_straight(id_unit, top_left_move)
    top_right, top_right_diff = posible_move_straight(id_unit, top_right_move)
    bottom_right, bottom_right_diff = posible_move_straight(id_unit, bottom_right_move)
    bottom_left, bottom_left_diff = posible_move_straight(id_unit, bottom_left_move)

    move.extend(top_left)
    move.extend(top_right)
    move.extend(bottom_right)
    move.extend(bottom_left)

    diff.append(top_left_diff)
    diff.append(top_right_diff)
    diff.append(bottom_right_diff)
    diff.append(bottom_left_diff)

    dif = []
    for difs in diff:
        if difs != []:
            dif.append(difs)

    return move, dif

def King_Move_Set(id_unit):
    unit_main = coreunit[id_unit]
    moveset = [[unit_main[6] - 1, unit_main[5] - 1],
               [unit_main[6], unit_main[5] - 1],
               [unit_main[6] + 1, unit_main[5] - 1],
               [unit_main[6] - 1, unit_main[5]],
               [unit_main[6] + 1, unit_main[5]],
               [unit_main[6] - 1, unit_main[5] + 1],
               [unit_main[6], unit_main[5] + 1],
               [unit_main[6] + 1, unit_main[5] + 1]]

    move, diff = posible_move_around(id_unit, moveset)

    if unit_main[4] == "B":
        id_rook1 = 0
        id_rook2 = 7
        if king_rook(id_unit, id_rook1):
            move.append([0, 0])
        elif king_rook(id_unit, id_rook2):
            move.append([7, 0])

    if unit_main[4] == "W":
        id_rook1 = 16
        id_rook2 = 23
        if king_rook(id_unit, id_rook1):
            move.append([0, 7])
        elif king_rook(id_unit, id_rook2):
            move.append([7, 7])

    return move, diff

def Knight_Move_Set(id_unit):
    unit_main = coreunit[id_unit]

    moveset = [
        [unit_main[6] + 1, unit_main[5] - 2],
        [unit_main[6] - 1, unit_main[5] - 2],
        [unit_main[6] + 1, unit_main[5] + 2],
        [unit_main[6] - 1, unit_main[5] + 2],
        [unit_main[6] - 2, unit_main[5] + 1],
        [unit_main[6] - 2, unit_main[5] - 1],
        [unit_main[6] + 2, unit_main[5] + 1],
        [unit_main[6] + 2, unit_main[5] - 1],
    ]

    move, diff = posible_move_around(id_unit, moveset)

    return move, diff

def Pawn_Move_Set(id_unit):
    unit_main = coreunit[id_unit]
    moveset = []
    if unit_main[4] == "W" and unit_main[8] == 0:
        moveset = [
            [unit_main[6], unit_main[5] - 1],
            [unit_main[6], unit_main[5] - 2],
            [unit_main[6] + 1, unit_main[5] - 1],
            [unit_main[6] - 1, unit_main[5] - 1],
        ]
    elif unit_main[4] == "W" and unit_main[8] != 0:
        moveset = [
            [unit_main[6], unit_main[5] - 1],
            [unit_main[6] + 1, unit_main[5] - 1],
            [unit_main[6] - 1, unit_main[5] - 1],
        ]
    elif unit_main[4] == "B" and unit_main[8] == 0:
        moveset = [
            [unit_main[6], unit_main[5] + 1],
            [unit_main[6], unit_main[5] + 2],
            [unit_main[6] + 1, unit_main[5] + 1],
            [unit_main[6] - 1, unit_main[5] + 1],
        ]
    elif unit_main[4] == "B" and unit_main[8] != 0:
        moveset = [
            [unit_main[6], unit_main[5] + 1],
            [unit_main[6] + 1, unit_main[5] + 1],
            [unit_main[6] - 1, unit_main[5] + 1],
        ]

    move, diff = posible_move_around(id_unit, moveset)
    moveout = []
    diffout = []
    for mov in move:
        if mov[0] - coreunit[id_unit][6] == 0:
            moveout.append(mov)
    for dif in diff:
        if dif[0] - coreunit[id_unit][6] != 0:
            diffout.append(dif)
    return moveout, diffout

def Rook_Move_Set(id_unit):
    unit_main = coreunit[id_unit]
    top_move = []
    right_move = []
    bottom_move = []
    left_move = []
    move = []
    diff = []
    for i in range(1, 9):
        top_move.append([unit_main[6], unit_main[5] - i])
        right_move.append([unit_main[6] + i, unit_main[5]])
        bottom_move.append([unit_main[6], unit_main[5] + i])
        left_move.append([unit_main[6] - i, unit_main[5]])

    top, top_diff = posible_move_straight(id_unit, top_move)
    right, right_diff = posible_move_straight(id_unit, right_move)
    bottom, bottom_diff = posible_move_straight(id_unit, bottom_move)
    left, left_diff = posible_move_straight(id_unit, left_move)

    move.extend(top)
    move.extend(right)
    move.extend(bottom)
    move.extend(left)

    diff.append(top_diff)
    diff.append(right_diff)
    diff.append(bottom_diff)
    diff.append(left_diff)

    dif = []
    for difs in diff:
        if difs != []:
            dif.append(difs)

    return move, dif

def Queen_Move_Set(id_unit):
    move = []
    diff = []
    b_move, b_diff = Bishop_Move_Set(id_unit)
    r_move, r_diff = Rook_Move_Set(id_unit)

    move.extend(b_move)
    move.extend(r_move)
    diff.extend(b_diff)
    diff.extend(r_diff)

    return move, diff

def move_set(id_unit):
    unit_main = coreunit[id_unit]
    if unit_main[3] == "BISHOP":
        return Bishop_Move_Set(unit_main[0])
    if unit_main[3] == "KING":
        return King_Move_Set(unit_main[0])
    if unit_main[3] == "KNIGHT":
        return Knight_Move_Set(unit_main[0])
    if unit_main[3] == "PAWN":
        return Pawn_Move_Set(unit_main[0])
    if unit_main[3] == "ROOK":
        return Rook_Move_Set(unit_main[0])
    if unit_main[3] == "QUEEN":
        return Queen_Move_Set(unit_main[0])

def check_danger_for_king(id_unit, move, diff):
    unit_main = coreunit[id_unit]
    index = []
    if unit_main[4] == "W":
        for unit in coreunit:
            if unit[4] == "B":
                index.append(unit[0])
    elif unit_main[4] == "B":
        for unit in coreunit:
            if unit[4] == "W":
                index.append(unit[0])
    danger = []
    for i in range(len(index)):
        dangermove, diffmove = move_set(index[i])
        if coreunit[index[i]][3] != "PAWN":
            danger.extend(dangermove)
        danger.extend(diffmove)

    for dan in danger:
        if move.count(dan) != 0:
            move.remove(dan)
        if diff.count(dan) != 0:
            diff.remove(dan)
    return move, diff

def checkmate(id_unit):
    unit_main = coreunit[id_unit]
    index = []
    if unit_main[4] == "W":
        for unit in coreunit:
            if unit[4] == "B" and unit[7] == "T":
                index.append(unit[0])
    elif unit_main[4] == "B":
        for unit in coreunit:
            if unit[4] == "W" and unit[7] == "T":
                index.append(unit[0])
    danger = []
    for i in range(len(index)):
        dangermove, diffmove = move_set(index[i])
        danger.extend(dangermove)
        danger.extend(diffmove)

    if danger.count([unit_main[6], unit_main[5]]) != 0:
        return True
    else:
        return False

def king_rook(id_king, id_rook):

    para1 = True
    para2 = True
    para3 = True
    para6 = True
    para5 = True

    if coreunit[id_king][4] == "B":
        para1, nouse = find_unit_by_pos([1, 0])
        para2, nouse = find_unit_by_pos([2, 0])
        para3, nouse = find_unit_by_pos([3, 0])
        para5, nouse = find_unit_by_pos([5, 0])
        para6, nouse = find_unit_by_pos([6, 0])

    if coreunit[id_king][4] == "W":
        para1, nouse = find_unit_by_pos([1, 7])
        para2, nouse = find_unit_by_pos([2, 7])
        para3, nouse = find_unit_by_pos([3, 7])
        para5, nouse = find_unit_by_pos([5, 7])
        para6, nouse = find_unit_by_pos([6, 7])

    if coreunit[id_king][3] == "KING" and coreunit[id_rook][3] == "ROOK":
        if coreunit[id_king][8] == 0 and coreunit[id_rook][8] == 0:
            if coreunit[id_rook][0] == 0 and not para1 and not para2 and not para3 and coreunit[id_king][4] == "B":
                return True
            elif coreunit[id_rook][0] == 7 and not para5 and not para6 and coreunit[id_king][4] == "B":
                return True

    if coreunit[id_king][3] == "KING" and coreunit[id_rook][3] == "ROOK":
        if coreunit[id_king][8] == 0 and coreunit[id_rook][8] == 0:
            if coreunit[id_rook][0] == 16 and not para1 and not para2 and not para3 and coreunit[id_king][4] == "W":
                return True
            elif coreunit[id_rook][0] == 23 and not para5 and not para6 and coreunit[id_king][4] == "W":
                return True

    return False

def pawn_queen(id_pawn):
    unit_main = coreunit[id_pawn]
    if unit_main[4] == "B" and unit_main[5] == 7 and unit_main[7] == "T":
        coreunit[id_pawn] = [id_pawn, "QP", 4, "QUEEN", unit_main[4], unit_main[5], unit_main[6], unit_main[7], unit_main[8]]
    if unit_main[4] == "W" and unit_main[5] == 0 and unit_main[7] == "T":
        coreunit[id_pawn] = [id_pawn, "QP", 4, "QUEEN", unit_main[4], unit_main[5], unit_main[6], unit_main[7], unit_main[8]]

def display(font_size, status, font_color, X1, X2, Y1, Y2, relative = False, posxInpt = 0, posyInpt = 0):
    status = str(status)
    font = pygame.font.SysFont('consolas', font_size)
    surface = font.render(status, True, font_color)
    size = surface.get_size()
    if relative:
        posx = posxInpt
        posy = posyInpt
    else:
        posx = (X1 - size[0]) / 2 + X2
        posy = (Y1 - size[1]) / 2 + Y2
    SCREEN.blit(surface, (posx, posy))
    return [posx, posy]

def displayImage(name_file, scaleX, scaleY, X1, X2, Y1, Y2, relative = False, posx = 0, posy = 0):
    surface = pygame.image.load('image/' + str(name_file))
    surface = pygame.transform.scale(surface, (scaleX, scaleY))
    size = surface.get_size()
    if relative:
        posx = posx
        posy = posy
    else:
        posx = (X1 - size[0]) / 2 + X2
        posy = (Y1 - size[1]) / 2 + Y2
    SCREEN.blit(surface, (posx, posy))
    return [posx, posy]

# Các class cở sở
class Board():

    def __init__(self):
        self.board = coreunit
        self.move = [[-1, -1], [-1, -1], True, "W"]
        self.unit_select = -1
        self.moveset = []
        self.diff = []
        self.player = -1
        self.checkmate = [False, None]
        self.safe_king = []
        self.kill = None
        self.history = []

    def draw(self):
        SCREEN.fill(SILVER)
        SCREEN.blit(background, (0, 0))
        # if self.player == -1:
        #     player = "White"
        # else:
        #     player = "Black"
        # display(40, player, BLACK, EXTRAWIDTH, WINDOWHEIGHT, WINDOWWIDTH, - WINDOWHEIGHT / 3)
        # display(40, player, BLACK, EXTRAWIDTH, WINDOWHEIGHT, WINDOWWIDTH, + WINDOWHEIGHT / 3)

        if self.unit_select != -1:
            if self.moveset != []:
                for moveset in self.moveset:
                    x = WIDTH * (moveset[0] + 1 + 1 / 10)
                    y = HEIGHT * (moveset[1] + 1 + 1 / 10)
                    pygame.draw.rect(SCREEN, CYAN, pygame.Rect(x, y, WIDTH * 4 / 5, HEIGHT * 4 / 5))
            if self.diff != []:
                for diff in self.diff:
                    x = WIDTH * (diff[0] + 1)
                    y = HEIGHT * (diff[1] + 1)
                    pygame.draw.rect(SCREEN, RED, pygame.Rect(x, y, WIDTH, HEIGHT))

        if self.move[0] != [-1, -1] and not self.move[2]:
            x = WIDTH * (self.move[0][0] + 1)
            y = HEIGHT * (self.move[0][1] + 1)
            pygame.draw.rect(SCREEN, YELLOW, pygame.Rect(x, y, WIDTH, HEIGHT))

        if self.checkmate[0]:
            x = WIDTH * (self.board[self.checkmate[1]][6] + 1)
            y = HEIGHT * (self.board[self.checkmate[1]][5] + 1)
            pygame.draw.rect(SCREEN, RED, pygame.Rect(x, y, WIDTH, HEIGHT))

        for unit in self.board:
            if unit[4] == "B":
                img_unit = B[unit[2]]
            else:
                img_unit = W[unit[2]]

            x = WIDTH * (unit[6] + 1) + WIDTH * 1 / 10
            y = HEIGHT * (unit[5] + 1) + HEIGHT * 1 / 10

            if unit[7] == "T":
                SCREEN.blit(img_unit, (x, y))

    def func_move(self, pos):
        has_unit, id_unit_start = find_unit_by_pos(pos)
        if self.move[2]:
            if has_unit and self.board[id_unit_start][4] == self.move[3]:
                self.move[0] = pos
                self.unit_select = id_unit_start
                self.moveset, self.diff = move_set(self.unit_select)
                if coreunit[self.unit_select][3] == "KING":
                    self.moveset, self.diff = check_danger_for_king(self.unit_select, self.moveset, self.diff)

            else:
                return
        else:
            self.move[1] = pos
        self.move[2] = not self.move[2]

    def reset_unit(self):
        # self.history.append([self.move[0], self.move[1], self.unit_select, self.kill])
        if self.player == -1:
            self.move = [[-1, -1], [-1, -1], True, "W"]
        else:
            self.move = [[-1, -1], [-1, -1], True, "B"]
        self.kill = None
        self.unit_select = -1
        self.moveset = []
        self.diff = []

    def update_move(self):
        if self.unit_select != -1:
            has_unit, id_unit_stop = find_unit_by_pos(self.move[1])

            has_move = []
            has_move.extend(self.moveset)
            has_move.extend(self.diff)

            if has_move.count(self.move[1]) != 0 and not has_unit:
                self.board[self.unit_select][6] = self.move[1][0]
                self.board[self.unit_select][5] = self.move[1][1]
                self.board[self.unit_select][8] += 1
                self.player *= -1
                self.check_mate("S")
                if self.checkmate[0]:
                    self.board[self.unit_select][6] = self.move[0][0]
                    self.board[self.unit_select][5] = self.move[0][1]
                    self.board[self.unit_select][8] -= 1
                    self.player *= -1
                self.check_mate("A")

            elif has_move.count(self.move[1]) != 0 and has_unit:
                if self.board[self.unit_select][4] == self.board[id_unit_stop][4]:
                    if self.board[self.unit_select][3] == "KING" and self.board[id_unit_stop][3] == "ROOK":
                        if king_rook(self.unit_select, id_unit_stop):
                            self.board[self.unit_select][6] = self.move[1][0]
                            self.board[self.unit_select][5] = self.move[1][1]
                            self.board[self.unit_select][8] += 1
                            self.board[id_unit_stop][6] = self.move[0][0]
                            self.board[id_unit_stop][5] = self.move[0][1]
                            self.board[id_unit_stop][8] += 1
                            self.player *= -1
                            self.check_mate("S")
                            if self.checkmate[0]:
                                self.board[self.unit_select][6] = self.move[0][0]
                                self.board[self.unit_select][5] = self.move[0][1]
                                self.board[self.unit_select][8] -= 1
                                self.board[id_unit_stop][6] = self.move[1][0]
                                self.board[id_unit_stop][5] = self.move[1][1]
                                self.board[id_unit_stop][8] -= 1
                                self.player *= -1
                            self.check_mate("A")
                    else:
                        pass
                else:
                    self.board[self.unit_select][6] = self.move[1][0]
                    self.board[self.unit_select][5] = self.move[1][1]
                    self.board[self.unit_select][8] += 1
                    self.player *= -1
                    self.board[id_unit_stop][7] = "F"
                    self.kill = id_unit_stop
                    self.check_mate("S")
                    if self.checkmate[0]:
                        self.board[self.unit_select][6] = self.move[0][0]
                        self.board[self.unit_select][5] = self.move[0][1]
                        self.board[self.unit_select][8] -= 1
                        self.player *= -1
                        self.board[id_unit_stop][7] = "T"
                        self.kill = None
                    self.check_mate("A")

            elif has_move.count(self.move[1]) == 0 and self.move[1] != [-1, -1]:
                self.reset_unit()
            elif self.move[0] == self.move[1]:
                self.reset_unit()
            else:
                return
            self.pq()
            self.reset_unit()

    def check_mate(self, typ):
        if typ == "A":
            if checkmate(4):
                self.checkmate = [True, 4]
            elif checkmate(20):
                self.checkmate = [True, 20]
            else:
                self.checkmate = [False, None]
        if typ == "S":
            if self.player == -1:
                if checkmate(4):
                    self.checkmate = [True, 4]
                else:
                    self.checkmate = [False, None]
            elif self.player == 1:
                if checkmate(20):
                    self.checkmate = [True, 20]
                else:
                    self.checkmate = [False, None]

    def pq(self):
        id_p = []
        for unit in self.board:
            if unit[7] == "T" and unit[3] == "PAWN":
                id_p.append(unit[0])
        for id_pa in id_p:
            pawn_queen(id_pa)

board = Board()
def main():

    board.__init__()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board.func_move(process_mouse_pos(pos))

        board.update_move()
        board.check_mate("A")
        board.draw()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()
