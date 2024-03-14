class MyStack:

    def __init__(self, size=0):
        self.items = []
        self.size = size

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items) == self.size:
            return True
        else:
            return False

    def push(self,item):
        if not self.isFull():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            last_value = self.items[len(self.items) - 1]
            self.items.remove(last_value)
            return last_value

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def display(self):
        print(self.items)


my_stack = MyStack()
my_stack.push(1)
my_stack.display()
# [1]
my_stack.push(2)
my_stack.display()
# [1, 2]
my_stack.push(3)
my_stack.display()
# [1, 2, 3]
my_stack.push(4)
my_stack.display()
# [1, 2, 3]  size 가 3 이기 때문에 추가가 안됩니다.
print(my_stack.isFull())
# True
print(my_stack.peek())
# 3
print(my_stack.pop())
# 3
print(my_stack.peek())
# 2
my_stack.display()
# [1, 2]
print(my_stack.isEmpty())
# False
print(my_stack.pop())
# 2
print(my_stack.pop())
# 1
print(my_stack.pop())
# None
print(my_stack.isEmpty())
# True
print(my_stack.peek())
# None
