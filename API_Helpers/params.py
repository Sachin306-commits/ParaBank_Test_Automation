
def bill_pay_params(account_id,amount):
    params = {
        "accountId": account_id,
        "amount": amount
    }
    return params
def deposit_params(account_id,amount):
    params = {
        "accountId": account_id,
        "amount": amount
    }
    return params
def transfer_amount_params(fromAccount_Id,toAccount_Id,amount):
    params = {
        "fromAccountId": fromAccount_Id,
        "toAccountId": toAccount_Id,
        "amount": amount
    }
    return params