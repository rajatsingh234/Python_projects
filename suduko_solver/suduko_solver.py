def find_next_empty(puzzle):
    #find the next row,column on the puzzle that is not filled yet
    #return row,col tuple or (None,None) if there is None

    #we are using 0-8 for our indeces
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None             #no empty space left
    pass

def is_valid(puzzle,guess,row,col):
    #returns True if guess is valid otherwise False

    #check if guess is the row
    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    
    #check if guess is in the column
    # col_vals=[]
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #check for 3*3 box
    #we have to get the starting index of row and col
    row_start = (row//3)*3
    col_start = (col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    
    return True               #if guess is valid
    pass

def suduko_solver(puzzle):
    #solve suduko using backtracking
    #our puzzle is a list of list each inner list is a row of puzzle
    #return weather a solution exists
    #mutates puzzle to be the solution(if solution exists)

    #step1: choose somewhere on the puzzle to make guess
    row,col= find_next_empty(puzzle)

    #step1.1:if there is no space left then we are done 
    if row==None:
        return True
    #step2: if there is a place to fill then we have to make a guess between 1-10
    for guess in range(1,10):
        #step3: check if guess is valid
        if is_valid(puzzle,guess,row,col):
            #step3.1: if guess is valid then place the value
            puzzle[row][col]=guess

            #step4: recursively call our function
            if suduko_solver(puzzle):
                return True
        #if not valid then we need to find new number
        puzzle[row][col]=-1

    #If we dont find any number then thjis puzzle is unsolvable
    return False

    pass

if __name__=='__main__':
    example_board=[
    [3,9,-1,  -1,5,-1,  1,-1,-1],
    [-1,-1,-1,  2,-1,-1,  -1,-1,5],
    [-1,-1,-1,  7,1,9,  -1,8,-1],
    
    [-1,5,-1,  -1,6,8,  -1,-1,-1],
    [2,-1,6,  -1,-1,3,  -1,-1,-1],
    [-1,-1,-1,  -1,-1,-1,  -1,-1,4],

    [5,-1,-1,  -1,-1,-1,  -1,-1,-1],
    [6,7,-1,  -1,-1,5,  -1,4,-1],
    [-1,-1,9,  -1,-1,-1,  2,-1,-1]
    ]
    print(suduko_solver(example_board))
    print(example_board)


"""
[
    [3,9,-1,  -1,5,-1,  -1,-1,-1],
    [-1,-1,-1,  2,-1,-1,  -1,-1,5],
    [-1,-1,-1,  7,1,9,  -1,8,-1],
    
    [-1,5,-1,  -1,6,8,  -1,-1,-1],
    [2,-1,6,  -1,-1,3,  -1,-1,-1],
    [-1,-1,-1,  -1,-1,-1,  -1,-1,4],

    [5,-1,-1,  -1,-1,-1,  -1,-1,-1],
    [6,7,-1,  -1,-1,5,  -1,4,-1],
    [-1,-1,9,  -1,-1,-1,  2,-1,-1]
]
"""