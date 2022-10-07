#!/bin/bash

cd /vagrant || exit
hosts=$(awk -F= '/ansible_host/ {print $NF}' inventory.txt)
for host in $hosts; do
  echo "- Copy SSH key to $host (default password is 'passw0rd')"
  ssh-copy-id -o StrictHostKeyChecking=no "$host"
  echo ""
done

echo "- Test ansible inventory"
ansible all --module-name=ping --inventory-file=inventory.txt
