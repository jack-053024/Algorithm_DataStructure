[TOC]

# 排序优化：如何实现一个通用的、高性能的排序函数？

## 一、问题分析

首先我们需要先选择一种排序算法，这个算法要尽可能的综合最优。线性排序的时间复杂度虽然低，但是其应用场景比较特殊，为了通用，所以我们不能选择线性排序。

如果是对于数据规模小的，我们可以使用时间复杂度为`O(n^2)`，但对于数据规模比较大的，使用时间复杂度为`O(nlogn)`的算法会更高效一些。而一般我们会选择时间**快速排序**或**堆排序**。不选用归并排序是因为它不是原地排序，对于数据规模大的，它会占用很多的额外的内存空间。另外可以记住的是，`java`用的是**堆排序**，`C`用的是**快排**

下面以**快速排序**为例。

但是如果只是单纯地使用快速排序，并不够通用和高效，所以接下来主要说的是如何去**优化**。

## 二、优化快速排序

我们知道**快排的关键点在于分区点的选择**，日常我们简单写一个快排代码时，都会将数据的**第一个元素或者最后一个元素**当做分区点，如果每次取分区点时，都刚好把数据均匀平分两边，那快排就达到最好时间复杂度，为`O(nlogn)`。但是当数据接近有序或者逆序，每次选择**第一个元素**或者**最后一个元素**作为分区点，都只会把数据分在一边，这时快排的时间复杂度就会退化到`O(n^2)`，即最坏时间复杂度。

因此，对于快排的优化，主要就是让分区点的选择尽可能地好，即**被分区点分开的两边，数据尽可能一样多。**

下面介绍两种比较常用、简单的分区算法

### 2.1 三数取中法

从数组中的首、中、尾分别取出一个数，然后比较这三个数的大小，取中间值作为分区点。例如取出来的值分别为`1，50，100`，则取`50`作为分区点。需要注意的是，如果数组太大，可以**五数取中**，甚至**九数取中**。

### 2.2 随机法

随机从数据中取出一个数，而不是固定取**第一个元素**或者**最后一个元素**。根据概率知识，这样子快排退化到`O(n^2)`的可能性很低。

## 三、分析`C`中的`qsort`排序函数

`qsort`通过名字，我们可以知道它是用快排来实现的，但是实际上，`qsort`用了多种排序算法，它是**分数据情况来决定使用哪种排序算法的**。主要有**归并排序、快排、插入排序**。

`qsort`优先使用**归并排序**，因为归并排序的时间复杂度稳定在`O(nlogn)`，虽然它不是原地排序，但是对于规模小的数据，可以用少量的空间来换取时间。

当数据规模变大时，`qsort`则会改用快排，值得注意的有三点：

* 快排分区点的选择用的是**三数取中法（可看源码）**
* `qsort`对于快排采用的是非递归的写法，自己手动模拟堆栈，防止递归时**堆栈溢出**。
* **当快排分区至区间内元素数量小于等于`4`的时候，会使用插入排序对区间进行排序。**

