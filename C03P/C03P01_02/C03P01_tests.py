import unittest

from C03P01 import Interval


class IntervalTests(unittest.TestCase):
    def setUp(self):
        self.start = 1
        self.mid = 5
        self.end = 10

        self.closed_interval = Interval(self.start, self.end)
        self.opened_interval = Interval(1, 10, start_opened=True, end_opened=True)
        self.opened_interval_start = Interval(1, 10, start_opened=True, end_opened=False)
        self.opened_interval_end = Interval(1, 10, start_opened=False, end_opened=True)

        self.test_instances_list = [
            self.closed_interval,
            self.opened_interval,
            self.opened_interval_start,
            self.opened_interval_end
        ]

    def test_stringify_produces_correct_result_closed_interval(self):
        expected = '[1, 10]'
        self.assertEqual(expected, self.closed_interval.stringify())

    def test_stringify_produces_correct_result_opened_interval(self):
        expected = '(1, 10)'
        self.assertEqual(expected, self.opened_interval.stringify())

    def test_stringify_produces_correct_result_opened_interval_start(self):
        expected = '(1, 10]'
        self.assertEqual(expected, self.opened_interval_start.stringify())

    def test_stringify_produces_correct_result_opened_interval_end(self):
        expected = '[1, 10)'
        self.assertEqual(expected, self.opened_interval_end.stringify())

    def test_is_inside_produces_correct_results_closed_interval(self):
        self.assertTrue(self.closed_interval.is_inside(self.start))
        self.assertTrue(self.closed_interval.is_inside(self.mid))
        self.assertTrue(self.closed_interval.is_inside(self.end))
        self.assertFalse(self.closed_interval.is_inside(self.start - 1))
        self.assertTrue(self.closed_interval.is_inside(self.start + 1))
        self.assertTrue(self.closed_interval.is_inside(self.end - 1))
        self.assertFalse(self.closed_interval.is_inside(self.end + 1))

    def test_is_inside_produces_correct_results_opened_interval(self):
        self.assertFalse(self.opened_interval.is_inside(self.start))
        self.assertTrue(self.opened_interval.is_inside(5))
        self.assertFalse(self.opened_interval.is_inside(self.end))
        self.assertFalse(self.opened_interval.is_inside(self.start - 1))
        self.assertTrue(self.opened_interval.is_inside(self.start + 1))
        self.assertTrue(self.opened_interval.is_inside(self.end - 1))
        self.assertFalse(self.opened_interval.is_inside(self.end + 1))

    def test_is_inside_produces_correct_results_opened_interval_start(self):
        self.assertFalse(self.opened_interval_start.is_inside(self.start))
        self.assertTrue(self.opened_interval_start.is_inside(self.mid))
        self.assertTrue(self.opened_interval_start.is_inside(self.end))
        self.assertFalse(self.opened_interval_start.is_inside(self.start - 1))
        self.assertTrue(self.opened_interval_start.is_inside(self.start + 1))
        self.assertTrue(self.opened_interval_start.is_inside(self.end - 1))
        self.assertFalse(self.opened_interval_start.is_inside(self.end + 1))

    def test_is_inside_produces_correct_results_opened_interval_end(self):
        self.assertTrue(self.opened_interval_end.is_inside(self.start))
        self.assertTrue(self.opened_interval_end.is_inside(self.mid))
        self.assertFalse(self.opened_interval_end.is_inside(self.end))
        self.assertFalse(self.opened_interval_end.is_inside(self.start - 1))
        self.assertTrue(self.opened_interval_end.is_inside(self.start + 1))
        self.assertTrue(self.opened_interval_end.is_inside(self.end - 1))
        self.assertFalse(self.opened_interval_end.is_inside(self.end + 1))

    def test_text_output_str_repr(self):
        expected = '[[1, 10], (1, 10), (1, 10], [1, 10)]'
        resulted = [result for result in self.test_instances_list]
        self.assertEqual(expected, str(resulted))


if __name__ == '__main__':
    unittest.main()

# closed_interval = Interval(1, 10)
#
# print(closed_interval.is_inside(1) is True)
# print(closed_interval.is_inside(5) is True)
# print(closed_interval.is_inside(10) is True)
#
# print(closed_interval.stringify() == '[1, 10]')
#
#
# closed_interval = Interval(1, 10, start_opened=True, end_opened=True)
#
# print(closed_interval.is_inside(1) is False)
# print(closed_interval.is_inside(5) is True)
# print(closed_interval.is_inside(10) is False)
#
# print(closed_interval.stringify() == '(1, 10)')
#
# half_opened_interval = Interval(1, 10, start_opened=False, end_opened=True)
#
# print(half_opened_interval.is_inside(1) is True)
# print(half_opened_interval.is_inside(5) is True)
# print(half_opened_interval.is_inside(10) is False)
#
# print(half_opened_interval.stringify() == '[1, 10)')
#
# half_opened_interval = Interval(1, 10, start_opened=True, end_opened=False)
#
# print(half_opened_interval.is_inside(1) is False)
# print(half_opened_interval.is_inside(5) is True)
# print(half_opened_interval.is_inside(10) is True)
#
# print(half_opened_interval.stringify() == '(1, 10]')
