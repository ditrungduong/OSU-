from classLibraryItem import LibraryItem
from classPatron import Patron


class Library:
    """Representing a library"""

    def __init__(self, initial_adding_day=0):
        """Initializes the current_date to zero"""
        self._current_day = 0
        self._holding = {}
        self._member = {}
        self._on_hold = {}

    def add_library_item(self, new_items):
        """Takes a LibraryItem object as a parameter and adds it to the holdings"""
        self._holding[new_items.get_library_item_id()] = new_items

    def add_patron(self, new_patrons):
        """Takes a Patron object as a parameter and adds it to the members"""
        self._member[new_patrons.get_patron_id()] = new_patrons

    def lookup_library_item_from_id(self, lookup_item_id):
        """ Returns the LibraryItem object corresponding to the ID parameter, or None"""
        if lookup_item_id in self._holding:
            return self._holding[lookup_item_id]
        return None

    def lookup_patron_from_id(self, lookup_patron_id):
        """ Returns the Patron object corresponding to the ID parameter, or None"""
        if lookup_patron_id in self._member:
            return self._member[lookup_patron_id]
        return None

    def check_out_library_item(self, patron_ids, library_item_ids):
        """Return patron and library item status"""
        if patron_ids not in self._member:
            print("Patron not found")
            return
        elif library_item_ids in self._holding:
            if self._holding[library_item_ids].get_location() == "CHECKED_OUT":
                print(f"Item already checked out")
            elif library_item_ids in self._on_hold:
                if self._on_hold[library_item_ids] == patron_ids:
                    self._member[patron_ids].checked_out_items[patron_ids] = library_item_ids
                    self._holding[library_item_ids]._checked_out_by[library_item_ids] = patron_ids
                    self._holding[library_item_ids].set_location("CHECKED_OUT")
                    self._holding[library_item_ids]._date_checked_out = self._current_day
                    del self._holding[library_item_ids]._requested_by[library_item_ids]
                    print(f"Item check out successful")
                else:
                    print(f"Item on hold by other patron")
            else:
                self._member[patron_ids].checked_out_items[patron_ids] = library_item_ids
                self._holding[library_item_ids]._checked_out_by[library_item_ids] = patron_ids
                self._holding[library_item_ids].set_location("CHECKED_OUT")
                self._holding[library_item_ids]._date_checked_out = self._current_day
                print(f"Item check out successful")
        else:
            print(f"Item {library_item_ids} not found")

    def return_library_item(self, library_item_ids):
        """Return library item using library item id"""
        if library_item_ids not in self._holding:
            print(f"Item {library_item_ids} not found")
            return
        elif self._holding[library_item_ids].get_location() != "CHECKED_OUT":
            print(f"Item {library_item_ids} already in library")
            return
        else:
            del self._holding[library_item_ids]._checked_out_by[library_item_ids]
            if library_item_ids in self._holding[library_item_ids]._requested_by:
                self._holding[library_item_ids].set_location("ON_HOLD_SHELF")
                print(f"Item {library_item_ids} return \"ON_HOLD_SHELF\" ")
            else:
                self._holding[library_item_ids].set_location("ON_SHELF")
                print(f"Item {library_item_ids} return \"ON_SHELF\" ")

    def request_library_item(self, patron_ids, library_item_ids):
        """Return request using patron id and library item ID"""
        if patron_ids not in self._member:
            print(f"Patron {patron_ids} not found")
            return
        elif library_item_ids not in self._holding:
            print(f"Item {library_item_ids} not found")
            return
        elif library_item_ids in self._holding[library_item_ids]._requested_by:
            print(f"Item {library_item_ids} already on hold")
        else:
            #print(f"This is the before status of this item {library_item_ids} {self._holding[library_item_ids].get_location()}")
            self._holding[library_item_ids].set_location("ON_HOLD_SHELF")
            #print(f"This is the after status of this item {library_item_ids} {self._holding[library_item_ids].get_location()}")
            self._holding[library_item_ids]._requested_by[library_item_ids] = patron_ids
            #print(f"{self._holding[library_item_ids]._requested_by}")
            self._on_hold[library_item_ids] = patron_ids
            #print(f"{self._on_hold}")
            return

    def pay_fine(self, patron_ids, fine_amount):
        """Update patron fine """
        if patron_ids not in self._member:
            return f"Patron {patron_ids} not found"

        else:
            #print(f"This is the fine amount before payment {self._member[patron_ids].get_fine_amount}")
            self._member[patron_ids].amend_fine(fine_amount)
            #print(f"This is the fine amount after payment {self._member[patron_ids].get_fine_amount}")
            return "Payment successful"


    def increment_current_date(self):
        """Increase 10 for each overdue date"""
        self._current_day += 1
        for item in self._holding:
            if self._holding[item].get_location() == "CHECKED_OUT":
                member = self._holding[item]._checked_out_by[item]
                check_out_item_due_date = self._holding[item].get_check_out_length()
                if self._current_day > check_out_item_due_date:
                    #print(f"This is the fine amount before {self._member[member].get_fine_amount()}")
                    self._member[member].amend_fine(0.10)
                    print(f"This is the fine amount after {self._member[member].get_fine_amount()}")

        print(f"This is the fine for {member} {self._member[member].get_fine_amount()}")