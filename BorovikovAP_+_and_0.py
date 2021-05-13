print("*" * 10, "Games noughts and crosses", "*" * 10)

board = list(range(1,10))

def draw_board(board): #рисует игровое поле
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3],  "|")
        print("-" * 13)

def take_input(player_token): #принимает ввод пользователя
    valid = False
    while not valid:
        player_answer = input("Куда поставить" + player_token+"?")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9")
def check_win(board): #функция проверки
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board): #главная функция запуска
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("x")
        else:
            take_input("0")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Нечья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для входа")