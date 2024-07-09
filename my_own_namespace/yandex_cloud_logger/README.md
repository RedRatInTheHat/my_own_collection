# Ansible Collection - my_own_namespace.yandex_cloud_logger

## Описание

Коллекция предназначена для создания файлов с указанным содержимым по указанному пути.

## Примеры использования

```yml
---
- name: Create file
  hosts: localhost
  gather_facts: false
  tasks:
    - ansible.builtin.import_role:
        name: my_own_namespace.yandex_cloud_logger.my_own_role
    - name: Create file with module
      my_own_namespace.yandex_cloud_logger.my_own_module:
        path: /tmp/some_file
        content: Some content
```

## Требования

* Ansible core 2.12.0 и выше.
* На стороне хоста: 
    * SSH service;
    * Python версии, [соответствующей Ansible core](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix).
