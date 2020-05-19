#coding:utf-8

from PIL import Image,ImageDraw,ImageFont
import textwrap

class Base():

	'''
		输入数据
		input数据
		ouput数据
	'''

	out_path = ""

	def setData(self,**kwargs):
		self.out_path = kwargs['out_path']
		pass

	def _setInput(self):
		pass

	def _setOutput(self):
		self.out_path = "out.jpg"
		pass
