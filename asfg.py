import re
with open('regex_test.txt') as f:
    data = f.readlines()
    

    names = re.compile("([A-Z][a-z]+) ([A-Z][a-z]* )*([A-Z][a-z]+)")

    for person in data:
        try:
            match = (names.search(person)).group()
            print(match)
        except:
            print(None)
            
           
            
            
 # """
# Expected Output
# Abraham Lincoln
# Andrew P Garfield
# Connor Milliken
# Jordan Alexander Williams
# None
# None
# """           
            # if match:
            #     print(match.groups())
            # else:
            #     print(None)