from brownie import SimpleStorage, accounts, config, network


def deploy_simple_storage():
    # account = accounts.add(config["wallets"]["from_key"])
    account = accounts[0]
    simple_storage = SimpleStorage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    stored_value = simple_storage.retrieve()
    print(f"Here is our starting stored variable {stored_value}")
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(f"Here is our new stored variable {updated_stored_value}")


def main():
    deploy_simple_storage()
