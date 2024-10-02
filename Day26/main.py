import pandas

data = pandas.read_csv("Day26/nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter a word to convert to Nato code: ").upper()

result = [dict[letter] for letter in word]
print(result)
    

