#coding:utf-8

import time
import os
import requests
import json
from PIL import Image,ImageDraw,ImageFont
import os
import shutil
import re
import sys
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import shutil
import time
import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas


PATH_BASE = r"source/"
PATH_COVER = PATH_BASE + "1cover/"
PATH_BG = PATH_BASE + "2bg/"
PATH_QR = PATH_BASE + "3qr/"
PATH_IMAGE = PATH_BASE + "4image/"
PATH_OUT = r"pdf/"
class FileBase():

	# 数组拆分
	def arr_size(self,arr,size):
		s=[]
		for i in range(0,int(len(arr))+1,size):
			c=arr[i:i+size]
			if len(c) > 0:
				s.append(c)
		return s

	# 读取所有二维码地址
	# @param
	# 	file_path 包含qr文件夹的地址
	def read_all_qr_path(self,file_path):
		qr_list = []
		for root, dirs, files in os.walk(file_path):
			files = sorted(files,key = lambda i:int(re.match(r'(\d+)',i).group())) #按名字排序
			for f in files:
				qr_list.append(root + f)
			return qr_list

	# 清空图片文件夹
	def clearImageFile(self,image_file):
		if not os.path.exists(image_file):
			os.mkdir(image_file)
		else:
			shutil.rmtree(image_file)
			os.mkdir(image_file)
'''
	@method 生成卡的样式
'''
class PilCard(FileBase):
	def set_num_8(self, qr_x=173 ,qr_y = 153, qr_size=500):
		# 8张的背景尺寸
		self.page_width = 3508
		self.page_height = 2480
		self.page_file = PATH_COVER + "bg_reverse.jpg"
		# 卡的尺寸
		self.card_width = 846
		self.card_height = 1235
		self.space = 0 #20
		self.space_left = 62 #基础28   # 广电打印机23
		self.space_top = 5
		self.rol = 4
		self.col = 2
		# 序列号
		self.sn_space = 15 # SN序列号的空白位置
		self.sn_size = 40
		# 二维码尺寸
		self.qr_x = qr_x #
		self.qr_y = qr_y   #
		self.qr_size = qr_size #

	def set_num_12(self,qr_x=46 ,qr_y = 125, qr_size=500):
		# 12张的背景尺寸
		self.page_width = 2480
		self.page_height = 3508
		self.page_file = PATH_COVER + "bg.jpg"
		# 卡的尺寸
		self.card_width = 591
		self.card_height = 1063
		self.space = 20 #20
		self.space_left = 28 #基础28   # 广电打印机23
		self.space_top = 128
		self.rol = 4
		self.col = 3
		# 序列号
		self.sn_space = 10 # SN序列号的空白位置
		self.sn_size = 25
		# 二维码尺寸
		self.qr_x = qr_x #
		self.qr_y = qr_y   #
		self.qr_size = qr_size #


	# 将正面的元素保存为外卖码
	'''
		@method  将正面的元素保存为外卖码
		@param
			qr_file:String   二维码地址
			front_file:String 正面图片的地址
			sn:Number  序列号
		@return
			card_img 正面图片的内存
	'''
	def front_to_card(self,qr_file,front_file):
		_qr = Image.open(qr_file)
		_qr = _qr.resize((self.qr_size ,self.qr_size))
		# card_img = Image.new('RGB', (self.card_width, self.card_height), (255, 255, 255))
		_front_img = Image.open(front_file)
		_front_img.paste(_qr, (self.qr_x , self.qr_y ), mask=_qr)

		# 写SN序列号
		ttfont = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF",self.sn_size)
		_draw = ImageDraw.Draw(_front_img)
		_sn = qr_file.split("/")[-1].split(".")[0]
		_draw.text((self.sn_space * 2 , self.sn_space * 2), str(u"小杯子集点卡(SN:" + _sn + ")"), fill=(64,56,65 , 120),font=ttfont)
		return _front_img

	# 将正面的元素保存为外卖码
	# 直接复制图片
	def back_to_card(self,back_file):
		_back_img = Image.open(back_file)
		return _back_img

'''
	@method 生成A4的样式
'''
class PilA4(PilCard):
	def draw_mark(self,A4_img):
		_draw = ImageDraw.Draw(A4_img)
		ttfont = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF",40)
		if(self.num == 8):
			self._draw_num8_mark(_draw,ttfont)
		else:
			self._draw_num12_mark(_draw,ttfont)


	def _draw_num8_mark(self,draw,ttfont):
		for i in range(0,self.rol+1):
			_bx = (self.card_width + self.space) * i + self.space_left - 14  # +的x偏移量为14
			for j in range(0,self.col+1):
				_by = (self.card_height + self.space) * j + self.space_top - 20 # +的y偏移量为20
				draw.text((_bx,_by), str("+"), fill=(51,51,51,0),font=ttfont)

	def _draw_num12_mark(self,draw,ttfont):
		for i in range(0,self.rol+1):
			_bx = (self.card_width + self.space  ) * i + self.space_left - 24  # +的x偏移量为24
			for j in range(0,self.col+1):
				_by = (self.card_height + self.space ) * j + self.space_top -  16
				draw.text((_bx,_by), str('+'), fill=(51,51,51,0),font=ttfont)

	# 将外卖码保存为A4大小
	def card_to_A4(self,_card_img_list):
		# _A4_img = Image.new('RGB', (self.page_width, self.page_height), (255, 255, 255))
		_A4_img = Image.open(self.page_file)

		_step = 0
		for i in range(0,self.rol):
			_bx = (self.card_width + self.space) * i + self.space_left
			for j in range(0,self.col):
				_by = (self.card_height + self.space) * j + self.space_top
				_A4_img.paste(_card_img_list[_step], (_bx, _by))
				_step = _step + 1
		self.draw_mark(_A4_img)
		return _A4_img

'''
	@method 生成PDF需要的各种参数
'''
class PilPDF(PilA4):
	def __init__(self,
				 path_qr_file,front_file,back_file,out_file,
				 qr_x ,qr_y,qr_size,num=12,
				 ):
		# super().__init__(path_qr_file,front_file,back_file)
		self.path_qr_file = path_qr_file
		self.front_file = front_file
		self.back_file = back_file
		self.path_image = PATH_IMAGE # 临时图片缓存文件夹
		self.num = num
		self.out_file = out_file
		if(num == 8):
			self.set_num_8( qr_x ,qr_y,qr_size)
		else:
			self.set_num_12(qr_x ,qr_y,qr_size)

	# 合成PDF
	def convertpdf(self,pdfFile,imageList):
		'''多个图片合成一个pdf文件'''
		(w, h) = landscape(A4) #
		# cv = canvas.Canvas(pdfFile, pagesize=landscape(A4))
		_width = self.page_width * 72 / 300
		_height = self.page_height * 72 / 300

		cv = canvas.Canvas(pdfFile, pagesize=(_width, _height) ,pageCompression = 0 )
		# cv = canvas.Canvas(pdfFile )
		for imagePath in imageList:
			# cv.drawImage(imagePath, 0, 0,self.page_width, self.page_height )
			cv.drawImage(imagePath, 0, 0,_width, _height)
			cv.showPage()
		cv.save()

	# 生成正面的图片列表
	def get_card_front_list(self ,qr_list ):
		_card_img_list = []
		for qr_file in qr_list:
			_card_img = self.front_to_card(qr_file, self.front_file)
			_card_img_list.append(_card_img)
		return _card_img_list
	# 生成反面的图片列表
	def get_card_back_list(self ,qr_list ):
		_back_list = []
		for i in range(0,len(qr_list)):
			_back_list.append( self.back_to_card( self.back_file) )
		return  _back_list

	# 制作完整pdf流程
	def save(self):
		self.clearImageFile(PATH_IMAGE) #清空缓存图片
		qr_list = self.read_all_qr_path(self.path_qr_file) # 读取qr列表
		_list = self.arr_size(qr_list,self.num) #将qr列表按数量做拆分
		_A4_list = []
		for i, sub_list in enumerate( _list ):
			_front_img_list = self.get_card_front_list(sub_list)
			_A4_front = self.card_to_A4(_front_img_list)
			_front_name = self.path_image + r"%s.jpg" % (i)
			_A4_front.save(_front_name)
			_A4_list.append(_front_name)

			_back_img_list = self.get_card_back_list(sub_list)
			_A4_back = self.card_to_A4(_back_img_list)
			_back_name = self.path_image + r"%sb.jpg" % (i)
			_A4_back.save(_back_name)
			_A4_list.append(_back_name)
		self.convertpdf(self.out_file,_A4_list)

if __name__  == '__main__':
	store_id = 1
	start = 1
	end = 12
	web = Web(store_id,start,end)
	path_qr_file = web.save() # 二维码路径
	front_file = PATH_COVER + str(store_id) + r'/front.jpg' #正面路径
	back_file = PATH_COVER + str(store_id) + r'/back.jpg'	#反面路径
	out_file = PATH_OUT + "%s_%s_%s.pdf" % (store_id,start,end)	#pdf输出路径
	pdf = PilPDF(path_qr_file ,front_file , back_file,out_file,num=12)
	pdf.save()



	# path_qr_file = r"source/3qr/1_1_10/"
	# print( pdf.path_qr_file)

	# wm_utils.process()