import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.previous_hash + str(self.timestamp) + str([t.hash for t in self.transactions]) + str(self.nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

    def __str__(self):
        transactions_str = '\n    '.join(str(tx) for tx in self.transactions)
        return f"Block(index: {self.index}, previous_hash: {self.previous_hash[:10]}..., hash: {self.hash[:10]}...)\n    Transactions:\n    {transactions_str}"
