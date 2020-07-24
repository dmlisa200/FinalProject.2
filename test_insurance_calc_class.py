import unittest
from insurance_calc_class import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = self.calculator.Calculator()

    def tearDown(self):
        del self.calculator

    def test_income_value(self):
        self.assertEqual(self.calculator.income_value, 150000)

    def test_other_inc_value(self):
        self.assertEqual(self.calculator.other_inc_value, 50000)

    def test_answer(self):
        self.assertEqual(self.calculator.answer, 'Y')

    def test_college_cost(self):
        self.assertEqual(self.calculator.college_cost, 60000)

    def test_debt(self):
        self.assertEqual(self.calculator.debt, 350000)

    def test_savings(self):
        self.assertEqual(self.calculator.savings, 50000)

    def test_retirement(self):
        self.assertEqual(self.calculator.retirement, 400000)

    def test_present_amount(self):
        self.assertEqual(self.calculator.present_amount, 100000)





if __name__ == '__main__':
    unittest.main()
