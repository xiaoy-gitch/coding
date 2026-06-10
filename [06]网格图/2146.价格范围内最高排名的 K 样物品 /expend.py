q.sort(key=lambda p:(grid[p[0]][p[1]],p))：
首先按 grid[p[0]][p[1]]（网格中的值）升序排序
如果值相同，则按坐标 p 升序排序（先比行，再比列）
            
ans.extend(p for p in q if l <= grid[p[0]][p[1]] <= h)：
entend()和append()的区别：
append 不会自动解包或迭代，它直接把传入的参数作为一个整体添加到列表中。
entend 会自动解包或迭代
这里 (p for p in q if condition) 是一个生成器表达式，它的语法本身就创建了一个生成器对象。往下看！

# 使用 extend（正确）
ans.extend(p for p in q if condition)
# 结果: ans = [(x0, y0)] 或 ans = []

# 使用 append（错误）
ans.append(p for p in q if condition)
# 结果: ans = [<generator object>]  # 添加的是生成器对象
