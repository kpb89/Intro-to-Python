def strip_string(word):
    '''The function will return the sentence without punctuation'''
    
    #Replacing punctuation with space when comparing
    newWord = word.replace(' ', '')
    newWord = newWord.replace('.', '')
    newWord = newWord.replace(',', '')
    newWord = newWord.replace('?', '')
    newWord = newWord.replace('!', '')
    newWord = newWord.replace('-', '')
    newWord = newWord.replace('\"', '')
    newWord = newWord.replace('\'', '')
    newWord = newWord.replace(':', '')
    newWord = newWord.replace(';', '')
    
    return newWord.lower()

def palindrome(word):
    '''The strings are split in the middle and the parts are compared.
       The function will return true if both parts are equal and will
       return false if not'''
    
    # Where to split the string
    split_pos = int(len(word)/2)
    part_one = word[0:split_pos]
    
    if len(word) % 2:
        part_two =  word[split_pos:]
    else:
        part_two =  word[split_pos-1:]
        
    reverse_part_two = ''
    for i in range(len(part_two)-1, 0, -1):
        reverse_part_two = reverse_part_two + part_two[i]

    #Comparing the the parts of sentence
    if part_one == reverse_part_two:
        return True
    else:
        return False
        
def main():
    '''If the user inputs STOP!, the program will stop running'''
    
    #Will stop running when user enters STOP!
    while True:
        sentence = input('Enter a message. Enter STOP! to quit\n')
        stop = sentence.find('STOP!')
        # If the user entered stop, exit the loop
        if stop >= 0:
            break
        newSentence = strip_string(sentence)
        if palindrome(newSentence) == True:
            print('Yes')
        else:
            print('No')
        
if __name__ == "__main__":
    main()
