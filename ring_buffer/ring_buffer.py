from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        # if full
        if self.storage.length == self.capacity:
            # set value of oldest to item
            self.current.value = item
            # if oldest is tail
            if self.current is self.storage.tail:
                # set to head
                self.current = self.storage.head
            else:
                #Otherwise set it to next
                self.current = self.current.next
        # otherwise if not full
        elif self.storage.length < self.capacity:
            # add item to tail
            self.storage.add_to_tail(item)
            #set oldest to head
            self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cur = self.storage.head
        while(cur):
            list_buffer_contents.append(cur.value)
            cur = cur.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
