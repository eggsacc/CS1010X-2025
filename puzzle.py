def additional_puzzle(*args):
    length = len(args)
    dic = {}
    num = 1
    for word in args[:-1]:
        for letter in word:
            if(num > 9):
                return False
            if(letter not in dic):
                dic[letter] = num
                num += 1
    
    return dic

print(additional_puzzle('ANT', 'MAN', 'COOL'))

