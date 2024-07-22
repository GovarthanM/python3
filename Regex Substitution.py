import re
def substitution(match):
    return ' and ' if match.group(0) == '&&' else ' or '


for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', substitution, input()))


#input: 1
#       A && B


#output: A and B
