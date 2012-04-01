#initial probabilities
p = [0.2, 0.2, 0.2, 0.2, 0.2]
#World`s map
world = ['green', 'red', 'red', 'green', 'green']
#Measurement
measurement = ['red','green']
#Probability of sensnig state and being in that state
pHit = 0.6
#Probablity of sensing state and being in other state
pMiss = 0.2
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
        q.append(p[(i-U) % len(p)])
    return q

for Z in measurement:   
    p = sense(p, Z)
    
p = move(p,-1)    
print p