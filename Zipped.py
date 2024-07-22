n, x = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(x)]

for student in zip(*marks):
    print(sum(student) / len(student))

#input: 1 2
#       60.0
#       90.0

#output: 75.0
