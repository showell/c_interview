def test():
    arr = BigArray()
    chunk_size = 10000
    for i in range(100):
        new_elems = range(i*chunk_size, (i+1)*chunk_size)
        arr.insert_elems(i*chunk_size, new_elems)
    assert 43999 == arr[43999]
    assert 500000 == arr[500000]
    arr.insert_elems(900000, range(3000))
    assert 0 == arr[900000]
    assert 1001 == arr[901001]
    assert 900001 == arr[903001]
    arr.insert_elems(903001, [1,2,3])
    assert 1 == arr[903001]
    assert 2 == arr[903002]
    assert 3 == arr[903003]
    assert 900001 == arr[903004]

class BigArray:
    def __init__(self, page_size = 1000):
        # Keep a list of pages, with an empty page
        # at the end for convenience.
        self.page_offsets = [0]
        self.pages = [[]]
        self.page_size = 1000

    def debug(self):
        for i in range(len(self.pages)):
            print i, self.page_offsets[i], len(self.pages[i])

    def __getitem__(self, i):
        if i > self.page_offsets[-1]:
            raise IndexError, "n too large"
        page = self._get_page(i)
        page_i = i - self.page_offsets[page]
        return self.pages[page][page_i]
        
    def insert_elems(self, n, lst):
        # insert elements from lst into BigArray
        # starting at index n
        if n > self.page_offsets[-1]:
            raise IndexError, "n too large"

        if n == self.page_offsets[-1]:
            return self.append_elem(lst)

        # Find the page where insertion starts.
        page = self._get_page(n)
        cnt = len(lst)

        # Split the page after the insertion point.  This
        # might create a small page, but we don't worry
        # about it for simplicity sake.  We can refine
        # this later by trying to balance our new elements
        # better.
        self._split_page(page, n)
        self._update_offsets_for_insertion(page, cnt)

        low = 0
        # See how much room we have in current page
        # to avoid needlessly creating new pages. We
        # may luck out with a partial page from a previous
        # insert.
        room = self.page_size - len(self.pages[page])
        if room > 0:
            # We might have extra room
            if room > cnt:
                room = cnt
            # Extend our current page
            self.pages[page].extend(lst[0:room])
            low = room

        # Now create new pages as needed.
        if low >= cnt: return
        new_pages = []
        new_offsets = []
        while low < cnt:
            page_size = min([cnt - low, self.page_size])
            new_pages.append(lst[low:low+page_size])
            new_offsets.append(n+low)
            low += page_size
        self.pages[page+1:page+1] = new_pages
        self.page_offsets[page+1:page+1] = new_offsets

    def append_elem(self, lst):
        # TODO: For now, we always create new pages, but
        # we could try to look at the last nonempty
        # page and see if there's room.
        cnt = len(lst)
        n = self.page_offsets[-1]
        # remove empty page temporarily
        self.page_offsets.pop()
        self.pages.pop()
        low = 0
        while low < cnt:
            page_size = min(self.page_size, cnt - low)
            self.page_offsets.append(n + low)
            self.pages.append(lst[low:low+page_size])
            low += page_size
        # put back empty page
        self.page_offsets.append(n+cnt)
        self.pages.append([])

    def _update_offsets_for_insertion(self, page, cnt):
        # update offsets of all the pages to the
        # right of the insertion point (if any)
        for i in range(page+1, len(self.pages)):
            self.page_offsets[i] += cnt
    
    def _get_page(self, n):
        # This should be a binary search, but
        # doing it as a linear search for clarity.
        for page in range(len(self.page_offsets) - 1):
            if n < self.page_offsets[page+1]:
                return page
        # the last page is unbounded, and it's usually
        # an empty page
        return len(self.page_offsets) - 1 
        
    def _split_page(self, page, n):
        if n >= self.page_offsets[page+1]:
            return
        self.page_offsets.insert(page+1, n)
        offset = n - self.page_offsets[page]
        self.pages.insert(page+1, self.pages[page][offset:])
        self.pages[page] = self.pages[page][:offset]

test()
