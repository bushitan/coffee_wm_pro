#coding:utf-8

from .file import *
from PIL import Image,ImageDraw,ImageFont

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
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class Draw(File):

	'''
		@method 创建画布
		@param
			mode  图片格式 RGB  CMYK
	'''
	img = None
	def draw_create(self,width,height,mode='RGB'):
		self.image_width = width
		self.image_height = height
		self.img = Image.new(mode, (self.image_width, self.image_height), (255, 255, 255))
		self.draw = ImageDraw.Draw(self.img)

	'''
		@method 重新绘制CMYK的画面
	'''
	def draw_save(self):
		# self.img.convert('CMYK')
		# self.img.save(self.out_path,quality = 100)


		_img = Image.new("RGB", (self.image_width, self.image_height), (255, 255, 255))
		_img.paste(self.img, ( 0 , 0 ))
		_img.save(self.out_path,quality = 100)



	'''
		@method 写文字
		@param

		@return
	'''
	def draw_text(self,text, x,y, color , type="" ,size=20, line_length=50 ):
		font = r"C:\\Windows\\Fonts\\STXINGKA.TTF"
		if type != "":
			font =  r"C:\\Windows\\Fonts\\%s" % (type)

		# font = r"C:\\Windows\\Fonts\\HYQiHeiX1-65W.otf"

		# text = u"1商务大厦23213".encode("utf-8")
		ttfont = ImageFont.truetype(font,size)
		self.draw.text(( x,y), text, fill=color,font=ttfont)

		# _space = 43
		# ttfont = ImageFont.truetype(font,size)
		# lines = textwrap.wrap(text, width=line_length)
		# print (lines)
		# for k, i in enumerate(lines):
		# 	print (k,i)
		# 	self.draw.text(( x ,y + k*_space), str(i), color,font=ttfont)  # 写地址


	'''
		@method 画logo
		@param
		@return
	'''
	def draw_logo(self,image_path,x,y,width,height ):

		_qr = Image.open(image_path)
		_qr = _qr.resize(( width ,height))
		self.img.paste(_qr, ( x , y ))

		pass

	def draw_logo(self, image_path,x,y,width ,height):
		ima = Image.open(image_path).convert("RGBA")
		size = ima.size
		print(size)

		# 因为是要圆形，所以需要正方形的图片
		r2 = min(size[0], size[1])
		if size[0] != size[1]:
			ima = ima.resize((r2, r2), Image.ANTIALIAS)

		# 最后生成圆的半径
		r3 = int(size[0]/2)
		imb = Image.new('RGBA', (r3*2, r3*2),(255,255,255,0))
		pima = ima.load() # 像素的访问对象
		pimb = imb.load()
		r = float(r2/2) #圆心横坐标

		for i in range(r2):
			for j in range(r2):
				lx = abs(i-r) #到圆心距离的横坐标
				ly = abs(j-r)#到圆心距离的纵坐标
				l = (pow(lx,2) + pow(ly,2))** 0.5 # 三角函数 半径

				if l < r3:
					pimb[i-(r-r3),j-(r-r3)] = pima[i,j]

		imb = imb.resize(( width ,height))
		self.img.paste(imb, ( x,y) ,mask=imb )
		# imb.save("test_circle.png")


	def draw_png(self,image_path ,x , y , width , height):
		_qr = Image.open(image_path)
		_qr = _qr.resize(( width ,height))
		self.img.paste(_qr, ( x , y ),mask=_qr)


	def draw_image(self,image_path ,x , y , width , height):
		_qr = Image.open(image_path)
		_qr = _qr.resize(( width ,height))
		self.img.paste(_qr, ( x , y ))
		# self.img.paste(_qr, ( x , y ), mask=_qr)
		pass


