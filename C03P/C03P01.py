class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start = start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened

    def is_inside(self, value):
        if self.start_opened and self.end_opened:
            return self.start < value < self.end
        if self.start_opened:
            return self.start < value <= self.end
        if self.end_opened:
            return self.start <= value < self.end
        return self.start <= value <= self.end

    def stringify(self):
        start_symbol = "["
        if self.start_opened:
            start_symbol = "("
        end_symbol = "]"
        if self.end_opened:
            end_symbol = ")"

        return f"{start_symbol}{self.start}, {self.end}{end_symbol}"

    def __str__(self):
        return self.stringify()

    def __repr__(self):
        return self.stringify()


closed_interval = Interval(1, 10)

print(closed_interval.is_inside(1) is True)
print(closed_interval.is_inside(5) is True)
print(closed_interval.is_inside(10) is True)

print(closed_interval.stringify() == "[1, 10]")

closed_interval = Interval(1, 10, start_opened=True, end_opened=True)

print(closed_interval.is_inside(1) is False)
print(closed_interval.is_inside(5) is True)
print(closed_interval.is_inside(10) is False)

print(closed_interval.stringify() == "(1, 10)")

half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)

print(half_opened_interval.is_inside(1) is True)
print(half_opened_interval.is_inside(5) is True)
print(half_opened_interval.is_inside(10) is False)

print(half_opened_interval.stringify() == "[1, 10)")

half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)

print(half_opened_interval.is_inside(1) is False)
print(half_opened_interval.is_inside(5) is True)
print(half_opened_interval.is_inside(10) is True)

print(half_opened_interval.stringify() == "(1, 10]")
