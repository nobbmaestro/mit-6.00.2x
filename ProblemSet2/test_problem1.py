# Problem Set 2, Problem 1

import unittest
import random

from ProblemSet2 import RectangularRoom, Position

class TestProblem1(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_init(self):
        test_object = RectangularRoom(5, 5)
        self.assertEqual(test_object.getNumTiles(), 25)

    def test_method_getNumTiles(self):
        test_data = {
            0: {'input': [15, 4], 'output': 60},
            1: {'input': [14, 8], 'output': 112},
            2: {'input': [18, 1], 'output': 18},
            3: {'input': [9,  2], 'output': 18},
            4: {'input': [1,  2], 'output': 2},

        }
        msg = 'Output at index {i} does not match expected output of \'{output}\''
        for i in test_data.keys():
            arg1 = test_data[i]['input'][0]
            arg2 = test_data[i]['input'][1]

            result = RectangularRoom(arg1, arg2).getNumTiles()
            expected_output = test_data[i]['output']

            self.assertEqual(result, expected_output, msg.format(i=i, output=expected_output))

    def test_unclean_tiles(self):
        arg1 = 4
        arg2 = 6
        test_object = RectangularRoom(arg1, arg2)

        # Test 1 - All tile shall be uncleaned, i.e., False
        for i in range(arg1):
            for j in range(arg2):
                self.assertEqual(test_object.isTileCleaned(i, j), False)

        # Test 2 - Zero tiles shall be cleaned
        self.assertEqual(test_object.getNumCleanedTiles(), 0)

    def test_cleaning_tiles(self):
        arg1 = random.randint(0, 100)
        arg2 = random.randint(0, 100)
        tiles = arg1*arg2
        test_object = RectangularRoom(arg1, arg2)

        # Test 1 - Zero tiles shall be cleaned
        self.assertEqual(test_object.getNumCleanedTiles(), 0)
        for i in range(arg1):
            for j in range(arg2):
                pos = Position(i, j)
                test_object.cleanTileAtPosition(pos)

                # Test 2 - Tile at position (i, j) shall be clean, i.e., return True
                self.assertEqual(test_object.isTileCleaned(i, j), True)

        # Test 3 - tiles number of Tiles shall be clean
        self.assertEqual(test_object.getNumCleanedTiles(), tiles)


    def test_cleaning_tiles_repeatedly(self):
        arg1 = 6
        arg2 = 16
        test_object = RectangularRoom(arg1, arg2)

        for i in range(5):
            n = 0
            for j in range(arg1):
                for k in range(arg2):
                    if n < 23:
                        pos = Position(j, k)
                        test_object.cleanTileAtPosition(pos)
                        n += 1

            # Test 1 - Tile at position (i, j) shall be clean, i.e., return True
            self.assertEqual(test_object.getNumCleanedTiles(), 23)

    def test_getRandomPosition(self):
        arg1 = 1
        arg2 = 1
        test_object = RectangularRoom(arg1, arg2)

        for i in range(100):
            result = test_object.getRandomPosition()
            self.assertEqual(result.getX() < (arg1*arg2), True)
            self.assertEqual(result.getY() < (arg1*arg2), True)

    def test_isPositionInRoom(self):
        arg1 = 6
        arg2 = 6
        test_object = RectangularRoom(arg1, arg2)

        for i in range(100):
            x = random.randint(0, arg1*2*1000)/1000
            y = random.randint(0, arg2*2*1000)/1000
            pos = Position(x, y)
            if x > arg1 or y > arg2:
                expected_result = False
            else:
                expected_result = True

            self.assertEqual(test_object.isPositionInRoom(pos), expected_result)
