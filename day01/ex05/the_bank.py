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
		self.error = 0

	def add(self, account):
		self.account.append(account)
		try:
			if not isinstance(account, Account):
				raise TypeError("The account to add must be an Account instance")
		except TypeError as te:
			exit(te)

	def transfer(self, origin, dest, amount):
		"""
			@origin: int(id) or str(name) of the first account
			@dest: int(id) or str(name) of the destination account
			@amount: float(amount) amount to transfer
			@return True if success, False if an error occurred
		"""
		if self.is_account_corrupted(origin) or self.is_account_corrupted(dest):
			return False
		if not isinstance(origin, (str, int)):
			return False
		if not isinstance(dest, (str, int)):
			return False
		if not isinstance(amount, float):
			return False
		if amount <= 0:
			return False
		for org_profil in self.account:
			if origin in org_profil.__dict__.values():
				for dest_profil in self.account:
					if dest in dest_profil.__dict__.values():
						if org_profil.value > amount:  # Check if stores enough to transfer
							org_profil.value -= amount
							dest_profil.value += amount
							return True
						else:
							break
		return False

	def is_account_corrupted(self, name):
		id_instance = None
		if isinstance(name, str):
			for count in self.account:
				if name in count.name:
					# print(f"{count.id=} for {count.name}")
					id_instance = int(count.id - 1)
		if len(self.account[id_instance].__dict__) % 2 == 0:
			return True
		if any(key.startswith('b') for key in self.account[id_instance].__dict__.keys()):
			return True
		if all([address not in self.account[id_instance].__dict__.keys() for address in ['zip', 'addr']]):
			return True
		if any([identity not in self.account[id_instance].__dict__.keys() for identity in ['id', 'name']]):
			return True
		return False

	def fix_account(self, account):
		"""
			fix the corrupted account
			@account: int(id) or str(name) of the account
			@return True if success, False if an error occurred
		"""
		id_instance = None
		if isinstance(account, int):
			id_instance = int(account - 1)
		elif isinstance(account, str):
			for count in self.account:
				if account in count.name:
					id_instance = int(count.id - 1)

		if len(self.account[id_instance].__dict__) % 2 == 0:
			setattr(self.account[id_instance], 'postal_code', '75000')
			return True
		if any(key.startswith('b') for key in self.account[id_instance].__dict__.keys()):
			for attribute in self.account[id_instance].__dict__.keys():
				if attribute.startswith('b'):
					new_attr = attribute[1:]
					new_value = self.account[id_instance].__dict__[attribute]
					delattr(self.account[id_instance], attribute)
					setattr(self.account[id_instance], new_attr, new_value)
					return True
		if all([address not in self.account[id_instance].__dict__.keys() for address in ['zip', 'addr']]):
			setattr(self.account[id_instance], '198-753', zip)
			return True
		if any([identity not in self.account[id_instance].__dict__.keys() for identity in ['id', 'name']]):
			setattr(self.account[id_instance], 'name', 'John Doe')
			return True
		return False


class Account:
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount

