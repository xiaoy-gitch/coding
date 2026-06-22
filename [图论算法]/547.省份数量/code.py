class Solution:
    #考察：连通图的数量
    #使用并查集
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(isConnected)):  
            uf.add(i)  #矩阵的行和列表示有哪些结点
            for j in range(i): #无向图遍历一半即可
                if isConnected[i][j]:
                    uf.merge(i,j)
        return uf.num_of_sets
class UnionFind:
    def __init__(self):
        self.father={}  #字典
        self.num_of_sets =0# 额外记录集合的数量
    def find(self,x):
        root =x
        while self.father[root]!=None:  #一直向上遍历
            root = self.father[root]
        while x != root:   #缩短路径  
            original_father = self.father[x]
            self.father[x] = root
            x = original_father  #可以看作最后一个元素更换了
        return root
    def merge(self,x,y):  #合并相当于联通
        root_x,root_y = self.find(x),self.find(y) #找到各自的祖先结点
        if root_x != root_y:  #说明二者不连通
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1
    def add(self,x):
        if x not in self.father:
            self.father[x]=None
            self.num_of_sets +=1



            
