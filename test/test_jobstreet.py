import unittest
import jobstreet as jb
import scraper

class TestCaseGetJobStreetUrl(unittest.TestCase):
    def test_getJobStreetUrl_given_keyword_manager_expect_url_with_manager(self):
        self.assertEqual("https://www.jobstreet.com.my/en/job-search/job-vacancy.php?ojs=10&key=manager", jb.getJobStreetUrl("manager"))

    def test_getJobStreetUrl_given_keyword_manager_expect_url_with_software_engineer(self):
        self.assertEqual("https://www.jobstreet.com.my/en/job-search/job-vacancy.php?ojs=10&key=software+engineer", jb.getJobStreetUrl("software engineer"))


class TestCaseGetNextPageUrl(unittest.TestCase):
    def test_getNextPageUrl_given_current_page_is_2_expect_url_correct(self):
        self.assertEqual("https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software+Engineer&area=1&option=1&job-source=1,64&classified=1&job-posted=0&sort=2&order=0&pg=3&src=16", jb.getNextPageUrl(scraper.getBeautifulSoupInHtml(jb.getJobStreetUrl("Software Engineer")), 2))

    def test_getNextPageUrl_given_invalid_current_page_expect_exception(self):
        try:
            self.assertEqual("https://www.jobstreet.com.my/en/job-search/job-vacancy.php?key=Software+Engineer&area=1&option=1&job-source=1,64&classified=1&job-posted=0&sort=2&order=0&pg=81&src=16", jb.getNextPageUrl(scraper.getBeautifulSoupInHtml(jb.getJobStreetUrl("Software Engineer")), 80))

        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
