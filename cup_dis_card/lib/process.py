#coding:utf-8
from qr import *
import os
# import sys
# # reload(sys)
# # sys.setdefaultencoding('utf8')
class Process(QR):


	'''
		param
			store_id: 门店ID
			logo：图片地址
			name：店铺名字
			qr:二维码地址
			reward ： 奖励
			condition ： 条件

			bg：背景图
			bg_width：背景宽度
			bg_height：背景高度


	'''

	def get_qr(self,store_id,qr_image):

		# 下载二维码

		token = self.qr_get_token(
			"wxcd49aa99fd3d1f6a",
			"6987d998aa8d01b4a8a6ad405386a239"
		)
		_data = {
			"path":"pages/route/route?shop_id=" + str(store_id),
			"is_hyaline" :True,
			"width":500,
		}
		self.qr_get( token ,_data ,qr_image)

	def make_cover(self,**kwargs):
		print (123)

		store_id = 2


		_file_path = os.getcwd() + r"\store\%s" % ( store_id)
		self.file_check_exists(_file_path)

		_bg_image = os.getcwd() + r"/static/bg.jpg"
		_qr_image = os.getcwd() + r"/store/%s/qr.jpg"	% ( store_id)
		_logo_image = os.getcwd() + r"/store/%s/%s.jpg"	% ( store_id,"logo")

		self.setData(
			out_path = r"%s/%s.jpg" % (_file_path,"cover")
		)

		if kwargs.has_key("is_web_qr") is False:
			is_web_qr = False
		else:
			is_web_qr = kwargs['is_web_qr']
		if is_web_qr == True  :
			self.get_qr(store_id,_qr_image)



		# 绘制
		_cover_width = 1275
		_cover_height = 1789

		self.draw_create(_cover_width,_cover_height,"RGB") # 生成图片
		self.draw_image(_bg_image,0,0,_cover_width,_cover_height) # 画背景
		self.draw_png(_qr_image,495,307,280,280) # 画二维码
		self.draw_logo(_logo_image,571,382,129,129) # 画logo


		self.draw_text(u"先享8.8折优惠",283,778,(255,255,255),type=u"ALIBABA-PUHUITI-HEAVY.OTF" , size=100) # 画logo
		self.draw_text(u"七天内消费3次",283,1207,(40,164,57),type=u"ALIBABA-PUHUITI-HEAVY.OTF" , size=100) # 画logo
		self.draw_text(u"活动说明：在seeking桃源店7天内消费3次，每次消费",283,1355,(42,164,57),type=u"ALIBABA-PUHUITI-MEDIUM.OTF" , size=30) # 画logo
		self.draw_text(u"满20元，立享8.8折优惠",283,1395,(42,164,57),type=u"ALIBABA-PUHUITI-MEDIUM.OTF" , size=30) # 画logo
		# self.draw_text(u"2132121",100,500,300) # 画logo






		# self.draw_image(_qr_image,0,0,500,500)
		# self.draw_image(_logo_image,200,200,200,200)


		self.draw_save()
		pass

