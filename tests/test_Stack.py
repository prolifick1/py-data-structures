import unittest
from Stack.Stack import Stack

class StackTester(unittest.TestCase):
    def test_oncreate_isEmpty_True(self):
        s = Stack()
        self.assertEqual(0, s.size())

    def test_push1_isEmpty_false(self):
        item = 5
        s = Stack()
        s.push(item)
        self.assertEqual(1, s.size())

    def test_push1_items(self):
        s = Stack()
        s.push(5)
        self.assertEqual([5], s.items)

    def test_push2_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual(2, s.size())
    def test_push2_items(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual([5, 6], s.items)

    def test_push2_pop1_size(self):
        s = Stack()
        s.push(5)
        s.push(6)
        s.pop()
        self.assertEqual(1, s.size())
    def test_push2_pop1_value(self):
        s = Stack()
        s.push(8)
        s.push(9)
        self.assertEqual(9, s.pop())
