import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('env.ini')


# Function to create a customer in lotus pay
def create_customer(customer_object):
    try:
        result = requests.post(config['lotus-pay-api']['url']+'customers/', data=customer_object,
                               auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


def retrieve_customer(customer_id):
    try:
        result = requests.get(config['lotus-pay-api']['url']+'customers/', params={'id':customer_id},
                              auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


def list_customer(limit):
    try:
        result = requests.get(config['lotus-pay-api']['url']+'customers/', params={'limit':limit},
                              auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()


# This function will crete a bank account for existing customer id
def create_bank_account(bank_object):
    try:
        id = bank_object['id_token']
        url = config['lotus-pay-api']['url']+'customers/' + f'{id}/bank_accounts'
        result = requests.post(url, data=bank_object, auth=(config['lotus-pay-api']['api-key'], ''))
    except Exception as e:
        result = e
    return result.json()



customer = {
    "email": "vinoihero@gmail.com",
    "mobile": "9052253688",
    "name": "Vinod Kumar.A.M",
    "pan": "HHHHH22889"
}


# This will create cust id
create_cus = create_customer(customer)


bank_object={
    "id_token": create_cus['id'],
    "account_holder_name": "Amit Jain",
    "account_ifsc": "ICIC0000047",
    "account_number": "12341234",
    "account_type": "savings"

}


# This will create a bank account for a Customer ID
create_bank=create_bank_account(bank_object)

print(create_cus)
print(create_bank)

