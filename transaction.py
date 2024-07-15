import hashlib

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((self.sender + self.recipient + str(self.amount)).encode('utf-8')).hexdigest()

    def __str__(self):
        return f"Transaction(from: {self.sender[:10]}..., to: {self.recipient[:10]}..., amount: {self.amount}, hash: {self.hash[:10]}...)"
