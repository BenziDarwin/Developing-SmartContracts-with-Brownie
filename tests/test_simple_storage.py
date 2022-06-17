from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    starting_value = simple_storage.showValue()
    expected = 0

    # Asserting
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    txn = simple_storage.giveValue(12, {"from": account})
    txn.wait(1)
    txn_value = simple_storage.showValue()
    value_after_transaction = 12

    # Asserting
    assert txn_value == value_after_transaction
