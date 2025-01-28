import time
import random

def resultBy(score_a,score_b,tem_a,tem_b):
    if score_a > score_b:
        return tem_a
    elif score_b > score_a:
        return tem_b
    else:
        return "Tie"


def main():
    team_a = "Arjentina"
    team_b = "Portugal"
    print(f"{team_a} vs {team_b}")
    print("Kick-off time: 8:00 PM IST")
    print("Predict the result: ")
    print(f"1. {team_a}")
    print(f"2. {team_b}")
    print("3. Tie")
    results = [team_a,team_b,"Tie"]
    user_prediction = int(input("Enter your choice: "))
    print("Simulating match..")
    time.sleep(2)
    print("Final Score: ")
    scr_a = random.randint(0,7)
    scr_b = random.randint(0,7)
    print(f"{team_a} {scr_a} - {scr_b} {team_b}")
    result = resultBy(scr_a,scr_b,team_a,team_b)

    if results[user_prediction - 1] == result:
        print("You Predicted Correctly!")

    else:
        print("You are wrong")

if __name__ == "__main__":
    main()
    

