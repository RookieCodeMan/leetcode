# title：输入链表的头结点，反转该链表并输出反转后，链表的头结点

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reversed_linked_list(p_head):
    # 首先定义一个反转后链表的头，reversed_list_head
    reversed_list_head = None
    p_node = p_head  # 当前节点
    p_pre_node = None  # 前个节点
    p_next_node = None  # 后个节点
    while p_node is not None:
        if p_node.next is None:  # 不可放到循环外，因为这样的话，就p_node==None了。
            reversed_list_head = p_node
        p_next_node = p_node.next  # 取出后一个节点的信息，
        p_node.next = p_pre_node
        p_head = p_next_node
        p_pre_node = p_head
    return reversed_list_head
