# Tic Tac Toe

# Napisz grę w kółko i krzyżyk człowieka z komputerem. W grze obowiązują klasyczne zasady. Układ planszy powinien być wymiaru 3x3.
import random
import time

print("Welcome in Tic Tac Toe!!!")
time.sleep(1)
print("Here is our game board:")
time.sleep(1)
print("")
print("    a    b    c")
print("1 [   ][   ][   ]")
print("2 [   ][   ][   ]")
print("3 [   ][   ][   ]")
print("")
time.sleep(1.5)
print("Select the position to insert 'x' by entering the coordinate")
print("Let's start!")
print("")
mapo = {}

mapo[-1] = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

#funkcja do weryfikowania zwycięzcy/przegranego

def horivertWinner(string1,string2, board):
    for number in string1: # abc
        tab = []
        for letter in string2: #123
            if (letter + number) in board.keys():
                tab.append(board[(letter + number)])
            elif (number + letter) in board.keys():
                tab.append(board[(number + letter)])
        if (len(tab) < 3):
            return ""
        else:
            if len(set(tab)) == 1:
                return tab[0]
def skosWinner(board):
    letters = ['a','b','c']
    number = ['1','2','3']
    tab = []
    for i in range(0,3):
        if (letters[i]+number[i]) in board.keys():
            tab.append((letters[i]+number[i]))
    if (len(tab) < 3):
        return ""
    else:
        if len(set(tab)) == 1:
            return tab[0]
    number = number[::-1]
    for i in range(0,3):
        if (letters[i]+number[i]) in board.keys():
            tab.append((letters[i]+number[i]))
    if (len(tab) < 3):
        return ""
    else:
        if len(set(tab)) == 1:
            return tab[0]

def verifyWinner(board):
        # Sprawdzenie rzędów
        tab = [horivertWinner('123','abc',board),horivertWinner('abc','123',board),skosWinner(board)]
        for player in tab:
            if player != "":
                return player
        return ""
    # try:
    #     # Sprawdzenie kolumn
    #     for column in 'abc':
    #         if board[f'{column}1'] == board[f'{column}2'] == board[f'{column}3'] and board[f'{column}1'] != ' ':
    #             return board[f'{column}1']
    # except Exception as e:
    #     print("")
    #
    # try:
    #     # Sprawdzenie przekątnych
    #     if board['a1'] == board['b2'] == board['c3'] and board['a1'] != ' ':
    #         return board['a1']
    #     if board['a3'] == board['b2'] == board['c1'] and board['a3'] != ' ':
    #         return board['a3']
    # except Exception as e:
    #     print("")
    #
    #     return None


#Pętla do wstawiania 'x' przez użytkownika i 'o' przez komputer
while len(mapo[-1]) > 0:

    coordinate = input("Your move: ")
    mapo[-1].remove(coordinate)
    mapo[coordinate] = "x"

    # Wywołanie funkcji
    result = verifyWinner(mapo)
    if result == "x":
        break
    elif result == "o":
        break


    if len(mapo[-1]) != 0:
        print("PC's turn:")
        pcCoordin = mapo[-1][random.randint(0, len(mapo[-1]) - 1)]
        mapo[-1].remove(pcCoordin)
        mapo[pcCoordin] = "o"
    print("    a    b    c")
    print(f"1 [ {mapo.get('a1', ' ')} ][ {mapo.get('b1', ' ')} ][ {mapo.get('c1', ' ')} ]")
    print(f"2 [ {mapo.get('a2', ' ')} ][ {mapo.get('b2', ' ')} ][ {mapo.get('c2', ' ')} ]")
    print(f"3 [ {mapo.get('a3', ' ')} ][ {mapo.get('b3', ' ')} ][ {mapo.get('c3', ' ')} ]")

    # Wywołanie funkcji
    result = verifyWinner(mapo)
    if result == "x":
        break
    elif result == "o":
        break


print("    a    b    c")
print(f"1 [ {mapo.get('a1', ' ')} ][ {mapo.get('b1', ' ')} ][ {mapo.get('c1', ' ')} ]")
print(f"2 [ {mapo.get('a2', ' ')} ][ {mapo.get('b2', ' ')} ][ {mapo.get('c2', ' ')} ]")
print(f"3 [ {mapo.get('a3', ' ')} ][ {mapo.get('b3', ' ')} ][ {mapo.get('c3', ' ')} ]")

# Wywołanie funkcji i wyświetlenie zwycięzcy
result = verifyWinner(mapo)
if result == "x":
    print("Gratulacje! Wygrałeś!")
elif result == "o":
    print("Przegrałeś :(")
else:
    print("Brak zwycięzcy.")
