from the_bank import Bank, Account
import unittest


class BankTest(unittest.TestCase):
	def test_fixing_corrupted_account(self):
		bank = Bank()
		# Jane account is corrupted because an attribute starts with 'b'
		jane = Account(
			'Smith Jane',
			zip='911-745',
			value=1000.0,
			bref='1044618427ff2782f0bbece0abd05f31'
		)
		william = Account(
			'William John',
			zip='100-064',
			value=6460.0,
			ref='58ba2b9954cd278eda8a84147ca73c87',
			info=None,
			other='This is the vice president of the corporation'
		)
		bank.add(jane)
		bank.add(william)

		# Accounts are added in Bank even if they are corrupted
		self.assertTrue(jane in bank.account)
		self.assertTrue(william in bank.account)

		# Check that Jane account is corrupted but not William's
		self.assertTrue(bank.is_account_corrupted('Smith Jane'))
		self.assertFalse(bank.is_account_corrupted('William John'))

		# Check that transfers fails when one of the account is corrupted
		self.assertFalse(bank.transfer('William John', 'Smith Jane', 545.0))

		# Checks that fix_account function return True when account is corrupted and False otherwise
		self.assertTrue(bank.fix_account('Smith Jane'))
		self.assertFalse(bank.fix_account('William John'))

		# Checks that the corrupted element has been removed from Jane's account
		self.assertFalse('bref' in jane.__dict__.keys())

		# Checks that transfer function now works with 2 uncorrupted accounts
		self.assertTrue(bank.transfer('William John', 'Smith Jane', 545.0))

		# Check that the money has been added to Jane and retrieved from William
		self.assertTrue(jane.value == (1000.0 + 545.0))
		self.assertTrue(william.value == (6460.0 - 545.0))


if __name__ == "__main__":
	unittest.main()
