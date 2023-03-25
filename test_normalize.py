import unittest

from normalize_md import add_cr, remove_cr, normalize_string


class TestNormalize(unittest.TestCase):

    def test_remove_cr(self):
        self.assertEqual(
            remove_cr("Hello\nworld\n\n!"),
            "Hello world\n\n!"
        )

    def test_add_cr(self):
        self.assertEqual(
            add_cr("Hello world! Good bye world...", max_line_length=15),
            "Hello world!\nGood bye\nworld..."
        )

    def test_normalize_string(self):
        self.assertEqual(
            normalize_string("Hello\nworld\n\n!\n\nHello world! Good bye world...", max_line_length=15),
            "Hello world\n\n!\n\nHello world!\nGood bye\nworld..."
        )



if __name__ == '__main__':
    unittest.main()
