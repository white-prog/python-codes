def high(x):
    words = x.split()
    list_of_score = []
    letters = "abcdefghijklmnopqrstuvwxyz"
    for word in words:
        score = 0
        for letter in word:
            score += letters.index(letter)+1
        list_of_score.append(score)
    maxim =list_of_score.index(max(list_of_score))
    print(words[maxim])

high("man txai need a taix up to ubud")
    
                
        