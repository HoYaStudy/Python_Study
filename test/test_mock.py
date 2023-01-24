from unittest import TestCase, mock

import calc

m = mock.Mock()
m.my_attribute = 7
m.my_method.return_value = 3
m.side_effect = lambda x: x % 2


class CalcTest(TestCase):
    def test_add(self):
        self.assertEqual(calc.add(m.my_attribute, 2), 9)
        m.my_method.assert_not_called()

    def test_multiply(self):
        self.assertEqual(calc.multiply(m.my_method(), 3), 9)
        m.my_method.assert_called_once()

    def test_mock(self):
        self.assertEqual(m(2), 0)
        m.assert_called_with(2)
        m.assert_called_once_with(2)

    def test_patch1(self):
        with mock.patch("calc.add") as mock_add:
            mock_add.return_value = 3
            self.assertEqual(calc.add(1, 2), 3)

    @mock.patch("calc.add")
    def test_patch2(self, mock_add):
        mock_add.return_value = 3
        self.assertEqual(calc.add(1, 2), 3)
