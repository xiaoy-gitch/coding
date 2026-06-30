class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj =defaultdict(list)
        recipe ={}
        for i,j in zip(recipes,ingredients):
            for k in j:
                adj[k].append(i)
            recipe[i] =len(j)
        ans =[]
        q = deque(supplies)
        while q:
            for i in adj[q.popleft()]:
                recipe[i] -=1
                if recipe[i]==0:
                    q.append(i)
                    ans.append(i)
        return ans 
