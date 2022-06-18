from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():

    # To use a specific account
    # account = accounts.load("metamask")

    account = chooseAccount()

    # Identifying the account
    # account = accounts[0]

    # Deploying the contract with the account to a block chain

    print("Deploying contract...")
    simple_storage_object = SimpleStorage.deploy({"from": account})
    print("Contract deployed!")

    # Using functions from the smart contacts deployed

    # Call
    print("Show number...\n")
    number_object = simple_storage_object.showValue()
    print(number_object)

    # Transaction changing a value

    print("Changing value...")
    txn = simple_storage_object.giveValue(12, {"from": account})
    txn.wait(1)
    print("Value changed!")

    updated_value = simple_storage_object.showValue()
    print(updated_value)

    # account = accounts.add(os.getenv(r"RINKEBY_PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    # print(simple_storage_object)


def chooseAccount():
    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
