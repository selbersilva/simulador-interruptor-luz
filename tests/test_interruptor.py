import unittest
from src.interruptor import acender_luz, apagar_luz

class TestInterruptor(unittest.TestCase):

    def test_acender_luz(self):
        # Capturar a saída padrão para verificar a impressão
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        acender_luz()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "A luz está ACESA.")

    def test_apagar_luz(self):
        # Capturar a saída padrão para verificar a impressão
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        apagar_luz()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "A luz está APAGADA.")

if __name__ == "__main__":
    unittest.main()
