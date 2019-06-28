import unittest
import pandas as pd


def get_min(df):
    return df.min()


def get_max(df):
    return df.max()


def get_mean(df):
    return df.mean()


class TestTimeMethods(unittest.TestCase):
    def test_get_min(self):
        d = {'col1': [1, 0, 2, 9, 8, 5], 'col2': [10, 0, -1, 1, -4, 6]}
        df = pd.DataFrame(data=d)
        self.assertEqual(get_min(df["col1"]), 0)
        self.assertEqual(get_min(df["col2"]), -4)

    def test_get_mean(self):
        d = {'col1': [1, 2, 3, 4, 5], 'col2': [10, 0, -1, 1, -4]}
        df = pd.DataFrame(data=d)
        self.assertEqual(get_mean(df["col1"]), 3)
        self.assertEqual(get_mean(df["col1"]), 3)

    def test_get_max(self):
        d = {'col1': [1, 0, 2, 9, 8, 5], 'col2': [10, 0, -1, 1, -4, 6]}
        df = pd.DataFrame(data=d)
        self.assertEqual(get_max(df["col1"]), 9)
        self.assertEqual(get_max(df["col2"]), 10)


if __name__ == '__main__':
    unittest.main()
