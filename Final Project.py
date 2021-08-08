
def getQuestionNumber(introMessage):
    return input(introMessage)

def correctMessage(guessedAnswer, questionAnswer):
        if guessedAnswer.lower() == questionAnswer.lower():
            return "Solution you guessed was " "\"" + guessedAnswer + "\" and the correct word was " + questionAnswer
1
def isCorrect(guessedAnswer, questionAnswer):
        if guessedAnswer.lower() == questionAnswer.lower():
            return True
        return False

def TryAnswer(questionMessage):
        return input(questionMessage)

def gameOver(questionAnswer):
        AnsweredValue = "Game is over. The correct answer was\"" + questionAnswer.title() + "\". """
        return AnsweredValue
def main():
    cluesDictionary = {1: {"whale": "This is the largest mammal type"},
                       2: {"eagle": "This is the US national bird"},
                       3: {"football": "This popular sport is played with helmets and pads"},
                       4: {"hawaii": "This state is a collection of islands"},
                       5: {"moon": "This satellite helps control the tides"}}
    introMessage = "Enter as question number from 1 to 5, and you will play that clue. Enter -1 to quit"
    while True:
        try:
            questionNumber = int(getQuestionNumber(introMessage))
        except:
            continue
        if questionNumber == -1:
            print("Good Bye")
            break
        if questionNumber not in range(1, 6):
                continue
        questionMessage = list(cluesDictionary[questionNumber].values())[0] + ". What is it?"
        questionAnswer = list(cluesDictionary[questionNumber].keys())[0].lower()
        guessedAnswer = TryAnswer(questionMessage)
        if isCorrect(guessedAnswer, questionAnswer):
            print(correctMessage(guessedAnswer, questionAnswer))
            print("wanna play the game again?")
        else:
            x = 0
            for i in questionAnswer:
                if x == 0:
                    print("The first letter is:", i + ".")
                    x += 1
                    guessedAnswer = TryAnswer("Try again")
                    if isCorrect(guessedAnswer, questionAnswer):
                        print(correctMessage(guessedAnswer, questionAnswer))
                        break
                elif i == len(questionAnswer) - 1:
                    print("The last letter was:", i + ".\n")
                    print(gameOver(questionAnswer))
                else:
                    print("answer was incorrect.")
                    print("The next letter is", i + ".")
                    x += 1
                    guessedAnswer = TryAnswer("Try again")
                    if isCorrect(guessedAnswer, questionAnswer):
                        print(correctMessage(guessedAnswer, questionAnswer))
                        break
main()
