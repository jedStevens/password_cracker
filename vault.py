## Well I didn't expect you to read this.
# Author: Jed Stevens
# Date Feb 5h 2017


import random, string

class User:
	def __init__(self, name, password):
		self.username = name
		self.password = password
		self.logged_in = False
	
	def login(self):
		self.logged_in = True
	
	def logout(self):
		self.logged_in = False
	
	def __str__(self):
		return self.username + ":" + "*"*len(self.password)
	def __repr__(self):
		return "User("+self.username+")"


class Vault:
	def __init__(self):
		self.users = []
		self.locked = False
		self.attempts = 100
		self.difficulty = 3
		
		self.users = self.create_default_list()
	
	def add_login(self, user, password):
		self.users.append(User(user, password))
	
	def login(self, name, password):
		if self.attempts <= 0:
			print("VAULT IS LOCKED! INTRUDER ALERT!")
		user = None
		for user in self.users:
			if user.username == name and user.password == password:
				user.login()
			elif user.username==name and user.password != password:
				self.attempts -= 1
				print(self.attempts, "more tries left before the Vault locks")
	
	def create_default_list(self):
		
		# You've found how the default users are being made
		# use this to find out what passwords they use
		
		names = ["Mr. Jed", "Dr. Jed", "Frodo", "Sauron", "Jed"]
		default_users = []
		for name in names:
			random_password = ""
			for j in range(self.difficulty):
				random_password += random.choice(string.ascii_letters)
			default_users.append(User(name, random_password))

		return default_users

	def has_user(self, name):
		for user in self.users:
			if user.username == name:
				return True
		return False
