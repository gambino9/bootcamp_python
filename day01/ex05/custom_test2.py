from the_bank import Bank, Account
import unittest


class BankTest(unittest.TestCase):
	def test_corrupt_even_number_of_argument(self):
		bank = Bank()
		jane = Account(
			'Smith Jane',
			zip='911-745',
			value=1000.0,
			ref='1044618427ff2782f0bbece0abd05f31'
		)
		# William account is corrupted because he has an even number of attributes
		william = Account(
			'William John',
			zip='100-064',
			value=6460.0,
			ref='58ba2b9954cd278eda8a84147ca73c87',
			info=None,
			other='This is the vice president of the corporation',
			addr='96 Boulevard Bessieres'
		)
		bank.add(jane)
		bank.add(william)

		# Accounts are added in Bank even if they are corrupted
		self.assertTrue(jane in bank.account)
		self.assertTrue(william in bank.account)

		# Check that William account is corrupted
		self.assertTrue(bank.is_account_corrupted('William John'))

		# Checks that fix_account function return True when account is corrupted and False otherwise
		self.assertTrue(bank.fix_account('William John'))

		# Checks that William has now an odd number of attributes
		self.assertFalse(len(william.__dict__) % 2 == 0)

		# Check that a new attributes has been added in William's account in order to make number odd
		self.assertTrue('postal_code' in william.__dict__)


if __name__ == "__main__":
	unittest.main()
