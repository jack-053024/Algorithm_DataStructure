[TOC]

# Basic theory of Graph

> 图可以用来存储例如微信、微博等社交网络`APP`的好友关系，e.g. 互加好友、关注，etc..
>
> 涉及图的算法很多，也很复杂，e.g. 图的搜索、最短路径、最小生成树、二分图，etc..

## 1. 什么是图？

当前我知道的非线性结构有树，而图是另一个比树还要复杂的非线性结构。

图有三种，e.g. 无向图、有向图、带权图

### 1.1 无向图

![img](assets/df85dc345a9726cab0338e68982fd1af.jpg)

树中的元素叫节点，图中的元素我们叫**顶点`vertex`**，一个顶点可与其他任意顶点建立联系，建立起来的联系称为**边`edge`**。无向图的典型应用在**互加好友**

e.g. 微信系统的好友关系网，一个顶点相当于一个用户，建立联系相当互加好友形成`edge`，一个顶点与多少条`edge`连接，就有多少个好友，也叫该顶点的**度`degree`**

### 1.2 有向图

![img](assets/c31759a37d8a8719841f347bd479b796.jpg)

有向图的典型应用在关注，`A` 指向 `B`，意味着 `A` 关注 `B`，相互指向即为相互关注。

在有向图中，顶点的度`degree`还分为**入度`In-degree`**和**出度`Out-degree`**。入度为箭头由外向内，出度为箭头由内向外。以 `A` 为例，`A` 的度为 3，入度为 1，出度为 2。入度表示多少人关注，出度表示关注了多少人。

### 1.3 带权图`Weighted graph`

![img](assets/55d7e4806dc47950ae098d959b03ace8.jpg)

典型应用在于表示好友之间的亲密度，e.g. `QQ`好友亲密度。带权图其实就是在无向图的基础上，给`edge`加上一个权重`weight`

## 2. 图在内存中是如何存储的

> 图作为一种高级且复杂的数据结构，**其存储是基于数组和链表的**。
>
> 图有两种存储方式：**邻接矩阵`Adjacent Matrix`和邻接表`Adjacent List`**

### 2.1 邻接矩阵`Adjacency Matrix`

邻接矩阵底层依赖二维数组，把所有顶点作为二维数组横纵轴的下标。

对于无向图，如果顶点 `i` 和顶点 `j` 有联系，则将 $$A[i][j]$$ 和 $$A[j][i]$$ 均标记为 1。

对于有向图，如果顶点 `i` 指向顶点 `j`，则将 $$A[i][j]$$ 标为 1，如果顶点 `j` 指向顶点 `i`，则将 $$A[j][i]$$ 标为 1。 

对于带权图，在无向图的基础上，不再标记 1，而是标记为所带权重值

![img](assets/625e7493b5470e774b5aa91fb4fdb9d2.jpg)

虽然使用邻接矩阵来存储图很简单直观，同时在获取两顶点关系时非常高效，也可以将对图的运算转换成对矩阵的运算，方便计算。但邻接矩阵非常浪费内存空间：

e.g. 对于无向图，当 $$A[i][j]==1$$ 时，$$A[j][i]==1$$ 必然成立，所以只需要存储一个即可，即不需要二维矩阵，只需要一个三角矩阵。

e.g. 微信用户有好几亿，但每个用户的好友只有几百，此时相对而言，该图只是**稀疏图`Sparse Matrix`**，如果用邻接矩阵存储，二维数组中的很多空间都会浪费。

### 2.2 邻接表`Adjacency List`

![img](assets/039bc254b97bd11670cdc4bf2a8e1394.jpg)

邻接表，先将图的元素用数组存储起来，然后对每个顶点拉一条链表，将与其有联系的顶点放入链表中。如上图所示，不过上图是以有向图为例，无向图也差不多

邻接表虽然节省空间，但是对于获取两顶点关系、用其来对图的计算并不那么友好。获取两顶点关系时，需要先在数组中找到顶点 `A`，然后再从顶点 `A` 拉出的链表中查找顶点 `B` 是否存在，如果存在，则有联系。因此，如果链表太长，则效率会很低。

但是，参考散列表使用链表法`Chaining`解决散列冲突时对链表的改造，我们同样可以对邻接表中的链表进行改造，使其查找的时间复杂度降低，e.g. 将链表改造为跳表、红黑树、有序动态数组、散列表，etc..

## 思考题

> 如何存储微博、微信等社交网络中的好友关系？提出具体的解决方案

微博是关注，微信是好友关系，前者用有向图，后者用无向图，两者方案相似，这里以微博为例

1. 初步判断用有向图存储

2. 思考需要支持哪一些操作，数据结构是为算法服务的，只是为了更高效。假设需要支持一下操作：

   * 判断 `A` 是否关注了 `B`
   * 判断 `B` 是否有粉丝 `A`
   * `A` 关注 `B`
   * `A` 取消关注 `B`
   * 根据用户首字母排序，分页获取 `A` 的粉丝列表
   * 根据用户首字母排序，分页获取 `A` 的关注列表

3. 由操作和常识可基本判定关系图为稀疏图，用邻接矩阵太过浪费空间，因此用邻接表来储存

4. 为了提高查找效率，对邻接表的链表进行改造，从跳表、红黑树、有序动态数组和散列表等中选择，由于操作需要分页，因此跳表更为合适。

5. 如果使用邻接表来存储，分页获取 `A` 的关注列表容易，但是分页获取 `A` 的粉丝列表却很难。因此可以用两张表，一张邻接表、一张逆邻接表，前者方便获取 `A`的关注列表，后者方便获取 `A` 的粉丝列表。

   ![img](assets/501440bcffdcf4e6f9a5ca1117e990a1.jpg)

6. 最后需要注意的是，如果用户量很少，两张表可直接放在内存中，但是如果用户量太大，则没有办法这样做。解决方法是利用哈希算法分片到多个计算机，或者用外部存储设备 + 数据库存储，给数据库字段构建索引。

---

---

#Applications of Graph

> Code files：`Graph/graph.py` --> `Graph/bfs_dfs_graph.py` --> `Graph/find_vertices_by_degree.py`
>
> `graph.py`是对无向图、有向图的结构实现。
>
> `bfs_dfs_graph.py`是基于结构之后的搜索算法：breadth first search, depth first search.
>
> `Graph/find_vertices_by_degree.py`是查找多度好友关系，给定图、起始顶点、度数即可。

## 1. 如何找出社交网络中的三度好友关系 

> 六度分割理论：平均只需要六步就可以联系到任何两个互不认识的人。
>
> Code is  implemented in Graph/find_vertices_by_degree.py

用户的一度好友就是用户的好友，二度就是用户好友的好友，以此类推。

## 2. 基于图的搜索算法

> 算法是作用于具体的数据结构上的；图的表达能力很强，大多数搜索场景都可以抽象为图；图的搜索算法有广度优先搜索、深度优先搜索、`A*`、`IDA*`，前两个比较简单暴力。

图有无向图、有向图、带权图。图的存储方式有邻接表、邻接矩阵。以下如无特殊说明，默认为针对邻接表存储的无向图。

### 2.1 Breadth-first search

> Code implementation is in `Graph/bfs_dfs_graph.py`

The path found using Breadth-first search is **shortest.** 

In the code, it's important to understand three variables: 

| variable |                            effect                            |
| :------: | :----------------------------------------------------------: |
| visited  | It is used to record the vertices that have been traversed to avoid repeated visits. If vertex q has been visited, the corresponding visited[q] should be set to True. |
|  queue   | Queue is always used in Breadth-first search. It is used to store the vertices that have been visited but its neighbours not. |
|   prev   | It is used to record the search path. e.g. prev[w] store the previous vertex of vertex w. |

性能分析：

* 时间复杂度：最坏情况下，需要遍历全部顶点，每条边也需要访问一遍，所以时间复杂度为：$$ O(E+V) $$，由于总边数一定大于等于总顶点数，所以时间复杂度为：$$O(E)$$。
* 空间复杂度：考虑 visited、queue、prev 三个临时变量内存储所占空间，由于三个变量存储的都是顶点，且顶点数不会超过总顶点数，因此空间复杂度为：$$O(V)$$。

### 2.2 Depth-first search

> Code implementation is in `bfs_dfs_graph.py`

图的深度优先遍历类似于走迷宫，入口为顶点s，出口为顶点t，路遇岔路则随便选择一条路，无法走出便折回重走。

典型的回溯思想，多用递归技巧编写代码，得到的路径并不是最短的。

代码中，有三个变量需要重点理解：

| variable |                            effect                            |
| :------: | :----------------------------------------------------------: |
| visited  | It is used to record the vertices that have been traversed to avoid repeated visits. If vertex q has been visited, the corresponding visited[q] should be set to True. |
|  found   |              Flag whether exit has been found.               |
|   prev   | It is used to record the search path. e.g. prev[w] store the previous vertex of vertex w. |

 性能分析：

* 时间复杂度：每条边最多被访问两次，一次访问、一次回退，所以时间复杂度为 $$O(E)$$。
* 空间复杂度：同广度优先搜索类似，为 $$O(V)$$ 。

### 2.3 Summary

`DFS`和`BFS`是暴力搜索算法，并没有经过优化，只适合于数据规模小的场景