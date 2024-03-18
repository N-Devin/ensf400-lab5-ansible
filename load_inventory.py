from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader


def load_inventory(inventory_file='hosts.yml'):
    # Initialize Ansible DataLoader
    loader = DataLoader()

    # Load inventory file
    inventory = InventoryManager(loader=loader, sources=inventory_file)

    return inventory


def print_host_info(host):
    name = host.name
    ip = host.vars.get('ansible_host', 'N/A')
    groups = ', '.join(group.name for group in host.groups)
    print(f"Host: {name}, IP: {ip}, Groups: {groups}")


def ping_all_hosts(inventory):
    print("\nPing Results:")
    for host in inventory.get_hosts():
        result = host.get_vars().get('_ansible_parsed', {}).get('ping', {})
        ping_status = result.get('ping', 'Failed')
        print(f"  {host.name}: {ping_status}")


if __name__ == "__main__":
    inventory_file = 'hosts.yml'
    inventory = load_inventory(inventory_file)

    print("Hosts:")
    for host in inventory.get_hosts():
        print_host_info(host)

    ping_all_hosts(inventory)
