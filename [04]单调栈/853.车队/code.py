class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #只要能追上前车，两车才会相遇，才会组成一个车队
        #能否追上前车，可以通过判断两车到达目的地所用的时间，如果后面的车所需的时间小于等于
        #前车，说明能够追上前车，两车是一个车队的。
        #1.按照位置进行降序排序，优先计算靠前的车
        dist =sorted(zip(position,speed),reverse =True)  #位置相同，按照速度排序
        #2.计算每个车到达目的地的时间与前车队的时间作比较
        stack =[]  #用来存放每个车队的时间
        for pos,s in dist:
            time = (target-pos)/s
            # 如果当前车的到达时间 > 最后一个车队的到达时间，说明追不上，形成新车队
            if not stack or time >stack[-1]:
                stack.append(time)
        return len(stack)
