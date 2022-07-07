# Flags for financial institution fraud detection

def cashout_great_amount(tx_type, amount):
    return tx_type == 'CASH_OUT' and amount > float(50000)
