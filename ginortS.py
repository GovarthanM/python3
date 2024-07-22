s = input("Enter a string: ")
def sorting_key(x):
    return (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x)

sorted_characters = sorted(s, key=sorting_key)
result = ''.join(sorted_characters)
print(result)


#input: Sorting1234


#output: ginortS1234
