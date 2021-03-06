[TOC]

**注意：**下面的应用最好自己用代码实现一下：

1. 合并有序小文件
2. 高性能定时器的应用
3. 求 Top K
4. 求中位数
5. 大文件关键字的统计

# The applications of Heap

> 在 `12_heapSorting.md` 中学习了堆和堆排序的一些理论知识、基础操作和实现。但是堆还有一些更典型的应用，例如优先级队列、Top K 问题、求中位数等等。

## 1. 优先级队列

> 普通队列是先进先出，而优先级队列是优先级最高的先出。

一个堆就相当于一个优先级队列，往堆中插入一个元素，就相当于往队列中加入一个元素，只是称谓不同而已。而堆顶元素就是优先级最高的任务，执行时先取出堆顶元素。

### 1.1 优先级队列应用场景

* 赫夫曼编码
* 图的最短路径
* 最小生成树
* Java 的 PriorityQueue
* C++ 的 priority_queue

### 1.2 优先级队列的具体应用实例

#### 1.2.1 合并有序小文件

> 假设我们有 100 个小文件，每个文件的大小是 100MB，每个文件中存储的都是有序的字符串。我们希望将这些 100 个小文件合并成一个有序的大文件。

1. 优先级队列思想
2. 分别从这 100 个小文件中取出一个字符串，构建一个节点数为 100 的小顶堆
3. 将堆顶元素放入创建好的有序大文件中，并从堆中删除
4. 从被删除的堆顶元素的所属小文件中取下一个字符串插入小顶堆中。
5. 直到 100 个小文件中的字符串均被放入大文件中

上述过程的时间复杂度主要来自堆中元素的插入与删除，其时间复杂度为 $$O(logn)$$，n 是指堆的元素，这里是 100

#### 1.2.2 高性能定时器

> 假设我们有一个定时器，定时器中维护了很多定时任务，每个任务都设定了一个要触发执行的时间点。时间点到了，就要执行任务，如下图

![img](assets/b04656d27fd0ba112a38a28c892069e7.jpg)

1. 优先级队列思想
2. 将各任务按照设置的时间点来构建一个小顶堆，堆顶元素为最先要执行的任务
3. 拿堆顶任务设置好的时间点减去当前时间，得到时间 T，即再过 T 时间，堆顶任务就要执行
4. 执行时，取出堆顶元素，有新任务时，往堆中插入元素。

## 2. Top K 问题

> 静态数据，求前 K 大数据，静态数据是指数据不会发生变化。

1. 维护一个具有 k 个元素的小顶堆
2. 从数据中先取出前 K 个数据，构建一个小顶堆。
3. 从第 K+1 个数据开始遍历数据集，与小顶堆堆顶元素比较，如果比堆顶元素大，则用当前元素将堆顶元素覆盖并堆化，如果比堆顶元素小，则不作处理，继续遍历下一个元素。
4. 当数据集中元素遍历完，此时的小顶堆中的元素，就是前 K 大的元素。

遍历数据集的时间复杂度为 $$O(n)$$，最坏情况下，每次遍历的元素都要入堆并堆化，则最坏时间复杂度为 $$O(nlogK)$$。

> 动态数据，求前 K 大数据，也就是实时 Top K。动态数据指数据集会发生变化，这里暂时只考虑元素增加

1. 可以理解为有两个操作，一个是元素添加，另一个是获取 Top K
2. 跟静态数据求 Top K 基本相同，唯一区别在于当元素添加时，就与堆顶元素比较。
3. 当请求 Top K 输出时，就直接返回堆元素即可。

## 3. 求中位数（中值）

> 求一组数据的中位数。中位数，即将数组排序，然后大于前面 50% 的数据的值，就是该组数据的中位数，例如 1, 2, 3, 4, 5,..., 50, 51, ..., 99, 100 的中位数就是 50。这里主要强调 50% 的数据，因为下面要讲的方法适合于求大于数据集中百分之xxxx的数据的值等问题，例如 **接口的 99% 响应时间**。

如果数据集的个数为偶数，则第 $$n // 2$$ 和第 $$ n // 2 + 1$$ 个数据都可以作为中位数，指定第 $$ n//2+1$$ 个数据为中位数，如果数据集的个数为奇数，则只有第 $$n//2+1$$ 个数据是中位数。

如果是静态数据，则直接排序然后返回第 $$ n//2+1$$ 个数据即可，虽然排序相对耗时，但实际很实用。

如果是动态数据，可以理解为两个操作，一个是数据的改变，一个是获得中位数。此时每次获取都需要进行排序，成本就会很高，因此需要另寻他法。

1. 将一开始的数据集进行排序，再将排好序的数据集从中间分为两部分，前部分都小于后部分
2. 将前部分数据构建成大顶堆，后部分数据构建成小顶堆，此时大顶堆的堆顶元素就是中位数
3. 如果新插入数据，则将新数据与大顶堆堆顶元素比较，如果大于堆顶元素，则将新元素插入小顶堆中，如果小于，则插入大顶堆中
4. 插入新元素后，两个堆的元素数量如果不符合 50%，则需要进行调整，根据需求将一个堆中的堆顶元素不断移向另一个堆，直到两个堆的元素数量符合要求。这样子，大顶堆中的堆顶元素就一直都是中位数

当构建好两个堆之后，新元素的插入需要的时间复杂度为 $$O(logn)$$，获取中位数只需要 $$O(1)$$。

## 思考题

> 有一个访问量非常大的新闻网站，我们希望将点击量排名 Top 10 的新闻摘要，滚动显示在网站首页 banner 上，并且每隔 1 小时更新一次。如果你是负责开发这个功能的工程师，你会如何来实现呢？

参考思路：

1. 对每篇新闻摘要计算一个hashcode，并建立摘要与hashcode的关联关系，使用map存储，以hashCode为key，新闻摘要为值
2. 按每小时一个文件的方式记录下被点击的摘要的hashCode
3. 当一个小时结果后，上一个小时的文件被关闭，开始计算上一个小时的点击top10
4. 将hashcode分片到多个文件中，通过对hashCode取模运算，即可将相同的hashCode分片到相同的文件中
5. 针对每个文件取top10的hashCode，使用Map<hashCode,int>的方式，统计出所有的摘要点击次数，然后再使用小顶堆（大小为10）计算top10,
6. 再针对所有分片计算一个总的top10,最后合并的逻辑也是使用小顶堆，计算top10
7. 如果仅展示前一个小时的top10,计算结束
8. 如果需要展示全天，需要与上一次的计算按hashCode进行合并，然后在这合并的数据中取top10
9. 在展示时，将计算得到的top10的hashcode，转化为新闻摘要显示即可