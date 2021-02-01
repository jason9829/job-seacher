import unittest
import os
import sys

ROOT_DIR = os.path.normpath(os.path.join(os.path.abspath(__file__), "..", ".."))
sys.path.insert(0, ROOT_DIR)

import common.file_manager as FM


class TestFileManager(unittest.TestCase):
    def test_is_path_exist_given_root_dir_expect_true(self):
        self.assertEqual(True, FM.is_path_exist(ROOT_DIR))

    def test_is_path_exist_given_invalid_dir_expect_false(self):
        self.assertEqual(False, FM.is_path_exist(os.path.join(ROOT_DIR, 'invalid')))


if __name__ == '__main__':
    unittest.main()