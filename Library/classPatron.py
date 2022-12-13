class Patron:
    """Representing a patron"""

    def __init__(self, patron_id, name):
        """Initializing a patron with id and name"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def __str__(self):
        return str(self._name) + str(self._fine_amount)

    def get_patron_id(self):
        """Return patron ID"""
        return self._patron_id

    def get_name(self):
        """Return patron name"""
        return self._name

    def get_checked_out_items(self):
        """Return a collection of Library Items that a patron currently has checked out"""
        self._checked_out_items


    def get_fine_amount(self):
        """Return the fine amount"""
        return float(self._fine_amount)

    def add_library_item(self, add_new_item_id):
        """Adds the specified LibraryItem to checked_out_items"""
        self._checked_out_items.append(add_new_item_id)
        return

    def remove_library_item(self, remove_item_id):
        """Remove the specified LibraryItem to checked_out_items"""
        self._checked_out_items.remove(remove_item_id)
        return

    def amend_fine(self, fine):
        """Return fine_amount, either increase or decreases it"""
        self._fine_amount += fine


