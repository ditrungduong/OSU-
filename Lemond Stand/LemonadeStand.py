# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 09/30/2022
# Description: Create Lemonade Stand Class and return total profit
class MenuItem:
    """Represent a Menu Item class with three data members item's name, cost and selling price"""

    def __init__(self, item_name, wholesale_cost, selling_price):
        """Crete a menu item profile with name, cost and selling price"""
        self._item_name = item_name
        self._wholesale_cost = float(wholesale_cost)
        self._selling_price = float(selling_price)

    def get_item_name(self):
        """"Return item name """
        return self._item_name

    def get_wholesale_cost(self):
        """Return item wholesale cost"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Return item selling price"""
        return self._selling_price


class SalesForday:
    """Represent the sale of a particular day with two data members numbers of day
    and dictionary of item sold and value"""

    def __init__(self, number_of_days, sale_dict):
        """Create sale of day with day and sale dictionary """
        self._number_of_days = number_of_days
        self._sales_dict = sale_dict  # key: name of item #value: number of items sold

    def get_day(self):
        """Return number of day"""
        return self._number_of_days

    def get_sales_dict(self):
        """Return sale dictionary"""
        return self._sales_dict


class InvalidSalesItemError(Exception):
    """user-defined exception for invalid sale item input"""
    pass


class LemonadeStand:
    """Represent a lemonade stand with four data member name, day, menu dictionary and
    a list of sale for day"""

    def __init__(self, stand_name):
        """Create a lemonade stand with name, current day, menu time dictionary and sale for day"""
        self._stand_name = stand_name
        self._current_day = 0
        self._menu_dict = {}  # key: name of item #value: MenuItem Object
        self._sales_record = []

    def get_stand_name(self):
        """Return stand name"""
        return self._stand_name

    def get_menu_dict(self):
        """Return menu dict"""
        return self._menu_dict

    def add_menu_item(self, new_menu_item_object):
        """ Take MenuItem object and adds it to the menu dictionary """
        self._menu_dict[new_menu_item_object.get_item_name()] = new_menu_item_object

    def enter_sales_for_today(self, day_number_sale_record):
        """Pre-return a dictionary where the keys are names of items sold and the values are
        how many of the item were sold"""
        try:
            zero_sale = {item for item in self._menu_dict if item not in day_number_sale_record}
            for item in zero_sale:
                day_number_sale_record[item] = 0
            self._sales_record.append(SalesForday(self._current_day, day_number_sale_record))
            invalid_item = {item for item in day_number_sale_record if item not in self._menu_dict}
            for index in range(len(invalid_item)):
                for item in invalid_item:
                    day_number_sale_record.pop(item)
                raise InvalidSalesItemError
        except InvalidSalesItemError:
            for item in invalid_item:
                print(f"This item \" {item} \" is not in the menu dict")
        self._current_day = + 1

    def sales_of_menu_item_for_day(self, day_of_sale, item_name):
        """Return number of item sold base on day input and item name input"""

        try:
            return(
                f"\n{self._sales_record[day_of_sale].get_sales_dict()[item_name]}")
        except KeyError:
            return (f"There is no sale record for {item_name}")


    def total_sales_for_menu_item(self, name_of_menu_item):
        """Return total sale of input item over the history of the stand"""
        result = 0
        for index in range(len(self._sales_record)):
            if name_of_menu_item in self._sales_record[index].get_sales_dict():
                result += int(self.sales_of_menu_item_for_day(index, name_of_menu_item))
            else:
                None
        return float(result)

    def total_profit_for_menu_item(self, name_of_menu_item):
        """Return total profit of item"""
        total_profit_for_item = 0
        total_profit_for_item = (self.total_sales_for_menu_item(name_of_menu_item)) * \
                                ((self._menu_dict[name_of_menu_item].get_selling_price()) - (self._menu_dict[name_of_menu_item].get_wholesale_cost()))
        return float(total_profit_for_item)

    def total_profit_for_stand(self):
        """Return total profit of all item"""
        total_stand_profit = 0
        for item in self._menu_dict:
            total_stand_profit += (self.total_sales_for_menu_item(item))
        return total_stand_profit


if __name__ == '__main__':
    new_stand = LemonadeStand('Sharbella')
    item1 = MenuItem('orange', 0.5, 1.5)
    new_stand.add_menu_item((item1))
    item2 = MenuItem('apple', 1, 2.0)
    new_stand.add_menu_item(item2)
    item3 = MenuItem('banana', 0.5, 2.0)
    new_stand.add_menu_item(item3)
    day_0_sales = {'orange': 3, 'apple': 5, 'chuoi': 0}
    day_1_sales = {'banana': 7, 'orange': 4, 'apple': 6}
    day_2_sales = {'banana': 10, 'orange': 4, 'apple': 6}

    new_stand.enter_sales_for_today(day_0_sales)
    new_stand.enter_sales_for_today(day_1_sales)
    new_stand.enter_sales_for_today(day_2_sales)
    print(new_stand.sales_of_menu_item_for_day(0, 'banana'))
    print(new_stand.total_sales_for_menu_item('orange'))


