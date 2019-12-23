[TOC]

# Graph

> 文件顺序：graph.py -> bfs_dfs_graph.py
>
> graph.py是对无向图、有向图的结构实现。
>
>bfs_dfs_graph.py是基于结构之后的搜索算法：breadth first search, depth first search.

## 1. 如何找出社交网络中的三度好友关系 
> 六度分割理论：平均只需要六步就可以联系到任何两个互不认识的人。

用户的一度好友就是用户的好友，二度就是用户好友的好友，以此类推。

## 2. 基于图的搜索算法
> 算法是作用于具体的数据结构上的；图的表达能力很强，大多数搜索场景都可以抽象为图；图的搜索算法有广度优先搜索、深度优先搜索、A*、IDA*，前两个比较简单暴力。

图有无向图、有向图、带权图。图的存储方式有邻接表、邻接矩阵。以下如无特殊说明，默认为针对邻接表存储的无向图。
### 2.1 Breadth-first search
> 代码实现见`bfs_dfs_graph.py`

The path found using Breadth-first search is shortest. In the code, it's important to understand three variables: 

|variable|effect|
| :----: | :----: |
| visited | It is used to record the vertices that have been traversed to avoid repeated visits. If vertex q has been visited, the corresponding visited[q] should be set to True. |
| queue | Queue is always used in Breadth-first search. It is used to store the vertices that have been visited but its neighbours not.|
| prev | It is used to record the search path. e.g. prev[w] store the previous vertex of vertex w.|

性能分析：

* 时间复杂度：最坏情况下，需要遍历全部顶点，每条边也需要访问一遍，所以时间复杂度为：$$ O(E+V) $$，由于总边数一定大于等于总顶点数，所以时间复杂度为：$$O(E)$$。
* 空间复杂度：考虑 visited、queue、prev 三个临时变量内存储所占空间，由于三个变量存储的都是顶点，且顶点数不会超过总顶点数，因此空间复杂度为：$$O(V)$$。

### 2.2 Depth-first search
> Code implementation is in `bfs_dfs_graph.py`

图的深度优先遍历类似于走迷宫，入口为顶点s，出口为顶点t，路遇岔路则随便选择一条路，无法走出便折回重走。

典型的回溯思想，多用递归技巧编写代码，得到的路径并不是最短的。

代码中，有三个变量需要重点理解：

|variable|effect|
| :----: | :----: |
| visited | It is used to record the vertices that have been traversed to avoid repeated visits. If vertex q has been visited, the corresponding visited[q] should be set to True. |
| found | Flag whether exit has been found.|
| prev | It is used to record the search path. e.g. prev[w] store the previous vertex of vertex w.|

 性能分析：

* 时间复杂度：每条边最多被访问两次，一次访问、一次回退，所以时间复杂度为 $$O(E)$$。
* 空间复杂度：同广度优先搜索类似，为 $$O(V)$$ 。

### 2.3 Summary

DFS和BFS是暴力搜索算法，并没有经过优化，只适合于数据规模小的场景