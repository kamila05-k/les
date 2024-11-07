class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description


# Класс для представления категории
class Category:
    def __init__(self, name):
        self.name = name

# Класс для управления бюджетом
class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def view_transactions(self, transaction_type=None, category=None):
        if not self.transactions:
            print("Нет доступных транзакций.")
            return

        filtered_transactions = self.transactions

        if transaction_type:
            filtered_transactions = [t for t in filtered_transactions if t.amount > 0] if transaction_type == "income" else [t for t in filtered_transactions if t.amount < 0]

        if category:
            filtered_transactions = [t for t in filtered_transactions if t.category.name.lower() == category.lower()]

        if filtered_transactions:
            for i, transaction in enumerate(filtered_transactions, start=1):
                print(f"{i}. {'Доход' if transaction.amount > 0 else 'Расход'}: {abs(transaction.amount)} сом. Категория: {transaction.category.name}. Описание: {transaction.description}")
        else:
            print("Не найдено соответствующих транзакций.")

    def display_statistics(self):
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expense = sum(t.amount for t in self.transactions if t.amount < 0)
        balance = total_income + total_expense

        print(f"Общий доход: {total_income} сом.")
        print(f"Общие расходы: {abs(total_expense)} сом.")
        print(f"Баланс: {balance} сом.")
