# Import Module --------------------------------------------------------------#
import unittest


# Class Definition to Test ---------------------------------------------------#
class TestClass1:
    pass


class TestClass2:
    pass


# Test Suite Class Definition ------------------------------------------------#
class TestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEqual(self):
        """
        actual == expected
        """
        actual = 1
        expected = 1
        self.assertEqual(actual, expected)

    def testNotEqual(self):
        """
        actual != expected
        """
        actual = 1
        expected = 2
        self.assertNotEqual(actual, expected)

    def testTrue(self):
        """
        bool(value) is True
        """
        value = True
        self.assertTrue(value)

    def testFalse(self):
        """
        bool(value) is False
        """
        value = False
        self.assertFalse(value)

    def testIs(self):
        """
        value1 is value2
        """
        value1 = TestClass1()
        value2 = value1
        self.assertIs(value1, value2)

    def testIsNot(self):
        """
        value1 is not value2
        """
        value1 = TestClass1()
        value2 = TestClass2()
        self.assertIsNot(value1, value2)

    def testIsNone(self):
        """
        value is None
        """
        value = None
        self.assertIsNone(value)

    def testIsNotNone(self):
        """
        value is not None
        """
        value = 'test'
        self.assertIsNotNone(value)

    def testIn(self):
        """
        value1 in value2
        """
        value1 = 1
        value2 = range(6)
        self.assertIn(value1, value2)

    def testNotIn(self):
        """
        value1 not in value2
        """
        value1 = 7
        value2 = range(6)
        self.assertNotIn(value1, value2)

    def testIsInstance(self):
        """
        isinstance(value1, value2)
        """
        value1 = TestClass1()
        value2 = TestClass1
        self.assertIsInstance(value1, value2)

    def testNotIsInstance(self):
        """
        not isinstance(value1, value2)
        """
        value1 = TestClass1()
        value2 = TestClass2
        self.assertNotIsInstance(value1, value2)

    def testAlmostEqual(self):
        """
        round(value1 - value2, 7) == 0
        """
        value1 = 1.23456789
        value2 = 1.23456788
        self.assertAlmostEqual(value1, value2)

    def testNotAlmostEqual(self):
        """
        round(value1 - value2, 7) != 0
        """
        value1 = 3.14
        value2 = 3.15
        self.assertNotAlmostEqual(value1, value2)

    def testGreater(self):
        """
        value1 > value2
        """
        value1 = 5
        value2 = 3
        self.assertGreater(value1, value2)

    def testGreaterEqual(self):
        """
        value1 >= value2
        """
        value1 = 5
        value2 = 3
        self.assertGreaterEqual(value1, value2)

    def testLess(self):
        """
        value1 < value2
        """
        value1 = 2
        value2 = 4
        self.assertLess(value1, value2)

    def testLessEqual(self):
        """
        value1 <= value2
        """
        value1 = 2
        value2 = 4
        self.assertLessEqual(value1, value2)

    def testRegex(self):
        """
        value2.search(value1)
        """
        value1 = 'test'
        value2 = 'e'
        self.assertRegex(value1, value2)

    def testNotRegex(self):
        """
        not value2.search(value1)
        """
        value1 = 'test'
        value2 = 'a'
        self.assertNotRegex(value1, value2)

    def testCountEqual(self):
        """
        value1 and value2 have the same elements in the same number,
          regardless of their order.
        """
        value1 = 'abcde'
        value2 = 'ecbda'
        self.assertCountEqual(value1, value2)

    def testMultiLineEqual(self):
        str1 = 'T\
                E\
                S\
                T'
        str2 = 'T\
                E\
                S\
                T'
        self.assertMultiLineEqual(str1, str2)

    def testSuquenceEqual(self):
        seq1 = range(6)
        seq2 = range(6)
        self.assertSequenceEqual(seq1, seq2)

    def testListEqual(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        self.assertListEqual(list1, list2)

    def testTupleEqual(self):
        tuple1 = (1, 2, 3)
        tuple2 = (1, 2, 3)
        self.assertTupleEqual(tuple1, tuple2)

    def testSetEqual(self):
        set1 = set([1, 2, 3])
        set2 = set([3, 2, 1])
        self.assertSetEqual(set1, set2)

    def testDictEqual(self):
        dict1 = {"key1": "value1", "key2": "value2"}
        dict2 = {"key2": "value2", "key1": "value1"}
        self.assertDictEqual(dict1, dict2)

# Main -----------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main()
