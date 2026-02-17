# printing new values
sign_list = []


def play(value):
    while True:
        x = int(input('Enter your preferable slot : '))
        x -= 1
        if x >= 0 and x < 10:
            if x in sign_list:
                print('This slot is blocked. Try another one!')
                continue

            sign_list.append(x)
        else:
            print('Input numbers between 1-9.')
        return x


# determining the winner
def calculate(player_one, player_two):
    if index_list[0] == index_list[1] == index_list[2] == 'X' or \
            index_list[3] == index_list[4] == index_list[5] == 'X' or \
            index_list[6] == index_list[7] == index_list[8] == 'X' or \
            index_list[0] == index_list[3] == index_list[6] == 'X' or \
            index_list[1] == index_list[4] == index_list[7] == 'X' or \
            index_list[2] == index_list[5] == index_list[8] == 'X' or \
            index_list[0] == index_list[4] == index_list[8] == 'X' or \
            index_list[2] == index_list[4] == index_list[6] == 'X':
        print(f'{player_one} is the WINNER!')
        quit('Thanks both for joining the game.')
    elif index_list[0] == index_list[1] == index_list[2] == 'O' or \
            index_list[3] == index_list[4] == index_list[5] == 'O' or \
            index_list[6] == index_list[7] == index_list[8] == 'O' or \
            index_list[0] == index_list[3] == index_list[6] == 'O' or \
            index_list[1] == index_list[4] == index_list[7] == 'O' or \
            index_list[2] == index_list[5] == index_list[8] == 'O' or \
            index_list[0] == index_list[4] == index_list[8] == 'O' or \
            index_list[2] == index_list[4] == index_list[6] == 'O':
        print(f'{player_two} is the WINNER!')
        quit('Thanks both for joining the game.')


# printing board
index_list = []
for i in range(9):
    index_list.append(' ')


def board():
    board = f'''
 {index_list[0]} | {index_list[1]} | {index_list[2]}
---|---|---
 {index_list[3]} | {index_list[4]} | {index_list[5]}
---|---|---
 {index_list[6]} | {index_list[7]} | {index_list[8]}
'''
    print(board)


def main():
    print('WELCOME TO TIC TAC TOE.')
    player_one = input('Enter first player name : ')
    player_two = input('Enter second player name :')
    print(
        f'''Welcome again {player_one} and {player_two}. {player_one} will start with'X'. {player_two} will play with 'O' ''')
    print('The board will look like this :')
    print(f'''
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9''')
    print('The game starts now :')
    board()
    for i in range(9):
        if i % 2 == 0:
            print(f'''{player_one}'s turn''')
            idx = play(player_one)
            index_list[idx] = 'X'
        else:
            print(f'''{player_two}'s turn''')
            idx = play(player_one)
            index_list[idx] = 'O'
        board()
        calculate(player_one, player_two)

    print('This game is a TIE. Please play again. ')


main()
