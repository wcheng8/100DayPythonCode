import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# Create phonetic dictionary from csv
phonetic_list = {}
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, code) in alphabet_df.iterrows():
    phonetic_list[code.letter] = code.code

# print(phonetic_list)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
accepted_word = True
# Use list comprehension to output phonetic word
while accepted_word:
    try:
        word = input("Input the text you want to turn into phonetic code? ")
        phonetic_word = [phonetic_list[letter] for letter in word.upper()]
        print(phonetic_word)
        accepted_word = False
    except KeyError:
        print("Only letter of the alphabets are accepted. Please enter again")
