import re
pattern = re.compile(r"""
    ^                    
    M{0,3}               
    (CM|CD|D?C{0,3})    
    (XC|XL|L?X{0,3})    
    (IX|IV|V?I{0,3})    
    $                    
""", re.VERBOSE)

print(bool(pattern.match(input())))


#input: VII


#output: True
