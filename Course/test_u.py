# import unittest
#
#
# class Product:
#     def __init__(self, name, price, count):
#         self.name = name
#         self.price = price
#         self.count = count
#
#
# class Cart:
#     def __init__(self, products=None):
#         self.products = products if products is not None else []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def _get_discount_rate(self, count):
#         if count > 20:
#             return 0.50
#         elif count >= 20:
#             return 0.30
#         elif count >= 10:
#             return 0.20
#         elif count >= 7:
#             return 0.10
#         elif count >= 5:
#             return 0.05
#         else:
#             return 0.0
#
#     def get_total_price(self):
#         total_price = 0
#         for product in self.products:
#             discount = self._get_discount_rate(product.count)
#             total_price += product.price * product.count * (1 - discount)
#         return total_price
#
#
# class CartTest(unittest.TestCase):
#     def setUp(self):
#         self.cart = Cart()
#
#     def test_empty_cart(self):
#         self.assertEqual(self.cart.get_total_price(), 0.0)
#
#     def test_get_total_price(self):
#         products = [Product('p1', 10, 2)]
#         self.cart = Cart(products)
#         self.assertEqual(self.cart.get_total_price(), 20.0)
#
#         products = [Product('p1', 10, 5)]
#         self.cart = Cart(products)
#         self.assertEqual(self.cart.get_total_price(), 47.5)
#
#         products = [Product('p1', 10, 7)]
#         self.cart = Cart(products)
#         self.assertEqual(self.cart.get_total_price(), 63.0)
#
#         products = [Product('p1', 10, 10)]
#         self.cart = Cart(products)
#         self.assertEqual(self.cart.get_total_price(), 80.0)
#
#         products = [Product('p1', 10, 20)]
#         self.cart = Cart(products)
#         self.assertEqual(self.cart.get_total_price(), 140.0)
#
#         products = [Product('p1', 10, 21)]
#         self.cart = Cart(products)
#         self.assertEqual(self.cart.get_total_price(), 105.0)
# import unittest
#
#
# def divide(num_1, num_2):
#     return float(num_1) / num_2
#
#
# class TestDivideFunction(unittest.TestCase):
#
#     def test_divide_positive_numbers(self):
#         self.assertEqual(divide(10, 2), 5.0)
#         self.assertEqual(divide(7, 3), 7.0 / 3)
#
#     def test_divide_negative_numbers(self):
#         self.assertEqual(divide(-10, 2), -5.0)
#         self.assertEqual(divide(10, -2), -5.0)
#         self.assertEqual(divide(-10, -2), 5.0)
#
#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(10, 0)
#
#     def test_divide_zero_by_number(self):
#         self.assertEqual(divide(0, 5), 0.0)
#
#     def test_divide_float_result(self):
#         self.assertEqual(divide(1, 2), 0.5)
#         self.assertEqual(divide(5, 2), 2.5)
#
#     def test_divide_large_numbers(self):
#         self.assertEqual(divide(1000000, 2), 500000.0)
#         self.assertEqual(divide(1, 1000000), 0.000001)
# import unittest
# import math
#
#
# def quadratic_equation(a, b, c):
#     if a == 0:
#         raise ValueError("Coefficient 'a' cannot be zero")
#
#     discriminant = b ** 2 - 4 * a * c
#
#     if discriminant < 0:
#         return None
#     elif discriminant == 0:
#         return -b / (2 * a)
#     else:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return (root1, root2)
#
#
# class QuadraticEquationTest(unittest.TestCase):
#
#     def test_discriminant_less_than_zero(self):
#         result = quadratic_equation(1, 2, 5)
#         self.assertIsNone(result)
#
#     def test_discriminant_greater_than_zero(self):
#         result = quadratic_equation(1, -3, 2)
#         expected_roots = (2.0, 1.0)
#         self.assertEqual(result, expected_roots)
#
#     def test_discriminant_equal_to_zero(self):
#         result = quadratic_equation(1, -4, 4)
#         self.assertEqual(result, 2.0)
#
#     def test_another_positive_discriminant(self):
#         result = quadratic_equation(2, -7, 3)
#         expected_roots = (3.0, 0.5)
#         self.assertEqual(result, expected_roots)
#
#     def test_another_zero_discriminant(self):
#         result = quadratic_equation(4, 4, 1)
#         self.assertEqual(result, -0.5)
#
#     def test_zero_a_coefficient(self):
#         with self.assertRaises(ValueError):
#             quadratic_equation(0, 2, 3)
# import unittest
# import math
#

# class TriangleNotValidArgumentException(Exception):
#     pass
#
#
# class TriangleNotExistException(Exception):
#     pass
#
#
# class Triangle:
#     def __init__(self, sides):
#         self._validate_arguments(sides)
#         self.sides = sides
#         self._validate_triangle()
#
#     def _validate_arguments(self, sides):
#         if not isinstance(sides, (list, tuple)) or len(sides) != 3:
#             raise TriangleNotValidArgumentException("Not valid arguments")
#
#         for side in sides:
#             if not isinstance(side, (int, float)):
#                 raise TriangleNotValidArgumentException("Not valid arguments")
#
#     def _validate_triangle(self):
#         a, b, c = self.sides
#         if a <= 0 or b <= 0 or c <= 0:
#             raise TriangleNotExistException("Can`t create triangle with this arguments")
#         if (a + b <= c) or (a + c <= b) or (b + c <= a):
#             raise TriangleNotExistException("Can`t create triangle with this arguments")
#
#     def get_area(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         return round(area, 2)
#
#
# class TriangleTest(unittest.TestCase):
#     valid_test_data = [
#         ((3, 4, 5), 6.0),
#         ((10, 10, 10), 43.30),
#         ((6, 7, 8), 20.33),
#         ((7, 7, 7), 21.21),
#         ((50, 50, 75), 1240.19),
#         ((37, 43, 22), 406.99),
#         ((26, 25, 3), 36.0),
#         ((30, 29, 5), 72.0),
#         ((87, 55, 34), 396.0),
#         ((120, 109, 13), 396.0),
#         ((123, 122, 5), 300.0)
#     ]
#
#     not_valid_triangle = [
#         (1, 2, 3),
#         (1, 1, 2),
#         (7, 7, 15),
#         (100, 7, 90),
#         (17, 18, 35),
#         (127, 17, 33),
#         (145, 166, 700),
#         (1000, 2000, 1),
#         (717, 17, 7),
#         (0, 7, 7),
#         (-7, 7, 7)
#     ]
#
#     not_valid_arguments = [
#         ('3', 4, 5),
#         ('a', 2, 3),
#         (7, "str", 7),
#         ('1', '1', '1'),
#         'string',
#         (7, 2),
#         (7, 7, 7, 7),
#         'str',
#         10,
#         ('a', 'str', 7)
#     ]
#
#     def test_valid_triangles(self):
#         for sides, expected_area in self.valid_test_data:
#             with self.subTest(sides=sides):
#                 triangle = Triangle(sides)
#                 self.assertAlmostEqual(triangle.get_area(), expected_area, places=1)
#
#     def test_not_valid_triangle(self):
#         for sides in self.not_valid_triangle:
#             with self.subTest(sides=sides):
#                 with self.assertRaises(TriangleNotExistException):
#                     Triangle(sides)
#
#     def test_not_valid_arguments(self):
#         for sides in self.not_valid_arguments:
#             with self.subTest(sides=sides):
#                 with self.assertRaises(TriangleNotValidArgumentException):
#                     Triangle(sides)
# import unittest
#
#
# class Worker:
#     def __init__(self, name, salary=0):
#         if salary < 0:
#             raise ValueError("Salary cannot be negative")
#         self.name = name
#         self.salary = salary
#
#     def get_tax_value(self):
#         tax = 0.0
#         salary = self.salary
#
#         if salary <= 1000:
#             return 0.0
#
#         brackets = [
#             (1000, 0.0),
#             (2000, 0.1),
#             (2000, 0.15),
#             (5000, 0.21),
#             (10000, 0.3),
#             (30000, 0.4),
#             (float('inf'), 0.47)
#         ]
#
#         lower_bound = 0
#         for bracket in brackets:
#             bracket_size, rate = bracket
#             upper_bound = lower_bound + bracket_size
#
#             if salary > lower_bound:
#                 taxable_amount = min(salary, upper_bound) - lower_bound
#                 tax += taxable_amount * rate
#                 lower_bound = upper_bound
#             else:
#                 break
#
#         return tax
#
#
# class WorkerTest(unittest.TestCase):
#     def setUp(self):
#         self.worker1 = Worker("John", 500)
#         self.worker2 = Worker("Alice", 2500)
#         self.worker3 = Worker("Bob", 7500)
#         self.worker4 = Worker("Charlie", 15000)
#         self.worker5 = Worker("Diana", 35000)
#         self.worker6 = Worker("Eve", 75000)
#
#     def tearDown(self):
#         del self.worker1
#         del self.worker2
#         del self.worker3
#         del self.worker4
#         del self.worker5
#         del self.worker6
#
#     def test_negative_salary(self):
#         try:
#             Worker("Test", -100)
#             self.fail("Expected ValueError was not raised")
#         except ValueError:
#             pass
#
#     def test_zero_salary_tax(self):
#         worker = Worker("Zero", 0)
#         self.assertEqual(worker.get_tax_value(), 0.0)
#
#     def test_low_income_tax(self):
#         self.assertEqual(self.worker1.get_tax_value(), 0.0)
#
#     def test_medium_income_tax(self):
#         self.assertEqual(self.worker2.get_tax_value(), 150.0)
#
#     def test_high_medium_income_tax(self):
#         self.assertEqual(self.worker3.get_tax_value(), 1025.0)
#
#     def test_high_income_tax(self):
#         self.assertEqual(self.worker4.get_tax_value(), 3050.0)
#
#     def test_very_high_income_tax(self):
#         self.assertEqual(self.worker5.get_tax_value(), 10550.0)
#
#     def test_extreme_income_tax(self):
#         self.assertEqual(self.worker6.get_tax_value(), 28300.0)
#
#     def test_default_salary(self):
#         worker = Worker("Vasia")
#         self.assertEqual(worker.get_tax_value(), 0.0)
# import unittest
#
#
# class Worker:
#     def __init__(self, name, salary=0):
#         if salary < 0:
#             raise ValueError("Salary cannot be negative")
#         self.name = name
#         self.salary = salary
#
#     def get_tax_value(self):
#         tax = 0.0
#         salary = self.salary
#
#         if salary <= 1000:
#             return 0.0
#
#         brackets = [
#             (1000, 0.0),
#             (2000, 0.1),
#             (2000, 0.15),
#             (5000, 0.21),
#             (10000, 0.3),
#             (30000, 0.4),
#             (float('inf'), 0.47)
#         ]
#
#         lower_bound = 0
#         for bracket in brackets:
#             bracket_size, rate = bracket
#             upper_bound = lower_bound + bracket_size
#
#             if salary > lower_bound:
#                 taxable_amount = min(salary, upper_bound) - lower_bound
#                 tax += taxable_amount * rate
#                 lower_bound = upper_bound
#             else:
#                 break
#
#         return tax
#
#
# class WorkerTest(unittest.TestCase):
#     def setUp(self):
#         self.worker1 = Worker("John", 500)
#         self.worker2 = Worker("Alice", 2500)
#         self.worker3 = Worker("Bob", 7500)
#         self.worker4 = Worker("Charlie", 15000)
#         self.worker5 = Worker("Diana", 35000)
#         self.worker6 = Worker("Eve", 75000)
#
#     def tearDown(self):
#         del self.worker1
#         del self.worker2
#         del self.worker3
#         del self.worker4
#         del self.worker5
#         del self.worker6
#
#     def test_negative_salary(self):
#         try:
#             Worker("Test", -100)
#             self.fail("Expected ValueError was not raised")
#         except ValueError:
#             pass
#
#     def test_zero_salary_tax(self):
#         worker = Worker("Zero", 0)
#         self.assertEqual(worker.get_tax_value(), 0.0)
#
#     def test_low_income_tax(self):
#         self.assertEqual(self.worker1.get_tax_value(), 0.0)
#
#     def test_medium_income_tax(self):
#         self.assertEqual(self.worker2.get_tax_value(), 150.0)
#
#     def test_high_medium_income_tax(self):
#         self.assertEqual(self.worker3.get_tax_value(), 1025.0)
#
#     def test_high_income_tax(self):
#         self.assertEqual(self.worker4.get_tax_value(), 3050.0)
#
#     def test_very_high_income_tax(self):
#         self.assertEqual(self.worker5.get_tax_value(), 10550.0)
#
#     def test_extreme_income_tax(self):
#         self.assertEqual(self.worker6.get_tax_value(), 28300.0)
#
#     def test_default_salary(self):
#         worker = Worker("Vasia")
#         self.assertEqual(worker.get_tax_value(), 0.0)
#
#     @unittest.expectedFailure
#     def test_expected_failure(self):
#         self.assertEqual(1, 2)
import unittest
from unittest.mock import mock_open, patch


def file_parser(file_path, find_str, replace_str=None):
    if replace_str is None:
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count(find_str)
            return f"Found {count} strings"
    else:
        with open(file_path, 'r') as file:
            content = file.read()

        count = content.count(find_str)
        new_content = content.replace(find_str, replace_str)

        with open(file_path, 'w') as file:
            file.write(new_content)

        return f"Replaced {count} strings"


class ParserTest(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data="hello world hello"))
    def test_file_parser_count_mode(self):
        result = file_parser("test.txt", "hello")
        self.assertEqual(result, "Found 2 strings")

    @patch('builtins.open', mock_open(read_data="hello world hello"))
    def test_file_parser_count_mode_no_match(self):
        result = file_parser("test.txt", "python")
        self.assertEqual(result, "Found 0 strings")

    def test_file_parser_replace_mode(self):
        with patch('builtins.open', mock_open(read_data="hello world hello")) as mock_file:
            result = file_parser("test.txt", "hello", "hi")
            self.assertEqual(result, "Replaced 2 strings")
            mock_file().write.assert_called_once()

    def test_file_parser_replace_mode_no_match(self):
        with patch('builtins.open', mock_open(read_data="hello world hello")) as mock_file:
            result = file_parser("test.txt", "python", "java")
            self.assertEqual(result, "Replaced 0 strings")
            mock_file().write.assert_called_once()

    @patch('builtins.open', mock_open(read_data="x x x x x x x x"))
    def test_file_parser_example_count(self):
        result = file_parser("file.txt", 'x')
        self.assertEqual(result, "Found 8 strings")

    def test_file_parser_example_replace(self):
        with patch('builtins.open', mock_open(read_data="x x x x x x x x")) as mock_file:
            result = file_parser("file.txt", 'x', 'o')
            self.assertEqual(result, "Replaced 8 strings")