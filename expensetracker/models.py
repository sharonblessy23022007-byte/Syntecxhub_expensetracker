class Transaction:
    def __init__(self, date, category, amount, trans_type):
        self.date = date
        self.category = category
        self.amount = amount
        self.trans_type = trans_type

    def validate(self):
        return (
            self.date and
            self.category and
            self.amount > 0 and
            self.trans_type in ["income", "expense"]
        )