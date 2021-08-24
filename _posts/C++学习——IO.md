---
layout:     post
title:      C++学习——基础篇(day 6)
subtitle:   C++学习——基础篇(day 6)
date:       2021-08-24
author:     Haihan Gao
header-img: img/post-bg-swift2.jpg
catalog: true
tags:
    - C++
---
# C++学习——IO

## IO类

一般而言，IO对象关联到用户的控制台窗口，当然，我们也可以让IO对象关联到文件(`fstream`)和内存中的string对象(`sstream`)

我们用`>>`表示从文件读入数据，用`<<`表示从文件读出数据，通过重载运算符实现统一接口

* IO对象无拷贝和赋值
* 条件状态——用于处理IO过程中出现的异常，strm是一种IO类型
  * iostate是一种机器相关的类型
  * badbit表示流已崩溃
  * failbit表示一个IO操作失败

一个错误的例子

```cpp
int x;
cin >> x;
// check whether cin is valid
while(cin >> x)
```

如果我们从标准输入设备输入一个字符串，`cin`进入错误状态，这个流将会返回FALSE，我们需要检测输入可能出现的错误、

### 管理条件状态

流对象`rdstate`成员返回iostate值，对应流的当前状态，`setstate`操作将相应的条件为置为某个特定值，`clear`成员是一个重载的函数，不带参数或者接受一个类型为iostate类型的参数

### 管理输入输出缓冲区

每个输出流都有一个在内存中的缓冲区，保存程序读写的数据，由于外设速度较慢，我们需要输入和输出的数据可能保存在缓冲区当中