import unittest
from platform import python_version
#from packaging import version

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('runs before every test')
        return

    def tearDown(self):
        print('close stuffs.')
        return

    def test_upper(self):
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