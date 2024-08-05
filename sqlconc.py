import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              passwd="S@hil2911")
c=con.cursor()
sql1="create database fds"
c.execute(sql1)
sql2="use fds"
c.execute(sql2)
sql3="create table fdss(fileNo integer,subject varchar(50),deptIn varchar(50),deptOut varchar(50),incoming date,outgoing date,pendingDays integer)"
c.execute(sql3)
con.commit()
