#duplicate_merge

# Copyright (c) 2023 alexandrosb88



import collections

inputFile = input("Please specify the path of the txt file to be processed: ")
outputFile = input("Please specify the name of the output file: ")


#Importing file and decompiling list

file = open(inputFile) #for greek characters (inputFile, encoding="utf-8")
wordlist = []
for word in file.read().split("\n"):
    wordlist.append(word)

counter_initial = len(wordlist)


 
#Usage of "Collection" for locating duplicates

dupl = ([item for item, count in collections.Counter(wordlist).items() if count > 1])

counter = len(dupl)



#Duplicates to be merged message

print("\n")
print("\n")
print("The duplicates below will be merged: \n \n \n" + str(dupl))



#Duplicates removal

while len(dupl) > 0:

    for word in dupl:
        wordlist.remove(word)

    dupl = ([item for item, count in collections.Counter(wordlist).items() if count > 1])

counter_final = len(wordlist)



#Sorting and re-compiling list

wordlist.sort()
wordlist = '\n'.join(wordlist)



#Export the txt file and print final message

file = open(outputFile, "w")
file.write(wordlist)
file.close()

print("\n")
print("\n")
print("%d duplicates were merged in file: %s" % (counter,outputFile))
print("\n")
print("The original list consisted of %d items." % counter_initial)
print("The revised list comprises a total of %d items." % counter_final)



