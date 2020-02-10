#coding:utf-8
from web import *
from pdf import PilPDF

class WmMach():

	# 测试
	def get_normal_8_data(self,store_id,start,end,front_img="front.jpg",back_img="back.jpg"):
		return {
			'store_id':store_id,'start':start,'end':end,
			'front_img':front_img ,'back_img':back_img,
			'qr_x':173 ,'qr_y' : 153,'qr_size':500 ,
			'num':8
		}
		# 测试
	def get_normal_12_data(self,store_id,start,end,front_img="front.jpg",back_img="back.jpg"):
		return {
			'store_id':store_id,'start':start,'end':end,
			'front_img':front_img ,'back_img':back_img,
			'qr_x':46 ,'qr_y' : 125,'qr_size':500 ,
			'num':12
		}
	# 白日梦想家
	def get_brm_data(self,store_id,start,end,front_img="front.jpg",back_img="back.jpg"):
		return {
			'store_id':store_id,'start':start,'end':end,
			'front_img':front_img ,'back_img':back_img,
			'qr_x':165 ,'qr_y' : 725,'qr_size':260 ,
			'num':12
		}
	# 又至园
	def get_yzy_data(self,store_id,start,end,front_img="front.jpg",back_img="back.jpg"):
		return {
			'store_id':store_id,'start':start,'end':end,
			'front_img':front_img ,'back_img':back_img,
			'qr_x':165 ,'qr_y' : 635,'qr_size':260 ,
			'num':12
		}

	def get_store_qr(self,store_id,start,end):
		web = Web(store_id,start,end)
		path_qr_file = web.save() # 二维码路径
	def create(
			self,**kwargs
			# store_id,start,end,
			# front_img , back_img,
			# qr_x=46 ,qr_y = 125, qr_size=500 ,num=12
	):

		web = Web(kwargs['store_id'],kwargs['start'],kwargs['end'])
		path_qr_file = web.save() # 二维码路径

		# 测试
		# path_qr_file= r"C:\lab\git\coffee\coffee_wm_pro\wm_mach\source\3qr\29_196301_197500/"

		front_file = PATH_COVER + str(kwargs['store_id']) + "/" + kwargs['front_img'] #正面路径
		back_file = PATH_COVER + str(kwargs['store_id']) + "/" + kwargs['back_img']	#反面路径
		out_file = PATH_OUT + "%s_%s_%s.pdf" % (kwargs['store_id'],kwargs['start'],kwargs['end'])	#pdf输出路径
		# pdf = PilPDF(path_qr_file ,front_file , back_file,out_file,
		# 			 qr_x=46 ,qr_y = 125, qr_size=500,num=12)
		pdf = PilPDF(path_qr_file ,front_file , back_file,out_file,
					 qr_x=kwargs['qr_x'] ,qr_y = kwargs['qr_y'], qr_size=kwargs['qr_size'],num=kwargs['num'])
		pdf.save()

if __name__  == '__main__':
	wm = WmMach()
	#wm.get_store_qr(17,101,101)


	# data =  wm.get_yzy_data(22,195101,196300,front_img="front.jpg")
	# wm.create( **data)

	# data =  wm.get_normal_12_data(29,196301,197500,front_img="12front.jpg")
	# wm.create( **data)

	# data =  wm.get_yzy_data(22,197501,198100 ,front_img="front.jpg")
	# wm.create( **data)

	data =  wm.get_normal_12_data(31,198101,199300 ,front_img="12front.jpg")
	wm.create( **data)


	data =  wm.get_normal_12_data(24, 199301,199900  ,front_img="front.jpg" , back_img="back1.jpg")
	wm.create( **data)
	data =  wm.get_normal_12_data(24,199901 ,200500  ,front_img="front.jpg" , back_img="back2.jpg")
	wm.create( **data)
	data =  wm.get_normal_12_data(24,200501 ,201100  ,front_img="front.jpg" , back_img="back3.jpg")
	wm.create( **data)
	# data =  wm.get_yzy_data(22,35001,35012)
	# print (data)















	# wm.create(store_id=1,start=1,end=8,
	# 	front_img="8front.jpg" , back_img="8front.jpg",qr_x=173 ,qr_y = 153, qr_size=500 ,num=8)


	# store_id = 1
	# start = 1
	# end = 8
	# # web = Web(store_id,start,end)
	# # path_qr_file = web.save() # 二维码路径
	# path_qr_file = r"C:\lab\git\coffee\coffee_wm_pro\wm_mach\source\3qr\1_1_8/"
	# front_file = PATH_COVER + str(store_id) + r'/8front.jpg' #正面路径
	# back_file = PATH_COVER + str(store_id) + r'/8back.jpg'	#反面路径
	# out_file = PATH_OUT + "%s_%s_%s.pdf" % (store_id,start,end)	#pdf输出路径
	# # pdf = PilPDF(path_qr_file ,front_file , back_file,out_file,
	# # 			 qr_x=46 ,qr_y = 125, qr_size=500,num=12)
	# pdf = PilPDF(path_qr_file ,front_file , back_file,out_file,
	# 			 qr_x=173 ,qr_y = 153, qr_size=500,num=8)
	# pdf.save()


