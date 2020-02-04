# Implement Queue With Stack
# We will only do the dequeue function
# We are only allowed one stack

class Q:

    def __init__(self, stack):
        self.stack = stack

    def dequeue(self):
        if self.stack:
            return self.recurse()
        else:
            return "Stack is empty"

    def recurse(self):
        if len(self.stack) == 1:
            return stack.pop()

        cur_val = self.stack.pop()
        result = self.recurse()
        self.stack.append(cur_val)
        return result

stack = [1, 2, 3, 4]
queue_obj = Q(stack)

print(queue_obj.stack)
print("Dequeue 1 = ", queue_obj.dequeue())
print(queue_obj.stack)

print("Dequeue 2 = ", queue_obj.dequeue())
print(queue_obj.stack)
