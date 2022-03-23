import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('env.ini')


# This function will perform, POST https://api-test.lotuspay.com/v1/customers/{ID}/bank_accounts/
def create_customer(customer_object):
    try:
        result = requests.post(config['lotus-pay-api']['url']+'customers/', data=customer_object,
                               auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


def retrieve_customer(customer_id):
    try:
        result = requests.get(config['lotus-pay-api']['url']+'customers/', params={'id': customer_id},
                              auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


def list_customer(limit):
    try:
        result = requests.get(config['lotus-pay-api']['url']+'customers/', params={'limit': limit},
                              auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


# This function will perform, POST https://api-test.lotuspay.com/v1/customers/{ID}/bank_accounts/
def create_bank_account(bank_info):
    try:
        customer_id = bank_info['id_token']
        url = config['lotus-pay-api']['url']+'customers/' + f'{customer_id}/bank_accounts'
        result = requests.post(url, data=bank_info, auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


# This function will perform POST https://api-test.lotuspay.com/v1/sources
def source(source_info):
    try:
        url = config['lotus-pay-api']['url']+'/sources'
        result = requests.post(url, data=source_info, auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    finally:
        print(result.reason)
        print(result)
    return result.json()


# Customer info to create a customer object in to the lotus pay
customer = {
    "email": "Aroha1@gmail.com",
    "mobile": "0052253600",
    "name": "Aroha1",
    "pan": "AHQPV2889"
}


# # Call create_customer function, store the api response
create_cus = create_customer(customer)


# Bank info of the Customer, to create a bank account into the lotus pay api
bank_object = {
    "id_token": create_cus['id'],
    "account_holder_name": "Aroha1",
    "account_ifsc": "ICIC0000047",
    "account_number": "12341234",
    "account_type": "savings"

}


# Call create_bank_account function, store the api response
create_bank = create_bank_account(bank_object)

source_details = {
    "type": "nach_debit",
    "nach_debit": {
        "amount_maximum": 10000,
        "debtor_agent_code": "ICIC",
        "debtor_account_name": "Aroha1",
        "debtor_account_number": "12345678",
        "debtor_account_type": "savings",
        "frequency": "MNTH",
        "reference1": 'CU0090BMZMKJRL',
    }
}

create_source = source(source_details)

print(create_cus)
print(create_bank)
print(create_source)