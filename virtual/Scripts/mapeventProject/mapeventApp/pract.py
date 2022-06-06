from typing import List


def pract1(list):
    temp = list[0]
    temp2 = list[len(list)-1]
    list[len(list)-1]= temp
    list[0] = temp2
    a = list[:]
    print(a)

list = [1,2,3,4,5,6]
pract1(list)
   
#select * from databasename.tablename where salary BETWWEN 50000 AND 60000;
#select * from database.tablename where employe_name LIKE['A%']