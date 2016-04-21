def inputMovieInfo(filename):

   '''filename (string) is the name of a file.
      Each line in filename contains a name followed by a list of movies,
      where commas separate the various names.  Here is an example: 
      Brad Pitt, Sleepers, Troy, Meet Joe Black, Oceans Eleven

      Read the data; and create and return two dictionaries:  
          actor2Movies: each key is an actor and the value is the list of movies the actor appears in
          movie2Actor:  each key is a movie and the value is the list of actors that appear in that movie
   '''   
   # create actor2Movies when reading in the data
   actor2Movies = {}
   f = open(filename,'r')
   for line in f:
      entries = line.split(',')
      #get rid of the \n at the end of the last entry and the space before each
      #movie title
      for i in range(len(entries)):
         entries[i] = entries[i].strip()
      actor = entries[0]
      movies = entries[1:]
      actor2Movies[actor] = movies
   #now create the inverted dictionary
   movie2Actors = {}
   for actor in actor2Movies:
      for movie in actor2Movies[actor]:
         if not movie in movie2Actors:
            movie2Actors[movie] = [actor]
         else:
            movie2Actors[movie].append(actor)     
   return actor2Movies,movie2Actors

def pairs(lst):
   '''Return all pairs of elements of list lst (as a list of lists).   The order of the      
      elements does not matter.  So, e.g., for [1,2,3], return                               
      [1,2], [1,3], and [2,3]; or [2,1], [1,3], and [3,2]; or ...'''
   pairs = []
   #Don't change the parameter!  Work with a copy of the list                                
   copy = lst[:]
   while copy:
      #Make a pair of the first element and each of the following elements                   
      for i in copy[1:]:
         pairs.append([copy[0],i])
      #Now, move on to the next element of copy!                                             
      copy = copy[1:]
   return pairs

def commonValues (key1,key2,data):
    '''key1 and key2 are keys into data (a dictionary whose values are lists).
       Return all list elements that are in both data[key1] and data[key2].'''

    both = []
    for item in data[key1]:
       if item in data[key2]:
          both.append(item)
    return both


def keysWithSharedItems(key,data):
   '''key is a key into data (a dictionary whose values are lists).
         Return (in a list) all of the other keys that share at least one list element with key
         The new list should NOT include key, and should not include duplicates.'''

   haveSharedItems = []
   for k in data:
      # Don't test if key shares items with itself!
      if k != key:
         # Make sure you don't add k more than once to haveSharedItems; just
         #   check if there is at least one item in commen
         found = False
         for item in data[k]:
            if item in data[key]:
               found = True
         if found:
            haveSharedItems.append(k) 
   return haveSharedItems 


def printList(lst):
   ''' Print the elements of lst using commas and 'and' appropriately, without any newlines.
       Print nothing if the list is empty '''
   copy = lst[:]
   copy.sort()
   if len(lst) == 1:
      print(lst[0],end="")
   elif len(lst) == 2:
      print(lst[0], 'and', lst[1],end="")
   elif len(lst) > 2:
      for a in lst[:-1]:
        print(a,", ",sep="",end="")
      print("and",lst[-1],end="")

def printAll(headerStr,lst):
   print(headerStr)
   for l in lst:
      print(" ",l)
   print("")

def printActorPairsWhoHaveAppearedTogether(allActors,actor2Movies):
   
   print('**These actor pairs have appeared together:')
   actorPairs = pairs(allActors)
   for pair in actorPairs:
      # Check if the actors of pair have movies in commen
      common = commonValues(pair[0],pair[1],actor2Movies)
      if common:
         common.sort()
         print(" ",pair[0],"and",pair[1],"both appeared in") 
         for m in common:
            print("    ",m)
   print("")
   print("")

def printMoviePairsThatShareCastMembers(allMovies,movie2Actors):   
   print('**These movie pairs share cast members:')
   moviePairs = pairs(allMovies)
   for pair in moviePairs:
      # All actors who appear in both movies of pair
      cc = commonValues(pair[0],pair[1],movie2Actors)
      if cc:
        print("  ",pair[0]," & ",pair[1],":",sep="")
        cc.sort()
        print("    ",end="")
        printList(cc)
        if len(cc) == 1:
          print(" was in them")
        elif len(cc) == 2:
          print(" were both in them")
        else:
          print(" were all in them")
   print("")
   print("")

def printWhoEachActorHasWorkedWith(allActors,actor2Movies):
   print("**Who has each actor worked with?")
   for actor in allActors:
      cas = keysWithSharedItems(actor,actor2Movies)
      if cas:
        cas.sort()
        print("  ",actor,"has appeared in movies with ",end="")
        printList(cas)
        print("")
   
def main():

   # input data and create dictionaries
   actor2Movies,movie2Actors = inputMovieInfo(smallInput.txt)

   # print all the actors
   allActors = list(actor2Movies.keys())
   allActors.sort()
   printAll('**All actors in the database:',allActors) 

   # print all the movies
   allMovies = list(movie2Actors.keys())
   allMovies.sort()
   printAll('**All movies in the database:',allMovies)

   printActorPairsWhoHaveAppearedTogether(allActors,actor2Movies)

   printMoviePairsThatShareCastMembers(allMovies,movie2Actors)   

   printWhoEachActorHasWorkedWith(allActors,actor2Movies)

main()

