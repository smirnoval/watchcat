import unittest
from watchcat import Watchcat
import os


class FindFilesTests(unittest.TestCase):

    def test_find_one_file(self):
        w = Watchcat(False, 'test_files/1.txt')
        self.assertEqual(1, len(w.files))

    def test_find_files_in_dir(self):
        w = Watchcat(False, 'test_files/1')
        self.assertEqual(5, len(w.files))

    def test_find_all_files(self):
        w = Watchcat(False, 'test_files/1', 'test_files/1.txt', 'test_files/2')
        self.assertEqual(8, len(w.files))


class FindChangesTests(unittest.TestCase):

    def test_find_changes_in_file(self):
        w = Watchcat(False, 'test_files/1.txt')
        w.watch_changes()
        test_value = w.mod_times[w.files[0]]
        text = 'new_text_for_changes'
        with open(os.path.abspath(w.files[0]), 'w') as f:
            f.write(text)
        w.watch_changes()
        self.assertNotEqual(test_value, w.mod_times[w.files[0]])


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FindFilesTests))
    suite.addTest(unittest.makeSuite(FindChangesTests))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
