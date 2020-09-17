# python Labs
计算机上，想到自己能做的，先问问 python 能不能做！？

## 1. python & web : Django
* [django start page](https://www.djangoproject.com/start/)

### 1.1 安装 Django

> [官方网站推荐 pip 安装](https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release)

```shell
// 指定 阿里云数据安装 Django，速度更快
pip3 install Django -i https://mirrors.aliyun.com/pypi/simpleo
```

### 1.2 验证安装

* 查看 install_test.py 文件

### 1.3 [Django tutorial01](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

Django 官方 tutorial，在这个说明下，通过 django 的 admin 工具，创建一个 web 项目，还有一个 polls 应用程序。 vscode 对此原生就有比较好的支持，请看参考1。代码请看 myside 目录。

> 参考1 [vscode for django](https://code.visualstudio.com/docs/python/tutorial-django)

### 1.4 [Django tutorial02](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)

Django 官方 tutorial02，紧跟着 tutorial01 的步骤。尝试使用数据库。

## 2 python & Redis

旨在使用 python 去测试以下 redis 的特性

### 2.1 write_100w_redis.py

[[Redis 实验室 1] Redis 源码分析 100W 数据的内存占用及优化](https://juejin.im/post/6868666173123198984)

## 3 python & ssh

2020-09-17 在公司饱受线上查询日志的痛苦，考虑是否有一个 python 脚本，可以自动拉取所有我需要的日志？

### 3.1 install paramiko
一个 ssh 工具