#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

recipent_names = []
with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        recipent_names.append(name.replace('\n', ''))

with open("./Input/Letters/starting_letter.txt") as message:
    letter = message.read()
    for name in recipent_names:
        new_file = open(f"./Output/ReadyToSend/{name}.txt", "w")
        new_file.write(letter.replace('[name]', name))
    
