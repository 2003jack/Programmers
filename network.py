
def DFS(node,computers,visited,n):
    visited[node] = True
    computer = computers[node]
    for i in range(n):
        if computer[i]==1 and not visited[i]:
            DFS(i,computers,visited,n)
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(0,n):
        if not visited[i]:
            DFS(i,computers,visited,n)
            answer +=1

    return answer
