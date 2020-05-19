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

    def not_if_completed(self, func):
        def new_func(*args, **kwargs):
            if self.transaction.completed:
                raise RuntimeError('This transaction is already completed.')
            else:
                return func(*args, **kwargs)
        return new_func

    @not_if_completed
    def old(self):
        transaction = self.Transactions.get(id=self.transaction_id)
        if transaction.server_id != self.server_id:
            raise RuntimeError("You didn't start this transaction")
        self.transaction = transaction
        self.load()

    def load(self):
        self.record = list(self.Items.filter(transaction_id=self.transaction_id))

    @not_if_completed
    def add(self, product_id, quantity):
        subtotal = models.Product.objects.get(id=product_id).price * quantity
        transaction_list_instance = models.TransactionsList(
            transaction_id=self.transaction_id,
            product_id=product_id,
            quantity=quantity,
            subtotal=subtotal)
        transaction_list_instance.save()
        return transaction_list_instance.id

    @not_if_completed
    def delete(self, transaction_list_id):
        self.Items.get(id=transaction_list_id).delete()

    def complete(self):
        self.transaction.completed = True
        self.transaction.save()
