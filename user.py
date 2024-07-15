import hashlib

class User:
    def __init__(self, name):
        self.name = name
        self.public_key = self.generate_public_key()
        self.balance = 0

    def generate_public_key(self):
        return hashlib.sha256(self.name.encode('utf-8')).hexdigest()

    def __str__(self):
        return f"User({self.name}, {self.public_key[:10]}..., Balance: {self.balance})"
