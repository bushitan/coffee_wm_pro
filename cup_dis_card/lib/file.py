#coding:utf-8
from base import *
import os

class File(Base):


	'''
		@method 检测文件夹是否存在
	'''
	def file_check_exists(self,image_file):

		if not os.path.exists(image_file):
			os.mkdir(image_file)


	'''
		@method 创建文件夹
	'''
	def file_make(self):
		pass

	# def file_