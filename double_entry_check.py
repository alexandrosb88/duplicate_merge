#double_entry_check

'''

Εισαγωγή λεξικού υπό τη μορφή αρχείου κειμένου
με κάθε αντικείμενο σε διαφορετική γραμμή.

Το πρόγραμμα εντοπίζει τις διπλοεγγραφές, τις
συγχωνεύει και πραγματοποιεί ταξινόμηση κατά
αλφαβητική σειρά.

'''

import collections

inputFile = input("Παρακαλώ δώστε το path του επιθυμητού αρχείου: ")
outputFile = input("Παρακαλώ δώστε όνομα του αρχείου εξαγωγής: ")

#Διάβασμα αρχείου και μετατροπή του σε λίστα
file = open(inputFile) #εάν περιέχει και ελληνικούς χαρακτήρες (inputFile, encoding="utf-8")
wordlist = []
for word in file.read().split("\n"): #χρήση χαρακτήρα \n διότι μεταξύ των λέξεων μεσολαβεί κενό
    wordlist.append(word)

counter_arxiko = len(wordlist)
 
#Λειτουργία collections για εύρεση διπλοεγγραφών
dupl = ([item for item, count in collections.Counter(wordlist).items() if count > 1])

counter = len(dupl)

#Εμφάνιση διπλοεγγραφών    
print("Οι παρακάτω εγγραφές θα συγχωνευθούν: \n \n \n" + str(dupl))

#Αφαίρεση διπλοεγγραφών από λίστα   
while len(dupl) > 0:

    for word in dupl:
        wordlist.remove(word)

    dupl = ([item for item, count in collections.Counter(wordlist).items() if count > 1])

counter_teliko = len(wordlist)

#Ταξινόμηση και μετατροπή wordlist από λίστα σε συμβολοσειρά ούτως ώστε να εγγραφεί
wordlist.sort()
wordlist = '\n'.join(wordlist)



#Εξαγωγή σε αρχείο
file = open(outputFile, "w")
file.write(wordlist)
file.close()

print("\n")
print("\n")
print("Βρέθηκαν %d διπλοεγγραφές και συγχωνεύθηκαν στο αρχείο: %s" % (counter,outputFile))
print("\n")
print("Το αρχείο εισαγωγής περιείχε %d εγγραφές." % counter_arxiko)
print("Το νέο αρχείο περιέχει %d εγγραφές." % counter_teliko)
