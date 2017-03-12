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
    if len(subFieldList) > 1:
        subNum = len(subFieldList) - 1
    else:
        subNum = 0
    subNum = random.randint(0,subNum)
    #rNum = random.randint(0,optNum)
    print(subNum)
    #print(subFieldList)
    #print(field)
    subFieldPick = subNum
    subField = field[ subFieldList[ subFieldPick ]]
    return subField

def main():
    choice = triviaChoice("angles")
    #choice = definitions.trig["angles"]
    print(choice)
    return

if __name__ == "__main__":
    main()
