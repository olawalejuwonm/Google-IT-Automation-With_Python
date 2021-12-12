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

# print(re.search(r"p?each", "To each thier own"))

# print(re.search(r"p?each", "I like peaches"))


#escape character
# print(re.search(r".com", "welcome"))

# print(re.search(r"\.com", "welcome"))
# print(re.search(r"\.com", "mydomain.com"))


# print(re.search(r"\w*", "This is an example")) #\w matches alphanumerics and underscore


# print(re.search(r"\w*", "And_this_is_another")) #\w matches alphanumerics and underscore
# \d for matching digits, \s for matching whitespace characters like space
# \b for word boundaries and a few others
#regex101.com

# print(re.search(r"A.*a", "Argentina"))

# print(re.search(r"A.*a", "Azerbaijan"))

# print(re.search(r"^A.*a$", "Azerbaijan"))
# print(re.search(r"^A.*a$", "Australia"))

# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern, "_this_is_a_valid_variable_name"))

# print(re.search(pattern, "this is isn't a valid variable"))

# print(re.search(pattern, "my_variable1"))
# print(re.search(pattern, "2my_variable1"))
#The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.
def check_web_address(text):
  pattern = r"\.[a-zA-Z]*$"
  result = re.search(pattern, text)
  return result != None

# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True

#The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
def check_time(text):
  pattern = r":[0-9][1-9][\samAMpmPM]"
  result = re.search(pattern, text)
  return result != None

# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False
# print(check_time("6:02km")) #False

#The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 
def contains_acronym(text):
  pattern = r"\([0-9A-Za-z]*\)" 
  result = re.search(pattern, text)
  return result != None

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


#Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
def check_zip_code (text):
  result = re.search(r"\s[0-9][0-9][0-9][0-9][0-9/w0-9]+", text)
  return result != None

# print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
# print(check_zip_code("90210 is a TV show")) # False
# print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
# print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
# while True:
#     res = input("Enter your email")

    
#capturing groups
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# print(result)
# print(result.groups()) #tuple
# print(result[0])
# print("{} {}".format(result[2], result[1]))

# def rearrange_name(name):
#     result = re.search(r"^(\w*), (\w*)$", name)
#     if result is None:
#         return name
#     return "{} {}".format(result[2], result[1])

# print(rearrange_name("Lovelace, Ada"))
# print(rearrange_name("Hopper, Grace M."))#did not match

# def rearrange_name(name):
#     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
#     if result == None:
#         return name
#     return "{} {}".format(result[2], result[1])

# print(rearrange_name("Hopper, Grace M."))


#numeric repition quantifier
# print(re.search(r"[a-zA-Z]{5}", "a ghost")) #looking for 5 letters word

# print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) #looking for 5 letters words or more

# print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")) #looking for 5 letters word exactly

# print(re.findall(r"\w{5,10}", "I really like strawberries")) #looking for 5 to 10 letters words - close ended

# print(re.findall(r"\w{5,}", "I really like strawberries")) #looking for 5 upward words  - open ended

# print(re.findall(r"s\w{,28}", "I really like strawberries")) #looking for s + 0 upto 28 words

#regex for getting pid in log file
# regex = r"\[(\d+)\]"
# log = "July 31 mycomputer bad process[12345]: ERROR Performing package upgrade"
# # print(re.search(regex, log)[1])
# result = re.search(regex, "99 elephants in a [cage]")
# # print(result[1])

# def extract_pid(log_line):
#     regex = r"\[(\d+)\]"
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result[1]
# print(extract_pid(log))
# print(extract_pid("99 elephants in a [cage]"))



#splitting and replacing
# res = re.split(r"[.?!]", "One sentence. Another One? And the last one!")
# print(res)

# res = re.split(r"([.?!])", "One sentence. Another One? And the last one!") #for group
# print(res)

# rs = re.sub(r"[\w.%+-]+@[\w.%+-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com") #substitute
# print(rs)

# rs = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada") #\2 to match second capture group, \1 for first
# print(rs)


#Question 1
#We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use the transform_record function to do that.


def transform_record(record):
  new_record = re.sub(r"((\d|-)+)", r"+1-\1", record)
  return new_record

# print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# # Sabrina Green,+1-802-867-5309,System Administrator

# print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# # Eli Jones,+1-684-3481127,IT specialist

# print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# # Melody Daniels,+1-846-687-7436,Programmer

# print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# # Charlie Rivera,+1-698-746-3357,Web Developer 



#The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
def multi_vowel_words(text):
  pattern =r"\b\w*[aeiou]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

# print(multi_vowel_words("Life is beautiful")) 
# # ['beautiful']

# print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# # ['Obviously', 'queen', 'courageous', 'gracious']

# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# # ['rambunctious', 'quietly', 'delicious']

# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# # ['queue']

# print(multi_vowel_words("Hello world!")) 
# # []



#Question 4
# The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function
def transform_comments(line_of_code):
  result = re.sub(r"#+", "//", line_of_code)
  return result

# print(transform_comments("### Start of program")) 
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable")) 
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable")) 
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)")) 
# # Should be "  return(number)"



#Question 5
#The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.

# def convert_phone_number(phone):
#   result = re.sub(r"([0-9]{3}\b)-([0-9]{3}\b-[0-9]{4}\b)", r"(\1) \2", phone)
#   return result

# print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
# print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
# print(convert_phone_number("123-123-12345")) # 123-123-12345
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300