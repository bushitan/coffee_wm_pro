#coding:utf-8

import time
import os
import requests
import json


PATH_BASE = r"source/"
PATH_COVER = PATH_BASE + "1cover/"
PATH_BG = PATH_BASE + "2bg/"
PATH_QR = PATH_BASE + "3qr/"
PATH_IMAGE = PATH_BASE + "4image/"
PATH_OUT = r"pdf/"
class Base():
	def __init__(self):
		self.create_file_path(PATH_COVER)
		self.create_file_path(PATH_BG)
		self.create_file_path(PATH_QR)
		self.create_file_path(PATH_IMAGE)
		self.create_file_path(PATH_OUT)
	# 创建文件夹
	def create_file_path(self,file_path):
		if  os.path.exists(file_path) is False:
			os.makedirs(file_path)
			return file_path
		else :
			return False

	'''
        @method 1 获取token
    '''
	def get_token(self,app_id , app_secret):
		url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (app_id , app_secret)
		r = requests.get(url)
		return json.loads( r.text)["access_token"]
	'''
		@method 2 向微信获取二维码
	'''
	def get_qr(self,access_token ,data,file_path):
		url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
		headers = {'content-type': 'application/json'}
		r = requests.post(url,data=json.dumps(data), headers=headers )
		f=open(file_path,"wb")
		f.write(r.content)
		f.close()
		return True

class Web(Base):
	URL_GET_WM_TIKECT = "http://123.207.38.251/dev/lite/print/get/wm_list/" # 获取外卖的API
	APP_ID = "wxd19bbe9cb3b293b6"
	APP_SECRET = "931ad8364ea6a1327ed65282af330415"
	token = ""
	path_qr_file = ""
	def __init__(self, store_id,start ,end ,qr_size=500):
		super().__init__()
		self.store_id = store_id
		self.start = start
		self.end = end
		self.qr_size = qr_size
	'''
		@method 获取二维码数组
	'''
	def get_ticket_web(self):
		url = self.URL_GET_WM_TIKECT
		data = {
			'token': 'bushitan',
			'start': self.start,
			'end': self.end,
		}
		r = requests.post(url, data=data)
		res = json.loads(r.content.decode('utf-8'))
		wm_list =  res['data']['wm_list']
		for i in wm_list:
			if  i['store_id'] != self.store_id:
				msg = u"店铺store_id不对,外卖编号：%s，店铺：%s" % ( i['short_id'], i['store_id'] )
				print ( msg)
				raise (msg)
			# print( i['store_id'],i['short_uuid'] )
		return wm_list

	def get_image_list(self,ticket_list):
		for t in ticket_list:
			short_uuid = t['short_uuid']
			self.path_qr_file = PATH_QR + "%s_%s_%s/" %(self.store_id , self.start , self.end)  #  文件命名
			self.create_file_path(self.path_qr_file) # 穿件外卖码的文件夹
			_qr_path = self.path_qr_file + "%s.png" %(t['short_id'])  #  文件命名
			_data = {
				"scene":"wm_%s" % (short_uuid),
				"is_hyaline" :True,
				"width":self.qr_size,
			}
			self.get_qr( self.token ,_data ,_qr_path)

	'''
		@method 执行外卖码下载，返回生成的路径
		@return
			path_qr_file 外卖码下载到的文件夹
	'''
	def save(self):
		_list = self.get_ticket_web()
		self.token = self.get_token( self.APP_ID ,self.APP_SECRET )
		self.get_image_list(_list)
		return self.path_qr_file

if __name__  == '__main__':
	store_id = 1
	start = 1
	end = 12
	web = Web(store_id,start,end)
	path_qr_file = web.save() # 二维码路径
	front_file = PATH_COVER + str(store_id) + r'/front.jpg' #正面路径
	back_file = PATH_COVER + str(store_id) + r'/back.jpg'	#反面路径
	out_file = PATH_OUT + "%s_%s_%s.pdf" % (store_id,start,end)	#pdf输出路径
	pdf = PDF(path_qr_file ,front_file , back_file,out_file,num=12)
	pdf.save()



	# path_qr_file = r"source/3qr/1_1_10/"
	# print( pdf.path_qr_file)

	# wm_utils.process()