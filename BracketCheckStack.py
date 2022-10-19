class Stack():
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def push(self, next):
        if next is None:
            return
        temp = self.next
        self.next = Stack(next)
        self.next.next = temp

    def print(self):
        item = self
        while item is not None:
            print(item.value, end=' ')
            item = item.next

    def is_empty(self):
        if self.value is None and self.next is None:
            return True
        else:
            return False

    def pop(self):
        self.next = self.next.next
        return

    @property
    def head(self):
        return self.next.value


dict_scob = {
    '(': ')',
    '{': '}',
    '[': ']',
}

container = Stack()

def check_valid(stro: str):
    global container
    for item in stro:
        if container.is_empty():
            container.push(item)
            continue
        if item == dict_scob.get(container.head, None):
            container.pop()
            continue
        else:
            container.push(item)
    return container.is_empty()


print(check_valid('{{{([(])}}}'))
