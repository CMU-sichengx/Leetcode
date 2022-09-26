from collections import deque
from collections import defaultdict

def Maze(n, steps):
    # Construct the graph
    graph = set([(0, 0)])

    coordinateChange = {
        "south": (0, -1),
        "north": (0, 1),
        "east": (1, 0),
        "west": (-1, 0)
    }

    direction = {
        (0, -1): "south",
        (0, 1): "north",
        (1, 0): "east",
        (-1, 0): "west"
    }

    x, y = 0, 0
    for dir in steps:
        dx, dy = coordinateChange[dir]
        x, y = x+dx, y+dy
        graph.add((x, y))
    print(graph)
    # Perform BFS search on the graph 
    destX, destY = x, y
    Q = deque()
    Q.append([(0, 0)])
    visited = set()
    visited.add((0, 0))

    def BFS():
        while Q:
            path = Q.popleft()
            x, y = path[-1]
            visited.add((x, y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newX, newY = x+dx, y+dy
                if (newX, newY) in visited or (newX, newY) not in graph: continue
                if newX == destX and newY == destY:
                    return path + [(destX, destY)]
                    
                else:
                    visited.add((newX, newY))
                    Q.append(path + [(newX, newY)])
    
    shortestPath = BFS()
    print(shortestPath)
    res = []
    for u, v in zip(shortestPath, shortestPath[1:]):
        x1, y1 = u
        x2, y2 = v
        res.append(direction[(x2-x1, y2-y1)])
    return res

input1 = ["south", "south", "south", "south", "east", "north", "east", "south", "east", "north", "north", "east"]
print(Maze(len(input1), input1))

input2 = ["south", "east", "east", "south", "south", "west", "west", "east", "east", "south"]
print(Maze(10, input2))
    
input3 = ["south"] * 3 + ["east"] * 5 + ["south"] * 2 + ["west"] * 5 + ["south"] * 2 + ["east"] * 2 + ["north"] * 2 \
    + ["east"] * 3 + ["north"] * 2 + ["west"] * 5 + ["north"] * 2 + ["east"] * 7 + ["south"] * 8
print(Maze(len(input3), input3))

s = "south"
n = "north"
e = "east"
w = "west"
input4 = [
    s,
    s,
    s,
    e,
    e,
    e,
    e,
    e,
    s,
    s,
    w,
    w,
    w,
    w,
    w,
    s,
    s,
    e,
    e,
    n,
    n,
    e,
    e,
    e,
    n,
    n,
    w,
    w,
    w,
    w,
    w,
    n,
    n,
    e,
    e,
    e,
    e,
    e,
    e,
    e,
    s,
    s,
    s,
    s,
    s,
    s,
    s,
    s
]
print("~~~", len(input4))
print(Maze(48, input4))

print("________________________")
input5 = [s, e, e, s, s, w, w, e, e, s]
print(Maze(len(input5), input5))

def CountMistakes(submissions):
    correct = [set() for i in range(len(submissions[0]))]
    mistakes = defaultdict(int) # word -> frequency
    

    for i in range(len(submissions[0])):
        counter = defaultdict(int)
        max_count = -1
        for submission in submissions:
            word = submission[i]
            counter[word] += 1
            max_count = max(max_count, counter[word])
        
        for word in counter:
            if counter[word] == max_count:
                correct[i].add(word)

    for submission in submissions:
        visited = set()
        for i in range(len(submission)):
            word = submission[i]
            if word not in correct[i]:
                if word not in visited:
                    visited.add(word)
                    mistakes[word] += 1

    print(correct)
    mistake_words = list(mistakes.keys())
    mistake_words.sort(key=lambda w : (-mistakes[w], w))
    return mistake_words


input1 = [
    ["your", "bear", "drinks", "beer"],
    ["your", "bear", "eats", "beer"],
    ["yuor",  "bear", "drinks", "beer"],
    ["your", "bear", "drinks", "beer"],
    ["yuor", "bear", "drinks", "bear"],
]
print(CountMistakes(input1))

input2 = [
    ["we", "run", "to", "mars"],
    ["they", "run", "to", "venus"],
    ["we",  "walk", "to", "mars"],
    ["they", "mars", "to", "run"],
]
print(CountMistakes(input2))

input3 = [
    ["your", "eats", "drinks", "beer"],
    ["yours", "bear", "eats", "beer"],
    ["the",  "bear", "the", "eats"],
    ["your", "the", "drinks", "beer"],
]
print(CountMistakes(input3))

