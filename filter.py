# -------------------------------------------------------
# code template for assignment-1
# -------------------------------------------------------

import time
import string 

def profanityFilter(aString, badWordList, subsitute_string="#%@$!"):
    # Write a function that replaces badWords in aString with the substitute string...
    # Note: do not change the substitute_string prior to submission
	
	remove = string.punctuation + string.whitespace
	
    # check for each bad words from badWordList
	for word in badWordList: 
		#Check if the line has the bad word
		if word.lower() in aString.translate(None, remove).lower():
			j = 0
			#Begin from the start of the string and keep jumping to places
			#where first alphabet of the bad word is present
			while j < (len(aString) - len(word) + 1):
				start_position = aString[j:].lower().find(word[0])
				if start_position < 0:
					break
				
				start_position = start_position + j;
				
				#Check if the immediate next set of alphabets(ignoring special charatcers)
				#has the remaining letters of the bad word
				if aString[start_position:].translate(None, remove)[0:len(word)].lower() == word.lower():
					aString = aString[:start_position] + subsitute_string[0] + aString[start_position+1:]
					#overwrote first alphabet of bad word	
					current_position = start_position+1
						
					#Keep looking for other alphabets of the bad word and keep replacing them
					for i in range(1,len(word)):
						start_position = aString[current_position:].lower().find(word[i].lower())
						aString = aString[:start_position+current_position] + subsitute_string[i] + aString[start_position+current_position+1:];
						current_position = current_position + start_position + 1
					j = current_position
				else:
					j = start_position + 1;
	return aString

# -------------------------------------------------------

if __name__ == "__main__":

    theStartTime = time.time()

    #here we open a file that contains the list of badwords to be removed...
    with open('unsavoury_word.txt') as theBadWordFile:
        badWords = filter(None, (line.rstrip() for line in theBadWordFile))

    #Here we send sample user input from a given file to your profanity filter...
    with open('input.txt') as theSampleInputFile, open('out.txt', 'w') as theOutputFile:
        for theSampleInput in theSampleInputFile:
            theOutputFile.write(profanityFilter(theSampleInput, badWords) + '\n')

        theOutputFile.write('elapsed: ' + str( time.time() - theStartTime) + '\n')
