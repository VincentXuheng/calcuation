import pymysql
conn = pymysql.connect(host='127.0.0.1', user = "root",
                       
passwd="123456", db="testd", port=3306, charset="utf8")
cur = conn.cursor()
sql = "insert into wuliao(userName, birth,owner) value(%s, %s,%s)"
person = [['小军', '1993-06-05','i'], ['小明', '1993-04-03','you']]

for i in range(len(person)):
    param = tuple(person[i])
    #执行sql语句
    count = cur.execute(sql, param)
    #判断是否成功
    if count > 0:
        print("添加数据成功！\n")
#提交事务
conn.commit()
#查询数据
cur.execute("select * from tb_user")
#获取数据
users = cur.fetchall();


#关闭资源连接
cur.close()
conn.close()
