from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
while q:
    print(q.popleft())
