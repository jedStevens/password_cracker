# Give ourselves access to the Vault
from vault import *

# Create a Vault named v
v = Vault()

# Show the current users with logins to the vault
print(v.users)

# Crack the vault by writing a program that will always guess
# a correct password. Your program should do this in less than
# 100 tries.

# Solutions

# Method A | Rip all info from the vault 	| 35pts
# Method B | Rewrite the Vault 			| 40pts
# Method C | Only rip names; guess passwords	| 45pts
# Method D | Brute force everything		| 50pts 

## Deductions

# Code will not run		| -25pts
# Code locked vault (up to 1)	| -15pts
# Code has no comments		| -5pts
