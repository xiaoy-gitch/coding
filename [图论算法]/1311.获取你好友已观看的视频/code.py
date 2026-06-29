class Solution:
    def watchedVideosByFriends(self,watchedVideos: List[List[str]],friends: List[List[int]],id: int,level: int,) -> List[str]:
        n = len(watchedVideos)
        video = defaultdict(list)
        g = [[] for _ in range(n)]
        for i, lst in enumerate(friends):
            for tmp in lst:
                g[i].append(tmp)
        q = deque()
        q.append(id)
        vis = [False] * n
        vis[id] = True
        while q and level:
            level -= 1
            size = len(q)
            for i in range(size):
                tmp = q.popleft()
                for j in g[tmp]:
                    if not vis[j]:
                        q.append(j)
                        vis[j] = True
        cnt = Counter()
        for i in range(len(q)):
            tmp = q.popleft()
            for c in watchedVideos[tmp]:
                cnt[c] += 1
        return sorted(cnt.keys(), key=lambda x: (cnt[x], x))   
