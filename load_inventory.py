from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.vars.manager import VariableManager
from ansible.plugins.callback import CallbackBase


class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host.get_name()
        ip = result._host.get_vars().get('ansible_host', 'N/A')
        groups = ', '.join(result._host.get_groups())
        print(f"Host: {host}, IP: {ip}, Groups: {groups}")
        print(f"Ping result: {result._result.get('ping')}")


def load_inventory(inventory_file='hosts.yml'):
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_file)
    return inventory


def ping_all_hosts(inventory):
    results_callback = ResultCallback()
    variable_manager = VariableManager(
        loader=inventory._loader, inventory=inventory)
    task_queue_manager = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=inventory._loader,
        passwords={},
        stdout_callback=results_callback,
    )
    ping_task = dict(
        name="Ping all hosts",
        action=dict(module="ping", args=""),
        hosts='all',
        roles=[],
    )
    task_queue_manager.run([ping_task])


if __name__ == "__main__":
    inventory_file = 'hosts.yml'
    inventory = load_inventory(inventory_file)
    print("Hosts and Ping Results:")
    ping_all_hosts(inventory)
