import csv
import pymysql

# 打开CSV文件并读取数据
file_instance = open("地震一年数据.txt", encoding='UTF-8')
csv_reader = csv.reader(file_instance)
data = []  # 存储读取的数据
for line in csv_reader:
    data.append(line)
file_instance.close()
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',charset='utf8',db='day1')
cursor=conn.cursor()
sql="""
create table sj(
     event_code varchar(255),
     zhenji decimal,
     time datetime,
     weidu decimal,
     jingdu decimal,
     shendu decimal,
     place varchar(100),
     lianjie varchar(255)
     )default charset=utf8
"""
cursor.execute(sql)
insert_query = ("insert into sj (event_code,zhenji,time,weidu,jingdu,shendu,place,lianjie)"
                " values (%s,%s,%s,%s,%s,%s,%s,%s)")
for line in data:
    cursor.execute(insert_query,line)
conn.commit()
print("数据已成功写入MySQL数据库。")
