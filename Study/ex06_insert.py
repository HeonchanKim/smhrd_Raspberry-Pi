import pymysql as ps
import spidevRead as sr
import time

conn = ps.connect(host='localhost', user='root', passwd='1234', db='test')
while True:
    curs = conn.cursor()
    readData = sr.analog_read(0)
    sql = f'insert into sensordb(sensing) values({readData})'
    curs.execute(sql)
    conn.commit()
    time.sleep(5)
