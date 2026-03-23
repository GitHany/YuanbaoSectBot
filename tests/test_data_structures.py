"""
数据结构单元测试
"""

import unittest
import sys
sys.path.append('/root/.openclaw/workspace/YuanbaoSectBot')

from algorithms.data_structures.linked_list import LinkedList, DoublyLinkedList
from algorithms.data_structures.stack_queue import Stack, Queue, Deque


class TestLinkedList(unittest.TestCase):
    """链表测试类"""
    
    def test_linked_list_append(self):
        """测试链表追加操作"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        self.assertEqual(ll.display(), "1 -> 2 -> 3")
        
        ll.prepend(0)
        self.assertEqual(ll.display(), "0 -> 1 -> 2 -> 3")
    
    def test_linked_list_delete(self):
        """测试链表删除操作"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        result = ll.delete(2)
        self.assertTrue(result)
        self.assertEqual(ll.display(), "1 -> 3")
        
        result = ll.delete(5)  # 删除不存在元素
        self.assertFalse(result)
        self.assertEqual(ll.display(), "1 -> 3")
    
    def test_linked_list_search(self):
        """测试链表搜索操作"""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        
        node = ll.search(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)
        
        node = ll.search(5)  # 搜索不存在元素
        self.assertIsNone(node)
    
    def test_doubly_linked_list(self):
        """测试双向链表"""
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        
        self.assertEqual(dll.display_forward(), "1 -> 2 -> 3")
        
        dll.prepend(0)
        self.assertEqual(dll.display_forward(), "0 -> 1 -> 2 -> 3")
        self.assertEqual(dll.display_backward(), "3 <- 2 <- 1 <- 0")


class TestStack(unittest.TestCase):
    """栈测试类"""
    
    def test_stack_basic_operations(self):
        """测试栈基本操作"""
        stack = Stack()
        
        # 测试入栈
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)
        
        # 测试出栈
        popped = stack.pop()
        self.assertEqual(popped, 3)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 2)
        
        # 测试空栈
        stack.pop()
        stack.pop()
        self.assertEqual(stack.size(), 0)
        self.assertTrue(stack.is_empty())
        
        # 测试空栈异常
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()
    
    def test_stack_edge_cases(self):
        """测试栈边界情况"""
        stack = Stack()
        
        # 空栈操作
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        
        # 大量元素
        for i in range(100):
            stack.push(i)
        
        self.assertEqual(stack.size(), 100)
        self.assertEqual(stack.peek(), 99)


class TestQueue(unittest.TestCase):
    """队列测试类"""
    
    def test_queue_basic_operations(self):
        """测试队列基本操作"""
        queue = Queue()
        
        # 测试入队
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.peek(), 1)
        
        # 测试出队
        dequeued = queue.dequeue()
        self.assertEqual(dequeued, 1)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.peek(), 2)
        
        # 测试空队列
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.size(), 0)
        self.assertTrue(queue.is_empty())
        
        # 测试空队列异常
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()
    
    def test_queue_edge_cases(self):
        """测试队列边界情况"""
        queue = Queue()
        
        # 空队列操作
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        
        # FIFO特性
        queue.enqueue('first')
        queue.enqueue('second')
        queue.enqueue('third')
        
        self.assertEqual(queue.dequeue(), 'first')
        self.assertEqual(queue.dequeue(), 'second')
        self.assertEqual(queue.dequeue(), 'third')


class TestDeque(unittest.TestCase):
    """双端队列测试类"""
    
    def test_deque_basic_operations(self):
        """测试双端队列基本操作"""
        deque = Deque()
        
        # 前端和后端添加
        deque.add_front(1)
        deque.add_rear(2)
        deque.add_front(0)
        
        self.assertEqual(deque.size(), 3)
        self.assertEqual(deque.peek_front(), 0)
        self.assertEqual(deque.peek_rear(), 2)
        
        # 前端和后端移除
        front_removed = deque.remove_front()
        rear_removed = deque.remove_rear()
        
        self.assertEqual(front_removed, 0)
        self.assertEqual(rear_removed, 2)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.peek_front(), 1)
        self.assertEqual(deque.peek_rear(), 1)
    
    def test_deque_edge_cases(self):
        """测试双端队列边界情况"""
        deque = Deque()
        
        # 空队列操作
        self.assertTrue(deque.is_empty())
        self.assertEqual(deque.size(), 0)
        
        # 大量元素
        for i in range(100):
            if i % 2 == 0:
                deque.add_front(i)
            else:
                deque.add_rear(i)
        
        self.assertEqual(deque.size(), 100)
        
        # 空队列异常
        empty_deque = Deque()
        with self.assertRaises(IndexError):
            empty_deque.remove_front()
        with self.assertRaises(IndexError):
            empty_deque.remove_rear()
        with self.assertRaises(IndexError):
            empty_deque.peek_front()
        with self.assertRaises(IndexError):
            empty_deque.peek_rear()


if __name__ == "__main__":
    unittest.main()