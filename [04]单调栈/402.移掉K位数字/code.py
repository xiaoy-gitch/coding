class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st =[]
        remain =len(num)-k
        for x in num:
            while k and st and st[-1]>x:
                st.pop()
                k -=1
            st.append(x)
        return "".join(st[:remain]).lstrip('0') or '0'
