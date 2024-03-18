from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager


def load_inventory(inventory_file='hosts.yml', private_key_file='./secrets/id_rsa'):
    # Initialize Ansible DataLoader
    loader = DataLoader()

    # Load inventory file
    inventory = InventoryManager(loader=loader, sources=inventory_file)

    # Initialize VariableManager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Set private key file
    if private_key_file:
        variable_manager.extra_vars = {
            'ansible_ssh_private_key_file': private_key_file}

    return inventory, variable_manager


if __name__ == "__main__":
    playbook_path = 'hello.yml'
    inventory_file = 'hosts.yml'
    private_key_file = './secrets/id_rsa'

    # Load inventory and variable manager
    inventory, variable_manager = load_inventory(
        inventory_file, private_key_file)

    # Initialize Ansible DataLoader
    loader = DataLoader()

    # Run playbook
    executor = PlaybookExecutor(
        playbooks=[playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords={},
    )

    results = executor.run()
    print(results)
