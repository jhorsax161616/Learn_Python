import unittest


def mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor(self):
        edad = 22

        resultado = mayor(edad)

        self.assertEqual(resultado, True)

    def test_es_menor(self):
        edad = 19

        resultado = mayor(edad)

        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main(verbosity=2)