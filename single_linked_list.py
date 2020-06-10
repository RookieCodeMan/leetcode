# 实现单项链表的一些常用的api基本功能
# 比如list，is_empty,len,prepend,append,insert,del_first,del_last,del,search,
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.__head = None

    # 判断链表是否为空
    def is_empty(self):
        return not self.__head

    # 往链表中添加节点
    def add(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node  # 设置了链表的头指针
        else:
            cur_node = self.__head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node

    # 遍历整个链表
    def travel(self):
        cur_node = self.__head
        while cur_node is not None:
            print(cur_node.value)
            cur_node = cur_node.next

    # 统计链表的长度
    def len(self):
        if self.__head is None:
            return 0
        cur_node = self.__head
        linked_list_len = 0
        while cur_node is not None:
            linked_list_len += 1
            cur_node = cur_node.next
        return linked_list_len

    def delete_node(self, item):
        # 删除节点
        cur_node = self.__head
        pre = None
        while cur_node is not None:
            # 找到了节点了
            if cur_node.value == item:
                if cur_node == self.__head:
                    # 将头指针下向下一个节点
                    self.__head = cur_node.next
                    return
                else:
                    pre.next = cur_node.next
                    return
            # 没找到节点
            else:
                pre = cur_node
                cur_node = cur_node.next


if __name__ == "__main__":
    link_list = SingleLinkedList()
    print(link_list.is_empty())
    link_list.add(1)
    link_list.add(2)
    link_list.add(8)
    link_list.add(4)
    link_list.add(5)
    link_list.travel()
    print(link_list.len())
    print('----')
    link_list.delete_node(8)
    print(link_list.len())
    link_list.travel()
