import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 840
WINDOWHEIGHT = 500
REVEALSPEED = 8
BOXSIZE = 40 # 박스 사이즈
BUTTONHIGHT = 18
BUTTONWEIGHT = 100
GAPSIZE = 5 # 박스 간격
BOARDWIDTH = 10 # 가로 박스 수
BOARDHEIGHT = 10 # 세로 박스 수
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)   # 가로 간격
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2) # 세로 간격

#            R    G    B
GRAY     = (170, 170, 170)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
BLACK    = (0, 0, 0)
BLUE     = ( 59, 139, 212)      # 색이름에 RGB값 지정

water = pygame.image.load("image/water.jpg")        # water변수에 배경이미지 지정

BGCOLOR = BLUE      # 배경색 : blue
BOXCOLOR = WHITE        # 가리는 상자 색 : white
TEXTCOLOR = BLACK       # 글씨 색 : black

click = 0
score = 1       # 점수에 쓰일 변수값 기초

list = [
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        ]

save = [
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
           [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        ]                                               # 게임


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, SPECIALFONT, ENDFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))  # 게임판 지정 
    BASICFONT = pygame.font.Font('HoonWhitecatR.ttf',18)    # 글씨 폰트 변수 지정
    SPECIALFONT = pygame.font.Font('HoonWhitecatR.ttf', 60)
    ENDFONT = pygame.font.Font('HoonWhitecatR.ttf', 25)
   
    mousex = 0 # 마우스의 x값 저장할 변수
    mousey = 0 # 마우스의 y값 저장할 변수
    pygame.display.set_caption('Battle Ship')   # 게임 이름


    DISPLAYSURF.fill(BGCOLOR)   # 배경 색 설정

    
    randomizeList(list, save) # 게임 판 설정
    runGame()       # 게임 실행

    if score >= 18:
        gameWon()
    else:
        gameOver()
    pygame.display.update()
    pygame.time.wait(2500)
    

def runGame():
    global click, score, menu
    revealedBoxes = generateRevealedBoxesData(False)
    mainBoard = []    # 게임판 설정
    DISPLAYSURF.blit(water, (0,0))          # 배경 이미지 지정

    pygame.display.flip()


    while True:
        mouseClicked = False

        drawBoard(mainBoard, revealedBoxes) # 게임판 그리기
        drawMenu(mainBoard)

        if score == 18:
            return 0

        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):   # 게임 종료 조건
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:     # 마우스의 움직임 저장
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
                if mousex >= WINDOWWIDTH - 155 and mousex <= WINDOWWIDTH - 55:
                    if mousey>= WINDOWHEIGHT- 80 and mousey <= WINDOWHEIGHT - 62:
                        # 종료
                        return 0
                    
        boxx, boxy = getBoxAtPixel(mousex, mousey)  # 마우스가 클릭한 박스 픽셀 저장
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy] and mouseClicked:  # 박스위를 클릭 할 때
                revealBoxesAnimation(mainBoard, [(boxx, boxy)]) # 박스를 제거하고 클릭수를 증가시킨다.
                revealedBoxes[boxx][boxy] = True
                if list[boxx][boxy] != 0:   # 옳은 곳을 클릭했을 때
                    score += 1
                else:
                    click += 1
                        
            # 게임판 업데이트
        scoreBox(click, score)
        pygame.display.update()

    
def randomizeList (list, save):     # 보트 랜덤 지정 함수

    i = 0
    j = 0
        
    select = random.randint(0,1)

    if select == 0 :
        i = random.randint(0,9)
        j = random.randint(0,5)

        list[i][j] = 5
        list[i][j + 1] = 5
        list[i][j + 2] = 5
        list[i][j + 3] = 5
        list[i][j + 4] = 5

        save[i][j] = 1
        save[i][j + 1] = 1
        save[i][j + 2] = 1
        save[i][j + 3] = 1
        save[i][j + 4] = 1
        
    else : 
        i = random.randint(0,5)
        j = random.randint(0,9)

        list[i][j] = 5
        list[i + 1][j] = 5
        list[i + 2][j] = 5
        list[i + 3][j] = 5
        list[i + 4][j] = 5

        save[i][j] = 1
        save[i + 1][j] = 1
        save[i + 2][j] = 1
        save[i + 3][j] = 1
        save[i + 4][j] = 1

    select = random.randint(0,1)

    if select == 0 :

        i = random.randint(0,9)
        j = random.randint(0,6)
    
        while(save[i][j] == 1 or save[i][j + 1] == 1 or save[i][j + 2] == 1 or save[i][j + 3] == 1) : 
            i = random.randint(0,9)
            j = random.randint(0,6)

        list[i][j] = 4
        list[i][j + 1] = 4
        list[i][j + 2] = 4
        list[i][j + 3] = 4

        save[i][j] = 1
        save[i][j + 1] = 1
        save[i][j + 2] = 1
        save[i][j + 3] = 1
        
    else : 
        i = random.randint(0,6)
        j = random.randint(0,9)

        while(save[i][j] == 1 or save[i + 1][j] == 1 or save[i + 2][j] == 1 or save[i + 3][j] == 1) : 
            i = random.randint(0,6)
            j = random.randint(0,9)

        list[i][j] = 4
        list[i + 1][j] = 4
        list[i + 2][j] = 4
        list[i + 3][j] = 4

        save[i][j] = 1
        save[i + 1][j] = 1
        save[i + 2][j] = 1
        save[i + 3][j] = 1  

    repeat = 1

    while repeat <= 2 :

        select = random.randint(0,1)

        if select == 0 :
            i = random.randint(0,9)
            j = random.randint(0,7)

            while(save[i][j] == 1 or save[i][j + 1] == 1 or save[i][j + 2] == 1) : 
                i = random.randint(0,9)
                j = random.randint(0,7)
            
            list[i][j] = 3
            list[i][j + 1] = 3
            list[i][j + 2] = 3

            save[i][j] = 1
            save[i][j + 1] = 1
            save[i][j + 2] = 1
        
        else : 
            i = random.randint(0,7)
            j = random.randint(0,9)

            while(save[i][j] == 1 or save[i + 1][j] == 1 or save[i + 2][j] == 1) : 
                i = random.randint(0,7)
                j = random.randint(0,9)

            list[i][j] = 3
            list[i + 1][j] = 3
            list[i + 2][j] = 3

            save[i][j] = 1
            save[i + 1][j] = 1
            save[i + 2][j] = 1
            
        repeat += 1

    if select == 0 :

        i = random.randint(0,9)
        j = random.randint(0,8)
    
        while(save[i][j] == 1 or save[i][j + 1] == 1) : 
            i = random.randint(0,9)
            j = random.randint(0,8)

        list[i][j] = 2
        list[i][j + 1] = 2

        save[i][j] = 1
        save[i][j + 1] = 1
        
    else : 
        i = random.randint(0,8)
        j = random.randint(0,9)

        while(save[i][j] == 1 or save[i + 1][j] == 1) : 
            i = random.randint(0,8)
            j = random.randint(0,9)

        list[i][j] = 2
        list[i + 1][j] = 2

        save[i][j] = 1
        save[i + 1][j] = 1

    return

def scoreBox(click, score):     # 점수박스 함수
    pygame.draw.rect(DISPLAYSURF, GRAY, ((WINDOWWIDTH - 160, 15, 100, 60)))
    
    
    clickSurf = BASICFONT.render('Click : %s' %click, True, TEXTCOLOR)
    clickRect = clickSurf.get_rect()
    clickRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(clickSurf, clickRect)
    
    scoreSurf = BASICFONT.render('Score : %s' %score, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def gameOver(): # 게임오버 글씨 함수
    gameOverSurf = ENDFONT.render('Game Over', True, RED)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.topleft = (WINDOWWIDTH - 150, 70)
    DISPLAYSURF.blit(gameOverSurf, gameOverRect)

def gameWon():
    gameWonSurf = SPECIALFONT.render('Win', True, RED)
    gameWonRect = gameWonSurf.get_rect()
    gameWonRect.topleft = (WINDOWWIDTH - 150, 100)
    DISPLAYSURF.blit(gameWonSurf, gameWonRect)

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)

def getBoxAtPixel(x, y):    # 박스의 좌표값 얻는 함수
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)

def drawIcon(boxx, boxy):# 보트의 위치를 알려주는 x그리는 함수

    left, top = leftTopCoordsOfBox(boxx, boxy) # get pixel coords from board coords
    for i in range(0, BOXSIZE, 4):
        pygame.draw.line(DISPLAYSURF, RED, (left, top + i), (left + i, top))
        pygame.draw.line(DISPLAYSURF, RED, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))


    
def generateRevealedBoxesData(val):     # 드러낸 박스 데이터 저장
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes




def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def getBoxAtPixel(x, y):        # 박스의 픽셀값 구하는 함수
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)




def drawBoxCovers(board, boxes, coverage):      # 게임판의 박스를 그리는 함수
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))
    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):     # 박스 없애는 효과 함수
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)


def drawBoard(board, revealed):     # 박스를 그리는 함수
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            elif list[boxx][boxy] != 0 :        # 위치에 보트가 있으면 아이콘 그리기
                drawIcon(boxx, boxy)
                
def drawMenu(board):    # 메뉴 버튼을 그리는 함수
    
    pygame.draw.rect(DISPLAYSURF, RED, ((WINDOWWIDTH - 155, WINDOWHEIGHT- 80, BUTTONWEIGHT, BUTTONHIGHT)))
    surf3 = BASICFONT.render('종료', True, BLACK)
    rect3 = surf3.get_rect()
    rect3.topleft = (WINDOWWIDTH - 110, WINDOWHEIGHT- 80)
    DISPLAYSURF.blit(surf3, rect3)
    
def makeTextObjs(text, font, color):        # 화면에 글씨를 그리는 함수
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


if __name__ == '__main__':
    main()
