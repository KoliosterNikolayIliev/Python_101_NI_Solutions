class Lev:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self):
        return f'{self.value}lv'

    def __eq__(self, other):
        try:
            self.isinstance(other)
            return self.value == other.value
        except ValueError:
            return False

    def __hash__(self):
        return id(self)

    def __add__(self, other):
        self.isinstance(other)

        sum_value = self.value + other.value
        return self.__class__(value=sum_value)

    def __sub__(self, other):
        self.isinstance(other)

        # TODO: Handle negative values
        sum_value = self.value - other.value
        return self.__class__(value=sum_value)

    def isinstance(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Different instances.')


five_levs = Lev(5)

# print(Lev(5) is Lev(5))
# print(Lev(5) == Lev(5))

ten_levs = Lev(10)

purse = {
    five_levs: 10,
    ten_levs: 100
}

# for key, value in purse.items():
#     print(hash(key), value)


# ten_levs.value = 111111111111111111
# print(hash(ten_levs))
# purse[ten_levs]

# print(purse)


# class Dollar:
#     def __init__(self, value):
#         self.value = value


# print(Lev(5) == Lev(10))
# print(Lev(5) == Dollar(5))

# print(five_levs + 10)
# print(ten_levs - five_levs)


class Batch:
    def __init__(self):
        self.bills = [five_levs, ten_levs, Lev(20), Lev(50)]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.bills):
            raise StopIteration

        value = self.bills[self.index]

        self.index += 1

        return value

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return 180000


batch = Batch()

for bill in batch:
    print(bill)
print('===============================')
for bill in batch:
    print(bill)

# print(batch[1:2:-1])  # TODO: Will this work???

print(len(batch))
