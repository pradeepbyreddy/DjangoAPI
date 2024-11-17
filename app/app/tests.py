from django.test import SimpleTestCase

from  app import addition

class Test_addition(SimpleTestCase):
    def testing_addition(self):
        res = addition.int_addition(3,4)
        self.assertEqual(res,7)