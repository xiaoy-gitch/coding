class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        left_rem, right_rem = 0, 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        ans = set()
        path = []
        
        def dfs(i, l, r, o):
            if i >= n:
                if o == 0:
                    ans.add(''.join(path.copy()))
                return

            if s[i] == '(':
                if l > 0:
                    dfs(i + 1, l - 1, r, o)
                path.append(s[i])
                dfs(i + 1, l, r, o + 1)
                path.pop()

            elif s[i] == ')':
                if r > 0:
                    dfs(i + 1, l, r - 1, o)
                if o > 0 :
                    path.append(s[i])
                    dfs(i + 1, l, r, o - 1)
                    path.pop()

            else:
                path.append(s[i])
                dfs(i + 1, l, r, o)
                path.pop()

        dfs(0, left_rem, right_rem, 0)
        return list(ans)

        
