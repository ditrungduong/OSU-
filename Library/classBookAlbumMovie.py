from classLibraryItem import LibraryItem


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
        return str(self._title) + " " + str(self._author)+ " " + str(self.check_out_length)

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
        return str(self._title) + " " + str(self._director)+ " " + str(self.check_out_length)

    def get_director(self):
        """Return movie director name"""
        return self._director

    def get_check_out_length(self):
        """Return rental length for Movie"""
        return self._check_out_length

    def get_location(self):
        """Return location of item"""
        return self._location
