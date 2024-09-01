import random
import pygame
import time
window = pygame.display.set_mode((700, 700))

class Case:
    def __init__(self, pos):
        self.visited = False
        self.linkto = []
        self.top = True
        self.botom = True
        self.righ = True
        self.left = True
        self.position = pos
  
grid = [[Case((x, y)) for x in range(10)] for y in range(10)]
running = True
stack = [(0, 0)]
visited = [(0, 0)]

def getifoofcase(pos):
    try:
        if pos[0] < 0 or pos[1] < 0:
            return False
        return grid[pos[0]][pos[1]], pos
    except:
        return False
        
def getneibors(pos):
    pos = getifoofcase([pos[0]+1, pos[1]]), getifoofcase([pos[0]-1, pos[1]]), getifoofcase([pos[0], pos[1]+ 1]), getifoofcase([pos[0], pos[1]-1])
    rep = []
    for position in pos:

        if position != False and position[0].visited == False :
            rep.append(position)
    return rep





#def displaytoplink(case):
#    if [case.position[1] + 1, case.position[0]] not in case.linkto:
#        pygame.draw.line(window, (100, 100, 100), (case.position[0] * 70, case.position[1]* 70), (case.position[0] + 1* 70, case.position[1]* 70))
        
        
#def displayleftlink(case):
#    if [case.position[1], case.position[0]-1] not in case.linkto:
#        pygame.draw.line(window, (100, 100, 100), (case.position[0] * 70, case.position[1]* 70), (case.position[0] * 70, case.position[1] - 1* 70))
        
    
    
    
def displaylabfun():
    print(visited)
    if len(visited) > 1:
        i = len(visited) - 2
        print(visited), print(i + 1)
        if visited[i][0] - visited[i+1][0] != visited[i][0] and  visited[i][0] - visited[i+1][0] > 0:
            dirrection = "right"
        if visited[i][0] - visited[i+1][0] != visited[i][0] and  visited[i][0] - visited[i+1][0] < 0:
            dirrection = "left"
                    
        if visited[i][1] - visited[i+1][1] != visited[i][1] and  visited[i][1] - visited[i+1][1] > 0:
            dirrection = "down"
        if visited[i][1] - visited[i+1][1] != visited[i][1] and  visited[i][1] - visited[i+1][1] < 0: 
            dirrection = "up"

        print((visited[i][0] * 70, visited[i][1]* 70), ((visited[i][0] + (1 if dirrection == "right" else -1 if dirrection == "left" else 0))* 70, (visited[i][1] + (1 if dirrection == "down" else -1 if dirrection == "up" else 0))* 70))
        pygame.draw.line(window, (100, 100, 100), (visited[i][0] * 70, visited[i][1]* 70), ((visited[i][0] + (1 if dirrection == "right" else -1 if dirrection == "left" else 0))* 70, (visited[i][1] + (1 if dirrection == "down" else -1 if dirrection == "up" else 0))* 70))
        pygame.display.flip()
        time.sleep(1)
      
def displaylab():
    
    for i in range(len(visited) -1):
        if visited[i][0] - visited[i+1][0] != visited[i][0] and  visited[i][0] - visited[i+1][0] > 0:
            dirrection = "right"
        if visited[i][0] - visited[i+1][0] != visited[i][0] and  visited[i][0] - visited[i+1][0] < 0:
            dirrection = "left"
            
        if visited[i][1] - visited[i+1][1] != visited[i][1] and  visited[i][1] - visited[i+1][1] > 0:
            dirrection = "down"
        if visited[i][1] - visited[i+1][1] != visited[i][1] and  visited[i][1] - visited[i+1][1] < 0: 
            dirrection = "up"
        print((visited[i][0] * 70, visited[i][1]* 70), ((visited[i][0] + (1 if dirrection == "right" else -1 if dirrection == "left" else 0))* 70, (visited[i][1] + (1 if dirrection == "down" else -1 if dirrection == "up" else 0))* 70))
        pygame.draw.line(window, (100, 100, 100), (visited[i][0] * 70, visited[i][1]* 70), ((visited[i][0] + (1 if dirrection == "right" else -1 if dirrection == "left" else 0))* 70, (visited[i][1] + (1 if dirrection == "down" else -1 if dirrection == "up" else 0))* 70))
        pygame.display.flip()
        time.sleep(0.2)
        
    
    
    
    i = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            i += 1
            
            
            
while running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                running = False
            
            
    if len(stack) > 0:
        neibors = getneibors(stack[-1])
        print(neibors)
        if len(neibors) == 0:
            stack.pop()
        else:
            
            rd = random.randint(0, len(neibors)-1)
            print(stack)
            grid[neibors[rd][1][0]][neibors[rd][1][1]].visited = True
            grid[neibors[rd][1][0]][neibors[rd][1][1]].linkto.append(stack[-1])
            grid[stack[-1][0]][stack[-1][1]].linkto.append(neibors[rd][1])
            stack.append(neibors[rd][1])
            visited.append((neibors[rd][1][0], neibors[rd][1][1]))

    else:
        
        displaylab()
    pygame.display.flip()

for x in range(len(grid)) :
    print("")
    for y in range(len(grid[x])):
        print(grid[x][y].linkto, end='')
