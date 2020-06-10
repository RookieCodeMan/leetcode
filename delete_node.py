# title: 在O（1）时间内，删除链表的节点
# 给定单项链表的头指针和一个节点指针，在O（1）时间内删除该节点

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# 正常思路从头开始遍历，时间复杂为0(n)

def delete_node(p_list_head, delete_node):
    cur_node = p_list_head
    if cur_node == delete_node:
        return cur_node.next
    while cur_node.next is not None:
        if cur_node.next == delete_node:
            cur_node.next = delete_node.next
        cur_node = cur_node.next
    return p_list_head


if __name__ == '__main__':
    node1 = Node(5)
    node2 = Node(5)
    print(node1 == node2)
