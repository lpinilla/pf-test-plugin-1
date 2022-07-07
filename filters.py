
def remove_transactions_lower_than(field, params):
    return field <= params['value']

def nameDest_starts_with_C(field):
    return field[0] == 'C'
