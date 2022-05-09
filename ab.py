import os.path
import sys
import time

from win32com.client import Dispatch

asdfad = 1
isjilu = True
zongbiaoshi_num = 100
tianjiangxiangrui_num = 100
mukui_num = 100
wokouxiaotoumu_num = 100
jiutianxuannv_num = 100
da_x = 0
da_y = 0
xiao_x = 9999
xiao_y = 9999


def isfight():
    """
    当前是否在战斗
    :return:
    """
    dm_ret = dm.FindPic(0, 0, 1256, 700, 'zhandou.bmp', '050505', 0.8, 0)
    if dm_ret[0] == -1:
        print('没在战斗')
        return False
    else:
        print('在战斗')
        return True


def move_to():
    """
    移动到下一个坐标点
    x = random.randint(0, 550)
    :return:
    """
    global asdfad
    # print('五指山移动到下一个坐标点')
    if asdfad < 100:
        dm.MoveTo(490 + (20 * 3), 350)
    elif asdfad == 100:
        dm.MoveTo(490, 350 - (20 * 10))
    elif asdfad < 200:
        dm.MoveTo(490 - (20 * 3), 350)
    elif asdfad == 200:
        dm.MoveTo(490 + (20 * 3), 350 + (20 * 10))
    asdfad = asdfad + 1
    if asdfad == 201:
        asdfad = 0
    dm.RightClick()
    time.sleep(2)


def zuorenwu(name, zuobiao_x, zuobiao_y):
    global zongbiaoshi_num
    global tianjiangxiangrui_num
    global mukui_num
    global wokouxiaotoumu_num
    global jiutianxuannv_num
    global isjilu
    dm_ret = dm.FindPic(0, 0, 1256, 700, 'zhandou.bmp', '050505', 0.9, 0)
    duihua1 = dm.FindPic(0, 0, 1256, 700, 'duihua1.bmp', '050505', 0.9, 0)
    if dm_ret[0] != -1:
        # print('在战斗')
        time.sleep(2)
        if isjilu:
            isjilu = False
            if '总镖师' == name:
                zongbiaoshi_num = zongbiaoshi_num - 1
            elif '天降祥瑞' == name:
                tianjiangxiangrui_num = tianjiangxiangrui_num - 1
            elif '木魁' == name:
                mukui_num = mukui_num - 1
            elif '倭寇小头目' == name:
                wokouxiaotoumu_num = wokouxiaotoumu_num - 1
            elif '九天玄女' == name:
                jiutianxuannv_num = jiutianxuannv_num - 1
        zuorenwu(name, zuobiao_x, zuobiao_y)
    elif duihua1[0] != -1:
        # print('对话')
        global da_x
        global da_y
        global xiao_x
        global xiao_y
        if zuobiao_x > 490:
            if da_x < zuobiao_x:
                da_x = zuobiao_x
        else:
            if xiao_x > zuobiao_x:
                xiao_x = zuobiao_x
        if zuobiao_y > 350:
            if da_y < zuobiao_y:
                da_y = zuobiao_y
        else:
            if xiao_y > zuobiao_y:
                xiao_y = zuobiao_y
        print('小x ' + str(xiao_x) + ' 小y ' + str(xiao_y) + ' 大x ' + str(da_x) + ' 大y ' + str(da_y))
        dm.MoveTo(int(duihua1[-2] + 20), int(duihua1[-1] + 5))
        dm.LeftClick()
        time.sleep(3)
        isjilu = True
        zuorenwu(name, zuobiao_x, zuobiao_y)
    else:
        pass


def zuorensdfsdfwu():
    global zongbiaoshi_num
    global tianjiangxiangrui_num
    global mukui_num
    global wokouxiaotoumu_num
    global jiutianxuannv_num
    jiutianxuannv1 = dm.FindPicEx(0, 150, 1256, 700,
                                  'zongbiaoshi1.bmp|tianjiangxiangrui1.bmp|mukui1.bmp|wokouxiaotoumu1.bmp|jiutianxuannv1.bmp',
                                  '050505', 0.9, 0)
    if len(jiutianxuannv1) != 0:
        strlist = jiutianxuannv1.split('|')
        for guai in strlist:
            # print('点怪')
            zuobiao = guai.split(',')
            dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
            dm.LeftClick()
            time.sleep(1)
            if zuobiao[0] == '0':
                if zongbiaoshi_num > 0:
                    zuorenwu('总镖师', int(zuobiao[-2]), int(zuobiao[-1]))
            elif zuobiao[0] == '1':
                if tianjiangxiangrui_num > 0:
                    zuorenwu('天降祥瑞', int(zuobiao[-2]), int(zuobiao[-1]))
            elif zuobiao[0] == '2':
                if mukui_num > 0:
                    zuorenwu('木魁', int(zuobiao[-2]), int(zuobiao[-1]))
            elif zuobiao[0] == '3':
                if wokouxiaotoumu_num > 0:
                    zuorenwu('倭寇小头目', int(zuobiao[-2]), int(zuobiao[-1]))
            elif zuobiao[0] == '4':
                if jiutianxuannv_num > 0:
                    zuorenwu('九天玄女', int(zuobiao[-2]), int(zuobiao[-1]))
    move_to()


if __name__ == '__main__':
    # pyinstaller -F -w main.py
    dm = Dispatch('dm.dmsoft')
    ret = dm.reg('hokki198785057a83d7c6d9c0417a65d06e7a32de', 'FwE0fqI')
    hwnd = dm.EnumWindow(0, '桃源二区   各位都是垃圾 ID:225', 'SunAwtFrame', 1 + 2)
    dm.BindWindow(hwnd, 'gdi', 'windows2', 'windows', 0)
    pash = os.path.join(sys.path[1], '') + 'pic\\'
    dm.SetPath(pash)
    dm.MoveWindow(hwnd, 0, 0)
    dm.MoveTo(490, 350)
    dm.RightClick()
    while True:
        zuorensdfsdfwu()
#
    print('程序结束')
