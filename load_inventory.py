import ansible_runner
import yaml
import os

os.environ['ANSIBLE_CONFIG'] = os.path.join(os.getcwd(), 'ansible.cfg')


# Load inventory using Python code and print host information
with open("hosts.yml") as host_file: 
    inventory_file = yaml.full_load(host_file) 

for group, hosts in inventory_file.items():
    print(f"Group: {group}") 
    for host, attrs in hosts.get('hosts', {}).items(): 
        print(f"  Name: {host}, IP Address: {attrs.get('ansible_host')}") 


ansible_runner.interface.run_command("export ANSIBLE_CONFIG=$(pwd)/ansible.cfg") 
result = ansible_runner.interface.run_command("ansible all:localhost -m ping") 
print("Results after pinging hosts:\n")
print(result)