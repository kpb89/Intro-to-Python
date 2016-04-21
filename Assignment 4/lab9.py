import sys

def inputMovieInfo(filename):

   '''filename (string) is the name of a file.
      Each line in filename contains a name followed by a list of movies,
      where commas separate the various names.  Here is an example: 
      Brad Pitt, Sleepers, Troy, Meet Joe Black, Oceans Eleven

      Read the data and print it, line by line.'''
   
   #open the file
   f = open(filename,'r')
   #printing file contents
   print(f)
   #each line in the file
   for line in f:
      line = line.strip()
      print(line)      
   return []
#This function returns the actor with their corresponding movies

def buildDict(line):
    #Create an empty dictionary
    actorData = {}
    #iterate over each line
    for l in line:
        #split the line at comma and creates list
        entry = line.split(',')
        print(line)
        #position of the actor will be the key in dictionary
        actorData[entry[0]] = entry[1:]
        print(actorData)
        
    return actorData

def actorsMovies(actor, movie):
print('**All actors in the database:', a)
print('**All movies in the database:', m)

def actorPairs(actor, movie):
   #Prints pairs of actors that have appeared together in a movie

def moviePairs(actor, movie):
   #Prints pairs of movies that have the same cast member

def actorWork(actor, movie):
   #Prints actors that each actor has worked with

   

def main():
   data = inputMovieInfo(sys.argv[1])
   
main()
