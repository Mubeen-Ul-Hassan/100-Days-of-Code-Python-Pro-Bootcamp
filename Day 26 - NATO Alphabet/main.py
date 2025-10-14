import pandas

student_dict = pandas.read_csv("./nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(student_dict)

#TODO 1. Create a dictionary in this format:
dict_nato = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Your name: ")

nato_alphabet = []
for letter in name.upper():
    nato_alphabet.append(dict_nato[letter])

print(nato_alphabet)

