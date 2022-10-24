

class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next

    def setValue(self, new_value):
        self.value = new_value

    def __str__(self):
        return "Node("+str(self.value)+")"

    def clear(self):
        self.value = None
        self.next = None

class LinkedList:

    def __init__(self, data = []):
        self.head, self.tail, self.len = None, None, 0
        for e in data:
            self.append(e)

    def __len__(self):
        return self.len

    def getHead(self):
        return self.head

    def setHead(self, new_head):
        if isinstance(new_head, Node) or new_head is None:
            self.head = new_head

    def getTail(self):
        return self.tail

    def setTail(self, new_tail):
        if isinstance(new_tail, Node) or new_tail is None:
            self.tail = new_tail
        self.tail.setNext(None)

    def isEmpty(self):
        return self.head is None and self.tail is None

    def append(self, e):
        new_node = Node(e)
        if self.isEmpty():
            self.setHead(new_node)
            self.setTail(new_node)
        else:
            #Encontrar el último nodo
            last = self.getTail()
            last.setNext(new_node)
            self.setTail(new_node)
        self.len+=1

    def search(self, e):
        current = self.getHead()
        while current is not None and current.getValue() != e:
            current = current.getNext()
        return current

    def update(self, old_value, new_value):
        node_to_update = self.search(old_value)
        if node_to_update is None:
            raise Exception("Value not found on sequence")
        node_to_update.setValue(new_value)

    def slice(self, value_start, n=1):
        node_tost = self.search(value_start)
        if node_tost is None:
            raise Exception("Value not found on sequence")
        result, elements = LinkedList(), 0
        while node_tost is not None and elements < n:
            result.append(node_tost.getValue())
            node_tost = node_tost.getNext()
            elements+=1
        return result

    def merge(self, list_b):
        if not isinstance(list_b, LinkedList):
            raise Exception("Incompatible types")
        if self.isEmpty():
            self.setHead(list_b.getHead())
            self.setTail(list_b.getTail())
        elif not list_b.isEmpty():
            self.tail.setNext(list_b.getHead())
            self.setTail(list_b.getTail())
        self.len = len(self) + len(list_b)

    def delete(self, e):
        if self.isEmpty():
            raise Exception("List is empty")
        node_to_del = self.search(e)
        if node_to_del is None:
            raise Exception("Value is not in List")
        if len(self) == 1:
            self.head, self.tail = None, None
        else:
            if node_to_del == self.head:
                self.setHead(node_to_del.getNext())
            else:
                prev = self.getHead()
                while prev.getNext() != node_to_del:
                    prev = prev.getNext()
                if node_to_del == self.tail:
                    self.setTail(prev)
                else:
                    prev.setNext(node_to_del.getNext())
        node_to_del.clear()
        self.len -= 1

    def reverse(self):
            anterior = None
            actual = self.head
            siguiente = None 
            while actual != None:
                siguiente = actual.getNext()
                actual.setNext(anterior)
                anterior = actual
                actual = siguiente
            self.head = anterior

    def __str__(self):
        arr = []
        current = self.head
        while current is not None:
            arr.append(current.getValue())
            current = current.getNext()
        return "LinkedList("+str(arr)+")"

def main():
    lista = LinkedList([i for i in range(100)])
    print(len(lista))
    print(lista.search(99))
    slc = lista.slice(80,5)
    hd = slc.getHead()
    while hd is not None:
        print(hd.getValue())
        hd = hd.getNext()
    la = LinkedList([i for i in range(100000)])
    lb = LinkedList([i for i in range(100000, 200000)])
    la.merge(lb)
    print(len(la))

    lt = LinkedList([3,4,5,6,7])
    lt.delete(5)
    print(lt)
    lt2 = LinkedList([3])
    lt2.delete(3)
    print(lt2)

main()