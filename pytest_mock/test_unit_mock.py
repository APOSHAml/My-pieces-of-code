import datetime
from unittest import TestCase
from unittest.mock import MagicMock, patch

import portion
from freezegun import freeze_time

import functions_mock
from functions_mock import Calculator, discount_calculator, search_db

# class TestCalculatorNoMock(TestCase):
#     def setUp(self):
#         self.calc = Calculator()

#     def test_sum_no_mock(self):
#         answer = self.calc.sum(2, 4)
#         self.assertEqual(answer, 6)


class TestCalculator1(TestCase):
    @patch("functions_mock.Calculator.sum", return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)


class TestBlog(TestCase):
    @patch("functions_mock.Blog")
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "Test Title",
                "body": "Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy/ lies a small unregarded yellow sun.",
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # Additional assertions
        assert MockBlog is functions_mock.Blog  # The mock is equivalent to the original

        assert MockBlog.called  # The mock wasP called

        blog.posts.assert_called_with()  # We called the posts method with no arguments

        blog.posts.assert_called_once_with()  # We called the posts method once with no arguments

        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments

        blog.reset_mock()  # Reset the mock object

        blog.posts.assert_not_called()  # After resetting, posts has not been called.


def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b


class TestCalculator(TestCase):
    @patch("functions_mock.Calculator.sum", side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(7, 3), 10)


class DatabaseSearchTest(TestCase):
    @patch("functions_mock.create_engine")
    def test(self, create_engine_mock):

        con_mock = MagicMock()
        con_mock.execute.return_value.fetchall.return_value = [
            (1, "bizibaza-api", 2),
            (2, "asdf", 3),
        ]

        engine_mock = MagicMock()
        engine_mock.connect.return_value.__enter__.return_value = (
            con_mock  # __enter__ это из-за контекст-менеджера тут(with)
        )

        create_engine_mock.return_value = engine_mock

        res = search_db("bizi")

        self.assertEqual(2, len(res))
        self.assertEqual("bizibaza-api", res[0].name)

        assert 5.05 in portion.open(5.00, 5.10)


class DiscountCalculatorTest(TestCase):
    @freeze_time("2020-04-28")
    def test_discount_yes(self):
        self.assertEqual(
            80.0,
            discount_calculator(
                value=100,
                due_date=datetime.date(year=2020, month=4, day=28),
                days=3,
                discount=0.2,
            ),
        )
