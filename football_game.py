def total_goals(num_of_goals):
    return sum(num_of_goals)

def average_goals(num_of_goals):
    return round(sum(num_of_goals) / len(num_of_goals), 2)


def main():
    goals = []
    print("-----Goals calculator------")
    matches_played = int(input("Enter total number of matches: "))
    for i in range(matches_played):
        goal = int(input("Enter goals: "))
        goals.append(goal)
    print(total_goals(goals))
    print(average_goals(goals))

if __name__ == "__main__":
    main()
    
