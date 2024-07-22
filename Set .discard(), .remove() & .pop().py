n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass  
    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))


#input: 9
#       1 2 3 4 5 6 7 8 9
#       5
#       pop
#       remove 9
#       discard 8
#       remove 7
#       pop



#output: 18
