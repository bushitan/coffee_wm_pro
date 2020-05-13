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

                if kwargs['is_web'] is True :
                        web = Web(kwargs['store_id'],kwargs['start'],kwargs['end'])
                        path_qr_file = web.save() # 二维码路径
                else:
		# 测试
                        path_qr_file= r"source\3qr\%s_%s_%s/" %(kwargs['store_id'],kwargs['start'],kwargs['end'])
                print (path_qr_file)
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

	# data =  wm.get_normal_12_data(31,198101,199300 ,front_img="12front.jpg")
	# wm.create( **data)


	# data =  wm.get_normal_12_data(24, 199301,199900  ,front_img="front.jpg" , back_img="back1.jpg")
	# wm.create( **data)
	# data =  wm.get_normal_12_data(24,199901 ,200500  ,front_img="front.jpg" , back_img="back2.jpg")
	# wm.create( **data)
	# data =  wm.get_normal_12_data(24,200501 ,201100  ,front_img="front.jpg" , back_img="back3.jpg")
	# wm.create( **data)




	#data =  wm.get_yzy_data(22,201101,202300 ,front_img="front.jpg")
	#wm.create( **data)
	#data =  wm.get_yzy_data(22,202301,203500 ,front_img="front.jpg")
	#wm.create( **data)

	#data =  wm.get_normal_12_data(53,203501,204100  ,front_img="front.jpg" , back_img="back.jpg")
	#data['is_web']=False
	#wm.create( **data)


	#data =  wm.get_yzy_data(22,204101,205300 ,front_img="front.jpg")
	#data['is_web']=False
	#wm.create( **data)
	#data =  wm.get_yzy_data(22,205301,206500 ,front_img="front.jpg")
	#data['is_web']=True
	#wm.create( **data)

##        # 112 白鲸手作（广场东里店、和平路店）
##	data =  wm.get_normal_12_data(29,206501	,207700,  front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	
##        # 113 Strong
##        data =  wm.get_normal_12_data(24,207701	,208300,  front_img="front.jpg" , back_img="back1.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,208301	,209500,  front_img="front.jpg" , back_img="back2.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,209501	,210100,  front_img="front.jpg" , back_img="back3.jpg")
##	data['is_web']=True
##	wm.create( **data)
##
##        # 114 Strong
##	data =  wm.get_normal_12_data(40,210101	,211300,  front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)

##        # 115 智域咖啡 
##	data =  wm.get_normal_8_data(59,211301	,212500,  front_img="front_8zhang.jpg" , back_img="back_8zhang.jpg")
##	data['is_web']=False
##	wm.create( **data)
##
##        # 116 eco一口 
##	data =  wm.get_normal_12_data(39,212501	,213700,  front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=False
##	wm.create( **data)


##        # 117 白熊咖啡 
##	data =  wm.get_normal_12_data(60,213701,214300,  front_img="12front.jpg" , back_img="12back.jpg")
##	data['is_web']=True
##	print(data)
##	wm.create( **data)

##        # 118 白日梦想家  1200张
##	data =  wm.get_brm_data(17,214301,215500,  front_img="front1.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	print(data)
##	wm.create( **data)
##        # 118 白日梦想家  600张
##	data =  wm.get_brm_data(17,215501,216100,  front_img="front2.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	print(data)
##	wm.create( **data)
##        # 118 白日梦想家  600张
##	data =  wm.get_brm_data(17,216101,216700,  front_img="front3.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	print(data)
##	wm.create( **data)
	
##        # 119 又至园 1200张
##	data =  wm.get_yzy_data(22,216701,217900 ,front_img="front.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	
##        # 120 愉市 1200张
##	data =  wm.get_normal_12_data(8,217901,219100 ,front_img="front.jpg")
##	data['is_web']=True
##	wm.create( **data)


##        # 121  1200张
##	data =  wm.get_normal_12_data(42,219101 , 220300 )
##	data['is_web']=False
##	wm.create( **data)

##        # 122  600张
##	data =  wm.get_normal_12_data(24,220301,220900 , front_img="front.jpg" , back_img="back4.jpg")
##	data['is_web']=False
##	wm.create( **data)


##        # 123  Leisure 600张
##	data =  wm.get_normal_12_data(41,220901,221500 , front_img="front.jpg" , back_img="41back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##
##        # 124  some more 600张
##	data =  wm.get_normal_12_data(46,221501,222100, front_img="front.jpg" , back_img="46back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	
##        # 125  Seeking 1800张
##	data =  wm.get_normal_12_data(28,222101,223900, front_img="front.jpg" , back_img="28back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##
##        # 126  白鲸手作（广场东里 1200张
##	data =  wm.get_normal_12_data(29,223901,225100, front_img="front.jpg" , back_img="29back.jpg")
##	data['is_web']=True
##	wm.create( **data)
	
##        # 127 岂止咖啡 600张
##	data =  wm.get_normal_12_data(49,225101,225700, front_img="front.jpg" , back_img="49back.jpg")
##	data['is_web']=True
##	wm.create( **data)

	
        # 128 Strong
##	data =  wm.get_normal_12_data(24,225701,226300 , front_img="front.jpg" , back_img="back1.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,226301,226900 , front_img="front.jpg" , back_img="back2.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,226901,227500 , front_img="front.jpg" , back_img="back3.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,227501,228100 , front_img="front.jpg" , back_img="back5.jpg")
##	data['is_web']=True
##	wm.create( **data)
	

##        #129 北海白鲸(贵兴店）
##	data =  wm.get_normal_12_data(31,228101,229300 , front_img="12front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(31,229301,229900 , front_img="12front.jpg" , back_img="29back.jpg")
##	data['is_web']=True
##	wm.create( **data)
	
##        #130 愉市
##	data =  wm.get_normal_12_data(8,229901,231100 , front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(8,231101,231700 , front_img="front.jpg" , back_img="8back.jpg")
##	data['is_web']=True
##	wm.create( **data)
		
##        #131 strong
##	data =  wm.get_normal_12_data(24,231701, 232900 , front_img="front.jpg" , back_img="back6.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,232901, 234100 , front_img="front.jpg" , back_img="back6.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(24,234101, 235300 , front_img="front.jpg" , back_img="back6.jpg")
##	data['is_web']=True
##	wm.create( **data)

##        #132 eco
##	data =  wm.get_normal_12_data(39,235301,236500 , front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
        
##        #133 幼稚园
##	data =  wm.get_yzy_data(22,236501,237700, front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)

##        #134 strong
##	data =  wm.get_normal_12_data(24,237701, 238900 , front_img="front.jpg" , back_img="back1.jpg")
##	data['is_web']=True
##	wm.create( **data)

##	#135 strong
##	data =  wm.get_normal_12_data(58,238901,240100, front_img="front.jpg" , back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)

##        # 136 愉市 1200张 + 600 
##	data =  wm.get_normal_12_data(8,240101,241300 ,front_img="front.jpg",back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(8,241301,241900 ,front_img="front.jpg",back_img="8back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	
##        # 137 浮梦造物 1200张 + 600 
##	data =  wm.get_normal_12_data(42,241901,243100 ,front_img="front.jpg",back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_normal_12_data(42,243101,243700 ,front_img="front.jpg",back_img="40back.jpg")
##	data['is_web']=True
##	wm.create( **data)

##        # 138 谢谢轻食馆	 
##	data =  wm.get_normal_12_data(82,243701,244900 ,front_img="front.jpg",back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)

##        # 139 又至园 3000张
##	data =  wm.get_yzy_data(22,244901,246100 ,front_img="front.jpg",back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_yzy_data(22,246101,247300 ,front_img="front.jpg",back_img="back.jpg")
##	data['is_web']=True
##	wm.create( **data)
##	data =  wm.get_yzy_data(22,247301,247900 ,front_img="front.jpg",back_img="22back.jpg")
##	data['is_web']=True
##	wm.create( **data)
        

        # 140 谢谢轻食馆	 
	data =  wm.get_normal_12_data(26,247901,249100 ,front_img="front.jpg",back_img="back.jpg")
	data['is_web']=True
	wm.create( **data)
        
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


