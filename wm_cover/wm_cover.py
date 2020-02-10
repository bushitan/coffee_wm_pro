#coding:utf-8

from PIL import Image,ImageDraw,ImageFont
import textwrap

class Base():
    img = None
    def save(self,path):
        self.img.save(path,quality = 100)

class Back(Base):
    def __init__(self):
        self.image_width = 846
        self.image_height = 1235
        self.img = Image.new('RGB', (self.image_width, self.image_height), (255, 255, 255))
        self.font_path = r"ps/字魂58号-创中黑.ttf"
        self.draw = ImageDraw.Draw(self.img)

        self.qr_x = 85
        self.qr_y = 890
        self.qr_size = 200
        self.qr_space = 35 # 二维码与文字的间距
        self.name_x = self.qr_x + self.qr_size + self.qr_space
        self.name_y = self.qr_y
        self.name_size = 55
        self.footer_x = self.name_x
        self.footer_y = 970
        self.footer_width = 19 #最长字符
        self.footer_size = 30
        self.footer_space = 45
    def init_canvas(self):
        pass

    '''
        @method 绘制logo
        @param
            path 路径
            size 所在尺寸大小，以高为主
            y   位置高度
    '''
    def add_logo(self,path,size=320,y=260):
        _logo = Image.open(path)
        _width = _logo.size[0]
        _height = _logo.size[1]
        _real_height = size # 固定logo高度
        _real_width = int(  _width / _height * _real_height )
        _logo = _logo.resize((_real_width,_real_height),Image.ANTIALIAS)
        _x =  int(( self.image_width-_real_width)/2)
        _y = y #
        # self.img.paste(_logo , ( _x,_y), mask=_logo)
        self.img.paste(_logo , ( _x,_y))

    def add_slogan(self,text,size=55,y=180):
        ttfont = ImageFont.truetype(self.font_path,size)
        w, h = self.draw.textsize(text,font=ttfont)
        print (w,h)
        _x = int((self.image_width - w) / 2)
        _y = y
        self.draw.text((_x,_y), str(text), fill=(50,51,51),font=ttfont)

    # 二维码为左端的起点
    def add_qr(self,path):
        _qr = Image.open(path)
        _qr = _qr.resize((self.qr_size,self.qr_size),Image.ANTIALIAS)
        # self.img.paste(_qr , (self.qr_x ,self.qr_y ), mask=_qr)
        self.img.paste(_qr , (self.qr_x ,self.qr_y ))
    def add_name(self,text):
        ttfont = ImageFont.truetype(self.font_path,self.name_size)
        self.draw.text(( self.name_x,self.name_y), str(text), fill=(0,0,0),font=ttfont)

    def add_footer(self,address ,tel):
        ttfont = ImageFont.truetype(self.font_path,self.footer_size)
        lines = textwrap.wrap(address, width=self.footer_width)
        for k, i in enumerate(lines):
            print (k)
            self.draw.text((self.footer_x,self.footer_y + k*self.footer_space), str(i), fill=(0,0,0),font=ttfont)  # 写地址
        self.draw.text((self.footer_x,self.footer_y + (len(lines)) * self.footer_space ), str(tel), fill=(0,0,0),font=ttfont)   # 写号码


class BackLite(Back):
    def __init__(self):
        self.image_width = 591
        self.image_height = 1063
        self.img = Image.new('RGB', (self.image_width, self.image_height), (255, 255, 255))
        self.font_path = r"ps/字魂58号-创中黑.ttf"
        self.draw = ImageDraw.Draw(self.img)

        self.qr_x = 45
        self.qr_y = 775
        self.qr_size = 150
        self.qr_space = 25 # 二维码与文字的间距
        self.name_x = self.qr_x + self.qr_size + self.qr_space
        self.name_y = self.qr_y
        self.name_size = 40
        self.footer_x = self.name_x
        self.footer_y = 835
        self.footer_width = 17 #最长字符
        self.footer_size = 25
        self.footer_space = 30

class Front(Base):
    def __init__(self):
        self.image_width = 846
        self.image_height = 1235
        self.img = Image.new('RGB', (self.image_width, self.image_height), (255, 255, 255))
        self.font_path = r"ps/msyh.ttf"
        self.draw = ImageDraw.Draw(self.img)

        self.sn_x = 15
        self.sn_y = 15
        self.sn_size = 30
        self.qr_size = 500
        self.qr_x = int(( self.image_width - self.qr_size)/2)
        self.qr_y = 153
        self.des_size = 37
        self.des_y = 850

    def add_gb(self,num):
        path = r'ps/8front_6.png'
        if(num == 5):
            path = r'ps/8front_5.png'
        if(num == 8):
            path = r'ps/8front_8.png'
        if(num == 10):
            path = r'ps/8front_10.png'
        _logo = Image.open(path)
        self.img.paste(_logo , ( 0,0))

    def add_sn(self):
        ttfont = ImageFont.truetype(r"C:\\Windows\\Fonts\\STXINGKA.TTF",self.sn_size)
        text = r"小杯子集点卡（SN:45783）"
        self.draw.text((self.sn_x ,self.sn_y), str(text),fill=(89,89,89 )  ,font=ttfont)

    def add_lite_qr(self,path):
        _qr = Image.open(path)
        _qr = _qr.resize((self.qr_size,self.qr_size),Image.ANTIALIAS)
        self.img.paste(_qr , (self.qr_x,self.qr_y))

    def add_des(self,text):
        ttfont = ImageFont.truetype(self.font_path,self.des_size)
        w, h = self.draw.textsize(text,font=ttfont)
        _x = int((self.image_width - w) / 2)
        self.draw.text((_x,self.des_y), str(text), fill=(50,51,51),font=ttfont)

class FrontLite(Front):
    def __init__(self):
        self.image_width = 591
        self.image_height = 1063
        self.img = Image.new('RGB', (self.image_width, self.image_height), (255, 255, 255))
        self.font_path = r"ps/msyh.ttf"
        self.draw = ImageDraw.Draw(self.img)

        self.sn_x = 15
        self.sn_y = 15
        self.sn_size = 25
        self.qr_size = 480
        self.qr_x = int(( self.image_width - self.qr_size)/2)
        self.qr_y = 145
        self.des_size = 26
        self.des_y = 765
    def add_gb(self,num):
        path = r'ps/12front_6.png'
        if(num == 5):
            path = r'ps/12front_5.png'
        if(num == 8):
            path = r'ps/12front_8.png'
        if(num == 10):
            path = r'ps/12front_10.png'
        _logo = Image.open(path)
        self.img.paste(_logo , ( 0,0))

class TaiKa(Base):
    def __init__(self):
        self.image_width = 1181
        self.image_height = 1772
        self.img = Image.new('RGB', (self.image_width, self.image_height), (255, 255, 255))
        self.font_path = r"ps/msyh.ttf"
        self.draw = ImageDraw.Draw(self.img)
    def init_canvas(self):
        pass
    def add_gb(self,num):
        path = r'ps/tk_6.png'
        if(num == 5):
            path = r'ps/tk_5.png'
        if(num == 8):
            path = r'ps/tk_8.png'
        if(num == 10):
            path = r'ps/tk_10.png'
        _logo = Image.open(path)
        self.img.paste(_logo , ( 0,0))

    def add_lite_qr(self,path):
        _qr = Image.open(path)
        _size = 550
        _qr = _qr.resize((_size,_size),Image.ANTIALIAS)
        _x =  int(( self.image_width-_size)/2)
        _y = 470
        self.img.paste(_qr , (_x,_y))

    def add_des(self,text):
        ttfont = ImageFont.truetype(self.font_path,42)
        w, h = self.draw.textsize(text,font=ttfont)
        print (w,h)
        _x = int((self.image_width - w) / 2)
        _y = 1275
        self.draw.text((_x,_y), str(text), fill=(50,51,51),font=ttfont)

class Factory():
    def make(self,obj):
        file = r'result/'
        ########### 8张 ##########
        b = Back()
        b.init_canvas()
        b.add_logo(obj.logo, size=obj.logo_size_8 ,y=obj.logo_y_8)
        b.add_slogan(obj.sloagn,size=obj.slogan_size_8,y=obj.slogan_y_8)
        b.add_qr(obj.host_qr)
        b.add_name(obj.name)
        b.add_footer( obj.address , obj.tel)
        b.save( file + u'8back.jpg')

        f = Front()
        f.add_gb(obj.num)
        f.add_des(obj.des)
        f.save(file + u'8front.jpg')
        f.add_sn()
        f.add_lite_qr(obj.lite_qr)
        f.save(file + u'8front_show.jpg')

        ########### 12张 ##########
        b = BackLite()
        b.init_canvas()
        b.add_logo(obj.logo, size=obj.logo_size_12 ,y=obj.logo_y_12)
        b.add_slogan(obj.sloagn,size=obj.slogan_size_12,y=obj.slogan_y_12)
        b.add_qr(obj.host_qr)
        b.add_name(obj.name)
        b.add_footer( obj.address , obj.tel)
        b.save(file + u'12back.jpg')

        f = FrontLite()
        f.add_gb(obj.num)
        f.add_des(obj.des)
        f.save(file + u'12front.jpg')
        f.add_sn()
        f.add_lite_qr(obj.lite_qr)
        f.save(file + u'12front_show.jpg')

        t = TaiKa()
        t.add_gb(obj.num)
        t.add_des(obj.des)
        t.add_lite_qr(obj.lite_qr)
        t.save(file + u'tk.jpg')

if __name__ == "__main__":
    factory = Factory()
    class obj ():
        ##back
        logo = r'img/logo.jpg'
        sloagn = u"自家烘培咖啡馆"
        host_qr = r'img/qr.jpg'
        name = u"术咖啡"
        address = u"ADD:金平区金墩园6栋北座106金平区金墩园"
        tel = u"TEL: 13592881703"

        ### front
        lite_qr = r'img/brm_store.png'
        num = 10 #点数
        des = u"（到店兑换任意15元内咖啡）"

        # logo 和slogan 的大小
        logo_size_8 = 400   #待修改
        logo_y_8 = 180      #待修改
        slogan_size_8 = 55
        slogan_y_8 = logo_size_8 + logo_y_8

        logo_size_12 = 320  #待修改
        logo_y_12 = 180     #待修改
        slogan_size_12 = 40
        slogan_y_12 = logo_size_12 + logo_y_12

    factory.make(obj)






















