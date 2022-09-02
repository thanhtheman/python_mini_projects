quiz = {
    'question 1': {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    'question 2': {
        'question': 'What is the capital of Germany?',
        'answer': 'Muchen'
    },
    'question 3': {
        'question': 'What is the capital of Netherland?',
        'answer': 'Amsterdam'
    },
    'question 4': {
        'question': 'What is the capital of England?',
        'answer': 'London'
    },
    'question 5': {
        'question': 'What is the capital of Italia?',
        'answer': 'Rome'
    },
    'question 6': {
        'question': 'What is the capital of Denmark?',
        'answer': 'Coppenhagen'
    }
}

score = 0

play_game = input('Do you want to play a game? Yes/No ')

if play_game.lower() == 'yes': 
    for x in quiz:
        print('The question is: ' + quiz[x]['question'])
        answer = input('Please enter your answer: ')
        if answer.lower() == quiz[x]['answer'].lower():
            print('Congrats! You earned 1 point.')
            score += 1
            print(f'Your score is: {score} \n')
        else:
            print("That's the wrong answer.")
            print(f"The correct answer is {quiz[x]['answer']}")
            print(f'Your score is: {score}\n')
else:
    print("Too bad! You don't want to play")
