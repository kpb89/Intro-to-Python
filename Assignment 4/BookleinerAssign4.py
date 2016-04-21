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
	movieInput = []
	#each line in the file
	for line in f:
		line = line.strip()
		movieInput.append(line)
	
	return movieInput

def actorMovies(actordata):
	'''Prints all actors and movies in the database'''
	
	# create a set for both the actor and movies
	actors = []
	movies = []
	# iterate over the dictionary, save each actor
	# and movie into the sets
	for key in actordata.keys():
		# if actor isn't a duplicate, add
		if key not in actors:
			actors.append(key)
	
	for val in actordata.values():
		# if movie isn't a duplicate, add
		for movie in val:
			if movie not in movies:
				movies.append(movie)
		
	print('**All actors in the database:')
	for actor in sorted(actors):
		print('  ' + actor)
	
	#prints all of the keys in the dictionary(the actors)
	print('\n**All movies in the database:')
	for movie in sorted(movies):
		print('  ' + movie)
	
	return actorMovies

def buildDict(a):
	'''Builds the dictionary containing actors and movies'''
	#Create an empty dictionary
	actorData = dict()
	#iterate over each line
	for line in a:
		#split the line at comma and creates list
		entry = line.split(',')
		
		#position of the actor will be the key in dictionary
		actorData[entry[0]] = []
		
		for i in range(1, len(entry)): 
			actorData[entry[0]].append( entry[i].lstrip() )

	# return the dictionary
	return actorData

def invertDictionary(myDict):
	'''Creates an inverted dictionary containing actors and movies'''
	# inverting the dictionary will give us
	# a mapping from movie to use
	inv_dict = dict()
	
	for actor, values in myDict.items():
		for movie in values:
			# if the movie has been added already as a key
			if movie in inv_dict:
				# check to see if the actor has 
				# been added to the movie
				if actor not in inv_dict[movie]:
					inv_dict[movie].append(actor)
			# else add the the movie as a new key,
			# and create the array
			else:
				inv_dict[movie] = [actor]
	
	return inv_dict
	
def actorPairs(movieDict):
	'''Prints pairs of actors that have appeared together in a movie'''
	# iterate over the inverted dictionary
	# to keep track of the pairs and store them
	actorPairs = dict()
	
	for movie in sorted(movieDict.keys()):
		# first check if a pair exists
		if len(movieDict[movie]) > 1:
			# next, iterate over the each actor
			for i in range(0, len(sorted(movieDict[movie]))):
				# iterate from the next actor (i+1) to the end
				for j in range(i+1, len(sorted(movieDict[movie]))):
					# check if the pair of actors has already been accounted for
					
					# add the actors as a key to the new 
					if movieDict[movie][i] > movieDict[movie][j]:
						actorKeyCombo = movieDict[movie][j] + " and "  + movieDict[movie][i]
					else:
						actorKeyCombo = movieDict[movie][i] + " and "  + movieDict[movie][j]
						
					if actorKeyCombo in actorPairs:
						# check to see if the movie has been accounted for
						if movie not in actorPairs[actorKeyCombo]:
							actorPairs[actorKeyCombo].append(movie)
					# else add the key combo to the dictionary
					else:
						actorPairs[actorKeyCombo] = [movie]
                    
	print('\n**These actor pairs have appeared together:')
    # iterate over the actor pairs and print the output
	for actors in sorted(actorPairs.keys()):
		print('  ' + actors + ' both appeared in\n     ' + str.join('\n     ', actorPairs[actors]) )
        	
	return actorPairs
	
def moviePairs(inv_dict):
	'''Prints pairs of movies each actor has appeared in'''
	# get a sorted list of keys
	keys = sorted(list(inv_dict))

	# iterate over the movies dictionary, getting the pairs
	for i in range(0, len( keys )):
		for j in range(i+1, len( keys )):
			
			# construct the key for the movie pairs
			if keys[i] < keys[j]:
				moviePairKey = keys[i] + ' & ' + keys[j]
			else:
				moviePairKey = keys[j] + ' & ' + keys[i]
			# Perform an intersection on the two lists.
			# The intersection returns the items that match.
			# The first value set must be converted to a set to 
			# use the intersection method.
			matches = set(inv_dict[keys[i]]).intersection(inv_dict[keys[j]])
			
			# define the printing grammar
			if len(matches) > 0:
				# if only one, verb is 'was'
				if len(matches) == 1:
					print('  ' + moviePairKey + ':\n    ' + ' and '.join(sorted(matches)) + ' was in them')
				# if two, verb is 'were', object compliment 'both'
				elif len(matches) == 2:
					print('  ' + moviePairKey + ':\n    ' + ' and '.join(sorted(matches)) +  ' were both in them')
				# if 3+, verb is 'were', object compliment 'all'
				else:
					print('  ' + moviePairKey + ':\n    ' + \
						', '.join(sorted(list(matches))[:-1]) + \
						', and ' + \
						sorted(list(matches))[-1] + ' were all in them')


def actorWork(actor_pairs, inv_dict):
	'''Prints who each actor has worked with'''
	# get the keys to each of the dictionaries
	actorKeys = sorted(list(actor_pairs))
	movieKeys = sorted(list(inv_dict))

	# dictionary keyed by actor
	sharedCast = dict()

	# iterate over the actor-keyed dictionary 
	for actor in actorKeys:
		# print the dictionary with the new element
		sharedCast[actor] = []
		# iterate over the movie-keyed dictionary
		for movie in movieKeys:
			# check to see was in the movie
			if actor in inv_dict[movie]:
				# perform a set difference to get the other actors
				coActors = set(inv_dict[movie]).difference(sharedCast[actor])
				# remove the actor we're comparing against
				coActors.remove(actor)
				# append each coActor to the shared cast dictionary
				for c in coActors:
					sharedCast[actor].append(c)

	# loop over the new newly created dictionary
	# and print the result
	for k,v in sorted(sharedCast.items()):
		if len(v) <= 2:
			print('   ' + k + ' has appeared in movies with ' + ' and '.join(sorted(v)))
		else:
			print('   ' + k + ' has appeared in movies with ' + ', '.join(sorted(v)[:-1]) + \
				', and ' + sorted(v)[-1])
def main():

        # get the input
    data = inputMovieInfo(smallInput.txt)
    
    myDict = buildDict(data)
    # invert the dictionary
    invDict = invertDictionary(myDict)

    actorMovies(myDict)
    actorPairs(invDict)
    print('\n\n**These movie pairs share cast members:')
    moviePairs(invDict)
    print('\n\n**Who has each actor worked with?')
    actorWork(myDict, invDict)

if __name__ == "__main__":
	main()
