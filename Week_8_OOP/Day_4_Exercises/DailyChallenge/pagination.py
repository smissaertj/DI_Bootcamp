import math


class Pagination():
    def __init__(self, items=[], items_per_page=10):
        self.items = items
        self.items_per_page = items_per_page if items_per_page > 0 else 1
        self.total_pages = math.ceil(len(self.items) / self.items_per_page)
        self.current_page_index = 0

        print(f'Total Pages: {self.total_pages}')

    def get_visible_items(self):
        print(self.items[self.current_page_index: self.current_page_index + self.items_per_page])

    def prev_page(self):
        if not (self.current_page_index - self.items_per_page) < 0:
            self.current_page_index -= self.items_per_page
        else:
            self.current_page_index = 0

    def next_page(self):
        if self.items_per_page <= self.total_pages:
            self.current_page_index += self.items_per_page

    def first_page(self):
        self.current_page_index = 0

    def last_page(self):
        self.current_page_index = len(self.items) - self.items_per_page

    def go_to_page(self, page):
        page = (page * self.items_per_page) - self.items_per_page if page < self.total_pages else (self.total_pages * self.items_per_page) - self.items_per_page
        self.current_page_index = page


alphabet = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabet, 5)

p.get_visible_items()

p.go_to_page(6)
p.get_visible_items()

p.go_to_page(5)
p.get_visible_items()

p.next_page()
p.get_visible_items()

p.go_to_page(2)
p.get_visible_items()

p.prev_page()
p.get_visible_items()

p.go_to_page(20000000)
p.get_visible_items()

"""
Pagination Indexes
1: 1 - 5
2: 6 - 10
3: 11 - 15
4: 16- 20
5: 21 - 25
6: 26
"""
