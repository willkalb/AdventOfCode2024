def brOffset(puzzle):
    col_len = len(puzzle)
    new_puzzle = []
    for i in range(0, col_len):
        new_puzzle.append(["." for _ in range(0, col_len - i - 1)] + puzzle[i] + ["." for _ in range(0, i)])

    return new_puzzle

def blOffset(puzzle):
    col_len = len(puzzle)
    new_puzzle = []
    for i in range(0, col_len):
        new_puzzle.append(["." for _ in range(0, i)] + puzzle[i] + ["." for _ in range(0, col_len - i - 1)])

    return new_puzzle

def wordCountInList(word, list):
    count = 0
    word_rev = word[::-1]

    str = "".join(list)
    str_len = len(str)
    for i in range(0, str_len):
        if i > str_len - len(word):
            continue
        
        searching = str[i:i + len(word)]
        if searching == word or searching == word_rev:
            count = count + 1

    return count

def countWord(word, puzzle):
    count = 0
    
    # row - 5
    for l_row in puzzle:
        count = count + wordCountInList(word, l_row)
    
    # col - 3
    for i_row in range(0, len(puzzle)):
        l_col = []
        for i_col in range(0, len(puzzle[i_row])):
            l_col.append(puzzle[i_col][i_row])
        
        count = count + wordCountInList(word, l_col)

    # diagonal to br - 5
    brOffsetPuzzle = brOffset(puzzle)

    for i_col in range(0, len(brOffsetPuzzle[0])):
        l_col = []
        for i_row in range(0, len(brOffsetPuzzle)):
            l_col.append(brOffsetPuzzle[i_row][i_col])
            
        count = count + wordCountInList(word, l_col)

    # diagonal to bl - 5
    blOffsetPuzzle = blOffset(puzzle)

    for i_col in range(0, len(blOffsetPuzzle[0])):
        l_col = []
        for i_row in range(0, len(blOffsetPuzzle)):
            l_col.append(blOffsetPuzzle[i_row][i_col])
            
        count = count + wordCountInList(word, l_col)

    return count

def countX_MAS(puzzle):
    count = 0
    for i_row in range(0, len(puzzle) - 2):
        for i_col in range(0, len(puzzle[i_row]) - 2):
            if puzzle[i_row + 1][i_col + 1] != "A":
                continue

            if not ((puzzle[i_row][i_col] == "M" and puzzle[i_row + 2][i_col + 2] == "S") or (puzzle[i_row][i_col] == "S" and puzzle[i_row + 2][i_col + 2] == "M")):
                continue
            
            if not ((puzzle[i_row][i_col + 2] == "M" and puzzle[i_row + 2][i_col] == "S") or (puzzle[i_row][i_col + 2] == "S" and puzzle[i_row + 2][i_col] == "M")):
                continue

            count = count + 1
    
    return count

puzzle = []
with open("./Inputs/day4.txt", "r") as f:
    puzzle = [ [ c for c in line if c != "\n" ] for line in f ]

print(f"Answer 1: { countWord("XMAS", puzzle) }")
print(f"Answer 2: { countX_MAS(puzzle) }")
