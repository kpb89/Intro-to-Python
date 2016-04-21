Vowels = 'AaEeIiOoUuYy'
def isAllVowels(st):
    '''This function iterates over the characters and will return isVowels'''

    prefix = ''
    stem = ''
    isVowels = True
    #Iterate over all the characters
    for char in st:
        #See if character isn't a vowel
        #If we find a consonant return false
       if char not in Vowels:
            isVowels = False
    #All vowels
    return isVowels
    
def transWord(word):
    '''The word was split at the vowel and the prefix and stem were switched.
       The function returns the word in pig latin'''
    
    #For special case of vowel only
    if isAllVowels(word) == True:     
        return word + 'yay'
    for i in range(0, len(word)):
        if isAllVowels(word[i]) == True:
            #Split the word at the vowel
            prefix, stem = word.split(word[i], 1)
            if len(stem) == 0:
                stem += word[i]
            #For words with few characters
            else:
                stem = word[i] + stem
            return stem + prefix + 'ay'
    return word + 'ay'

def transSent(sent):
    '''The function will return the new sentence with a period added at the
       end'''

    words = sent.split()
    print(words)
    newSent = ''
    for i in range(0, len(words)):
        print(i)
        if i < len(words)-1:
            newSent = newSent + transWord(words[i]) + ' '
        #Put period at end of sentence instead of space
        else:
            newSent = newSent + transWord(words[i]) + '.'
    return newSent

def isCorrect(original,myAns,correctAnswer):
   '''Prints a message about the correctness of the answer; returns True if
      the answer is correct, and False otherwise'''
   print(original,"-->",correctAnswer,end="")
   if myAns == correctAnswer:
       print("YUP!")
       return True
   else:
       print("WRONG: your answer is",myAns)
       return False

def main():
   # Testing
   allCorrect = True
   st = "My friend is a pig"
   ans = isCorrect(st,transSent(st),"yMay iendfray isay ayay igpay.")
   allCorrect = allCorrect and ans
   st = "The boss is coming"
   ans = isCorrect(st,transSent(st),"eThay ossbay isay omingcay.")
   allCorrect = allCorrect and ans
   st = "Iaaa"
   ans = isCorrect(st,transSent(st),"Iaaayay.")
   allCorrect = allCorrect and ans
   st = "I"
   ans = isCorrect(st,transSent(st),"Iyay.")
   allCorrect = allCorrect and ans
   st = ""
   ans = isCorrect(st,transSent(st),"")
   allCorrect = allCorrect and ans
   st = "Shhh He can hear us"
   ans = isCorrect(st,transSent(st),"Shhhay eHay ancay earhay usay.")
   allCorrect = allCorrect and ans
   if allCorrect:
      print("All correct! now you can input your own sentences.  Enter '**' to indicate you are done")
      sent = input("enter an English sentence (no punctuation)\n") 
      while sent != '**':
         print("Pig Latin:",transSent(sent))     
         sent = input("enter an English sentence (no punctuation)\n") 

def main1():
   # Testing
   inputs = ["My friend is a pig","The boss is coming","Iaaa","I","","Shhh He can hear us"]
   outputs = ["yMay iendfray isay ayay igpay.","eThay ossbay isay omingcay.","Iaaayay.","Iyay.","","Shhhay eHay ancay earhay usay."]
   i = 0
   allCorrect = True
   while i < len(inputs):
      ans = isCorrect(inputs[i],transSent(inputs[i]),outputs[i])
      allCorrect = allCorrect and ans
      i += 1
      
   if allCorrect:
      print("All correct! now you can input your own sentences.  Enter '**' to indicate you are done")
      sent = input("enter an English sentence (no punctuation)\n") 
      while sent != '**':
         print("Pig Latin:",transSent(sent))     
         sent = input("enter an English sentence (no punctuation)\n") 

if __name__ == "__main__":
    main()
