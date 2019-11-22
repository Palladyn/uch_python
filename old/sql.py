import pypyodbc

mySql="ADMIN\SQLEXPRESS"
myDB="northwind"

#connect=pypyodbc.connect('Driver={SQL Server;};'
 #                        'Server=ADMIN\SQLEXPRESS:'
  #                       'Database=northwind:'
                      #   'uid=username;'
                  #     $   'pwd=mypass;')


connect=pypyodbc.connect('driver={SQL Server};'
                         'server='+mySql+';'
                         'database='+myDB+';')

cursor=connect.cursor()
SqlQwe=("""SELECT companyname, contactname, country   FROM dbo.Customers  WHERE country='usa'""")

cursor.execute(SqlQwe)
res= cursor.fetchall()
for i in res:
    print(i)

connect.close()  