class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.row_index = 0
        self.col_index = 0

    def __iter__(self):
        self.row_index = 0
        self.col_index = 0
        return self

    def __next__(self):
        if self.row_index >= len(self.list_of_list):
            raise StopIteration

        if self.col_index >= len(self.list_of_list[self.row_index]):
            self.row_index += 1
            self.col_index = 0
            return self.__next__()

        item = self.list_of_list[self.row_index][self.col_index]
        self.col_index += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_iterator = FlatIterator(list_of_lists_1)
    for flat_iterator_item, check_item in zip(
            flat_iterator,
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
