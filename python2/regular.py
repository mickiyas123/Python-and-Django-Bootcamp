import re

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

# test_phrase='sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
# test_patterns=['sd*']

test_phrase="This is a string! But it has punctuation. How can we remove it?"
test_patterns=['sd+']



# multi_re_find(test_patterns,test_phrase)


# print(re.findall('match','test phrase match in middle'))

# text='This is a string with term1,not the other!'

# match=re.search('term1',text)

# x=match.start()
# y=match.end()
# print(text[x:y])
