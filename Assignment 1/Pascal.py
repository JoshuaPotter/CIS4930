''' 
    Joshua Potter, jop13
    Pascal.py 
'''

def printTriangle(rows):
    '''
        Print new line for each row, then 
        print each value and a space
    '''
    for row in range(0, rows):
        print()
        for rowElement in range(0, row + 1):
            print(coefficient(row, rowElement), end = "")
            print(" ", end = "")

def coefficient(row, elem):
    '''
        Calculate element position, then calculate
        element binomial coeffecient value
    '''
    coefficient = 1
    # Element position
    if(row - elem < elem):
        elem = row - elem
    # Binomial coefficient
    for index in range(0, elem):
        coefficient = coefficient * (row - index)
        coefficient = coefficient // (index + 1)
    return coefficient

if __name__ == "__main__":
    N = int(input("Enter the number of rows: "))
    printTriangle(N)
