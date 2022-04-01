import pymysql as ps

conn = ps.connect(host = 'localhost', user='root', passwd='1234', db='test')
curs = conn.cursor()

def select_sensordb():
    sql = 'select * from sensordb'
    curs.execute(sql)
    result = curs.fetchall()
    r = '<br>'.join(map(str, result))
    return r

#for s, t in result:
#    print('sensing:{} / ts:{}'.format(s,t))

