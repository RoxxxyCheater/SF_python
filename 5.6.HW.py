print("Добро пожаловать в игру Крестики/Нолики!")


def player_input(A, MOV):
    while True:
        cord = input(
            f"Игрок {MOV}, Введите кординаты выбраной (от 0 до 2) клетки в формате (1 1) через пробел:").split()
        if len(cord) != 2:
            print("Введите кординаты в формате (1 1) через пробел!")
            continue
        if not (cord[0].isdigit() and cord[1].isdigit()):
            print("Подсказка: При вводе кординат,используются только цифры")
            continue
        x, y = map(int, cord)
        num = range(3)
        if x not in num or y not in num:
            print("Введите численное значение кординат в диапазоне от 0 до 2")
            continue
        if not A[x][y] == "-":
            print(f"Кординаты {x} и {y} уже водились игркоком {MOV}, повторите ход:D")
            continue
        break

    return x, y


def main_game():
    H, V, A, MOV, COUNT = 3, 3, [], "X", 0
    A = [["-"] * H for i in range(V)]
    print(A)
    while True:
        if COUNT < 9:
            x, y = player_input(A, MOV)
            A[x][y] = MOV
            output_matrix(A)
            COUNT += 1
            if check_game(A, MOV):
                print(f"Поздраляем игрока" ' ' '%s' ' ' f"с победой за {COUNT} ходов!!!" % MOV)
                new_game(MOV)
                break
            if MOV == "X":
                MOV = "0"
            else:
                MOV = "X"
        else:
            print("Ничья - Победила дружба!")
            print('-' * 55, MOV)
            new_game(MOV)
            break


def output_matrix(A):
    print("  0 1 2")
    for i in range(len(A)):
        print(str(i), *A[i])


def check_game(A, MOV):
    if (A[0][0] == A[1][1] == A[2][2] != '-') or (A[0][2] == A[1][1] == A[2][0] != '-') or (
            A[0][0] == A[1][0] == A[2][0] != '-') or (A[1][0] == A[1][1] == A[1][2] != '-') or (
            A[2][0] == A[2][1] == A[2][2] != '-') or (A[0][0] == A[0][1] == A[0][2] != '-') or (
            A[0][1] == A[1][1] == A[2][1] != '-') or (A[0][2] == A[1][2] == A[2][2] != '-'):
        return True
    return False


def new_game(MOV):
    task = input(f"Игрок {MOV}, ссыграем снова? Для начала новой игры введите Y, введите N для окончания игры: ")
    if task == "Y":
        main_game()
    else:
        return False


main_game()
