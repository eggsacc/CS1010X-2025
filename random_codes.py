table = {}  # table to memoize computed values

def num_of_paths(n, m):
    # your code here
    if(n-1 == 0 or m-1 == 0):
        return 1
    
    if((n, m) in table):
        return table[(n, m)]
    
    table[(n, m)] = num_of_paths(n-1, m) + num_of_paths(n, m-1)
    
    return table[(n, m)]

def num_of_paths2(maze):
    # your code here
    rows = len(maze)
    clmns = len(maze[0])
    dp_table = [[0 for i in range(clmns)] for j in range(rows)]
    if(maze[0][0] == 1):
        dp_table[0][0] = 1
    else:
        dp_table[0][0] = 0

    for i in range(1, rows):
        if(maze[i][0] == 1):
            dp_table[i][0] = dp_table[i-1][0]
        else:
            dp_table[i][0] = 0
            break

    for i in range(1, clmns):
        if(maze[0][i] == 1):
            dp_table[0][i] = dp_table[0][i-1]
        else:
            dp_table[0][i] = 0
            break
    
    for row in range(1, rows):
        for clmn in range(1, clmns):
            if(maze[row][clmn] == 1):
                dp_table[row][clmn] = dp_table[row-1][clmn] + dp_table[row][clmn-1]
            else:
                dp_table[row][clmn] = 0

    print("####################################")
    for item in dp_table:
        print(item)
    print("####################################")
    return dp_table[rows-1][clmns-1]

    
# Do NOT modify
maze1 = ((1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
         (1, 0, 0, 1, 1, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
         (1, 1, 0, 1, 1, 1, 1, 0, 1, 1),
         (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
         (1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
         (1, 1, 0, 1, 0, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
         (1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
         (1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
         (1, 1, 0, 1, 0, 1, 0, 1, 1, 1))


maze2 = ((1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1))

maze3 = ((1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 0),
         (1, 0, 0, 1))

print(num_of_paths2(maze1))
print(num_of_paths2(maze2))
print(num_of_paths2(maze3))