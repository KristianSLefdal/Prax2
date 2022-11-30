#2.	Create a script named editor.py. In this script, prompt the user to enter a string of text. The following needs to happen until the user decides to exit the program, by pressing "e":

sentence = "change my delimiter"
sentencelist = sentence.split (" ")

print(sentence, sep="-")

print (";".join(sentencelist))
print(":".join(sentencelist))
print ("|".join(sentencelist))

sentencereplacement = sentence.split (" ")
print(sentence, sep= '_')

print (" ".join(sentencelist))
print("#".join(sentencelist))
print (">>".join(sentencelist))