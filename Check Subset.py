for _ in range(int(input())):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))




#input: 1
#       3
#       1 2 3
#       5
#       1 2 3 4 5



#output: True
