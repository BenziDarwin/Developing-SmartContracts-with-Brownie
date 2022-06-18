from brownie import SimpleStorage, config


def read_contract():
    simple_storage = SimpleStorage[config["tracker"] + 1]
    print(simple_storage.showValue())


def main():
    read_contract()
