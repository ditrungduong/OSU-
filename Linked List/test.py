import unittest
from Rachel_Covington_LinkedList import LinkedList


class UnitTests(unittest.TestCase):

    def test_insert(self):
        my_list = LinkedList()
        my_list.add(13)
        my_list.add(81)
        my_list.insert(2, 0)
        reg_list = my_list.to_plain_list()
        a = reg_list[0]
        b = reg_list[1]
        c = reg_list[2]
        self.assertEqual(a, 2)
        self.assertEqual(b, 13)
        self.assertEqual(c, 81)

    def test_testName1(self):
        my_list = LinkedList()
        my_list.add(13)
        my_list.add(81)
        my_list.insert(2, 1)
        reg_list = my_list.to_plain_list()
        a = reg_list[0]
        b = reg_list[1]
        c = reg_list[2]
        self.assertEqual(a, 13)
        self.assertEqual(b, 2)
        self.assertEqual(c, 81)

    def test_testName2(self):
        my_list = LinkedList()
        my_list.add(13)
        my_list.add(81)
        my_list.insert(2, 2)
        reg_list = my_list.to_plain_list()
        a = reg_list[0]
        b = reg_list[1]
        c = reg_list[2]
        self.assertEqual(a, 13)
        self.assertEqual(b, 81)
        self.assertEqual(c, 2)

    def test_testName3(self):
        my_list = LinkedList()
        my_list.add(13)
        my_list.add(81)
        my_list.insert(2, 5)
        reg_list = my_list.to_plain_list()
        a = reg_list[0]
        b = reg_list[1]
        c = reg_list[2]
        self.assertEqual(a, 13)
        self.assertEqual(b, 81)
        self.assertEqual(c, 2)

    def test_testName4(self):
        my_list = LinkedList()
        my_list.insert(3, 3)
        reg_list = my_list.to_plain_list()
        self.assertEqual(reg_list[0], 3)
