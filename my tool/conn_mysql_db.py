# coding=utf-8
import pymysql
from sshtunnel import SSHTunnelForwarder


def ssh_mapping_connect_db(db_name):
    server = SSHTunnelForwarder(
        ssh_address_or_host=('permission.preo.2dupay.com', 22),  # 指定ssh登录的跳转机的address
        ssh_username='platform',  # 跳转机的用户
        ssh_password='Inspiry2017',  # 跳转机的密码
        remote_bind_address=('rm-m5eqq23sw28y8ad5b.mysql.rds.aliyuncs.com', 3306))
    server.start()
    db_conn = pymysql.connect(
        user="paipai_admin",
        passwd="Inspiry2016",
        host="127.0.0.1",
        db=db_name,
        port=server.local_bind_port)

    return db_conn


def connect_db(db_name):
    db_conn = pymysql.connect(
        host='192.168.20.61',
        port=3306,
        user='admin',
        password='maxwit',
        database=db_name
    )

    return db_conn
