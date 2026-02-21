"""
This project demonstrates an iterative solution to the Tower of Hanoi algorithm that I coded as one of my certification
projects for the freeCodeCamp Python Developer certification. The Tower of Hanoi is a classical logic puzzle that
traditionally contains three towers with a number of disks on the first tower. The goal of the puzzle is to move the 
disks from the first tower to the third tower, following two simple rules:

1. You may only move one disk at a time.
2. You may not put a larger disk on top of a smaller disk.

This algorithm solves the Tower of Hanoi for any number of disks on the starting tower. It then outputs, step by
step, which disks to move, and to which tower, in order to solve the Tower of Hanoi in the minimum number of moves possible
(calculated by the formula 2^n - 1, where n represents thenumber of disks). The starting point is set by creating 3 lists,
with each one representing one of the towers. It then follows a set pattern that solves the Tower in 2^n - 1 moves.
"""


disks = int(input("How many disks on the starting tower? "))

def hanoi_solver(disks = int):
    list1 = list(range(disks, 0, -1))
    list2 = []
    list3 = []
    move_index = 0
    moves = []
    moves.append([list(list1), list(list2), list(list3)])
    

    """
    The Tower of Hanoi can be solved by following a set pattern. The pattern is determined by whether the number of starting
    disks are even or odd. This algorithm uses two pieces of information to determine the proper move at any given time:

    1. Whether the number of starting disks are even or odd.
    2. What the move number (marked by move_index) is.

    The smallest disk will move every odd-numbered turn. If the number of starting disks is odd, the smallest disk will move
    to the left on each odd-numbered turn, and move to the third tower if it is on the first tower. If the number of starting
    disks is even, the smallest disk will move to the right on each odd-numbered turn, and will move to the first tower if it
    is on the third tower. The smallest disk will always move on odd-numbered turns and never on even-numbered moves.

    Since the smallest disk will never move on even-numbered moves, the tower which contains the smallest disk will not be
    touched during even-numbered moves. Since each disk on the tower is a different size, and the smallest disk and its
    tower will not be touched on even-numbered moves, that leaves only one remaining legal move between the remaining two
    towers. This algorithm determines which move is legal and executes it. It then joins all of the moves made at the
    end and provides a printout.
    """

    while len(list3) < disks:
        move_index += 1
        if disks % 2 == 1:
            if move_index % 2 == 1:
                if list1 and list1 [-1] == 1:
                    list1.pop()
                    list3.append(1)
                    moves.append([list(list1), list(list2), list(list3)])
                elif list2 and list2[-1] == 1:
                    list2.pop()
                    list1.append(1)
                    moves.append([list(list1), list(list2), list(list3)])
                elif list3 and list3[-1] == 1:
                    list3.pop()
                    list2.append(1)
                    moves.append([list(list1), list(list2), list(list3)])
            elif move_index % 2 == 0:
             if list1 and list1[-1] == 1:
                if list2 and list3:
                    if list2[-1] < list3[-1]:
                        list3.append(list2.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                    elif list3[-1] < list2[-1]:
                        list2.append(list3.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                elif list2 and not list3:
                    list3.append(list2.pop())
                    moves.append([list(list1), list(list2), list(list3)])
                elif list3 and not list2:
                    list2.append(list3.pop())
                    moves.append([list(list1), list(list2), list(list3)])
             elif list2 and list2[-1] == 1:
                if list1 and list3:
                    if list1[-1] < list3[-1]:
                        list3.append(list1.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                    elif list3[-1] < list1[-1]:
                        list1.append(list3.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                elif list1 and not list3:
                    list3.append(list1.pop())
                    moves.append([list(list1), list(list2), list(list3)])
                elif list3 and not list1:
                    list1.append(list3.pop())
                    moves.append([list(list1), list(list2), list(list3)])
             elif list3 and list3[-1] == 1:
                if list1 and list2:
                    if list1[-1] < list2[-1]:
                        list2.append(list1.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                    elif list2[-1] < list1[-1]:
                        list1.append(list2.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                elif list1 and not list2:
                    list2.append(list1.pop())
                    moves.append([list(list1), list(list2), list(list3)])
                elif list2 and not list1:
                    list1.append(list2.pop())
                    moves.append([list(list1), list(list2), list(list3)])
        elif disks % 2 == 0:
            if move_index % 2 == 1:
                if list1 and list1 [-1] == 1:
                    list1.pop()
                    list2.append(1)
                    moves.append([list(list1), list(list2), list(list3)])
                elif list2 and list2[-1] == 1:
                    list2.pop()
                    list3.append(1)
                    moves.append([list(list1), list(list2), list(list3)])
                elif list3 and list3[-1] == 1:
                    list3.pop()
                    list1.append(1)
                    moves.append([list(list1), list(list2), list(list3)])
            elif move_index % 2 == 0:
                if list1 and list1[-1] == 1:
                    if list2 and list3:
                        if list2[-1] < list3[-1]:
                            list3.append(list2.pop())
                            moves.append([list(list1), list(list2), list(list3)])
                        elif list3[-1] < list2[-1]:
                            list2.append(list3.pop())
                            moves.append([list(list1), list(list2), list(list3)])
                    elif list2 and not list3:
                        list3.append(list2.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                    elif list3 and not list2:
                        list2.append(list3.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                elif list2 and list2[-1] == 1:
                    if list1 and list3:
                        if list1[-1] < list3[-1]:
                            list3.append(list1.pop())
                            moves.append([list(list1), list(list2), list(list3)])
                        elif list3[-1] < list1[-1]:
                            list1.append(list3.pop())
                            moves.append([list(list1), list(list2), list(list3)])
                    elif list1 and not list3:
                        list3.append(list1.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                    elif list3 and not list1:
                        list1.append(list3.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                elif list3 and list3[-1] == 1:
                    if list1 and list2:
                        if list1[-1] < list2[-1]:
                            list2.append(list1.pop())
                            moves.append([list(list1), list(list2), list(list3)])
                        elif list2[-1] < list1[-1]:
                            list1.append(list2.pop())
                            moves.append([list(list1), list(list2), list(list3)])
                    elif list1 and not list2:
                        list2.append(list1.pop())
                        moves.append([list(list1), list(list2), list(list3)])
                    elif list2 and not list1:
                        list1.append(list2.pop())
                        moves.append([list(list1), list(list2), list(list3)])




    return "\n".join([" ".join([str(rod) for rod in step]) for step in moves])

print(hanoi_solver(disks))