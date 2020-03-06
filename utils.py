
import re 


def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))


def h1_heuristic(board_state, goal_state):
    misplaced = 0
    for i in range(4):
        for j in range(4):
            if board_state[i][j] != goal_state[i][j] and board_state[i][j] != 0:
                misplaced += 1

    return misplaced


def h2_heuristic(board_state, goal_state):
    """
    Manhattan distance
    """  
    distance = 0

    for i in range(4):
        for j in range(4):
            if board_state[i][j] == 0: continue
            i2,j2 = index_2d(goal_state,  board_state[i][j] )
            distance += abs(i2 - i) + abs(j2 - j)
                
    return distance


def count_inversions(arr):
    inversion_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] == 0):
                continue 

            if (arr[i] > arr[j]) and arr[j] != 0:
                inversion_count += 1
    
    return inversion_count


def convert_2d_arr_to_list(arr_2d):
    new_list = []

    for i,e in enumerate(arr_2d):
        new_list.extend(e)
    
    return new_list


def find_solvability(arr_2d):
    col_idx, row_idx = index_2d(arr_2d, 0)

    inv_count = count_inversions(convert_2d_arr_to_list(arr_2d))
   
    if ((col_idx == 3 or col_idx == 1 ) and inv_count % 2 == 0 ):
        return True
    elif ((col_idx == 2 or col_idx == 0) and inv_count % 2 == 1):
        return True
    else:
         return False


def convert_input_line_to_2d_arr(line):
    cols, rows = 4, 4
    arr_2d = [[0 for x in range(cols)] for x in range(rows)]
    numlist = re.findall('\d+',line)
    numlist = list(map(int, numlist))
    arr_2d[0] = numlist[0:4]
    arr_2d[1] = numlist[4:8]
    arr_2d[2] = numlist[8:12]
    arr_2d[3] = numlist[12:16]

    return arr_2d





