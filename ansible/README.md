# Installation Steps Ansible

## Prerequisite:
Make sure python is installed in the VM 

## Ubuntu Installation

### Update APT package index:

sudo apt update

### Install software-properties-common:

sudo apt install software-properties-common

### Add Ansible PPA repository:

sudo add-apt-repository --yes --update ppa:ansible/ansible

### Install Ansible:

sudo apt install ansible

### Verify installation:

ansible --version

## Create a role in Ansible 

### Navigate to the directory where you want to create the role:

cd /path/to/ansible/project

### Use ansible-galaxy to create the role:

ansible-galaxy role init <role_name>

### Replace <role_name> with the name of your role. For example:

ansible-galaxy role init myrole

### Here's a basic directory structure for an Ansible project with the folders defaults, handlers, meta, tasks, tests, and vars:

ansible-project/
├── defaults/
│   └── main.yml
├── handlers/
│   └── main.yml
├── meta/
│   └── main.yml
├── tasks/
│   └── main.yml
├── tests/
└── vars/
    └── main.yml

### You can execute the main playbook using the following command 
play.yml
- name: Executing main playbook
  hosts: localhost
  become: yes
  roles:
    - name: myrole
ansible-playbook play.yml
