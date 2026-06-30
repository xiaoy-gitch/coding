class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 用多个状态来标记各个节点，0表示未遍历过，1表示该点在环里或者递归中处于被遍历过（不安全），2表示该点是安全的
        n = len(graph)
        state = [0] * n

        def safe_judge(node):
            # 如果该点被遍历过，那么返回该点是否安全
            if state[node]>0:
                return state[node]==2
            # 先标记该点被遍历过
            state[node] = 1
            # dfs遍历下去，如果该点在环上，则一定会遍历回来，这时候遇到该点state为1，则说明该点不安全，会返回False
            # 只要遇到一条dfs路径有问题，根据题意，都需要返回False来表示该点不安全
            for n in graph[node]:
                if not safe_judge(n):
                    return False
            # 如果dfs遍历下去均未遍历回来，则说明该点不在环里，属于安全结点，修改状态并返回True
            state[node] = 2
            return True

        # 依次以每一个结点为出发进行遍历，由于有state数组记录状态，复杂度会低很多
        return [i for i in range(n) if safe_judge(i)]
