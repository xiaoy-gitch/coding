class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st =[]
        cnt =Counter(s)
        for c in s:
            if c not in st:
                while st and st[-1]>c and cnt[st[-1]]>0:
                    st.pop()
                st.append(c)
            cnt[c] -=1
        return ''.join(st)
