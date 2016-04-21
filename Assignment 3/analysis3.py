def vocabulary(word_and_punctuation_instances, punctuation):
    '''word_and_punctuation_instances is a list of strings; punctuation is
    a list of punctuation characters. Return a new list that is the
    vocabulary of word_and_punctuation_instances, that is, all the distinct elements of
    word_and_punctuation_instances that are not in the punctuation list.
    By all the distinct elements, we mean the list returned does not include
    duplicates.'''
    for e in word_and_punctuation:
        for c in punctuation:
            if c not in punctuation:
                return c
    
    
def analyze_vocabulary(word_and_punctuation_instances, punctuation):

    '''Determine and print the number of words in the vocabulary of
    word_and_punctuation_instances, as well as a sorted list of those
    words.  "punctuation" is a list of punctuation characters.  They
    may occur in word_and_punctuation_instances, but are not treated
    as words in the vocabulary.'''

    # note:  if v is a list, then v.sort() shorts the list and puts the 
    #        results back in v
    
def print_stats(word_and_punctuation_instances, within_sentence_punctuation, \
		end_sentence_punctuation):    
    '''"word_and_punctuation_instances" is a list of strings;
    "within_sentence_punctuation" and "end_sentence_punctionation" are
    lists of punctuation characters that can occur in the middle
    of a sentence, or at the end of a sentence, respectively.  Print
    statistics about the words, sentences, and readability of
    word_and_punctuation_instances (the print statements below
    tell you which statistics to calculate).  The float values 
    are printed to 2 decimal places.'''
    words = s.split()
    # Add code here to make your calculations. s is the string
    num_distinct = 1
    #Finding the number of words
    num_words = len(words)
    #Finding average length of the words
    total_avg = 0
    for avg in words:
        e = len(avg)
        total_avg = total_avg + e
        avg_word_length = total_avg / num_words  
    #num_sentences find number of end punctionations in the string
    sentence = s
    num_sentences = 0
    for sent in sentence:
        if sent in end_punct:
            num_sentences = num_sentences + 1
    #avg_sent_length =
    avg_sent_length = num_words / num_sentences
    
    ari = 4.71 * (num_char / num_words) + 0.5 * (num_words / num_sentences) - 21.43
    # In each print statement below, replace the value 99 with an appropriate
    # expression.
    print("Number of distinct words:", num_distinct)
    print("Number of words:", (num_words)
    print("Average word length:", format(avg_word_length, '.2f'))
    print("Number of sentences:", (num_sentences)
    print("Average sentence length:", format(avg_sent_length, '.2f'))
    print("ARI:", format(ari, '.2f'))

    
def separate_punctuation(strings, punctuation_list):
    '''strings is a list of strings.  "punctuation" is a list of 
    punctuation characters.  Return a new list that is the same as strings, 
    but for every string that ends in a punctuation character, the string 
    (without the punctuation) and the punctuation are separated and
    made two elements of the list.'''
    s.split(inner_punct)

    # suppose s is a string.  s[-1] is the last char of s, and s[:-1] is all
    #   but the last char of s.

def print_one_line(list):
    '''Print the strings in 'list' on a single line, with commas separating
    them.  '''

    # Make sure you do not print a comma after the last item!
  
def get_valid_command(valid):
    '''Prompt for and return a string that is a valid command, i.e., a string
    in the list "valid".'''
    
    # Uncomment out the following two lines and use them, as many times as 
    # needed, as your ONLY input and output in this function:
    
    #command = input("Please enter a command: ")
    #print("Invalid command")
    

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
    
    # Separate any punctuation that is attached to the end of words.
    contents = separate_punctuation(contents, punct)
    
    # Tell the user what the valid commands are, then
    # read and process the user's command.
    valid_commands = ["stats", "vocab"]
    print "The valid commands are:", 
    print_one_line(valid_commands)
    command = get_valid_command(valid_commands)
    if command == "stats":
	print_stats(contents, inner_punct, end_punct)
    elif command == "vocab":
	analyze_vocabulary(contents, punct)

main()
