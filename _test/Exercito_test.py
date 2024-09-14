import random, unittest
from src.Exercito import Exercito

class TestExercito(unittest.TestCase):
    def test_new_exercito(self):
        self.cor = 'white'
        self.quantidade = 3
        self.exercito = Exercito(self.cor, self.quantidade)
        self.assertEqual( self.exercito.get_cor(), self.cor)
        self.assertEqual(self.exercito.get_quantidade(), self.quantidade)

    def test_set_cor(self):
        self.cor = 'black'
        self.quantidade = 3
        self.exercito = Exercito(None, self.quantidade)
        self.exercito.set_cor(self.cor)
        self.assertEqual( self.exercito.get_cor(),self.cor)
        
    def test_set_quantidade(self):
        self.cor = 'black'
        self.quantidade = 3
        self.exercito = Exercito(self.cor, None)
        self.exercito.set_quantidade(self.quantidade)
        self.assertEqual( self.exercito.get_quantidade(), self.quantidade)
        self.assertTrue(self.exercito.get_quantidade() <4 and self.exercito.get_quantidade() >0)
        self.assertEqual( type(self.exercito.get_quantidade()), int)
        
if __name__ == '__main__':
    unittest.main()