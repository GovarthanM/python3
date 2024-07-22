A = set(map(int, input().split()))
n = int(input())
is_strict_superset = True
for _ in range(n):
    B = set(map(int, input().split()))
    if not (A > B):
        is_strict_superset = False
        break

print(is_strict_superset)



#input: 1 2 3 4 5
#       1
#       6 7


#output: False
