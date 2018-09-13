''' Joshua Potter, jop13
    Pascal.py '''

def coefficient(row, elem):
    coefficient = 1

    if(row - elem < elem):
        elem = row - elem

    for index in range(0, elem):
        coefficient = coefficient * (row - index)
        coefficient = coefficient // (1 + index)
    
    return coefficient

def printTriangle(N):
    for row in range(0, N):
        print()
        for rowElement in range(0, row + 1):
            print(" ", coefficient(row, rowElement), end = "")
    print()

if __name__ == "__main__":
    N = int(input("Enter the number of rows: "))
    printTriangle(N)
