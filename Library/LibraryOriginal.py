# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/07/2022
# Description: Create Lemonade Stand Class and return total profit

class LibraryItem:
    """Represent a library item with id, title, location, availability status, user_request"""

    def __init__(self, library_item_id, title):
        """Initialize a library item"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = {}
        self._requested_by = {}
        self._date_checked_out = 0

    def get_library_item_id(self):
        """Return unique library item id"""
        return self._library_item_id

    def get_title(self):
        """Return title of item - cannot be assumed to be unique"""
        return self._title

    def set_location(self, new_location):
        """Return update location from parameter"""
        self._location = new_location
        return

    def get_location(self):
        """Return location of item"""
        return self._location

    def get_checked_out_by(self):
        """Return get check out by patron"""
        return self._checked_out_by

    def requested_by(self):
        """Return requested by"""
        return self._requested_by


class Book(LibraryItem):
    """Initialize a book item"""

    def __init__(self, library_item_id, title, author):
        """"Having the same properties as other library items plus additional field author"""
        super().__init__(library_item_id, title)
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = {}
        self._requested_by = {}
        self._date_checked_out = {}
        self._author = author
        self._check_out_length = 21

    def __str__(self):
        return str(self._title) + " " + str(self._author)

    def get_author(self):
        """Return book author"""
        return self._author

    def get_check_out_length(self):
        """Return rental length for book"""
        return self._check_out_length

    def get_location(self):
        """Return location of item"""
        return self._location


class Album(LibraryItem):
    """Initialize an album item"""

    def __init__(self, library_item_id, title, artist):
        """Having the same properties as other library items plus additional field artist """
        super().__init__(library_item_id, title)
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = {}
        self._requested_by = {}
        self._date_checked_out = {}
        self._artist = artist
        self.check_out_length = 14

    def __str__(self):
        return str(self._title) + " " + str(self._artist) + " " + str(self.check_out_length)

    def get_check_out_length(self):
        """Return rental length for Album"""
        return self.check_out_length

    def get_artist(self):
        """Return artist name"""
        return self._artist

    def get_location(self):
        """Return location of item"""
        return self._location


class Movie(LibraryItem):
    """Initialize a movie item"""

    def __init__(self, library_item_id, title, director):
        """Having the same properties as other library items plus additional field director """
        super().__init__(library_item_id, title)
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = {}
        self._requested_by = {}
        self._date_checked_out = {}
        self._director = director
        self._check_out_length = 7

    def __str__(self):
        return str(self._title) + " " + str(self._director)

    def get_director(self):
        """Return movie director name"""
        return self._director

    def get_check_out_length(self):
        """Return rental length for Movie"""
        return self._check_out_length

    def get_location(self):
        """Return location of item"""
        return self._location


class Patron:
    """Representing a patron"""

    def __init__(self, patron_id, name):
        """Initializing a patron with id and name"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = {}
        self._fine_amount = 0

    def __str__(self):
        return str(self._name) + str(self._fine_amount)

    def get_patron_id(self):
        """Return patron ID"""
        return self._patron_id

    def get_name(self):
        """Return patron name"""
        return self._name

    def checked_out_items(self):
        """Return a collection of Library Items that a patron currently has checked out"""
        return self._checked_out_items

    def get_fine_amount(self):
        """Return the fine amount"""
        return float(self._fine_amount)

    def add_library_item(self, add_new_item_id):
        """Adds the specified LibraryItem to checked_out_items"""
        self._checked_out_items[add_new_item_id] = self._patron_id
        return

    def remove_library_item(self, remove_item_id):
        """Remove the specified LibraryItem to checked_out_items"""
        del self._checked_out_items[remove_item_id]
        return

    def amend_fine(self, fine):
        """Return fine_amount, either increase or decreases it"""
        self._fine_amount += fine


class Library:
    """Representing a library"""

    def __init__(self):
        """Initializes the current_date to zero"""
        self._current_day = 0
        self._holding = {}
        self._member = {}

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
            elif library_item_ids in self._holding.values():
                print(self._holding.values())
                if self._holding[library_item_ids].values == patron_ids:
                    self._member[patron_ids].add_library_item(library_item_ids)
                    self._holding[library_item_ids]._checked_out_by[library_item_ids] = patron_ids
                    self._holding[library_item_ids].set_location("CHECKED_OUT")
                    self._holding[library_item_ids]._date_checked_out = self._current_day
                    del self._holding[library_item_ids]._requested_by[library_item_ids]
                    print(f"Item check out successful")
                else:
                    print(f"Item on hold by other patron")
            else:
                self._member[patron_ids].add_library_item(library_item_ids)
                self._holding[library_item_ids]._checked_out_by[library_item_ids] = patron_ids
                self._holding[library_item_ids].set_location("CHECKED_OUT")
                self._holding[library_item_ids]._date_checked_out = self._current_day
                print(f"Item check out successful")
        else:
            print(f"Item not found")

    def return_library_item(self, library_item_ids):
        """Return library item using library item id"""
        if library_item_ids not in self._holding:
            print(f"Item not found")
            return
        elif self._holding[library_item_ids].get_location() != "CHECKED_OUT":
            print(f"Item already in library")
            return
        else:
            self._member[self._holding[library_item_ids]._checked_out_by[library_item_ids]].remove_library_item(
                library_item_ids)
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
            print(f"Patron not found")
            return
        elif library_item_ids not in self._holding:
            print(f"Item not found")
            return
        elif library_item_ids in self._holding[library_item_ids]._requested_by:
            print(f"Item already on hold")
        else:
            self._holding[library_item_ids].set_location("ON_HOLD_SHELF")
            self._holding[library_item_ids]._requested_by[library_item_ids] = patron_ids
            print(f"Request for item is successful")
            return

    def pay_fine(self, patron_ids, payment_amount):
        """Update patron fine """
        if patron_ids not in self._member:
            return f"Patron not found"
        else:
            self._member[patron_ids].amend_fine(-payment_amount)
            return "Payment successful"

    def increment_current_date(self):
        """Increase 10 for each overdue date"""
        self._current_day += 1
        for item in self._holding:
            if self._holding[item].get_location() == "CHECKED_OUT":
                if int(self._current_day) > int(self._holding[item].get_check_out_length()):
                    self._member[self._holding[item]._checked_out_by[item]].amend_fine(0.10)

b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
# print(b1.get_author())
# print(a1.get_artist())
# print(m1.get_director())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")
p3 = Patron("def", "Jose")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_library_item(m1)

lib.add_patron(p1)
lib.add_patron(p2)
lib.add_patron(p3)
#print("bcd check out 567")
#lib.check_out_library_item("bcd", "567")
#print(f"Status of item 567 after check out {m1.get_location()}")
#print("abc request for 890")
print(b1.get_location())

lib.request_library_item("abc", "345")
print(b1.get_location())
lib.request_library_item("def", "345")
# print(f"Status of item 567 after request but still in check out {m1.get_location()}")

# print("def request for 567")
# lib.request_library_item("def", "567")
# print("abc check out for 567 after request")
# lib.check_out_library_item("abc", "567")

# lib.return_library_item("567")

# lib.return_library_item("456")
# for _ in range(7):
#   lib.increment_current_date()  # 7 days pass

# loc = m1.get_location()
# print(loc)
# print(loc)
# for _ in range(57):
#    lib.increment_current_date()  # 57 days pass
# p2_fine = p2.get_fine_amount()
# p1_fine = p1.get_fine_amount()
# print(f"This is p2 fine : {p2_fine}")
# print(f"This is p2 fine : {p1_fine}")
# lib.pay_fine("bcd", p2_fine)
# lib.return_library_item("456")
# print(f"This is p2 fine : {p2_fine}")
# print(f"This is p1 fine : {p1_fine}")