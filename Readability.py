# Readability

# Getting text input
text = input("Enter text: ")

# Defining counters & punctuations
letter_count = 0
word_count = 1
sent_count = 0
punctuations = ['.', '!', '?']

# Counting letters (a-z, A-Z), words & sentences
for letter in text:
    if letter == ' ':
        word_count += 1
    elif letter.isalpha():
        letter_count += 1
    elif letter in punctuations:
        sent_count += 1
              
# Calculating L & S
L = (letter_count/word_count) * 100 
S = (sent_count/word_count) * 100

# Calculating & rounding Coleman-Liau index
index = round(0.0588 * L - 0.296 * S - 15.8)

# Classifying & printing grade of input text
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade {}".format(index))
