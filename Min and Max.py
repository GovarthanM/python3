import re
vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (consonants, vowels, consonants), input(), re.I)
print('\n'.join(m or ['-1']))


#input: 2 2
#       1 2
#       3 4


#output: 3
