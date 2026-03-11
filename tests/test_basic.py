import unittest
import sys
import os

# Add the current directory to sys.path so we can import dbgp
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestDBGPClient(unittest.TestCase):
    def test_import(self):
        try:
            import dbgp.client
            from dbgp.client import h_main, backendCmd
        except ImportError as e:
            self.fail("Failed to import dbgp.client: {0}".format(e))

    def test_h_main(self):
        from dbgp.client import h_main
        hm = h_main()
        self.assertEqual(hm.name, '__main__')
        self.assertTrue(hasattr(hm, 'module'))
        self.assertTrue(hasattr(hm, 'locals'))
        self.assertTrue(hasattr(hm, 'globals'))

    def test_backendCmd_init(self):
        from dbgp.client import backendCmd, h_main
        # Just test instantiation with default arguments
        try:
            client = backendCmd("test_key", None, [], module=h_main())
            self.assertIsNotNone(client)
        except Exception as e:
            self.fail("Failed to instantiate backendCmd: {0}".format(e))

if __name__ == '__main__':
    unittest.main()
