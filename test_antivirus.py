import unittest
from unittest.mock import patch, Mock
from tkinter import Tk
from antivirus_app import AntivirusApp

class TestAntivirusApp(unittest.TestCase):
    def setUp(self):
        self.app = AntivirusApp()

    @patch('tkinter.filedialog.askdirectory', return_value='/fake/directory')
    @patch('antivirus_app.AntivirusAnimation')
    def test_scan_files(self, mock_animation, mock_ask_directory):
        self.app.scan_files()
        mock_animation.assert_called_once_with(
            self.app, "Scanning Files", self.app.simulate_scan('/fake/directory')
        )

    @patch('antivirus_app.AntivirusAnimation')
    def test_device_security(self, mock_animation):
        self.app.device_security()
        mock_animation.assert_called_once_with(
            self.app, "Checking Device Security", self.app.device_security_result()
        )

    @patch('antivirus_app.AntivirusAnimation')
    def test_network_security(self, mock_animation):
        self.app.network_security()
        mock_animation.assert_called_once_with(
            self.app, "Checking Network Security", self.app.network_security_result()
        )

    @patch('antivirus_app.AntivirusAnimation')
    def test_browser_control(self, mock_animation):
        self.app.browser_control()
        mock_animation.assert_called_once_with(
            self.app, "Controlling Browser Security", self.app.browser_control_result()
        )

if __name__ == '__main__':
    unittest.main()
