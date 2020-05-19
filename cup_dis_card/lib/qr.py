#coding:utf-8
from .draw import *
import os
import requests
import json


class QR(Draw):


	def qr_get_token(self,app_id , app_secret):
			url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (app_id , app_secret)
			r = requests.get(url)
			return json.loads( r.text)["access_token"]
	'''
		@method 2 向微信获取二维码
	'''
	def qr_get(self,access_token ,data,file_path):
		# url = 'https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token=%s' % (access_token)
		url = 'https://api.weixin.qq.com/wxa/getwxacode?access_token=%s' % (access_token)
		headers = {'content-type': 'application/json'}
		r = requests.post(url,data=json.dumps(data), headers=headers )
		f=open(file_path,"wb")
		f.write(r.content)
		f.close()
		return True
	# def file_