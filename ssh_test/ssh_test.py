#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ssh_test.py
@Time    :   2020/09/17 23:49:58
@Author  :   Liu YuanYuan :)
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import logging as log
import sys
from paramiko import AuthenticationException
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import NoValidConnectionsError


class MySSHClient():

    def __init__(self):
        self.ssh_client = SSHClient()

    def ssh_login(self, host_ip, username, password):
        try:
            self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
            self.ssh_client.connect(
                host_ip, port=22, username=username, password=password)
        except AuthenticationException:
            log.warning('username or password error')
            return 1001
        except NoValidConnectionsError:
            log.warning('connect time out')
            return 1002
        except:
            log.warning('unkown error')
            print("Unexpect error:", sys.exc_info()[0])
            return 1003
        return 1000

    def ssh_logout(self):
        log.warning('will exit host')
        self.ssh_client.close()

    def execute_some_command(self, command):
        _, stdout, _ = self.ssh_client.exec_command(command)
        print(stdout.read().decode())


if __name__ == "__main__":
    host_ip = "local.qpm.com"
    username = "root"
    password = "qpm123"

    command = 'tree compose_software'

    my_ssh_client = MySSHClient()
    if my_ssh_client.ssh_login(host_ip, username, password) == 1000:
        log.warning(
            f"{host_ip} - login success, will execute command: {command}")
        my_ssh_client.execute_some_command(command)
        my_ssh_client.ssh_logout()

    # 获取目录中，所有配置文件中包含 mysql 的行
    command = 'find . -name "*.yml" -exec cat {} \; | grep -A10 -B10 mysql'
    if my_ssh_client.ssh_login(host_ip, username, password) == 1000:
        my_ssh_client.execute_some_command(command)
        my_ssh_client.ssh_logout()
