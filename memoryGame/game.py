import definitions
import random

#api example sine = definitions.trig["functions"]["sine"]["name"]

def triviaChoice(triv):
    '''
    Randomly generates and returns a random piece of data.
    :type triv: string
    :param triv: key used to access data interface subject of choice
    '''
    subject = definitions.trig[triv]
    fieldList = subject["fieldList"]
    subFieldList = subject["subFieldList"]
    #Offset the length by 3 to make intended fields inaccessible
    optNum = len(subject) - 3
    fieldPick = random.randint(0,optNum)
    field = subject[ fieldList[ fieldPick ]]
    optNum = len(field) - 1
    subFieldPick = random.randint(0,optNum)
    subField = field[ subFieldList[ subFieldPick ]]
    return subField

def main():
    choice = triviaChoice("angles")
    #choice = definitions.trig["angles"]
    print(choice)
    return

if __name__ == "__main__":
    main()
