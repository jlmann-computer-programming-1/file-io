def end_with_s(word_list):
    ''' how many words end with s? '''
    count = 0
    for word in word_list:
        if word[-1] == 's':
            count += 1

    return count

def two_letters(word_list):
    ''' how many words are 2 letters long? '''
    count = 0
    for word in word_list:
        if len(word) == 2:
            count += 1

    return count


# read a big file, don't try to print all items!
with open('scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()

print(words[:10])

# call functions to answer questions
print( end_with_s(words) )
print( two_letters(words) )
