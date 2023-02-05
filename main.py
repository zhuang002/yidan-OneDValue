class EdgeChange:
    pos: int
    vChg: int

    def __init__(self, pos, vChg):
        self.pos = pos
        self.vChg = vChg


l, n, t = map(int, input().split(' '))
edgeChanges = []
for i in range(n):
    start, end, value = map(int, input().split(' '))
    edgeChanges.append(EdgeChange(start, value))
    edgeChanges.append(EdgeChange(end, -value))

edgeChanges.sort(key=lambda x: x.pos)
previousV = 0
currentV = 0
previousPos = 0
lengthLargeThanT = 0

for edgChg in edgeChanges:
    currentV += edgChg.vChg
    if currentV >= t > previousV:
        previousPos = edgChg.pos
    elif currentV < t <= previousV:
        lengthLargeThanT += edgChg.pos - previousPos
    previousV = currentV

print(lengthLargeThanT)


