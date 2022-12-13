# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 09/30/2022
# Description: Create unit tests for Lemonade Stand
import unittest
from LemonadeStand import LemonadeStand
from LemonadeStand import MenuItem
from LemonadeStand import SalesForday

class TestLemonadeStand(unittest.TestCase):
    """Contain unit tests some of the function inside Lemonade Stand file"""
    def test_get_name_(self):
        """Return correct name"""
        item1 = MenuItem('cam', 1, 2.5)
        result = item1.get_item_name()
        self.assertNotEqual(result, 'orange')

    def test_get_selling_price_(self):
        """Return correct selling price"""
        item1 = MenuItem('cam', 1, 2.5)
        result = item1.get_selling_price()
        self.assertEqual(result, 2.5)

    def test_sales_of_menu_item_for_day_(self):
        """Return correct sell unit for particular item"""
        new_stand = LemonadeStand('Sharbella')
        item1 = MenuItem('orange', 0.5, 1.5)
        new_stand.add_menu_item((item1))
        item2 = MenuItem('apple', 1, 2.0)
        new_stand.add_menu_item(item2)
        item3 = MenuItem('banana', 0.5, 2.0)
        new_stand.add_menu_item(item3)
        day_0_sales = {'orange': 3, 'apple': 5, 'chuoi': 0}
        new_stand.enter_sales_for_today(day_0_sales)
        result = int(new_stand.sales_of_menu_item_for_day(0, 'orange'))
        print(result)
        self.assertEqual(result, 3)

    def test_total_sale_for_menu_item_(self):
        """Return total sale for a particular item"""
        new_stand = LemonadeStand('Sharbella')
        item1 = MenuItem('orange', 0.5, 1.5)
        new_stand.add_menu_item(item1)
        item2 = MenuItem('apple', 1, 2.0)
        new_stand.add_menu_item(item2)
        item3 = MenuItem('banana', 0.5, 2.0)
        new_stand.add_menu_item(item3)
        day_0_sales = {'orange': 3, 'apple': 5, 'banana': 0}
        day_1_sales = {'banana': 7, 'orange': 4, 'apple': 6}
        day_2_sales = {'banana': 10, 'orange': 4, 'apple': 6}
        new_stand.enter_sales_for_today(day_0_sales)
        new_stand.enter_sales_for_today(day_1_sales)
        new_stand.enter_sales_for_today(day_2_sales)
        result = int(new_stand.total_sales_for_menu_item('banana'))
        self.assertEqual(result, 17.0)

    def test_menu_dict_(self):
        """Return menu dictionary"""
        new_stand = LemonadeStand('Sharbella')
        item1 = MenuItem('orange', 0.5, 1.5)
        new_stand.add_menu_item(item1)
        item2 = MenuItem('apple', 1, 2.0)
        new_stand.add_menu_item(item2)
        item3 = MenuItem('banana', 0.5, 2.0)
        new_stand.add_menu_item(item3)
        result = (new_stand.get_menu_dict())
        self.assertTrue(result, dict)

    def test_item_in_dict_(self):
        """Return menu dictionary"""
        new_stand = LemonadeStand('Sharbella')
        item1 = MenuItem('orange', 0.5, 1.5)
        new_stand.add_menu_item(item1)
        item2 = MenuItem('apple', 1, 2.0)
        new_stand.add_menu_item(item2)
        item3 = MenuItem('banana', 0.5, 2.0)
        new_stand.add_menu_item(item3)
        result = (new_stand.get_menu_dict())
        self.assertIn('orange', result)



if __name__ == '__main__':
    unittest.main()


