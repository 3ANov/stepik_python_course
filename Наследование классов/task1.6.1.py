import sys
sys.stdin = open("input.txt", "r")

classes = {}
n = int(input())
for _ in range(n):
    inp_str = input()
    inp_list = inp_str.split(':')
    if len(inp_list) == 1:
        classes[inp_list[0]] = ['Obj']
    else:
        classes[inp_list[0].split()[0]] = inp_list[1].split()


print(classes)

n = int(input())


def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if not graph.get(start):
        return None

    for node in graph[start]:

        if node not in path:

            newpath = find_path(graph, node, end, path)

            if newpath: return newpath

    return None


for _ in range(n):
    parent, child = input().split()
    if find_path(classes,child, parent) is not None:
        print("Yes")
    else:
        print("No")



'''
BFS(start_node, goal_node) {
 for(all nodes i) visited[i] = false; // изначально список посещённых узлов пуст
 queue.push(start_node);              // начиная с узла-источника
 visited[start_node] = true;
 while(! queue.empty() ) {            // пока очередь не пуста
  node = queue.pop();                 // извлечь первый элемент в очереди
  if(node == goal_node) {
   return true;                       // проверить, не является ли текущий узел целевым
  }
  foreach(child in expand(node)) {    // все преемники текущего узла, ...
   if(visited[child] == false) {      // ... которые ещё не были посещены ...
    queue.push(child);                // ... добавить в конец очереди...
    visited[child] = true;            // ... и пометить как посещённые
   }
  }
 }
 return false;                        // Целевой узел недостижим
}
'''
'''
def bfs(start_node, goal_node):
    visited = {}
    queue = []
    queue.append(start_node)
    visited[start_node] = True
    while len(queue) != 0:
        node = queue.pop(0)
        if node == goal_node:
            print('Yes')
            return
        for child in classes[node]:
            if visited[child] == False:
                queue.append(child)
                visited[child] = True
    print('No')
    return
'''