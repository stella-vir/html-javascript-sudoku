from random import randint

# 9x9 grid
sudoku = []
row = []
for i in range(9):
    for j in range(9):
        sudoku.append(row)
print(len(sudoku))
print(sudoku)

def getRandomInt(max):
    return randint(0, max)

def clearSudoku():
    for i in range(9):
        for j in range(9):
            sudoku = []

# new data type slot() cell()
int x_s, y_s = 0, 0
int x_c, y_c = 0, 0

def getCell(x_s, y_s):
    x_c = x_s/3
    y_c = y_s/3

    return (x_c, y_c)

def getSlots(x_c, y_c):
    slots = []
    for x in range(3):
        for y in range(3):
            x_s = x*3 + x
            y_s = y*3 + y
            slots.append((x_s, y_s))
    return slots

def getVals(slots):
    values = []
    for i in range(len(slots)):
        x, y = x_s, y_s
        values.append(sudoku[x][y])
    return values

def NotAppearedVal(cell):
    slots = getSlots(cell)
    values = getVals(slots)
    res = []

    for val in range(1, 9):
        bHasAppeared = False
        for i in range(0, len(values)):
            if values[i] == val:
                bHasAppeared == True
                break
        if not bHasAppeared:
            res.append(val)
    return res

def checkDuplicateX(slot, val):
    for x in range(0, 9):
        if x == slot[x]:
            continue;
        if val == sudoku[x][slot[y]]:
            return True
    return False

def checkDuplicateY(slot, val):
    for y in range(0, 9):
        if y == slot[y]:
            continue;
        if val == sudoku[x][y1]:
            return True
    return False

def randVal(slot):
    cell = getCell(slot)
    notAppV = NotAppearedVal(cell)
    validVal = []
    rdm = getRandomInt(len(validVal))


    if len(notAppV) == 0:
        return False
    for i in range(0, len(notAppV)):
        val = notAppV[i]
        if not checkDuplicateX(slot, val) and not checkDuplicateY(slot, val):
            validVal.append(val)

    if len(validVal) == 0:
        return False

    x, y = slot[x], slot[y]
    sudoku[x][y] = validVal[rdm]
    return True

def generateWhiteSpaces():
    for i in range(40):
        rdm_x = getRandomInt(9)
        rdm_y = getRandomInt(9)

        sudoku[rdm_x][rdm_y] = 0

def randomizeSudoku(ct):
    clearSudoku()
    bSuccess = True
    slot((0, 0))

    for x in range(9) and bSuccess:
        for y in range(9):
            if not randVal(slot(x, y)):
                bSuccess = False
                break

    if bSuccess:
        print('Finished', ct, 'iterations.')
        generateWhiteSpaces()
    else:
        randomizeSudoku(ct + 1)

def printSudoku():
    slot((0, 0))
    for y in range(9):
        if y > 0 and y % 3 == 0:
            print('\n')
        print(' ')
        for x in range(9):
            if x > 0 and x % 3 == 0:
                print('| ')
            if sudoku[x][y] == 0:
                print('| ')
            else:
                print('|', sudoku[x][y])
        print('| \n')

if __name__ == __main__:

    randomizeSudoku()
    printSudoku()




# end
