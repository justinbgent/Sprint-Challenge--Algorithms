'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    
    # this solution came to my mind first now converting to recursion
    #for i in range(0, len(word)):
    #    if (i < len(word) - 1):
    #        letters = word[i] + word[i+1]
    #        if (letters == "th"):
    #            count += 1
    #return count

    if(len(word) < 2):
        return count
    
    letters = word[0] + word[1]
    if letters == "th":
        count += 1
    
    count += count_th(word[1:])
    
    return count
