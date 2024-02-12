


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.counter = -1
        self.first_index_list = 0
        self.second_index_list = -1
        return self


    def __next__(self):
        self.max_count = [len(item)*len(self.list_of_list) for item in self.list_of_list]

        if self.counter > self.max_count[0]:
            raise StopIteration

        self.second_index_list = self.second_index_list + 1

        if self.second_index_list == len(self.list_of_list[self.first_index_list]):
            self.first_index_list = self.first_index_list + 1
            self.second_index_list = 0

        item = self.list_of_list[self.first_index_list][self.second_index_list]

        self.counter = self.counter + 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
