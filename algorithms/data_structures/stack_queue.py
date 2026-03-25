"""
栈和队列数据结构实现
"""


class Stack:
    """
    栈数据结构 (Stack) - LIFO (后进先出)
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """
        入栈操作

        参数:
            item: 要入栈的元素
        """
        self.items.append(item)

    def pop(self):
        """
        出栈操作

        返回:
            item: 栈顶元素

        异常:
            IndexError: 如果栈为空
        """
        if self.is_empty():
            raise IndexError("栈为空")
        return self.items.pop()

    def peek(self):
        """
        查看栈顶元素

        返回:
            item: 栈顶元素

        异常:
            IndexError: 如果栈为空
        """
        if self.is_empty():
            raise IndexError("栈为空")
        return self.items[-1]

    def is_empty(self):
        """
        检查栈是否为空

        返回:
            bool: True如果栈为空
        """
        return len(self.items) == 0

    def size(self):
        """
        获取栈的大小

        返回:
            int: 栈中元素数量
        """
        return len(self.items)


class Queue:
    """
    队列数据结构 (Queue) - FIFO (先进先出)
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        入队操作

        参数:
            item: 要入队的元素
        """
        self.items.append(item)

    def dequeue(self):
        """
        出队操作

        返回:
            item: 队首元素

        异常:
            IndexError: 如果队列为空
        """
        if self.is_empty():
            raise IndexError("队列为空")
        return self.items.pop(0)

    def peek(self):
        """
        查看队首元素

        返回:
            item: 队首元素

        异常:
            IndexError: 如果队列为空
        """
        if self.is_empty():
            raise IndexError("队列为空")
        return self.items[0]

    def is_empty(self):
        """
        检查队列是否为空

        返回:
            bool: True如果队列为空
        """
        return len(self.items) == 0

    def size(self):
        """
        获取队列的大小

        返回:
            int: 队列中元素数量
        """
        return len(self.items)


class Deque:
    """
    双端队列数据结构 (Deque) - 可以从两端添加或删除元素
    """

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
        添加到前端

        参数:
            item: 要添加的元素
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        添加到后端

        参数:
            item: 要添加的元素
        """
        self.items.append(item)

    def remove_front(self):
        """
        从前端移除

        返回:
            item: 前端元素

        异常:
            IndexError: 如果双端队列为空
        """
        if self.is_empty():
            raise IndexError("双端队列为空")
        return self.items.pop(0)

    def remove_rear(self):
        """
        从后端移除

        返回:
            item: 后端元素

        异常:
            IndexError: 如果双端队列为空
        """
        if self.is_empty():
            raise IndexError("双端队列为空")
        return self.items.pop()

    def peek_front(self):
        """
        查看前端元素

        返回:
            item: 前端元素

        异常:
            IndexError: 如果双端队列为空
        """
        if self.is_empty():
            raise IndexError("双端队列为空")
        return self.items[0]

    def peek_rear(self):
        """
        查看后端元素

        返回:
            item: 后端元素

        异常:
            IndexError: 如果双端队列为空
        """
        if self.is_empty():
            raise IndexError("双端队列为空")
        return self.items[-1]

    def is_empty(self):
        """
        检查双端队列是否为空

        返回:
            bool: True如果双端队列为空
        """
        return len(self.items) == 0

    def size(self):
        """
        获取双端队列的大小

        返回:
            int: 双端队列中元素数量
        """
        return len(self.items)


if __name__ == "__main__":
    # 测试栈
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"栈顶元素: {stack.peek()}")
    print(f"出栈: {stack.pop()}")
    print(f"栈大小: {stack.size()}")

    # 测试队列
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"队首元素: {queue.peek()}")
    print(f"出队: {queue.dequeue()}")
    print(f"队列大小: {queue.size()}")

    # 测试双端队列
    deque = Deque()
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(0)
    print(f"前端元素: {deque.peek_front()}")
    print(f"后端元素: {deque.peek_rear()}")
    print(f"从前端移除: {deque.remove_front()}")
    print(f"从后端移除: {deque.remove_rear()}")
    print(f"双端队列大小: {deque.size()}")
