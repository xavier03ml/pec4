import unittest
from covid_approval_checker import functions as f
from pathlib import Path

dir_path = Path(__file__).parent


class TestFunctions(unittest.TestCase):

    def test_datasets_ready(self):
        """
        Prueba que los datasets estén cargados correctamente.
        """
        ac = f.ApprovalChecker(f'{dir_path}\\covid_approval_polls.csv',
                               f'{dir_path}\\covid_concern_polls.csv',
                               f'{dir_path}\\pollster_ratings.xlsx')
        ac.preparar_datasets()
        self.assertEqual(ac.is_ready(), True)

    def test_datasets_not_ready(self):
        """
        Prueba que los datasets no estén cargados correctamente.
        Si una de las rutas es incorrecta, no puede usarse los 
        restantes métodos para resolver la PEC.
        """
        ac = f.ApprovalChecker(f'{dir_path}\\covid_approval_polls.csv',
                               f'{dir_path}\\covid_concern_polls_err.csv',
                               f'{dir_path}\\pollster_ratings.xlsx')
        try:
            ac.preparar_datasets()
        except Exception as e:
            pass
        self.assertEqual(ac.is_ready(), False)

    def test_ejercicio1(self):
        """
        Prueba las ocurrencias de palabras/URLs según las instrucciones del ejercicio 1
        """
        
        ac = f.ApprovalChecker(f'{dir_path}\\covid_approval_polls.csv',
                               f'{dir_path}\\covid_concern_polls.csv',
                               f'{dir_path}\\pollster_ratings.xlsx')
        ac.preparar_datasets()

        self.assertEqual(ac.contar_termino_palabra('Huffington Post'), 112)
        self.assertEqual(ac.contar_termino_palabra('Término inexistente'), 0)
        
        url= 'https://d25d2506sfb94s.cloudfront.net/cumulus_uploads/document/73jqd6u5mv/econTabReport.pdf'
        self.assertEqual(ac.contar_termino_url(url), 4)
        self.assertEqual(ac.contar_termino_url('https://aserver/afile.pdf'), 0)

if __name__ == '__main__':
    unittest.main()