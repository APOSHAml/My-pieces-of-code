import time

import mysql.connector as mysql

try:
    datebase_sql = mysql.connect(
        host="database-1.cqpxsublkhcn.eu-central-1.rds.amazonaws.com",
        port=3306,
        user="user1",
        passwd="1Passw0rd1",
        database="QAP-05",
    )
except Exception as err:
    print(err)


cursor = datebase_sql.cursor(dictionary=True)

group_name = """(
    SELECT s.name, s.surname, g.name as group_name, l.book_title, l.return_date FROM students s LEFT JOIN library l ON s.id = l.student
    LEFT JOIN `groups` g  ON s.id = g.id
    )"""
cursor.execute(group_name)
result_table = cursor.fetchall()
count = 0
for students in result_table:
    if students["return_date"] != None:
        students["return_date"] = time.strftime(
            "%B %d, %Y", time.strptime(students["return_date"], "%Y-%m-%d")
        )
    if students["return_date"] is None:
        students["return_date"] = "неизвестного времени"
    if students["book_title"] is None:
        students["book_title"] = "не брал книгу"
    if students["group_name"] is None:
        students["group_name"] = "нет информации"

    print(
        f"Студент {students['name']} {students['surname']} учится в группе {students['group_name']} и взял в библиотеке следующую книгу: {students['book_title']} до {students['return_date']} года"
    )
datebase_sql.commit()
datebase_sql.close()
