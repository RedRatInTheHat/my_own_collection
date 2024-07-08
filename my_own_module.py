#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Netology example module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: The module creates a text file at the specified path with the specified content.

options:
    path:
        description: Full path to file to create.
        required: true
        type: str
    new:
        description: File content.
        required: true
        type: str
'''

EXAMPLES = r'''
# Pass in a message
- name: Create file
  my_namespace.my_collection.my_own_moduel:
    path: /tmp/file_name
    content: That text will be in file.
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )


    full_file_path = module.params["path"]
    directory_path = os.path.dirname(full_file_path)
    content = module.params["content"]


    if not is_path_exist(directory_path):
        module.fail_json(msg=f'Path {directory_path} doesn`t exist.', **result)
    if not has_write_permission(directory_path):
        module.fail_json(msg=f'Current user has no permission to write in {directory_path}.', **result)

    if not has_content_already(full_file_path, content):
        create_file(full_file_path, content)
        result["changed"] = True

    module.exit_json(**result)
    

def is_path_exist(file_path):
    return os.path.exists(file_path)

def has_write_permission(directory_path):
    return os.access(directory_path, os.W_OK)

def has_content_already(file_path, content):
    if not is_path_exist(file_path):
        return False

    with open(file_path) as file:
            file_content = file.read()

    return file_content == content

def create_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    

def main():
    run_module()


if __name__ == '__main__':
    main()