#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_array = []

# Read letter and save blueprint
with open("./Input/Letters/starting_letter.txt", 'r') as letter:
    letter_blueprint = letter.readlines()

# Read names and save them into list
with open("./Input/Names/invited_names.txt", 'r') as names:
    for name in names.readlines():
        name_array.append(name[:-1])

# Replace actual name into blueprint and create file
for i in range(len(name_array)):
    with open(f"./Output/ReadyToSend/{name_array[i]}.txt", 'w') as sending:
        first = letter_blueprint[0]
        first = first.replace("[name]", name_array[i])
        sending.write(first)
        for line in letter_blueprint[1:]:
            sending.write(line)

# print(name_array)
# print(letter_blueprint)