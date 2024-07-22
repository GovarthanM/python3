n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

print(len(s1.symmetric_difference(s2)))



#input: 5
#       1 2 3 4 5
#       3
#       5 6 7


#output: 6
