Role Name
=========

Роль для создания файлов. Позволяет указать директорию и название файла, а также задать содержимое файла. 

Requirements
------------

* Ansible core 2.12.0 и выше.
* На стороне хоста: 
    * SSH service;
    * Python версии, [соответствующей Ansible core](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix).

Role Variables
--------------

[defaults/main.yml](defaults/main.yml)

| Параметр | Default | Что это |
|----------|---------|---------|
| path | /tmp/file |  Полный путь до файла, включая его название. |
| path | "Wow!\n<br/>So much text!\n<br/>So much Ansible!" |  Содержимое файла |

Example Playbook
----------------

```yml
- name: Create file
  hosts: localhost
  gather_facts: false
  tasks:
    - ansible.builtin.import_role:
        name: my_own_role
```

