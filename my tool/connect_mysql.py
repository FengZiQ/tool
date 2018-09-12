# coding=utf-8
import pymysql


def send_sql_cmd(sentence):
    result = {'data': ''}
    conn = pymysql.connect(
        host='192.168.20.61',
        port=3306,
        user='admin',
        password='maxwit',
        database='dm_inspos'
    )
    if 'select' in sentence or 'Select':
        cur = conn.cursor()
        cur.execute(sentence)
        result['data'] = cur.fetchall()

    return result


if __name__ == "__main__":
    send_sql_cmd('select id from dm_customer')