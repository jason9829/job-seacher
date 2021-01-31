import unittest

ROOT_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__), "..", ".."))
sys.path.insert(0, ROOT_DIR)

import src.jobstreet_common as JobStreet

class TestJobStreet(unittest.TestCase):
    def test_is_salary_given_expected_salary_string(self):
        self.assertEqual(True, JobStreet.is_salary('MYR'))
        self.assertEqual(True, JobStreet.is_salary('SGD'))
        self.assertEqual(True, JobStreet.is_salary('MYR 8000'))
        self.assertEqual(True, JobStreet.is_salary('USD 1230 - 2220'))
        self.assertEqual(True, JobStreet.is_salary('SGD 1088 - 2288 monthly'))

    def test_is_salary_given_wrong_salary_string(self): 
        self.assertEqual(False, JobStreet.is_salary('MXR'))
        self.assertEqual(False, JobStreet.is_salary('STD'))
        self.assertEqual(False, JobStreet.is_salary('$ 8000'))
        self.assertEqual(False, JobStreet.is_salary('$$ 1230 - 2220'))
        self.assertEqual(False, JobStreet.is_salary('XXX 1088 - 2288 monthly'))


if __name__ == '__main__':
    unittest.main()