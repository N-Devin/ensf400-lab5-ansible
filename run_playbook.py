import ansible_runner

playbook_path = "./hello.yml"
inventory_file = "./hosts.yml"

# Run the playbook
runner = ansible_runner.run(private_data_dir='.', playbook=playbook_path, inventory=inventory_file)

# Print playbook execution results
print("\n================Playbook Results========== \n")
print(runner.stats)

# Print playbook events
print("\n===========Events ===============\n")
for event in runner.events:
    print(event['event'])


