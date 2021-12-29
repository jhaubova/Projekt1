# vstupni hodnoty
users = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}
line = "-" * 30

# nadpis
print("$ python projekt1.py")

# zeptej se uzivatele na jmeno a heslo a podminky správnosti hesla
while True:
    username = input("Enter your username:")
    if not username:
        print(f"Unregistered user.\nTerminating the program.")
    else:
        break
while True:
    password = input("Enter your password:")
    if not password:
        print(f"Unregistered user.\nTerminating the program.")
    else:
        break

if password == str(users.get(username)):
    print(f"Welcome to the app., {username}.\nWe have 3 texts to be analyzed.")
else:
    print(f"unregistered user, {username}.\nTerminating the program..")
    exit()
print(line)

# vlozeni textu a carky
TEXTS = [
'''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# vyber textu
text_selection = 0
while True:
    selection = input("Enter a number between 1 and 3 to select: ")
    if not selection:
        print(f"Not correct...")
    else:
        break
if selection.isnumeric():
    selection = int(selection)
    if selection < 1 or selection > 3:
        print(f"Is not between numbers 1 and 3. Ending app...")
        exit()
    else:
        text_selection = TEXTS[selection - 1]

# statistika
divided_text = text_selection.split()
divided_text_1 = [word.strip(',.?!') for word in divided_text]
numbers_of_length = [len(word) for word in divided_text_1]
titlecase = [word for word in divided_text_1 if word.istitle() and word.isalpha()]
uppercase = [word for word in divided_text_1 if word.isupper() and word.isalpha()]
lowercase = [word for word in divided_text_1 if word.islower() and word.isalpha()]
numeric = [word for word in divided_text_1 if word.isnumeric()]
numeric_suma = [int(number) for number in numeric]
print(line)
print(f"There are {len(divided_text)} words in the selected text.")
print(f"There are {len(titlecase)} titlecase words.")
print(f"There are {len(uppercase)} uppercase words.")
print(f"There are {len(lowercase)} lowercase words.")
print(f"There are {len(numeric)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric_suma)}.")
print(line)
print(f"LEN | OCCURENCES.center(1) | NR.")
print(line)

# tabulka
stars = "+"
spaces = " "
numbers = set(numbers_of_length)
frequency = []
for cislo in numbers:
    frequency.append(numbers_of_length.count(cislo))
highest_number = max(frequency)
for num in numbers:
    count_of_spaces = highest_number - numbers_of_length.count(num)
    print(f"{num} | {stars * numbers_of_length.count(num)} {spaces * count_of_spaces} | {numbers_of_length.count(num)}")

    print(line)


