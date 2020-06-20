class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, number):
        self.queue.append(number)

    def dequeue(self):
        self.queue.pop(0)

    @property
    def length(self):
        return len(self.queue)

    @property
    def content(self):
        return self.queue

    @property
    def first(self):
        return self.queue[0]

    def print_content(self):
        if len(self.queue) == 0: print('Empty')
        else:
            for el in self.queue:
                print(f"{el}, ", end='')
            print()
    

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        self.stack.pop() if len(self.stack) > 0 else print('Unable to pop')

    @property
    def top(self):
        return self.stack[-1] if len(self.stack) > 0 else print('No top number')

    @property
    def is_empty(self):
        return True if len(self.stack) == 0 else False

    @property
    def length(self):
        return len(self.stack)

    @property
    def content(self):
        return self.stack

    def print_content(self):
        if len(self.stack) == 0: print('Empty')
        else:
            for el in self.stack:
                print(f"{el}, ", end='')
            print()
