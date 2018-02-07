#!/usr/bin/env python  
#coding=utf-8  

import xlwt
import MySQLdb
import datetime
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import parseaddr, formataddr
from email.Header import Header
import smtplib
import os


def createExcel():
	workbook = xlwt.Workbook(encoding='utf-8')
	return workbook

def createSheet(workbook, sheetname, fields, results):
	sheet = workbook.add_sheet(sheetname,cell_overwrite_ok=True)  
	for ifs in range(0,len(fields)):  
	    sheet.write(0,ifs,fields[ifs][0])  

	ics=1  
	jcs=0  

	for ics in range(1,len(results)+1):  
	    for jcs in range(0,len(fields)):  
	        sheet.write(ics,jcs,results[ics-1][jcs])  


def getDataFromDB(sql, cursor):
	cursor.execute(sql)
	results = cursor.fetchall()
	fields = cursor.description

	return fields, results

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
    	Header(name, 'utf-8').encode(), \
    	addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendEmail(fileName,fileNameWithoutPath, timeflag):

	# 输入Email地址和口令:
	from_addr = 'tjbb@lxfintech.com'
	password = 'paymax@2015'
	# 输入SMTP服务器地址:
	smtp_server = 'smtp.mxhichina.com'
	smtp_port = 465
	# 输入收件人地址:
	to_addr_list = ['Bison <bison@lxfintech.com>','wxw <wangxiaowei@lxfintech.com>','anson <chengwei@lxfintech.com>','xurui_sh <xurui_sh@lakala.com>','yuyijing <yuyijing@lakala.com>','chenyanxi <chenyanxi@lakala.com>','chengfei <chengfei@lakala.com>','fanzhiguo <fanzhiguo@lxfintech.com>','yanjinghua <yanjinghua@lakala.com>','liuzijun <liuzijun@lakala.com>','qie <qie@lxfintech.com>','xieqin <xieqin@lakala.com>','luping <luping@lakala.com>','zhouhaocon <zhouhaocong@lakala.com>','wangmengqi <wangmengqi@lakala.com>']

	content = '''
		(由系统每日定时自动发出)
		附件excel中含：\n
    		累计的分商户、分渠道统计；\n
    		昨日的分商户、分渠道统计；\n
	'''

	#生成邮件体
	msg = MIMEMultipart('utf-8')
	msg['From'] = _format_addr(from_addr)
	to_addr = []
	for addr in to_addr_list:
		to_addr.append(_format_addr(addr))
	msg['To'] = ','.join(to_addr)
	msg['Subject'] = Header(u'Paymax 数据统计 '+timeflag, 'utf-8').encode()
	
	body=MIMEText(content)
	msg.attach(body)

	att = MIMEText(open(fileName,'rb').read(),'base64','utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment;filename="%s"' % Header(fileNameWithoutPath, 'utf-8').encode()
	msg.attach(att)

	#连接邮件服务器发送邮件
	server = smtplib.SMTP_SSL(smtp_server, smtp_port)
	# server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, to_addr, msg.as_string())
	server.quit()


def main():

	lastDate = datetime.date.today() - datetime.timedelta(days=1)

	timeflagToday = datetime.date.today().strftime('%y_%m_%d')
	# 日志格式 yyyy-MM-dd
	timeflag = lastDate.strftime('%Y-%m-%d')

	conn=MySQLdb.connect(host='rr-2ze10444nlw3kt70h.mysql.rds.aliyuncs.com',user='payright',passwd='payright',charset='utf8')  
	cursor=conn.cursor()

	sql_merchant = "select b.company_name 公司名称,ifnull(((a.pay_success_amount-a.refund_success_amount)),a.pay_success_amount) 余额,a.pay_success_amount 支付成功金额,ifnull(a.refund_success_amount,0) 退款成功金额,concat(c.create_time,' ') 注册时间,ifnull(c.email,'无') 邮箱,ifnull(c.phone,'无') 手机号 from (select merchant_id,sum(amount) pay_success_amount,sum(refund_amount) refund_success_amount from orders.t_charge_order where status = 'SUCCEED' group by merchant_id) a left join merchant.t_merchant_company b on a.merchant_id = b.merchant_id left join merchant.t_member c on b.merchant_id = c.merchant_id order by pay_success_amount desc"
	sql_partner = "select ifnull(sc.channel_name,'无') 渠道,ifnull(mc.real_name,'无') 销售,b.company_name 公司名称,if(c.merchant_no='{','',c.merchant_no) 商户号,ifnull(((a.pay_success_amount-a.refund_success_amount)),a.pay_success_amount) 余额,a.pay_success_amount 支付成功金额,a.pay_req_num 成功交易笔数,ifnull(a.refund_success_amount,0) 退款成功金额,c.name 支付渠道名称,c.rate 签约费率 from (select merchant_id,channel_id,sum(amount) pay_success_amount,sum(refund_amount) refund_success_amount,count(1) pay_req_num from orders.t_charge_order where status = 'SUCCEED' group by merchant_id,channel_id) a left join (select merchant_id,company_name from merchant.t_merchant_company ) b on a.merchant_id = b.merchant_id left join (select tc.id,tcc.name,tc.rate rate,if(tc.channel_config_id = 6 or tc.channel_config_id = 7 or tc.channel_config_id = 8 or tc.channel_config_id = 9  or tc.channel_config_id = 10  or tc.channel_config_id = 11 or tc.channel_config_id = 12,substring_index(substring_index(tc.parameters,'\"merchant_id\":\"',-1),'\"',1),'') merchant_no from channel.t_channel tc left join channel.t_channel_config tcc on tc.channel_config_id = tcc.id) c on a.channel_id = c.id left join merchant.t_merchant_sale_config msc on msc.merchant_id = a.merchant_id left join merchant.t_member m on msc.sale_id = m.id left join merchant.t_merchant_contacts mc on m.merchant_id = mc.merchant_id left join management.t_sale_channel_member scm on scm.member_id = msc.sale_id left join management.t_sale_channel sc on sc.id = scm.sale_channel_id order by pay_success_amount desc"
	sql_merchant_day = "select b.company_name 公司名称,ifnull(((a.pay_success_amount-a.refund_success_amount)),a.pay_success_amount) 余额,a.pay_success_amount 支付成功金额,ifnull(a.refund_success_amount,0) 退款成功金额,concat(c.create_time,' ') 注册时间,ifnull(c.email,'无') 邮箱,ifnull(c.phone,'无') 手机号 from (select merchant_id,sum(amount) pay_success_amount,sum(refund_amount) refund_success_amount from orders.t_charge_order where status = 'SUCCEED' and date(trade_time) = '%s' group by merchant_id) a left join merchant.t_merchant_company b on a.merchant_id = b.merchant_id left join merchant.t_member c on b.merchant_id = c.merchant_id order by pay_success_amount desc" % (timeflag)
	sql_partner_day = "select ifnull(sc.channel_name,'无') 渠道,ifnull(mc.real_name,'无') 销售,b.company_name 公司名称,if(c.merchant_no='{','',c.merchant_no) 商户号,ifnull(((a.pay_success_amount-a.refund_success_amount)),a.pay_success_amount) 余额,a.pay_success_amount 支付成功金额,a.pay_req_num 成功交易笔数,ifnull(a.refund_success_amount,0) 退款成功金额,c.name 支付渠道名称,c.rate 签约费率 from (select merchant_id,channel_id,sum(amount) pay_success_amount,sum(refund_amount) refund_success_amount,count(1) pay_req_num from orders.t_charge_order where status = 'SUCCEED' and date(trade_time) = '%s' group by merchant_id,channel_id) a left join (select merchant_id,company_name from merchant.t_merchant_company ) b on a.merchant_id = b.merchant_id left join (select tc.id,tcc.name,tc.rate rate,if(tc.channel_config_id = 6 or tc.channel_config_id = 7 or tc.channel_config_id = 8 or tc.channel_config_id = 9  or tc.channel_config_id = 10  or tc.channel_config_id = 11 or tc.channel_config_id = 12,substring_index(substring_index(tc.parameters,'\"merchant_id\":\"',-1),'\"',1),'') merchant_no from channel.t_channel tc left join channel.t_channel_config tcc on tc.channel_config_id = tcc.id) c on a.channel_id = c.id left join merchant.t_merchant_sale_config msc on msc.merchant_id = a.merchant_id left join merchant.t_member m on msc.sale_id = m.id left join merchant.t_merchant_contacts mc on m.merchant_id = mc.merchant_id left join management.t_sale_channel_member scm on scm.member_id = msc.sale_id left join management.t_sale_channel sc on sc.id = scm.sale_channel_id order by pay_success_amount desc" % (timeflag)

	workbook = createExcel()

	fields, results = getDataFromDB(sql_merchant, cursor)
	createSheet(workbook,"分商户统计",fields,results)

	fields, results = getDataFromDB(sql_partner, cursor)
	createSheet(workbook,"分渠道统计",fields,results)

	fields, results = getDataFromDB(sql_merchant_day, cursor)
	createSheet(workbook,lastDate.strftime('%m%d')+"分商户统计",fields,results)

	fields, results = getDataFromDB(sql_partner_day, cursor)
	createSheet(workbook,lastDate.strftime('%m%d')+"分渠道统计",fields,results)

	cursor.close()
	conn.close()

	fileNameWithoutPath = "Paymax 数据统计%s.xls" % (timeflagToday)
	
	fileName = "/data/script/%s" % (fileNameWithoutPath)

	workbook.save(fileName)

	sendEmail(fileName, fileNameWithoutPath, timeflagToday)

	os.remove(fileName)


main()



