import re

# ^ use to match word that begins/cobntains.  findstr ^fruit words 
# $ match words that ends with findstr cat$ words

result = re.search(r"aza", "plaza")# r indicate raw string
result = re.search(r"aza", "bazaar")# r indicate raw string
result = re.search(r"aza", "maze")# r indicate raw string
# print(re.search(r"^x", "xenon"))
# print(re.search(r"p.ng", "penguin"))
# print(re.search(r"p.ng", "clapping"))
# print(re.search(r"p.ng", "sponge"))
# print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))


# caharacter classess are inside []

# print(re.search(r"[Pp]ython", "Python"))
# print(re.search(r"[a-z]way", "The end of the highway"))
 # print(result)
# print(re.search(r"[a-z]way", "What a way to go?"))
#or
# print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# print(re.search("cloud[a-zA-Z0-9]", "cloud9"))


#This search for any pattern thats not a letter
# print(re.search(r"[^a-zA-Z]", "This is a senentence with spaces."))

# print(re.search(r"[^a-zA-Z ]", "This is a senentence with spaces."))

#  | is use for or

# print(re.search(r"cat|dog", "I like cats."))

# print(re.search(r"cat|dog", "I like dogs."))


# print(re.search(r"cat|dog", "I like both dogs and cats."))

#findall is use to get all possible matches

# print(re.findall(r"cat|dog", "I like both dogs and cats."))


#Repeated qualifiers

# print(re.search(r"Py.*n", "Pygmalion")) # the * means match the whole word
# print(re.search(r"Py.*n", "Python Programming")) # the * means match the whole word

# print(re.search(r"Py[a-z]*n", "Python Programming")) # the * means match the whole word
# print(re.search(r"Py[a-z]*n", "Pyn")) # the * means match the whole word

#multipliers + and ?
# print(re.search(r"o+l+", "goldfish"))
# print(re.search(r"o+l+", "woolly"))

# print(re.search(r"o+l+", "boil"))

# ? is another multiplier that means either zero or one occurence of the characte before it

print(re.search(r"p?each", "To each thier own"))

print(re.search(r"p?each", "I like peaches"))

# while True:
#     res = input("Enter your email")

    
