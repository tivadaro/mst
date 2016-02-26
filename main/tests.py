from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 2 > 1.
        """
        if 2 > 1:
            return True