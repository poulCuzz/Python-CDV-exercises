#Tic Tac Toe
import random
#Napisz grę w kółko i krzyżyk człowieka z komputerem. W grze obowiązują klasyczne zasady. Układ planszy powinien być wymiaru 3x3.
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
while len(coordinList) > 0:

    coordinate = input("Your move: ")
    coordinList.remove(coordinate)
    mapo[coordinate] = "x"
    # print(coordinList)
    if len(coordinList) != 0:
        print("PC's turn:")
        pcCoordin = coordinList[random.randint(0, len(coordinList) - 1)]
        print(pcCoordin)
        coordinList.remove(pcCoordin)
        mapo[pcCoordin] = "o"
    print("    a    b    c")
    print(f"1 [ {mapo.get('a1', ' ')} ][ {mapo.get('b1', ' ')} ][ {mapo.get('c1', ' ')} ]")
    print(f"2 [ {mapo.get('a2', ' ')} ][ {mapo.get('b2', ' ')} ][ {mapo.get('c2', ' ')} ]")
    print(f"3 [ {mapo.get('a3', ' ')} ][ {mapo.get('b3', ' ')} ][ {mapo.get('c3', ' ')} ]")




print("    a    b    c")
print(f"1 [ {mapo.get('a1', ' ')} ][ {mapo.get('b1', ' ')} ][ {mapo.get('c1', ' ')} ]")
print(f"2 [ {mapo.get('a2', ' ')} ][ {mapo.get('b2', ' ')} ][ {mapo.get('c2', ' ')} ]")
print(f"3 [ {mapo.get('a3', ' ')} ][ {mapo.get('b3', ' ')} ][ {mapo.get('c3', ' ')} ]")






