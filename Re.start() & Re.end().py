import re
s = input()
k = input()
pattern = re.compile(k)
m = pattern.search(s)
if not m:
    print("(-1, -1)")

while m:
    print(f"(Pattern Between: {m.start()}, {m.end() - 1})")
    m = pattern.search(s, m.start() + 1)


#input: ABCDC
#       DC


#output: (Pattern Between: 3, 4)
