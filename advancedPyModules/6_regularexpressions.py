# eg. search for a pattern strcuture of a string you're looking for 
# like an email of phone number 

# regex -- regular expressions -- allow us to search fot general patterns in text data

# re library creates specialised pattern strings and searches for patterns within text 
# primary skillset for regex -- understanding the special syntax for these pattern strings

# covert what you're looking for into specialised pattern syntax 
# and you can look up the necessary patterns, quantifiers, identifiers that you need

# backslashes correspond to unique identifiers 
# like placeholders waiting for a match based off a particular data type

text = "The agent's phone number is 408-373-2321. Call soon!"

print('phone' in text)

import re

pattern = 'phone'


#################
# SEARCH FUNCTION
#################
# RETRUN BACK THE FIRST MATCH OBJECT


print(re.search(pattern, text)) # <re.Match object; span=(12, 17), match='phone'>
# span= (12, 17) -- start index, end index 

pattern = "Not in text"

print(re.search(pattern, text)) # None


pattern = 'phone'
match = re.search(pattern, text)

print(match)
print(match.span())
print(match.start())
print(match.end(), '\n')

text = 'my phone once, my phone twice'
match = re.search('phone', text)
# find the first match
print(match) # <re.Match object; span=(3, 8), match='phone'>


# find all the matches
##################
# FINDALL FUNCTION
##################
# RETURNS THE LIST OF MATCHES INDICATING THE STRINGS THAT MATCHED 

matches = re.findall('phone', text)
print(matches)

print(len(matches))


# get back actual match objects -- use an interator 
##########
# FINDITER
##########
# COMBINATION OF THE 2 ABOVE 
# RETURN MATCH OBJECTS FOR THE ACTUAL PATTERN YOU'RE SEARCHING FOR 
# AND YOU CAN CALL ANY METHOD ON THAT MATCH OBJECT 

for match in re.finditer('phone', text):
    # print(match.span())
    print(match.group())
# phone
# phone

print('\n')

# building actual patterns with identifier syntax

# CHARACTER IDENTIFIERS
# \d -- digit -- file_\d\d
# \w -- alphanumeric -- \w-\w\w\w -- A-b_1 -- alphanumeric also include _
# \s -- white space -- a\sb\sc -- a b c 
# \D -- a non digit -- \D\D\D -- ABC
# \W -- non-alphanumeric -- *-+=)
# \S -- non-whitespace -- Yoyo
    
text = 'My phone number is 304-082-2344'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text) # use r in front of the string bcs the / are not escape slashes
print(phone)

# RETURN THE ACTUAL PEACE OF STRING THAT MATCHES
print(phone.group(), '\n')


# use of QUANTIFIERS to indicate repetition of the same character 

# * -- occurs zero or more times -- A*B*C* -- eg. AAACC
# ? -- once or none  -- plurals? -- eg. plural

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)


# extract the area code of the phone number 
# compile -- compiles together diff expression pattern codes 
# () -- indicate groups of the pattern
# with compile you can call the groupings individually


phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)

print(results.group())

# call by group position
# index starts at 1
print(results.group(1)) # 304

print(results.group(2))

# COMPILE -- extract parts of information while looking for a complete match

print('\n')


# OR OPERATOR TO SEARCH FOR MULTIPLE TERMS 

# the pipe operator to look for cat or dog in the string
result = re.search(r'cat|dog', 'The dog is here')
print(result)


# WILD CARD OPERATOR AS A PLACEMENT THAT WILL MATCH ANY CHARACTER PLACED THERE
matches = re.findall(r'at', 'The cat in the hat sat there.')
print(matches) # ['at', 'at', 'at']

# grab the letter in front of at 
letter_in_front = re.findall(r'.at', 'The cat in the hat sat there.')
print(letter_in_front) # ['cat', 'hat', 'sat']

# more wild card characters 
# for more control, use the character idenfiers 
more_wildchar = re.findall(r'...at', 'The cat in the hat went splat.')
print(more_wildchar) # ['e cat', 'e hat', 'splat']


# STARTS WITH: ^

# the string I'm searching through starts with a number
# it searches in the entire text itself
result = re.findall(r'^\d', '1 is a number')
print(result) # ['1']

result = re.findall(r'^\d', 'The 2 is a number')
print(result) # []


# ENDS WITH: $
result = re.findall(r'\d$', 'The 2 is a number')
print(result) # []

result = re.findall(r'\d$', 'The number is 2')
print(result, '\n') # ['2']



# EXCLUSION of characters 

phrase = 'there are 3 numbers 34 inside 5 this sentence'

# get back everything that isn't a number in the sentence: r'[^\thingstoexclude]
# exclude any digits
pattern = r'[^\d]'
print(re.findall(pattern, phrase)) # list of every single non-number character

# to get the words back together:
pattern = r'[^\d]+'  # ['there are ', ' numbers ', ' inside ', ' this sentence']
print(re.findall(pattern, phrase))


# get rid of PUNCTUATION from a sentence 
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall(r'[^!.?]+', test_phrase)) # ['This is a string', ' But it has punctuation', ' How can we remove it']

# also remove the spaces:
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.? ]+', test_phrase)
print(clean) # get a list with all the words

print(' '.join(clean), '\n') # join the words: This is a string But it has punctuation How can we remove it


# GROUPING FOR INCLUSION

text = "Only find the hyphen-word in this sentence. But you do not know how long-ish they are."
pattern = r'[\w]+' # look for a group of alphanumerics
result = re.findall(pattern, text)
print(result) # ['Only', 'find', 'the', 'hyphen', 'word', 'in', 'this', 'sentence', 'But', 'you', 'do', 'not', 'know', 'how', 'long', 'ish', 'they', 'are']


# look for hyphenated words 
pattern = r'[\w]+-[\w]+' # one group of alphn occuring one or more times x 2
result = re.findall(pattern, text)
print(result) # ['hyphen-word', 'long-ish']

# this can also be written like that: r'\w+-\w+'
# braces may be useful to keep the grouping syntax: [\w]+-[\w\d]+ 


# PARANTHESES FOR MULTIPLE OPTIONS

text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

result = re.search(r'cat(fish|nap|erpillar)', textthree)
print(result) # <re.Match object; span=(26, 37), match='caterpillar'>
