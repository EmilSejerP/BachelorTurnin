import unittest
from os import path
import pandas as pd


class UnitTests(unittest.TestCase):

        # Testing for the existing of the heart data set
        def test_df_import(self):
            self.assertTrue(path.exists('Datasets/heart.csv'))

        #Testing if nan exists in the data set
        def test_if_nan_exist(self):
            df = pd.read_csv(r"Datasets/heart.csv", low_memory=False)
            for i in df.columns:
                self.assertFalse(df[i].isnull().values.any())

        #
        def test_if_non_numeric_exists(self):
            df = pd.read_csv(r"Datasets/heart.csv", low_memory=False)
            for i in df.columns:
                self.assertEqual(str(df[i].dtypes), 'int64' or 'float64')

        # Testing for the existing of the parson heatmap
        def test_mlr(self):
            self.assertTrue(path.exists('assets/parson_heatmap.png'))


if __name__ == 'main':
    unittest.main()
