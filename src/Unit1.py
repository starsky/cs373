#initial probabilities
from cherrypy.test.test_conn import pov
#World`s map
world = ['green', 'red', 'red', 'green', 'green']
#initial distributions
p = [1./len(world)]*len(world)
#Measurement
measurement = ['red','red']
motions = [1,1]
#Probability of sensnig state and being in that state
pHit = 0.6
#Probablity of sensing state and being in other state
pMiss = 0.2
#Add exact probability
pExact = 0.8
#Add overshoot probability
pOvershoot = 0.1
#Add undershoot probability
pUndershoot = 0.1

def sense(p, Z):#Define a function sense return q
    q = []
    for i in range(len(world)):
        hitted = Z == world[i]
        q.append(p[i] * ((hitted * pHit) + (1-hitted)*pMiss))
        s = sum(q)
    return [e/s for e in q]

def move(p,U):
    q = []
    for i in range(len(p)):
        s =  pExact * p[(i-U) % len(p)]
        s += pOvershoot * p[(i-U-1) % len(p)]
        s += pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for i in range(len(measurement)):
    p = sense(p, measurement[i])
    p = move(p, motions[i])
    
print p