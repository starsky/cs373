'''
Created on 29-02-2012

@author: michal
'''
colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

def initProbabilities(p,w,h):
    cells = w*h
    for i in range(h):
        tmp_list = []
        for j in range(w):
            tmp_list.append(1./cells)
        p.append(tmp_list)
    return p

def move(p,vect):
    q = [x[:] for x in [[0]*len(p[0])]*len(p)]
    for i in range(len(p)):
        for j in range(len(p[i])):
            q[(i + vect[0]) % len(p)][(j + vect[1])%len(p[i])] += p[i][j] * p_move
            q[i][j] += p[i][j] * (1 - p_move)
    return q

def sense(p,m):
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (colors[i][j] == m)
            p[i][j] = hit*(p[i][j]*sensor_right) + (1-hit)*(p[i][j]*(1-sensor_right))
    s = 0
    for i in range(len(p)):
        s += sum(p[i])
    for i in range(len(p)):
        for j in range(len(p[i])):
            p[i][j] /= s
    return p
    
p = []

p = initProbabilities(p,len(colors[0]),len(colors))
for i in range(len(motions)):
    p = move(p, motions[i])
    p = sense(p,measurements[i])

#Your probability array must be printed 
#with the following code.

show(p)




