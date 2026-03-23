"""
链表数据结构 (Linked List)
包括单向链表和双向链表的实现
"""

class Node:
    """
    链表节点类
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    单向链表实现
    """
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """
        添加节点到链表尾部
        
        参数:
            data: 节点的数据
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    
    def prepend(self, data):
        """
        添加节点到链表头部
        
        参数:
            data: 节点的数据
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """
        删除指定数据的节点
        
        参数:
            data: 要删除的数据
        
        返回:
            bool: 是否成功删除
        """
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """
        搜索指定数据的节点
        
        参数:
            data: 要搜索的数据
        
        返回:
            Node or None: 找到的节点或None
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def display(self):
        """
        显示链表所有节点
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) if nodes else "空链表"


class DoublyNode:
    """
    双向链表节点类
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    双向链表实现
    """
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """
        添加节点到链表尾部
        
        参数:
            data: 节点的数据
        """
        new_node = DoublyNode(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def prepend(self, data):
        """
        添加节点到链表头部
        
        参数:
            data: 节点的数据
        """
        new_node = DoublyNode(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def display_forward(self):
        """
        正向显示链表
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) if nodes else "空链表"
    
    def display_backward(self):
        """
        反向显示链表
        """
        nodes = []
        current = self.tail
        while current:
            nodes.append(str(current.data))
            current = current.prev
        return " <- ".join(nodes) if nodes else "空链表"


if __name__ == "__main__":
    # 测试单向链表
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print("单向链表:", ll.display())
    
    # 搜索节点
    node = ll.search(2)
    print(f"搜索 2: {node.data if node else '未找到'}")
    
    # 删除节点
    ll.delete(2)
    print("删除 2 后:", ll.display())
    
    # 测试双向链表
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print("双向链表正向:", dll.display_forward())
    print("双向链表反向:", dll.display_backward())