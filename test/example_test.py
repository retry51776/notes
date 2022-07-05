import unittest
from platform import python_version
#from packaging import version
#rom typing import List

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> unittest.TestCase:
        cls.a = 1
        return cls

    def setUp(self) -> None:
        self.test_a = 2
        print('runs before every test')
        return

    def tearDown(self):
        print('close stuffs.')
        return

    def test_upper(self):
        print('self.a', self.a, 'test_a', self.test_a)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @unittest.skipIf(
        python_version()[0] == "3",
        "not supported in this python version"
    )
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()