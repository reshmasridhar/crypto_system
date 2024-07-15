from user import User
from blockchain import Blockchain

# Create users
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

# Create a blockchain
crypto_chain = Blockchain(difficulty=4)

# Add users to the blockchain
crypto_chain.add_user(alice)
crypto_chain.add_user(bob)
crypto_chain.add_user(charlie)

# Set initial balances
crypto_chain.users[alice.public_key].balance = 50
crypto_chain.users[bob.public_key].balance = 30
crypto_chain.users[charlie.public_key].balance = 20

# Print initial balances
print("\nInitial User Balances:")
for user in crypto_chain.users.values():
    print(user)

# Create transactions
crypto_chain.create_transaction(alice.public_key, bob.public_key, 10)
crypto_chain.create_transaction(bob.public_key, charlie.public_key, 5)

# Mine pending transactions
crypto_chain.mine_pending_transactions(alice.public_key)

# More transactions
crypto_chain.create_transaction(charlie.public_key, alice.public_key, 2)
crypto_chain.create_transaction(bob.public_key, alice.public_key, 3)

# Mine again
crypto_chain.mine_pending_transactions(bob.public_key)

# Print the blockchain
crypto_chain.print_chain()

# Print final balances
print("\nFinal User Balances:")
for user in crypto_chain.users.values():
    print(user)
