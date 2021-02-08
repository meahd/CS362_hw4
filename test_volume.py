import unittest
import volume


class TestCase(unittest.TestCase):
#calcVolume
    def test1(self):
        self.assertEqual(volume.calcVol(2, 0, 2),0)
    def test2(self):
        self.assertEqual(volume.calcVol(-1, 0, 2),0)
    def test3(self):
        self.assertEqual(volume.calcVol(30.5, 10, 10),3050)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
