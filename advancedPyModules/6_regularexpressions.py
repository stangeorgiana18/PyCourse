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
