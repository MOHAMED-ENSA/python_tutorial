#  unit testing + name/main : 
import unittest 
#assert  7 == 2*4 , "should be 8 ! " 
class test(unittest.TestCase) : 
    def testOne(self) : 
        self.assertTrue(14 > 16 , "Should be true ! ")
    def testTwo(self) : 
        self.assertEqual(100,101,"Should be equal ")    

if __name__ == "__main__": # run dirictly only
    unittest.main()