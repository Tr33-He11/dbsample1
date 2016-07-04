#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cx_Oracle
import datetime
import os
#import sys

def oracle(sql,outfile,header):
    #config
    fetchpertime=10000
    dsn=cx_Oracle.makedsn('10.0.24.82',1521,service_name='fjghsj')
    connect_o = cx_Oracle.connect('chaxun', 'chaxun', dsn)
    cursor_o = connect_o.cursor()

    f=file(outfile,'w')
    if header!=None:
        print>>f,header

    cursor_o.execute(sql)
    count=0

    #print sql

    while True:
        fetchdat=cursor_o.fetchmany(fetchpertime)
        if len(fetchdat)==0:
            break
        count+=len(fetchdat)

        for line in fetchdat:
            print>>f,','.join(str(i) for i in line)
        f.flush()

        #print '\r',count,
        #sys.stdout.flush()

    f.close()

    cursor_o.close()
    connect_o.close()
    return count

oracle("select distinct(zdcj.tkhdl.khh),ip from zdcj.tkhdl left join crm.tkhxx on zdcj.tkhdl.khh=crm.tkhxx.khh where crm.tkhxx.yyb=0033 and drRQ>=20160521",'/home/heiser/work/khh_ip_0033.20160521.csv;',header=None)
oracle("select distinct(zdcj.tkhdl.khh),ip from zdcj.tkhdl left join crm.tkhxx on zdcj.tkhdl.khh=crm.tkhxx.khh where crm.tkhxx.yyb=0035 and drRQ>=20160521",'/home/heiser/work/khh_ip_0035.20160521.csv;',header=None)
oracle("select distinct(zdcj.tkhdl.khh),ip from zdcj.tkhdl left join crm.tkhxx on zdcj.tkhdl.khh=crm.tkhxx.khh where crm.tkhxx.yyb=0253 and drRQ>=20160521",'/home/heiser/work/khh_ip_0253.20160521.csv;',header=None)

