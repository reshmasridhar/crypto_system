from block import Block
from transaction import Transaction
import time

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.pending_transactions = []
        self.users = {}
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", int(time.time()), [])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def create_transaction(self, sender, recipient, amount):
        if sender in self.users and self.users[sender].balance >= amount:
            transaction = Transaction(sender, recipient, amount)
            self.pending_transactions.append(transaction)
            print(f"Transaction created: {transaction}")
        else:
            print(f"Transaction failed: Insufficient balance for user {sender}")

    def mine_pending_transactions(self, miner_address):
        if not self.pending_transactions:
            print("No transactions to mine")
            return

        new_block = Block(len(self.chain), self.get_last_block().hash, int(time.time()), self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        # Reward the miner
        reward_transaction = Transaction("System", miner_address, 10)
        self.pending_transactions = [reward_transaction]

        print(f"Block added to the chain: {new_block}")

        # Update balances
        for transaction in new_block.transactions:
            if transaction.sender != "System":
                self.users[transaction.sender].balance -= transaction.amount
            self.users[transaction.recipient].balance += transaction.amount

    def add_user(self, user):
        self.users[user.public_key] = user
        print(f"User added: {user}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        for block in self.chain:
            print(block)
