print("*************************          CHOOSE BEST YOUNG PLAYERS      ***********************************")
candidates = [("Yamal",'Y'),("Mbappe",'K'),("Haaland",'H'),("Musiala",'M')]

voters = 5

votes = {}
voters_name = {}
for i in candidates:
    print("{} : {}".format(i[0],i[1]))



for i in range(voters):
    name = input("Enter your name: ")
    vote = input("Your favourite player code: ")
    if vote not in votes:
        votes[vote] = 1
    else:
        votes[vote] += 1
    voters_name[name] = vote

winner = 'Default'
min = -999
for i in votes:
    if votes[i] > min:
        min = votes[i]
        winner = i

for i in candidates:
    if i[1] == winner:
        print("Hurray "+i[0]+" won!!!!")
#include all other settings later

