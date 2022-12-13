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
