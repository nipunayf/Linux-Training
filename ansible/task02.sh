#!/bin/sh

ansible web1 -m hostname -a name='lt-2021-013-webserver1' -i inventory --become
ansible web2 -m hostname -a name='lt-2021-013-webserver2' -i inventory --become
