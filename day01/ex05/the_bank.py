# Has to verify each Account instance by checking :
# If it is an instance of Account
# Not corrupted
# Stores enough money to complete the transfer

# A corrupt bank account has :
# An even number of attributes
# An attribute starting with b
# No attribute zip or addr
# No attribute name id and value

# A transaction is invalid if amount < 0 or if
# the amount is larger than the balance of the account
class Bank:
	"""The bank"""

	def __init__(self):
		self.account = []

	def add(self, account):
		try:
			if not isinstance(account, Account):
				raise TypeError("The account to add must be an Account instance")
			# Check if not corrupted
			if len(account.__dict__) % 2 == 0:
				raise ValueError
			if any(key.startswith('b') for key in account.__dict__.keys()):
				raise ValueError
			if all([address not in account.__dict__.keys() for address in ['zip', 'addr']]):
				raise ValueError
			if any([necessary not in account.__dict__.keys() for necessary in ['id', 'name']]):
				raise ValueError
			self.account.append(account)
		except TypeError as te:
			exit(te)
		except ValueError as ve:
			self.fix_account(account)
			self.account.append(account)

	def transfer(self, origin, dest, amount):
		"""
			@origin: int(id) or str(name) of the first account
			@dest: int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return True if success, False if an error occurred
		"""
		if not isinstance(origin, (str, int)):
			return False
		if not isinstance(dest, (str, int)):
			return False
		if not isinstance(amount, float):
			return False
		if amount <= 0:
			return False
		# if all(person in self.account for person in [origin, dest]):
		# 	self.account.__dict__[origin]
		for org_profil in self.account:
			if origin in org_profil.__dict__.values():
				for dest_profil in self.account:
					if dest in dest_profil.__dict__.values():
						if org_profil['value'] > amount:  # Check if stores enough to transfer
							org_profil['value'] -= amount
							dest_profil['value'] += amount
						else:
							return False
		return True

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return True if success, False if an error occurred
		"""
		pass


class Account:
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1
		# self.value = None

	def transfer(self, amount):
		self.value += amount

