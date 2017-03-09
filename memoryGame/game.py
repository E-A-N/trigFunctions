import definitions
import random

#api example sine = definitions.trig["functions"]["sine"]["name"]

def triviaChoice(triv):
    '''
        @string triv: key used to access definitions api
    '''
    subject = definitions.trig[triv]
    optNum = len(subject) - 1
    fieldPick = random.randint(0,optNum)
    subFieldPick = random.randint(0,optNum)

    return subject

def main():
    choice = triviaChoice("angles")["theta"]["definition"]
    print(choice)
    return

if __name__ == "__main__":
    main()
