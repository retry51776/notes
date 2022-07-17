# Test

> orgranize by same subject tests into single file

# unittest
## modules
    - TestCase
    - IsolatedAsyncioTestCase
    - TestLoader
    - TestResult

```

class SomeTest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    def setUp():
        pass
    def test():
        pass
    def tearDown():
        pass

```

## Command-Line Interface
```
python -m unittest discover -p '*_test.py

```

# mock

> mock can implement through 3 ways
>   decorator
>   object
>   context manager

```

mock
    patch
    Mock // Class
        - return_value // single return value always same
        - side_effect = [1, 2, 3] // return different values 
        - mock_calls
        - called
        - call_count
        - call_args.args & call_args.kwargs
        - assert_called_once_with(123)
        - method_calls
        - mock_calls

    MagicMock // method
        - return_value
```
## Python Script
```
assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(x)
assertFalse(x)
assertIs(a, b)
assertIsNot(a, b)
assertIsNone(x)
assertIsNotNone(x)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertNotIsInstance(a, b)

// @path takes string
@patch("package_name.attribute_name")
def test(xxx_atr_mock)

// @path takes class object
import abc
import efg
@patch.object(efg, 'attribute_name')
@patch.object(abc, 'attribute_name')
def test(self, _abc, _efg):
    xxx_atr_mock.return_value = 123

#        package_name attribute  
with patch('employee.requesets.get') as mocked_get:
    mocked_get.return_value.ok = True

```

## Test Doubles
- Dummy Object
- Fake Data
- Mocks
  - Test Stub (return value)
  - Test Spy (conditionally have different behavior)
  - Mock Obj (event trigger)


# pytest
```
import pytest
@pytest.fixture
def xxx():
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock
```