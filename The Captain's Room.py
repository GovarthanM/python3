k = int(input())
rooms = list(map(int, input().split()))
captain_room = (sum(set(rooms)) * k - sum(rooms)) // (k - 1)

print(captain_room)


#input: 3
#       1 2 3 4 5


#output: 15
