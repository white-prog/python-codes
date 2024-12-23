

def main():
    print("------------------------QUIZ--------------------------")
    for i in range(3):
        print()


    football_quiz = {
    "Who won the FIFA World Cup in 2018?": "France",
    "Which player has won the most Ballon d'Or awards?": "Lionel Messi",
    "What is the name of the stadium where Manchester United plays?": "Old Trafford",
    "Which country is known as the birthplace of football?": "England",
    "Who holds the record for the most goals scored in international football?": "Cristiano Ronaldo"
    }
    cnt = 1
    score = 0
    for i in football_quiz:
        print(f"Question {cnt} : {i}")
        user = input("Enter answer: ")
        cnt += 1
        if user == football_quiz[i]:
            score += 1
            print("Correct!")
        else:
            score -= 1
            print("Wrong!")
    print()
    print(f"Score : {score}")







if __name__ == "__main__":
    main()