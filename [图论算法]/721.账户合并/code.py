class Solution:
    # 如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人，姓名一定是相同的
    #1.首先同一列表中的邮箱是连通的
    #2.其次有公共邮箱的两个列表中邮箱是连通的
    #3.最后将连通的邮箱进行排序+姓名，输出
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #1.通过哈希(字典)
        email_dict=defaultdict(list)
        for i,account in enumerate(accounts):
            for email in account[1:]:
                email_dict[email].append(i)
        vit=[False]*len(accounts)
        def dfs(x:int):
            vit[x] =True
            for email in accounts[x][1:]:
                if email in email_set:
                    continue
                email_set.add(email)
                for y in email_dict[email]:# 遍历所有包含该邮箱地址的账户下标 j
                    if not vit[y]:
                        dfs(y)
        ans =[]
        for i in range(len(accounts)):
            if not vit[i]:
                email_set=set()# 用于收集该连通分量中访问到的邮箱地址
                dfs(i)
                ans.append([accounts[i][0]]+sorted(email_set)) #sorted(email_set)集合转成排序后的列表
        return ans      
