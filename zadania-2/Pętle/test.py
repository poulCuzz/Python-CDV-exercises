# Tic Tac Toe

# Napisz grę w kółko i krzyżyk człowieka z komputerem. W grze obowiązują klasyczne zasady. Układ planszy powinien być wymiaru 3x3.
import random
import time

print("Welcome in Tic Tac Toe!!!")
time.sleep(1)
print("Here is our game board:")
time.sleep(1)
print("    a    b    c")
time.sleep(0.3)
print("1 [   ][   ][   ]")
time.sleep(0.3)
print("2 [   ][   ][   ]")
time.sleep(0.3)
print("3 [   ][   ][   ]")
time.sleep(1.5)
print("Select the position to insert 'x' by entering the coordinate")
time.sleep(1.8)
print("Let's start!")
print("")
coordinList = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
mapo = {}

def verifyWinner(board):
    try:

        # Sprawdzenie rzędów
        for row in '123':
            if board[f'a{row}'] == board[f'b{row}'] == board[f'c{row}'] and board[f'a{row}'] != ' ':
                return board[f'a{row}']

        # Sprawdzenie kolumn
        for column in 'abc':
            if board[f'{column}1'] == board[f'{column}2'] == board[f'{column}3'] and board[f'{column}1'] != ' ':
                return board[f'{column}1']

        # Sprawdzenie przekątnych
        if board['a1'] == board['b2'] == board['c3'] and board['a1'] != ' ':
            return board['a1']
        if board['a3'] == board['b2'] == board['c1'] and board['a3'] != ' ':
            return board['a3']

        return None
    except Exception as e:
        print("")


#Pętla do prowadzania współrzędnych przez gracza i przez komputer
while len(coordinList) > 0:
    coordinate = input("Your move: ")
    coordinList.remove(coordinate)
    mapo[coordinate] = "x"

    # Wywołanie funkcji weryfikującej, aby sprawdzić czy jest wygrana
    result = verifyWinner(mapo)
    if result == "x":
        break

    print("    a    b    c")
    print(f"1 [ {mapo.get('a1', ' ')} ][ {mapo.get('b1', ' ')} ][ {mapo.get('c1', ' ')} ]")
    print(f"2 [ {mapo.get('a2', ' ')} ][ {mapo.get('b2', ' ')} ][ {mapo.get('c2', ' ')} ]")
    print(f"3 [ {mapo.get('a3', ' ')} ][ {mapo.get('b3', ' ')} ][ {mapo.get('c3', ' ')} ]")


    if len(coordinList) != 0:
        print("PC's turn:")
        time.sleep(1)
        pcCoordin = coordinList[random.randint(0, len(coordinList) - 1)]
        print(pcCoordin)
        coordinList.remove(pcCoordin)
        mapo[pcCoordin] = "o"
    print("    a    b    c")
    print(f"1 [ {mapo.get('a1', ' ')} ][ {mapo.get('b1', ' ')} ][ {mapo.get('c1', ' ')} ]")
    print(f"2 [ {mapo.get('a2', ' ')} ][ {mapo.get('b2', ' ')} ][ {mapo.get('c2', ' ')} ]")
    print(f"3 [ {mapo.get('a3', ' ')} ][ {mapo.get('b3', ' ')} ][ {mapo.get('c3', ' ')} ]")

    #Wywołanie funkcji weryfikującej, aby sprawdzić czy jest przegrana
    result = verifyWinner(mapo)
    if result == "o":
        break


#Wyświetlenie wyniku
time.sleep(1)
result = verifyWinner(mapo)
if result == "x":
    print("Gratulacje! Wygrałeś!")
elif result == "o":
    print("Przegrałeś :(")
else:
    print("Brak zwycięzcy.")
