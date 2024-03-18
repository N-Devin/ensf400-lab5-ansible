import subprocess

# Set ANSIBLE_CONFIG environment variable
ansible_config_path = "$(pwd)/ansible.cfg"
subprocess.run(["export", f"ANSIBLE_CONFIG={ansible_config_path}"], shell=True)

# List hosts using ansible command
list_hosts_command = ["ansible", "all:localhost", "--list-hosts"]
list_hosts_output = subprocess.run(list_hosts_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the output of listing hosts
print("Listing Hosts:")
print(list_hosts_output.stdout.strip())

# Ping hosts using ansible command
ping_command = ["ansible", "all:localhost", "-m", "ping"]
ping_output = subprocess.run(ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the output of pinging hosts
print("\nPinging Hosts:")
print(ping_output.stdout.strip())

# Run the playbook using ansible-playbook command
playbook_command = ["ansible-playbook", "hello.yml"]
playbook_output = subprocess.run(playbook_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Print the output of running the playbook
print("\nRunning Playbook:")
print(playbook_output.stdout.strip())
