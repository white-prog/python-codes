def random_goal():
    lis = ["goal","saved"]
    import random
    num = random.randint(0,1)
    return lis[num]

team_1 = []
team_2 = []
for i in range(5):
    team_1.append(random_goal())
    team_2.append(random_goal())

def more(num1,num2):
    if num1 > num2:
        return str(num1) + " team 1 wins"
    elif num1 == num2:
        return "draw"
    else:
        return str(num2) + " team 2 wins"

score_team1 = len([i for i in team_1 if i == "goal"])
score_team2 = len([i for i in team_2 if i == "goal"])
print(more(score_team1,score_team2))

