# coding=utf-8


# 数据库增、改、删操作
# INSERT INTO TableName(key1, key2, ...) VALUES ('value1', 'value2', ...)
# UPDATE TableName SET key=value
# DELETE FROM EMPLOYEE WHERE key=value
def data_change_action(connect, sql):
    cursor = connect.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        connect.commit()
    except:
        # 如果发生错误则回滚
        connect.rollback()
    connect.close()
    return


# 数据库查询操作
def select_action(connect, sql):
    results = None
    cursor = connect.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
    except:
        print("Error: unable to fetch data")
    connect.close()
    return results
