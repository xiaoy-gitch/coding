class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        st =[]
        cnt =Counter(s)
        for c in s:
            while st and st[-1]>c and cnt[st[-1]]>1:
                c1 = st.pop()
                cnt[c1] -=1
            st.append(c)
        # 最后，移除末尾的重复字母，可以让字典序更小
        while cnt[st[-1]]>1:
            cnt[st.pop()] -=1
            
        return ''.join(st)
