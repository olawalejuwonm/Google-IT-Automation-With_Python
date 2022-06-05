import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase 
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  #remove all punctuation from both strings
  string1 = re.sub(r'[%s]' % re.escape(punctuation), '', string1)
  string2 = re.sub(r'[%s]' % re.escape(punctuation), '', string2)
  #DEBUG CODE GOES HERE
  #print(___)

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False