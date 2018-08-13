import collections

class Solution:
	def __init__(self):
		self.key_value_store = dict()
		self.transaction_list = []
		self.transaction_log = collections.defaultdict(dict)
		self.transaction = 0

	def getKey(self, key):
		if key in self.key_value_store:
			return self.key_value_store[key]
		else:
			return None

	def set(self, key, value):
		if self.transaction_list:
			current_transaction = self.transaction_list[-1]
			if key in self.transaction_log[current_transaction]:
				self.key_value_store[key] = value
			else:
				self.transaction_log[current_transaction][key] = self.key_value_store[key]
				self.key_value_store[key] = value
		else:
			self.key_value_store[key] = value

	def begin_transaction(self):
		self.transaction_list.append(self.transaction)
		self.transaction += 1

	def end_transaction(self):
		if self.transaction_list:
			current_transaction = self.transaction_list.pop()
			del self.transaction_log[current_transaction]
		else:
			print ("No current transaction to end")


	def rollback_transaction(self):
		if self.transaction_list:
			current_transaction = self.transaction_list.pop()
			for key, value in self.transaction_log[current_transaction].items():
				self.key_value_store[key] = value
			del self.transaction_log[current_transaction]
		else:
			print ("No current transaction to roll back")

s = Solution()
print(s.getKey('a'))
print(s.set('a', 2))
print(s.getKey('a'))
print(s.begin_transaction())
print(s.set('a', 5))
print(s.getKey('a'))
print(s.begin_transaction())
print(s.set('a', 6))
print(s.getKey('a'))
print(s.end_transaction())
print(s.getKey('a'))
print(s.rollback_transaction())
print(s.getKey('a'))