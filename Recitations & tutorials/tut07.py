# 1)
def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))
    
def accumulate_n(op, init, sequences):
    print(sequences)
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ( [accumulate(op, init, list(map(lambda x: x[0], sequences)))]
               + accumulate_n(op, init, list(map(lambda x: x[1:], sequences))))
    
# 2a)
def col_sum(m):
    # Leave your answers here
    return accumulate_n(lambda x, y: x + y, 0, m)

# 2b)
def transpose(m):
    rows = len(m)
    clmns = len(m[0])
    
    new_mat = [[0 for i in range(rows)] for j in range(clmns)]
    
    for i in range(rows):
        for j in range(clmns):
            new_mat[j][i] = m[i][j]
    return new_mat
           
def row_sum(m):
    # Fill in your answers here
    return accumulate_n(lambda x, y: x + y, 0, transpose(m))

# 3a)
def count_sentence(sentence):
    # Fill in your answers here
    words = len(sentence)
    letters = 0
     
    for word in sentence:
        letters += 1
        letters += accumulate(lambda x, y: 1 + y, 0, word)
    
    return [words, letters - 1]

# Order of growth: 
# Time: average O(m^2/n), where m is the total number 
# of characters, and n is the number of words
# Assuming each word is of equal length m/n.
# 
# Space: O(m^2), where m is the length of the longest word

# 3b)
def letter_count(sentence):
    # Fill in your code here
    occ = {}
    lst = []
    
    for word in sentence:
        for letter in word:
            if(letter not in occ):
                occ[letter] = 1
            else:
                occ[letter] += 1
    
    for item in occ.items():
        lst.append(list(item))
        
    return lst

# Order of growth:
# Time: O(n*m), where n is the total number of characters and 
# m is the number of uniqe characters.
# Space: O(m), where m is the number of unique characters

# 3c)
def most_frequent_letters(sentence):
    
    if(sentence == []):
        return {}
        
    letters = letter_count(sentence)
    letters_freq = [item[1] for item in letters]
    
    most_freq = max(letters_freq)
    
    return {item[0] for item in letters if item[1] == most_freq}

# Order of growth:
# Time: O(n), where n is the total number of characters
# Space: O(n), where n is the total number of characters

# 4)
def make_queue():
    return []

def enqueue(q, item):
    q.append(item)

def dequeue(q):
    return q.pop(0)
    
def size(q):
    return len(q)

# 5)
def who_wins(m, players):    
    q = make_queue()
    
    for player in players:
        enqueue(q, player)
        
    cnt = 0
    
    while len(q) > m-1:
        player = dequeue(q)
        
        if(cnt == m):
            cnt = 0
            continue
        
        enqueue(q, player)
            
        cnt += 1
        
    return q