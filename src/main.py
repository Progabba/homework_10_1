from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions

if __name__ == "__main__":

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions)["id"])

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)
