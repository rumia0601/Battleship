#Line 1 ~ Line 788 : 프로그램이 사용하는 함수 정의
#Line 790 ~ Line 876 : 프로그램의 시작과 끝
#"잘못 입력하셨습니다"는 사용자가 이상하지 않은 값을 입력할 때까지 계속 사용자가 입력한 값을 검토하는 부분

import random #난수를 발생시키는 randint힘수
import os #콘솔출력 화면을 지우는 system함수    

def changej(j) :

    if j == '1' :
        return 0
    elif j == '2' :
        return 1
    elif j == '3' :
        return 2
    elif j == '4' :
        return 3
    elif j == '5' :
        return 4
    elif j == '6' :
        return 5
    elif j == '7' :
        return 6
    elif j == '8' :
        return 7
    elif j == '9' :
        return 8
    elif j == '10' :
        return 9
    else :
        return -1 #사용자가 입력한 게임판의 x좌표를 0부터 9까지의 수로 바꾸는 함수 (-1은 에러)
    
def changei(i) :
    
    if i == 'A' :
        return 0
    elif i == 'B' :
        return 1
    elif i == 'C' :
        return 2
    elif i == 'D' :
        return 3
    elif i == 'E' :
        return 4
    elif i == 'F' :
        return 5
    elif i == 'G' :
        return 6
    elif i == 'H' :
        return 7
    elif i == 'I' :
        return 8
    elif i == 'J' :
        return 9
    else :
        return -1 #사용자가 입력한 게임판의 y좌표를 0부터 9까지의 수로 바꾸는 함수 (-1은 에러)

def showscreen (screen):

    print(" ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print('A', screen[0][0], screen[0][1], screen[0][2], screen[0][3], screen[0][4], screen[0][5], screen[0][6], screen[0][7], screen[0][8], screen[0][9])
    print('B', screen[1][0], screen[1][1], screen[1][2], screen[1][3], screen[1][4], screen[1][5], screen[1][6], screen[1][7], screen[1][8], screen[1][9])
    print('C', screen[2][0], screen[2][1], screen[2][2], screen[2][3], screen[2][4], screen[2][5], screen[2][6], screen[2][7], screen[2][8], screen[2][9])
    print('D', screen[3][0], screen[3][1], screen[3][2], screen[3][3], screen[3][4], screen[3][5], screen[3][6], screen[3][7], screen[3][8], screen[3][9])
    print('E', screen[4][0], screen[4][1], screen[4][2], screen[4][3], screen[4][4], screen[4][5], screen[4][6], screen[4][7], screen[4][8], screen[4][9])
    print('F', screen[5][0], screen[5][1], screen[5][2], screen[5][3], screen[5][4], screen[5][5], screen[5][6], screen[5][7], screen[5][8], screen[5][9])
    print('G', screen[6][0], screen[6][1], screen[6][2], screen[6][3], screen[6][4], screen[6][5], screen[6][6], screen[6][7], screen[6][8], screen[6][9])
    print('H', screen[7][0], screen[7][1], screen[7][2], screen[7][3], screen[7][4], screen[7][5], screen[7][6], screen[7][7], screen[7][8], screen[7][9])
    print('I', screen[8][0], screen[8][1], screen[8][2], screen[8][3], screen[8][4], screen[8][5], screen[8][6], screen[8][7], screen[8][8], screen[8][9])
    print('J', screen[9][0], screen[9][1], screen[9][2], screen[9][3], screen[9][4], screen[9][5], screen[9][6], screen[9][7], screen[9][8], screen[9][9])
    
    return #10x10 게임판을 출력하는 함수

def randomizeship (list, save, number) :
    
    select = random.randint(0,1)

    if select == 0 : #number칸 짜리 배를 가로로 배치
        i = random.randint(0,9)
        j = random.randint(0,9 - number + 1)

        duplicated = 0

        for count in range(0, number) :
            if save[i][j + count] == 1 :
                duplicated = 1
        
        while(duplicated == 1) : #그 좌표에 이미 다른 배가 있는 경우 다른 좌표에 배치 시도
            i = random.randint(0,9)
            j = random.randint(0,9 - number + 1)

            duplicated = 0

            for count in range(0, number) :
                if save[i][j + count] == 1 :
                    duplicated = 1

        for count in range(0, number) :
            list[i][j + count] = number
            save[i][j + count] = 1
        
    elif select == 1: #number칸 짜리 배를 세로로 배치
        i = random.randint(0,9 - number + 1)
        j = random.randint(0,9)

        duplicated = 0

        for count in range(0, number) :
            if save[i + count][j] == 1 :
                duplicated = 1
        
        while(duplicated == 1) : #그 좌표에 이미 다른 배가 있는 경우 다른 좌표에 재배치 시도
            i = random.randint(0,9 - number + 1)
            j = random.randint(0,9)

            duplicated = 0

            for count in range(0, number) :
                if save[i + count][j] == 1 :
                    duplicated = 1

        for count in range(0, number) :
            list[i + count][j] = number
            save[i + count][j] = 1    

    return #게임판(list)의 임의의 공간에 number칸 짜리 배를 배치하는 함수, 배를 배치하기 전에 또다른 게임판(save)에 저장된 값을 판별하여 중복 배치가 발생하지 않도록 함     

def randomizelist (list, save):

    i = 0
    j = 0
        
    randomizeship(list, save, 5)
    randomizeship(list, save, 4)
    randomizeship(list, save, 3)
    randomizeship(list, save, 3)
    randomizeship(list, save, 2)
    

    return #게임판(list)의 임의의 공간에 5칸, 4칸, 3칸, 3칸, 2칸 짜리 배를 배치하는 함수

def play (shoot, hit) :
    
    showscreen(screen)
    
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
            ]
    
    while hit < 17 : #CPU의 17척의 배가 모두 격추되면 "연습모드"종료

        print("공격 시도 횟수 : ", shoot, ", 격추된 횟수 : ", hit)
    
        j = input("공격할 x좌표 입력 : ")
        j = changej(j)
    
        if j == -1 :
            os.system('cls')
            showscreen (screen)
        
            print("잘못 입력하셨습니다")
            continue
    
        i = input("공격할 y좌표 입력 : ")
        i = changei(i)
    
        if i == -1 :
            os.system('cls')
            showscreen (screen)
        
            print("잘못 입력하셨습니다")
            continue

        #공격할 좌표를 입력받음

        if save[i][j] == 1 : #이미 공격한 좌표인 경우
            os.system('cls')
            showscreen (screen)
            
            print("이미 공격한 곳입니다")
            continue

        if list[i][j] == 0 : #공격이 실패한 경우
            screen[i][j] = 'X'
            shoot += 1
            save[i][j] = 1

            os.system('cls')
            showscreen (screen)
        
            print("아무것도 격추되지 않았습니다")

        if list[i][j] != 0 : #공격이 성공한 경우
            screen[i][j] = 'O'
            shoot += 1
            hit += 1
            save[i][j] = 1

            os.system('cls')
            showscreen (screen)
        
            print("무언가가 격추되었습니다")
        
    print("모든 것을 격추하였습니다")
    print("공격 시도 횟수 : ", shoot, ", 격추된 횟수 : ", hit)

    select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")

    #"연습모드"가 종료되면 출력되는 문구
                   
    return #"연습모드"에 해당하는 함수, "연습모드"에선 나만 공격권이 있고 CPU는 공격을 맞기만 함, 총 공격 시도 횟수와 공격 성공 횟수가 표시됨

def locateship(screen, number) :
    
    while 1 :
        select = input(str(number) + "칸짜리 배를 어떻게 놓겠습니까? (가로 = H, 세로 = V) : ") #number칸 짜리 배를 배치할 방법 입력

        if select == 'H' : #number칸 짜리 배를 가로로 배치
             j = input("배치할 가로로 놓인" + str(number) + "칸짜리 배의 맨 왼쪽 x좌표 입력 : ")
             j = changej(j)
    
             if j == -1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue

             elif j > 9 - number + 1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue
    
             i = input("배치할 가로로 놓인" + str(number) + "칸짜리 배의 y좌표 입력 : ")
             i = changei(i)

             duplicated = 0

             for count in range(0, number) :
                 if screen[i][j + count] != ' ' :
                     duplicated = 1
             
             if i == -1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue

             #number칸 짜리 배를 배치할 좌표를 입력받음

             elif duplicated == 1: #이미 다른 배가 있음
                os.system('cls')
                showscreen (screen)
        
                print("이미 다른 배가 있습니다")
                continue
                
             else :
                for count in range(0, number) :
                    screen[i][j + count] = number

                return

        elif select == 'V' : #number칸 짜리 배를 세로로 배치
            j = input("배치할 세로로 놓인" + str(number) + "칸짜리 배의 x좌표 입력 : ")
            j = changej(j)
    
            if j == -1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue

            i = input("배치할 세로로 놓인" + str(number) + "칸짜리 배의 맨 위 y좌표 입력 : ")
            i = changei(i)

            if i == -1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue


            elif i > 9 - number + 1 :
                os.system('cls')
                showscreen (screen)
                
                print("잘못 입력하셨습니다")
                continue

            duplicated = 0

            for count in range(0, number) :
                if screen[i + count][j] != ' ' :
                    duplicated = 1
            
            if i == -1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue
    
            elif i > 9 - number + 1 :
                os.system('cls')
                showscreen (screen)
        
                print("잘못 입력하셨습니다")
                continue

            #number칸 짜리 배를 배치할 좌표를 입력받음
            
            elif duplicated == 1: #이미 다른 배가 있음
                os.system('cls')
                showscreen (screen)
        
                print("이미 다른 배가 있습니다")
                continue

            else :
                for count in range(0, number) :
                    screen[i + count][j] = number
                    
                return

        else :
             os.system('cls')
             showscreen (screen)
        
             print("잘못 입력하셨습니다")

    #사용자가 입력한 게임판(screen)의 특정 좌표에 number칸 짜리 배를 배치하는 함수, 배를 배치하기 전에 게임판(screen)에 저장된 값을 판별하여 중복 배치가 발생하지 않도록 함        

def inputscreen(screen) :

    showscreen(screen)

    locateship(screen,5)
    os.system('cls')
    showscreen (screen)
    locateship(screen,4)
    os.system('cls')
    showscreen (screen)
    locateship(screen,3)
    os.system('cls')
    showscreen (screen)
    locateship(screen,3)
    os.system('cls')
    showscreen (screen)
    locateship(screen,2)
    os.system('cls')
              
    showscreen (screen)

    return #사용자가 입력한 게임판(screen)의 특정 좌표에 5칸, 4칸, 3칸, 3칸, 2칸짜리 배를 배치하는 함수

def practice(list, save, shoot, hit) :
    
    randomizelist(list, save)
    play(shoot,hit)

    return #"연습모드"에선 CPU의 게임판(list)을 임의로 발생시키고 게임을 시작함

def myturn(screen, screen2, shooting, shooted) :

    while 1 :
        print("당신의 턴입니다")

        j = input("공격할 x좌표 입력 : ")
        j = changej(j)
    
        if j == -1 :
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")
            continue
    
        i = input("공격할 y좌표 입력 : ")
        i = changei(i)
    
        if i == -1 :
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")
            continue

        #공격할 좌표를 입력받음

        attack = input("공격이 성공했습니까? (성공 = O, 실패 = X , 잘못누름 = R) : ") #실수로 이미 공격한 곳을 공격한 경우 공격자가 수동적으로 정정해야 함
                                                                                      #네트워크를 구현할 수 있다면 이 부분을 수정하여 공격 성공 여부를 간접적으로 묻지 않고도 판정 가능함

        if attack == 'O' : #적 배를 격추시킨 경우
            screen2[i][j] = '0'
            shooting += 1
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
           
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")

            return shooting

        elif attack == 'X' : #적 배를 격추시키지 못한 경우
            screen2[i][j] = 'X'
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")

            return shooting

        else :
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")

            continue

        #"VS 플레이어 모드"에서 자신의 차례일때 실행되는 함수, 적의 게임판(screen2)의 특정 좌표에 공격을 하고 그 결과를 처리한다

def enemyturn(screen, screen2, shooting, shooted) :

    while 1 :
        print("상대방의 턴입니다")

        j = input("공격당할 x좌표 입력 : ")
        j = changej(j)
    
        if j == -1 :
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")
            continue
    
        i = input("공격당할 y좌표 입력 : ")
        i = changei(i)
    
        if i == -1 :
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")
            continue

        #공격당할 좌표를 입력받음
    
        if screen[i][j] == 5 or screen[i][j] == 4 or screen[i][j] == 3 or screen[i][j] == 2 : #내 배가 격추돤 경우
            screen[i][j] = 'O'
            shooted += 1
                
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")

            return shooted

        elif screen[i][j] == ' ' : #내 배가 격추되지 않은 경우
            screen[i][j] = 'X'
                
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
         
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")

            return shooted

        elif screen[i][j] == 'X' or screen[i][j] == 'O': #실수로 상대방이 이미 공격한 곳을 공격한 경우 자동적으로 정정됨               
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")
            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")
            continue

        #"VS 플레이어 모드"에서 상대방의 차례일때 실행되는 함수, 나의 게임판(screen)의 특정 좌표에 공격을 하고 그 결과를 처리한다

def vsplayer(screen, screen2, save) :
        
    inputscreen(screen)

    os.system('cls')
    print("적의 게임판")
    showscreen(screen2)
    print("\n\n\n")
    print("나의 게임판")
    showscreen(screen)

    before = 0

    while before != 'I' and before != 'Y' :
    
        before = input("선제 공격권이 누구에게 있나요? (나 = I, 상대방 = Y) : ")

        if before == 'I' : #선제 공격권이 나에게 있는 경우
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
        elif before == 'Y' : #선제 공격권이 상대방에게 있는 경우
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)

        else :
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)
        
            print("잘못 입력하셨습니다")

            continue

    shooting = 0
    shooted = 0
    
    while shooting != 17 and shooted != 17 :
        
        if before == 'I' :
            shooting = myturn(screen, screen2, shooting, shooted)

            if shooting == 17 and shooted != 17 : #상대방의 배 17척이 먼저 모두 격추된 경우
                print("당신의 승리입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
 
            elif shooted != 17 and shooting == 17 : #나의 배 17척이 먼저 모두 격추된 경우
                print("당신의 패배입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
                
            shooted = enemyturn(screen, screen2, shooting, shooted)

            if shooting == 17 and shooted != 17 : #상대방의 배 17척이 먼저 모두 격추된 경우
                print("당신의 승리입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
 
            elif shooted != 17 and shooting == 17 : #나의 배 17척이 먼저 모두 격추된 경우
                print("당신의 패배입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
            
        elif before == 'Y' :
            shooted = enemyturn(screen, screen2, shooting, shooted)

            if shooting == 17 and shooted != 17 : #상대방의 배 17척이 먼저 모두 격추된 경우
                print("당신의 승리입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
 
            elif shooted != 17 and shooting == 17 : #나의 배 17척이 먼저 모두 격추된 경우
                print("당신의 패배입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
                
            shooting = myturn(screen, screen2, shooting, shooted)
            
            if shooting == 17 and shooted != 17 : #상대방의 배 17척이 먼저 모두 격추된 경우
                print("당신의 승리입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
 
            elif shooted != 17 and shooting == 17 : #나의 배 17척이 먼저 모두 격추된 경우
                print("당신의 패배입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return

           #"VS 플레이어"에 해당하는 함수, 자신의 게임판(screen)을 직접 설정한 다음 선제공격권을 정한 뒤, 상대방의 게임판(screen2) 에 내가 공격을 하거나 자신의 게임판에 상대방이 공격하며
           #게임이 진행됨. 둘 중 한명의 배가 모두 격추되면 게임 종료 

def vscpu(screen, screen2, list, save) :

    shooting = 0
    shooted = 0

    inputscreen(screen)
    randomizelist(list,save)

    while shooting != 17 and shooted != 17 : #둘 중 한명의 배가 모두 격추당하면 게임 종료
    
        while 1: #나의 공격 차례
            os.system('cls')
            print("적의 게임판")
            showscreen(screen2)
            print("\n\n\n")
            print("나의 게임판")
            showscreen(screen)

            print("내 배가", 17 - shooted, "척 남았습니다")
            print("적 배가", 17 - shooting, "척 남았습니다")
            print("당신의 턴입니다")

            j = input("공격할 x좌표 입력 : ")
            j = changej(j)
    
            if j == -1 :
                continue
    
            i = input("공격할 y좌표 입력 : ")
            i = changei(i)
    
            if i == -1 :
                continue

            #공격할 좌표를 입력받음

            if screen2[i][j] == 'O' or screen2[i][j] == 'X' : #실수로 공격한 장소를 또 공격한 경우
                continue
            
            if list[i][j] != 0 : #나의 공격이 성공한 경우
                attack = 'O'

            elif list[i][j] == 0 : #나의 공격이 실패한 경우
                attack = 'X'

            if attack == 'O' : #나의 공격이 성공한 경우
                list[i][j] = 0
                screen2[i][j] = 'O'
                shooting += 1
                os.system('cls')
                print("적의 게임판")
                showscreen(screen2)
                print("\n\n\n")
                print("나의 게임판")
                showscreen(screen)
           
                print("내 배가", 17 - shooted, "척 남았습니다")
                print("적 배가", 17 - shooting, "척 남았습니다")

                select = input("아무 키나 입력하면 CPU의 차례가 됩니다 : ")
            
                break

            elif attack == 'X' : #나의 공격이 실패한 경우
                screen2[i][j] = 'X'
                os.system('cls')
                print("적의 게임판")
                showscreen(screen2)
                print("\n\n\n")
                print("나의 게임판")
                showscreen(screen)
        
                print("내 배가", 17 - shooted, "척 남았습니다")
                print("적 배가", 17 - shooting, "척 남았습니다")

                select = input("아무 키나 입력하면 CPU의 차례가 됩니다 : ")
            
                break

        if shooting == 17 and shooted != 17 : #CPU의 배 17척이 모두 격추된 경우
                print("\n당신의 승리입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return
 
        elif shooted != 17 and shooting == 17 : #나의 배 17척이 모두 격추된 경우
                print("\n당신의 패배입니다")
                select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
                return    

        while 1 : #CPU의 공격 차례
                  #CPU는 항상 임의의 x좌표와 y좌표를 생성한 이후 나의 게임판(screen)을 공격함. 하지만 한번 공격한 장소는 다시 공격하지 않음 (단일 패턴)
                  #인공지능을 더 발전시킬 수 있다면 이 부분을 수정하여 더 향상된 CPU의 행동 패턴을 만들 수 있음
        
            print("CPU의 턴입니다")

            i = random.randint(0,9)
            j = random.randint(0,9)

            if screen[i][j] == 'O' or screen[i][j] == 'X' : #이미 공격한 장소를 또 공격하는 경우
                continue
            
            elif screen[i][j] == 2 or screen[i][j] == 3 or screen[i][j] == 4 or screen[i][j] == 5 : #CPU의 공격이 성공한 경우
                attack = 'O'

            elif screen[i][j] == ' ' : #CPU의 공격이 실패한 경우
                attack = 'X'

            if attack == 'O' : #CPU의 공격이 성공한 경우
                screen[i][j] = 'O'
                shooted += 1
                os.system('cls')
                print("적의 게임판")
                showscreen(screen2)
                print("\n\n\n")
                print("나의 게임판")
                showscreen(screen)
           
                print("내 배가", 17 - shooted, "척 남았습니다")
                print("적 배가", 17 - shooting, "척 남았습니다")

                select = input("아무 키나 입력하면 당신의 차례가 됩니다 : ")
            
                break

            elif attack == 'X' : #CPU의 공격이 실패한 경우
                screen[i][j] = 'X'
                os.system('cls')
                print("적의 게임판")
                showscreen(screen2)
                print("\n\n\n")
                print("나의 게임판")
                showscreen(screen)
        
                print("내 배가", 17 - shooted, "척 남았습니다")
                print("적 배가", 17 - shooting, "척 남았습니다")

                select = input("아무 키나 입력하면 당신의 차례가 됩니다 : ")
            
                break

        if shooting == 17 and shooted != 17 : #CPU의 배 17척이 모두 격추된 경우
            print("\n당신의 승리입니다")
            select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
            return
 
        elif shooted != 17 and shooting == 17 : #나의 배 17척이 모두 격추된 경우
            print("\n당신의 패배입니다")
            select = input("아무 키나 입력하면 타이틀 화면으로 돌아갑니다 : ")
            return

        #"VS CPU"에 해당하는 함수, 자신의 게임판(screen)을 직접 설정하고 CPU의 게임판(screen2)은 랜덤 설정한다. 자신이 screen2를 공격한 뒤 CPU가 screen을 공격하는것을 반복하다가
        #둘 중 한명의 배가 모두 격추당하면 게임을 종료한다

shoot = 0
hit = 0
select = 0

while select != 4 : #사용자가 4번 키를 누르면 프로그램이 종료됨

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
        ]

    screen = [
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]

    screen2 = [
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]

    os.system('cls')

    print("@@@@    @   @@@@@ @@@@@ @     @@@@@  @@@@ @   @ @@@@@ @@@@@")
    print("@   @  @ @    @     @   @     @     @     @   @   @   @   @")
    print("@@@@  @@@@@   @     @   @     @@@@@  @@@  @@@@@   @   @@@@@")
    print("@   @ @   @   @     @   @     @         @ @   @   @   @    ")
    print("@@@@  @   @   @     @   @@@@@ @@@@@ @@@@  @   @ @@@@@ @    \n")
    
    print("1 : 연습 모드")
    print("2 : VS CPU 모드")
    print("3 : VS 플레이어 모드")
    print("4 : 종료\n")

    select = int(input(""))

    os.system('cls')
    
    if select == 1: #사용자가 1번 키를 누르면 "연습 모드"를 실행함
        practice(list, save, shoot, hit)

    elif select == 2: #사용자가 2번 키를 누르면 "VS CPU 모드"를 실행함
        vscpu(screen, screen2, list, save)

    elif select == 3: #사용자가 3번 키를 누르면 "VS 플레이어 모드"를 실행함
        vsplayer(screen, screen2, save)

    elif select == 4:
        select = 4        
