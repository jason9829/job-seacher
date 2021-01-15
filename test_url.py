import unittest
import url


class TestCaseChangeUrlQueryValue(unittest.TestCase):
    def test_changeUrlQueryValue_jobstreet_example_url_change_pg_from_3_to_5_expect_changed_correctly(self):
        urlSample = "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software+Engineer&area=1&option=1&job-source=1,64&classified=1&job-posted=0&sort=2&order=0&pg=3&src=16"
        # Change page number from 3 to 5
        expectedUrl = "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software+Engineer&area=1&option=1&job-source=1,64&classified=1&job-posted=0&sort=2&order=0&pg=5&src=16"
        self.assertEqual(expectedUrl, url.changeUrlQueryValue(urlSample, 'pg', '5'))

    def test_changeUrlQueryValue_jobstreet_example_change_area_from_1_to_10000_expect_changed_correctly(self):
        urlSample = "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software+Engineer&area=1&option=1&job-source=1,64&classified=1&job-posted=0&sort=2&order=0&pg=3&src=16"
        # Change area number from 1 to 10000
        expectedUrl = "https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software+Engineer&area=10000&option=1&job-source=1,64&classified=1&job-posted=0&sort=2&order=0&pg=3&src=16"
        self.assertEqual(expectedUrl, url.changeUrlQueryValue(urlSample, 'area', '10000'))

if __name__ == '__main__':
    unittest.main()
