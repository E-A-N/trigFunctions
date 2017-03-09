import definitions
import random

#api example sine = definitions.trig["functions"]["sine"]["name"]

def triviaChoice(triv):
    '''
        @string triv: key used to access definitions api subject of choice
    '''
    subject = definitions.trig[triv]
    fieldList = subject["fieldList"]
    subFieldList = subject["subFieldList"]
    optNum = len(subject) - 1
    fieldPick = random.randint(0,optNum)
    field = subject[fieldPick]
    optNum = len(field) - 1
    subFieldPick = random.randint(0,optNum)
    subField = field[subFieldPick]

    return

def main():
    choice = triviaChoice("angles")
    print(choice)
    return

if __name__ == "__main__":
    main()
