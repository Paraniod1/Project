# -*- codeing = utf-8 -*-
# @Time : 2021/8/7 14:20
# @Author : chao
# @File : Link.py
# @Software : PyCharm

# python 实现链表的基本操作

# 结点对象
class Node:
    def __init__(self, item):
        self.item = item  # 该结点的值
        self.next = None  # 链接下一个结点

# 链条对象
class SinglyLinkedList():
    ''''链表对象'''
    def __init__(self):
        self.__head = None

    def add(self, item):
        '''
        头部添加结点
        :param item:
        :return:
        '''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''
        尾部添加结点
        :param item:
        :return:
        '''
        cur = self.__head
        if not cur:              # 判断是否为空链表
            self.add(item)
        else:
            node = Node(item)
            while cur.next:
                cur = cur.next
            cur.next = node

    @property
    def is_empty(self):
        '''
        判断链表是否为空表，只看头部是否有结点
        :return:
        '''
        if self.__head:
            return False
        else:
            return True

    @property
    def length(self):
        '''
        获取链表的长度
        :return:
        '''
        cur = self.__head
        n = 0
        if not cur:
            return n
        else:
            while cur.next:
                cur = cur.next
                n += 1
            return n+1

    def ergodic(self):
        '''
        遍历链表
        :return:
        '''
        cur = self.__head
        if not cur:
            print('None')
        else:
            while cur.next:
                print(cur.item)
                cur = cur.next
            print(cur.item)

    def insert(self, index, item):
        '''
        在指定位置插入结点（设置索引从0开始）
        :param index:
        :param item:
        :return:
        '''
        if index == 0:               # 当索引为0从头部插入
            self.add(item)
        elif index >= self.length:   # 当索引超出范围则尾部插入
            self.append(item)
        else:                        # 找到插入位置的上一个结点，修改上一个结点的next属性
            cur = self.__head
            n = 1
            while cur.next:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def deltel(self, item):
        '''
        删除结点
        :param item:
        :return:
        '''
        if self.is_empty:   # 结点是否为空 抛出异常
            raise ValueError("null")
        cur = self.__head
        pre = None           # 记录删除结点的上一个结点
        if cur.item == item: # 当删除结点为第一个
            self.__head = cur.next
            while cur.next:
                pre = cur
                cur = cur.next
                if cur.item == item:
                    pre.next = cur.next

    def search(self, item):
        '''
        查找结点是否存在
        :param item:
        :return:
        '''
        cur = self.__head
        while None != cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':

    node = Node
    linklist = SinglyLinkedList()
    linklist.append(6)
    linklist.append(89)
    linklist.append(6)
    linklist.append(68)
    linklist.ergodic()



