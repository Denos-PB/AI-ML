# test_alg.py
import io
import sys
import types
import unittest
from contextlib import redirect_stdout

import alg


class TestHigherOrderAndLambdas(unittest.TestCase):
    def test_outer_closure(self):
        f = alg.outer("Alice")
        buf = io.StringIO()
        with redirect_stdout(buf):
            f()
        self.assertIn("Hello, Alice!", buf.getvalue())

    def test_create_lambda(self):
        eq_hello = alg.create("hello")
        self.assertTrue(eq_hello("hello"))
        self.assertFalse(eq_hello("world"))


class TestAccountFactory(unittest.TestCase):
    def test_create_account_validation_password_length(self):
        with self.assertRaises(ValueError):
            alg.create_account("user", "Ab1!", ["a"])

    def test_create_account_validation_complexity(self):
        # Missing special character
        with self.assertRaises(ValueError):
            alg.create_account("user", "Abc123", ["a"])
        # Missing uppercase
        with self.assertRaises(ValueError):
            alg.create_account("user", "abc123!", ["a"])
        # Missing lowercase
        with self.assertRaises(ValueError):
            alg.create_account("user", "ABC123!", ["a"])
        # Missing digit
        with self.assertRaises(ValueError):
            alg.create_account("user", "Abcdef!", ["a"])

    def test_create_account_checker_exact_match(self):
        check = alg.create_account("bob", "A1bcde!", ["red", "blue", "green"])
        # Exact match
        self.assertTrue(check("A1bcde!", ["red", "blue", "green"]))
        # Order-insensitive match
        self.assertTrue(check("A1bcde!", ["green", "blue", "red"]))
        # Allow one mismatch
        self.assertTrue(check("A1bcde!", ["green", "blue", "black"]))
        # More than one mismatch -> False
        self.assertFalse(check("A1bcde!", ["black", "white", "yellow"]))
        # Wrong password
        self.assertFalse(check("wrong", ["red", "blue", "green"]))
        # Different lengths -> False
        self.assertFalse(check("A1bcde!", ["red", "blue"]))


class TestGenerators(unittest.TestCase):
    def test_divisor_basic(self):
        g = alg.divisor(6)
        # Divisors of 6: 1,2,3,6 then None forever
        self.assertEqual([next(g), next(g), next(g), next(g)], [1, 2, 3, 6])
        for _ in range(3):
            self.assertIsNone(next(g))

    def test_random_word_nonempty(self):
        words = ["a", "b", "c"]
        gen = alg.randomWord(words)
        # Collect a full first cycle
        first_cycle = [next(gen) for _ in range(len(words))]
        self.assertCountEqual(first_cycle, words)
        # Collect second cycle; guaranteed not equal to first if len>1
        second_cycle = [next(gen) for _ in range(len(words))]
        self.assertCountEqual(second_cycle, words)
        self.assertNotEqual(first_cycle, second_cycle)

    def test_random_word_empty(self):
        gen = alg.randomWord([])
        for _ in range(5):
            self.assertIsNone(next(gen))


class TestLoggerDecoratorAndConcat(unittest.TestCase):
    def test_logger_and_concat(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            out = alg.concat("a", "b", x="c")
        self.assertEqual(out, "abc")
        log = buf.getvalue()
        self.assertIn("Executing of function concat with arguments a, b, c...", log)


class TestPizza(unittest.TestCase):
    def test_order_counter_increments(self):
        start = getattr(alg.Pizza, "_order_counter", 0)
        p1 = alg.Pizza(["cheese"])
        p2 = alg.Pizza(["beef"])
        self.assertEqual(p1.order_number, start + 1)
        self.assertEqual(p2.order_number, start + 2)

    def test_classmethods(self):
        g = alg.Pizza.garden_feast()
        h = alg.Pizza.hawaiian()
        m = alg.Pizza.meat_festival()
        self.assertIn("spinach", g.ingredients)
        self.assertIn("pineapple", h.ingredients)
        self.assertIn("bacon", m.ingredients)


class TestEmployee(unittest.TestCase):
    def test_name_split_and_kwargs(self):
        e = alg.Employee("John Doe", role="dev", level=2)
        self.assertEqual(e.name, "John")
        self.assertEqual(e.lastname, "Doe")
        self.assertEqual(e.role, "dev")
        self.assertEqual(e.level, 2)


class TestStudentAndTestpaper(unittest.TestCase):
    def test_take_test_no_tests_then_dict(self):
        tp = alg.Testpaper("Math", ["a", "b", "c", "d"], "50%")
        s = alg.Student()
        self.assertEqual(s.tests_taken, "No tests taken")
        s.take_test(tp, ["a", "x", "c", "y"])  # 2/4 = 50% → Passed
        self.assertIsInstance(s.tests_taken, dict)
        self.assertEqual(s.tests_taken["Math"], "Passed! (50%)")

    def test_take_test_fail(self):
        tp = alg.Testpaper("Sci", ["a", "b", "c", "d"], "75%")
        s = alg.Student()
        s.take_test(tp, ["a", "b", "x", "y"])  # 2/4 = 50% → Failed
        self.assertEqual(s.tests_taken["Sci"], "Failed! (50%)")


class TestGallows(unittest.TestCase):
    def test_valid_sequence(self):
        g = alg.Gallows()
        self.assertEqual(g.play("apple"), ["apple"])
        self.assertEqual(g.play("ear"), ["apple", "ear"])
        self.assertEqual(g.play("rat"), ["apple", "ear", "rat"])

    def test_game_over_conditions(self):
        g = alg.Gallows()
        self.assertEqual(g.play(""), "game over")
        self.assertEqual(g.play("anything"), "game over")
        g.restart()
        self.assertEqual(g.play("apple"), ["apple"])
        self.assertEqual(g.play("pear"), "game over")  # 'p' != last char 'e'
        g.restart()
        self.assertEqual(g.play("apple"), ["apple"])
        self.assertEqual(g.play("apple"), "game over")  # duplicate
        self.assertEqual(g.restart(), "game restarted")


class TestLibraryDomain(unittest.TestCase):
    def setUp(self):
        self.lib = alg.Library()
        self.b1 = alg.Book("Dune", "Frank Herbert", 1965, quantity=2)
        self.b2 = alg.Book("Neuromancer", "William Gibson", 1984, quantity=1)
        self.ebo = alg.EBook("Snow Crash", "Neal Stephenson", 1992, format_type="EPUB", quantity=3)
        self.lib.add_book(self.b1)
        self.lib.add_book(self.b2)
        self.lib.add_book(self.ebo)

    def test_add_book_merges_quantities(self):
        # Adding same identity increases quantity and book_count
        prev_count = self.lib.book_count
        self.lib.add_book(alg.Book("Dune", "Frank Herbert", 1965, quantity=1))
        self.assertEqual(self.lib.find_book_by_title("Dune").quantity, 3)
        self.assertEqual(self.lib.book_count, prev_count + 1)

    def test_find_book_by_title(self):
        self.assertIsNotNone(self.lib.find_book_by_title("dune"))
        self.assertIsNone(self.lib.find_book_by_title("unknown"))

    def test_customer_borrow_and_return_by_title(self):
        c = alg.Customer("Alice")
        ok = c.borrow_book(self.lib, "Dune")
        self.assertTrue(ok)
        self.assertEqual(self.lib.find_book_by_title("Dune").quantity, 1)
        self.assertEqual(self.lib.book_count, 2 + 1 + 3 - 1)  # initial total minus one
        ok = c.return_book(self.lib, "Dune")
        self.assertTrue(ok)
        self.assertEqual(self.lib.find_book_by_title("Dune").quantity, 2)
        self.assertEqual(self.lib.book_count, 2 + 1 + 3)

    def test_customer_borrow_and_return_by_reference(self):
        c = alg.Customer("Bob")
        # Borrow by reference
        ok = c.borrow_book(self.b2)
        self.assertTrue(ok)
        self.assertEqual(self.b2.quantity, 0)
        # Returning by reference works even without Library context
        ok = c.return_book(self.b2)
        self.assertTrue(ok)
        self.assertEqual(self.b2.quantity, 1)

    def test_customer_borrow_unavailable(self):
        c = alg.Customer("Eve")
        # Borrow Neuromancer once (only 1 copy)
        self.assertTrue(c.borrow_book(self.lib, "Neuromancer"))
        # Now unavailable
        self.assertFalse(c.borrow_book(self.lib, "Neuromancer"))

    def test_customer_return_not_borrowed(self):
        c = alg.Customer("Zed")
        # Not borrowed, attempt to return by title in library context
        self.assertFalse(c.return_book(self.lib, "Dune"))
        # Not borrowed, attempt to return by reference
        self.assertFalse(c.return_book(self.b1))

    def test_customer_str(self):
        c = alg.Customer("Carol")
        s = str(c)
        self.assertIn("Carol borrowed books:", s)

    def test_ebook_display_and_str(self):
        # Ensure overridden behavior doesn't crash; content not strictly asserted beyond inclusion
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.ebo.display_info()
        self.assertIn("EBook:", buf.getvalue())
        s = str(self.ebo)
        self.assertIn("Format:", s)


class TestLibraryManagementSystem(unittest.TestCase):
    def test_register_and_lookup(self):
        lms = alg.LibraryManagementSystem()
        c1 = alg.Customer("Ana")
        lms.register_customer(c1)
        # Duplicate registration prints a message; just verify it doesn’t add twice
        lms.register_customer(alg.Customer("Ana"))
        self.assertEqual(len(lms.customers), 1)
        # Lookup by object and by name
        self.assertIs(lms._get_customer(c1), c1)
        self.assertIs(lms._get_customer("Ana"), c1)
        self.assertIsNone(lms._get_customer("Unknown"))

    def test_display_functions_do_not_crash(self):
        lms = alg.LibraryManagementSystem()
        buf = io.StringIO()
        with redirect_stdout(buf):
            lms.display_all_books()
            lms.display_customer_books("NoOne")
        output = buf.getvalue()
        self.assertIn("Library has no books.", output)
        self.assertIn("Customer 'NoOne' not found.", output)


if __name__ == "__main__":
    unittest.main()