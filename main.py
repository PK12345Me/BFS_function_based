import itertools, sys, time, random

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

class Explored:

    def __init__(self) -> None:
        self._explored = []
    
    def add(self, val):
        self._explored.append(val)

    def nodes_explored(self):    
        return self._explored

explored = Explored()
goal = random.randint(1, 9)
print("goal is: ", goal)

frontierList = []
direction = {'up':(-1,0),
          'down':(1,0),
          'left':(0,-1),
          'right':(0,1)}

def all_nodes(value):
    listCheck = []
    current = [(key1,key) for key1, value1 in enumerate(grid) for key,val in enumerate(value1) if val == value]

    explored.add(grid[current[0][0]][current[0][1]])

    print("explored.nodes",explored.nodes_explored())

    for kya in direction:
        #print("direction is:", ky)
        ky = direction[kya]
        x = current[0][0] + ky[0]
        y = current[0][1] + ky[1]
        if 0 <= x < 3 and 0 <= y < 3:

            listCheck.append(grid[x][y])
    #print("outfrom All_nodes function ", listCheck)
    return frontier(listCheck)   #frontier(listCheck)

def frontier(item):
    global frontierList

    if isinstance(item, list):
   
        frontierList.extend(item)
    else:
        frontierList.append(item)
    time.sleep(1)
    print("this is the frontierList: ",frontierList)
    
    while frontierList: 
        
        node = frontierList[0]
        #print("explored nodes now is: ", explored.nodes_explored())
        print("node now is: ", node)

        if node in explored.nodes_explored():
            #print(f"node  {node} already explored - removing it")
            frontierList = frontierList[1:]
            #print(f"new first node of {frontierList} is {frontierList[0]}")
            
        elif node == goal or explored.nodes_explored()[0] == goal:
            print("Goal reached, code execution ended!")
            break

        elif node not in explored.nodes_explored():
            #print(f"to expand this {node} node")
            frontierList = frontierList[1:]

            return all_nodes(node)

    else:
        return Exception("Frontier is empty")


def main():
    # random int generator
    a = random.randint(1, 9)
    print("search starts with", a)
    listP = a
    all_nodes(listP)


main()
