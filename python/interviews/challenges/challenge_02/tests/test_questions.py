import json
import os.path
import unittest
from question_2.simple_linear_regr_utils import generate_data
from question_3.utils.model_tools import get_prediction
from question_4.setup_package.challenge02package.utils import benchmark, simple_linear_regr
import glob

class Testing(unittest.TestCase):
    def test_q1(self):
        test_val = os.path.exists('./question_1/README.md')
        self.assertTrue(test_val)

    def test_q2(self):
        X_train, y_train, X_test, y_test = generate_data()
        test_val = X_test[0][0]
        self.assertIsInstance(test_val, (float, int))

    def test_q3(self):
        with open('./question_3/utils/artifacts/regression_model_v1.json', 'r') as _f:
            loaded_model = json.load(_f)
        data = [1]
        pred = get_prediction(model=loaded_model, input_data=data)

        val = list(pred.values())[0]
        self.assertIsInstance(val, (float, int))

    def test_q4(self):
        test_val = glob.glob('./question_4/setup_package/packages/challenge02package-*-py3-none-any.whl')
        self.assertTrue(test_val)

    def test_q4_1(self):
        simple_linear_regr.make_model()

if __name__ == '__main__':
    unittest.main()