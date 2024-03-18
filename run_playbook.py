from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager


def load_inventory(inventory_file='hosts.yml'):
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_file)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    return inventory, variable_manager


def run_playbook(playbook_path, inventory):
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    passwords = {}

    playbook_executor = PlaybookExecutor(
        playbooks=[playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords
    )
    result = playbook_executor.run()
    print(result)


if __name__ == "__main__":
    playbook_path = 'hello.yml'
    inventory_file = 'hosts.yml'
    inventory, _ = load_inventory(inventory_file)
    run_playbook(playbook_path, inventory)
