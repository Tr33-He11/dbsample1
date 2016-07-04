import sqlite3,csv


num = 0
conn = sqlite3.connect('E:\PycharmProjects\location.db')
cursor = conn.cursor()
# cursor.execute("create table original33 (num int primary key,id varchar(15),ip varchar)")
with open('E:\PycharmProjects\dbsample1\data\khh_ip_0033.201606.csv','r') as f1:
    rawfile = csv.reader(f1)
    for row in rawfile:
        num = num + 1
        data = [num, row[0],row[1]]
        try:
            cursor.execute("insert into original33 (num,id,ip) values (?,?,?)" , data)
        finally:

            conn.commit()
cursor.close()
conn.close()




