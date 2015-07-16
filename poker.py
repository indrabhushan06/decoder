#!/usr/bin/env python2.7

def pokerEvaluate(Users):
    for key,value in Users.iteritems():
        values,suit=setCards(Users[key])
        print values
        #Users[key]=ge(values,suit)   

def setCards(l):
    values=[]
    suits=[]
    x=l.split()
    for i in x:
        suits.append(i[-1])
        if i[0]=='J':
            values.append(11)
        elif i[0]=='Q':
            values.append(12)
        elif i[0]=='K':
            values.append(13)
        elif i[0]=='A':
            values.append(14)
        else:
            values.append(int(i[:len(i)-1]))
    return sorted(values),suits
            
print pokerEvaluate({'Joe':'8C 10S KC 9H 4S', 'Bob':'7D 2S 5D 3S AC', 'Sally':'8C AD 8D AC 9C', 'Tina':'7C 5H 8D QD KS'})

