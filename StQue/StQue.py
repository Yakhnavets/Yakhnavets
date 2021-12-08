class Stack:

    def __init__(self):
        self.__stack=[]

    def push(self,item):
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack)==0:
            return None
        return self.__stack.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__stack)>0:
            return self.pop()
        else:
            raise StopIteration

    def get_stack(self):
        return self.__elements


class Queue:

    def __init__(self):
        self.__queue=[]

    def add(self,item):
        self.__queue.insert(0,item)

    def pop(self):
        if len(self.__queue)==0:
            return None
        return self.__queue.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__queue)>0:
            return self.pop()
        else:
            raise StopIteration

    def get_queue(self):
        return self.__queue

if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.pop()
    for i in q:
        print(i)

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    for i in s:
        print(i)
