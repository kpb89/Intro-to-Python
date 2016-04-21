def vocabulary(word_and_punctuation_instances, punctuation):
    '''word_and_punctuation_instances is a list of strings; punctuation is
    a list of punctuation characters. Return a new list that is the
    vocabulary of word_and_punctuation_instances, that is, all the distinct elements of
    word_and_punctuation_instances that are not in the punctuation list.
    By all the distinct elements, we mean the list returned does not include
    duplicates.'''
    
    # list of all distinct words from word_and_punctuation_instances
    distinct = []
    words = separate_punctuation(word_and_punctuation_instances, punctuation)

    # iterate over all the words
    for word in words:
        # add the word to our list of distinct words
        # without punctuation
        if word not in distinct:
            distinct.append(word)
            
    return distinct
    
def analyze_vocabulary(word_and_punctuation_instances, punctuation):
    '''Determine and print the number of words in the vocabulary of
    word_and_punctuation_instances, as well as a sorted list of those
    words.  "punctuation" is a list of punctuation characters.  They
    may occur in word_and_punctuation_instances, but are not treated
    as words in the vocabulary.'''

    #find the vocabulary
    vocab = vocabulary(word_and_punctuation_instances, punctuation)
    # sorted sorts the vocab
    sorted_vocab = sorted(vocab)
    print(vocab)
    # print the number of words
    print('The number of distinct words is: ' + str(len(sorted_vocab)) )
    # print the sorted vocab list
    print('The sorted word list is: [' + print_one_line(sorted_vocab) + ']' )

def print_stats(word_and_punctuation_instances, within_sentence_punctuation, end_sentence_punctuation):
    '''"word_and_punctuation_instances" is a list of strings;
    "within_sentence_punctuation" and "end_sentence_punctionation" are
    lists of punctuation characters that can occur in the middle
    of a sentence, or at the end of a sentence, respectively.  Print
    statistics about the words, sentences, and readability of
    word_and_punctuation_instances (the print statements below
    tell you which statistics to calculate).  The float values
    are printed to 2 decimal places.'''

    punct = within_sentence_punctuation + end_sentence_punctuation
    #print(word_and_punctuation_instances)
    # seperate the punctuation from each sentences
    vocab = vocabulary(word_and_punctuation_instances, punct)
    words = separate_punctuation(word_and_punctuation_instances, punct)
    #finding distinct number of words
    num_distinct = len(words)

    #finding the number of words
    num_words = len(separate_punctuation(word_and_punctuation_instances, punct))
    
    #finding average length of the words
    num_char = 0
    for avg in words:
        e = len(avg)
        num_char = num_char + e
    avg_word_length = num_char / num_words
    #finding number of sentences by counting end punctuation marks
        
    num_sentences = 0
    for string in word_and_punctuation_instances: 
        if string[-1] in end_sentence_punctuation:
            num_sentences = num_sentences + 1

    #finding average sentence length
    avg_sent_length = num_words / num_sentences
    #finding ARI

    num_char = 0
    no_punct = separate_punctuation(word_and_punctuation_instances, punct)
    for word in no_punct:
        num_char = num_char + len(word)
    
    ari = 4.71 * (num_char / num_words) + 0.5 * (num_words / num_sentences) - 21.43
   
    print("Number of distinct words:", num_distinct)
    print("Number of words:", (num_words))
    print("Average word length:", format(avg_word_length, '.2f') )
    print("Number of sentences:", (num_sentences))
    print("Average sentence length:", format(avg_sent_length, '.2f') )
    print("ARI:", format(ari, '.2f'))

def separate_punctuation(strings, punctuation_list):

    # new words that will be returned without ending
    # punctuation
    new_words = []

    # iterate over all the words
    for word in strings:
        last_char = -1
        # iterate until we don't find punctuation
        while word[last_char] in punctuation_list:
            # next character
            last_char -= 1
            # if we iterated past the last character

        if last_char < -1:
            new_words.append(word[:last_char+1])
        # no punctuation at the end
        else:
            new_words.append(word)
    
    return new_words

def print_one_line(list):
    '''Print the strings in 'list' on a single line, with commas separating
    them.'''
    
    variable_commands = ''
    for command in list:
        variable_commands = variable_commands + command + ', '
    variable_commands = variable_commands[:-2]
    print (variable_commands)

    return variable_commands
  
def get_valid_command(valid):
    '''Prompt for and return a string that is a valid command, i.e., a string
    in the list "valid".'''
    
    command = input("Please enter a command: ")
    while command not in valid:
        print("Invalid command")
        command = input("Please enter a valid command: ")
    return command

def main():
    # Get the name of a file to analyze, and put its contents into a
    # list of strings.
    filename = input("File to analyze: ")
    f = open(filename, 'r')
    contents = f.read().split()
     
    # inner_punct is a list of within-sentence punctuation.
    # end_punct is a list of end-of-sentence punctuation.
    # punct is a list of all punctuation characters.
    inner_punct = [",", ";", "-"]
    end_punct = ["!", "?", "."]
    punct = inner_punct + end_punct
    
    # Tell the user what the valid commands are, then
    # read and process the user's command.
    valid_commands = ["stats", "vocab"]
    print ("The valid commands are:")
    print_one_line(valid_commands)
    command = get_valid_command(valid_commands)
    if command == "stats":
	    print_stats(contents, inner_punct, end_punct)
    elif command == "vocab":
	    analyze_vocabulary(contents, punct)

if __name__ == "__main__":
    main()
