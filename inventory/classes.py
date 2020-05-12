from inventory import models


class TransactionHandler:
    def __init__(self, server_id, customer, transaction_id=-1):
        self.Transactions = models.Transaction.objects
        self.Items = models.TransactionsList.objects
        self.transaction_id = transaction_id
        self.record = []
        self.server_id = server_id
        if transaction_id != -1:
            self.old()
        else:
            self.transaction = models.Transaction(server_id=server_id, customer=customer)

    def old(self):
        transaction = self.Transactions.get(id=self.transaction_id)
        if transaction.completed:
            raise RuntimeError('This transaction has already been completed')
        elif transaction.server_id != self.server_id:
            raise RuntimeError("You didn't start this transaction")
        self.transaction = transaction
        self.load()

    def load(self):
        self.record = list(self.Items.filter(transaction_id=self.transaction_id))
