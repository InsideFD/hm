import unittest
from src.masks import get_mask_card_number, get_mask_account


class TestMaskFunctions(unittest.TestCase):
    def test_card_masking(self):
        """Тестирование маскировки номера карты"""
        self.assertEqual(get_mask_card_number("7000792289606361"), "7000 79** **** 6361")
        self.assertEqual(get_mask_card_number("1234567890123456"), "1234 56** **** 3456")

    def test_account_masking(self):
        """Тестирование маскировки номера счета"""
        self.assertEqual(get_mask_account("73654108430135874305"), "**4305")
        self.assertEqual(get_mask_account("1234567890"), "**7890")


if __name__ == '__main__':
    unittest.main()
