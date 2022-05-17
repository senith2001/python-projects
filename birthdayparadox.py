import random,datetime

def valid(size):
    if (size.isdecimal() and (1 <= int(size)<=100)):
        return True
    else :
        return False
    
def generateGroup(size):
    group = []
    date = datetime.date(2001,1,1)
    for i in range(size):
        rand = datetime.timedelta(random.randint(1,364))
        group.append(date+rand)
    return group
    
def checkRepeat(group):
    if len(group) == len(set(group)):
        return None
    else:
        for i in range(len(group)):
            for j  in range(i+1,len(group)):
                if group[i] == group[j]:
                    return group[i]
    
def printG(group):
    for i in range(len(group)):
        print(months[group[i].month-1]," ",group[i].day,end=", " if (i<len(group)-1) else "")
    
months = ['january','february','march','april','may','june','july','august','september','october',
'november','december']
def simulate(size):
    sim = 0
    for i in range(100000):
        group = generateGroup(size)
        if checkRepeat(group) != None:
            sim +=1
        if i%10000 == 0 and i>0:
            print("running {}simulations".format(i))
    print()
    print("100000 simulations ran.")
    print("out of 100000 simulations there were {} same birthdays occured.".format(sim))
    print("so probabilty of 2 same birthdays occur in {} group of people is {}.".format(size,
    round((sim/100000)*100,2)))


def main():
    print('''
            birthday paradox by senith deelaka.
            This program shows that out of N group of people,odds of two people having the same birthdays 
            is suprisingly large''')
    size = ""
    while not valid(size):
        size = input("enter the size of group: ")
        
    group = generateGroup(int(size))
    printG(group)
    print()
    if checkRepeat(group) != None:
        print(months[checkRepeat(group).month-1]," ",checkRepeat(group).day)
    input("to run 100000 simulations press enter")
    simulate(int(size))


if __name__ == "__main__":
    main()