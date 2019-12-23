

[TOC]

# 递归：如何用三行代码找到”最终推荐人“

**推荐注册返佣金**这个功能是很多 `APP` 上都有的，`A` 推荐 `B`，`B` 推荐 `C`，则 `B` 和`C` 的**最终推荐人**都是 `A`，现如果随便给出一个用户，要查找出这个用户的**最终推荐人**，则可以使用递归。

递归是一种应用非常广泛的算法（或说是编程思想）。很多种数据结构和算法的代码实现，都能用到，比如 `DFS（深度优先搜索）`。

递归的理解：先 **递推**，后 **回归**

## 一、适合用递归的问题

判断一个问题是否能用递归来解决，可以通过思考下面三个条件：

1. 问题能否一个或多个子问题来解决。所谓的子问题是指规模更小的问题
2. 子问题除了数据规模不同，求解的思路同父问题完全一样
3. 存在递归终止条件

如果一个问题同时满足上述三个条件，则可以考虑用递归来求解

## 二、用代码实现递归

### 2.1 思考步骤

1. 递推公式**（最主要、也最难的一部分）**
2. 递推终止条件

### 2.2 避免思维误区

对递归问题的思考，人的思维习惯是**将递归问题平铺展开，循环递推，然后再层层返回，试图搞清楚递归的全部步骤，这样子百分百会把自己绕进去。**

**正确思考方式：**

判断完一个问题可用递归之后，说明这个问题 A 可以拆分成若干个子问题 B、C、D，假设子问题 B、C、D都是已知的，那 A 与 B、C、D 存在着什么关系，用式子表示出来，则得到**递推公式**，然后再思考**递推终止条件**即可。

## 三、递归存在的问题

虽然递归的代码简洁、思路清晰、可读性很强，但是**递归有利有弊**。递归在实际应用中，会遇到很多问题，常见的问题有**堆栈溢出**、**重复计算**、**过多的函数调用导致耗时较多**等等。

### 3.1 堆栈溢出

我们知道，程序在调用函数时，会将主程序的信息以临时变量的形式封装成栈帧压入内存栈，当函数执行完，再出栈。而系统栈或虚拟机栈的空间一般都不大，所以如果递归求解的数据规模太大，递推层次太深，一直入栈，则可能导致堆栈溢出。

#### 那么，该如何避免堆栈溢出？

* 限制递推最大深度。定义一个全局变量`maxDepth`，每次递推调用函数都使`maxDepth += 1`，当该`maxDepth`达到某个值后，则直接返回报错。

  但是这种做法并无法很好地解决堆栈溢出问题，原因在于`maxDepth`最大值的设置与当前线程剩余的栈空间有关，需要实时计算，过于复杂，影响代码可读性。所以这种方法只有在当`maxDepth`设定值较小时才比较实用，例如 `maxDepth <= 10` 或 `maxDepth <= 50` 等等。

* 采用迭代循环的非递归写法。手动模拟系统栈，存放子问题结果。

### 3.2 重复计算

递归求解过程中，会衍生出很多子问题的求解，这些子问题中，会出现重复的现象，也就会导致同一子问题的重复计算，浪费计算资源。

#### 那么，如何避免重复计算？

* 散列表（哈希表）记录已计算过的子问题结果。

  每次递归计算前，先判断该子问题是否被记录在散列表中，如果存在，则直接取出表中结果，加以利用。如果不存在，则将该子问题计算出来，然后记录到散列表中。

### 3.3 过多的函数调用导致耗时更多

递归采用多层次的函数调用，这样的调用过程会导致程序更多的开销。

#### 避免过多的函数调用

* 代码采用**迭代循环**的**非递归写法**。

#### 是否所有的递归问题，都可以采用`迭代循环的非递归写法`？

笼统地讲，是的。**递归本身是借助栈来实现，只不过我们使用的栈是系统栈或者虚拟机栈**，我们没有感知到。所以我们也可以**在自己的内存堆上实现栈，手动模拟入栈、出栈过程，这样任何递归代码都可以改写成看上去不是递归代码的样子**。这种思路本质是将递归改为了**手动**递归，递归本质并没有变，而且也并没有解决递归可能存在的其他问题，只是解决了`过多的函数调用`这个问题。

## 四、拓展&经验

### 4.1 IDE对递归代码的调试

假设条件，当前递归代码的数据规模很大，递推层次很深。

1. 打印日志发现递归值
2. 结合条件断点进行调试

### 4.2 对环的检测

假设环上元素不重复，则定义一个散列表，遍历每个元素，判断元素是否在散列表中，如果不存在，则将元素放入散列表，如果存在，则说明是环。

**元素重复呢？**