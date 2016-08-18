# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/8/18'
#    __Desc__ = 给出1080*1920分辨率的图片，自动生成android屏幕适配的套图
from PIL import Image
import os

# 获取即将生成的文件夹的名称
def getdirs():
    file = open(r'./modules/cfg.txt', 'rb')
    dirs = []
    for item in file.readlines():
        dirs.append(item.strip('\n').strip('\r'))
    file.close()
    return dirs

# 初始化操作，生成工作目录及图片生成目录
def init():
    dirs = getdirs()
    # generate source and destination
    if not os.path.exists(r'./' + str('source')):
        os.mkdir(r'./'+ str('source'))
    if not os.path.exists(r'./' + str('modules')):
        os.mkdir(r'./' + str('modules'))
        os.open(r'./modules/cfg.txt','wb')
    if not os.path.exists(r'./' + str('destination')):
        os.mkdir(r'./' + str('destination'))
        # generate folders
        for item in dirs:
            print item
            if not os.path.exists(r'./destination/' + item):
                os.mkdir(r'./destination/' + item)

# 获取对应于cfg.txt文件夹下的分辨率比率
def getpercent():
    dirs = getdirs()
    # file = open(r'./modules/percent.txt','wb')
    percent = []
    for item in dirs:
        width,height = item.split('x')
        percent.append(float(int(width)*int(height))/(1080*1920))
    return percent


# 获得源图片的图片名称
def get_true_name(pathname):
    return pathname.split('/')[-1]


# 根据不同的适配方案，生成对应的图片文件名称
def generate_new_name(sourcepath,diritem):
   sourcename= sourcepath.split('/')[-1]
   prefix = sourcename.split('.')[0]
   affix = sourcename.split('.')[-1]
   return str(diritem)+str('/')+prefix+str('-')+str(diritem)+str('.')+affix



def generate_images_by_image(sourcepath,percentlist=getpercent()):
    # 获取生成图片所在的文件夹列表
    dirs = getdirs()
    image = Image.open(sourcepath)
    width,height = image.size
    index = 0
    for item in percentlist:
        resized_image = image.resize((int(width * item), int(height * item)), Image.ANTIALIAS)
        newname = r'./destination/'+generate_new_name(sourcepath,dirs[index])
        print newname
        resized_image.save(newname)
        index +=1

def generate_images__patchly(sourcepath):
    source_images = os.listdir(sourcepath)
    for item in source_images:
        newname = sourcepath+item
        generate_images_by_image(newname, getpercent())


if __name__=="__main__":
    # init()
    # source = r'./source/'
    # generate_images__patchly(source)
    user_input = sys.argv[1]
    if user_input == "init":
        init()
    elif user_input == "generate":
        generate_images__patchly(r'./source/')