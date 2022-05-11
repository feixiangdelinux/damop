import os.path
import sys
import time

from win32com.client import Dispatch

asdfad = 0
isjilu = True
zongbiaoshi_num = 100 - 38
tianjiangxiangrui_num = 100 - 45
mukui_num = 100 - 100
wokouxiaotoumu_num = 100 - 62
jiutianxuannv_num = 100 - 100


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
    # global asdfad
    # # print('五指山移动到下一个坐标点')
    # if asdfad < 100:
    #     dm.MoveTo(490 + (20 * 3), 350)
    # elif asdfad == 100:
    #     dm.MoveTo(490, 350 - (20 * 10))
    # elif asdfad < 200:
    #     dm.MoveTo(490 - (20 * 3), 350)
    # elif asdfad == 200:
    #     dm.MoveTo(490 + (20 * 3), 350 + (20 * 10))
    # asdfad = asdfad + 1
    # if asdfad == 201:
    #     asdfad = 0
    # dm.RightClick()
    # time.sleep(2)

    global asdfad
    # print('五指山移动到下一个坐标点')
    if asdfad == 0:
        dm.MoveTo(490, 350 + (20 * 10))
        time.sleep(1)
    elif asdfad < 75:
        dm.MoveTo(490 + (20 * 3), 350 + (20 * 10))
    elif asdfad == 75:
        dm.MoveTo(490, 350)
        time.sleep(1)
    elif asdfad < 149:
        dm.MoveTo(490 - (20 * 3), 350)
    elif asdfad == 149:
        asdfad = -1
    asdfad = asdfad + 1
    dm.RightClick()
    time.sleep(1)
    dm.MoveTo(280, 30)
    time.sleep(1)


def zuorenwu(name, zuobiao_x, zuobiao_y):
    global zongbiaoshi_num
    global tianjiangxiangrui_num
    global mukui_num
    global wokouxiaotoumu_num
    global jiutianxuannv_num
    global isjilu
    dm_ret = dm.FindPic(0, 0, 956, 700, 'zhandou.bmp', '050505', 0.9, 0)
    duihua1 = dm.FindPic(0, 0, 956, 700, 'duihua1.bmp', '050505', 0.9, 0)
    taiyuan = dm.FindStrFast(0, 0, 956, 700, '你距离太远', 'ffff0b-101010', 1.0)
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
        dm.MoveTo(int(duihua1[-2] + 20), int(duihua1[-1] + 5))
        dm.LeftClick()
        time.sleep(3)
        isjilu = True
        zuorenwu(name, zuobiao_x, zuobiao_y)
    #     if dm_ret[0] != -1:
    elif taiyuan[0] != -1:
        # print('太远了')
        # 如果是太远了,记录x,y坐标,以后超过这个坐标的就不在点击了
        # print('点击x ' + str(zuobiao_x) + '点击y ' + str(zuobiao_y) + '小x ' + str(xiao_x) + ' 小y ' + str(
        #     xiao_y) + ' 大x ' + str(da_x) + ' 大y ' + str(da_y))
        pass
    else:
        # print('都不是')
        pass


def zuorensdfsdfwu():
    global zongbiaoshi_num
    global tianjiangxiangrui_num
    global mukui_num
    global wokouxiaotoumu_num
    global jiutianxuannv_num
    renwuzuobiao = dm.FindPicEx(0, 0, 956, 700, 'haigui1.bmp|haigui2.bmp|haigui3.bmp|haigui4.bmp', '050505', 0.95, 0)
    if len(renwuzuobiao) != 0:
        zuobiao = renwuzuobiao.split(',')
        jiutianxuannv1 = dm.FindPicEx(int(zuobiao[-2]) - 100, int(zuobiao[-1]) - 100, int(zuobiao[-2]) + 100,
                                      int(zuobiao[-1]) + 100,
                                      'zongbiaoshi1.bmp|tianjiangxiangrui1.bmp|mukui1.bmp|wokouxiaotoumu1.bmp|jiutianxuannv1.bmp',
                                      '050505', 0.98, 0)
        if len(jiutianxuannv1) != 0:
            strlist = jiutianxuannv1.split('|')
            for guai in strlist:
                # print('点怪')
                zuobiao = guai.split(',')
                if zuobiao[0] == '0':
                    if zongbiaoshi_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('总镖师', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '1':
                    if tianjiangxiangrui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('天降祥瑞', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '2':
                    if mukui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('木魁', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '3':
                    if wokouxiaotoumu_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('倭寇小头目', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '4':
                    if jiutianxuannv_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('九天玄女', int(zuobiao[-2]), int(zuobiao[-1]))
        jiutianxuannv1 = dm.FindPicEx(int(zuobiao[-2]) - 100, int(zuobiao[-1]) - 100, int(zuobiao[-2]) + 100,
                                      int(zuobiao[-1]) + 100,
                                      'zongbiaoshi2.bmp|tianjiangxiangrui2.bmp|mukui2.bmp|wokouxiaotoumu2.bmp|jiutianxuannv2.bmp',
                                      '050505', 0.98, 0)
        if len(jiutianxuannv1) != 0:
            strlist = jiutianxuannv1.split('|')
            for guai in strlist:
                # print('点怪')
                zuobiao = guai.split(',')
                if zuobiao[0] == '0':
                    if zongbiaoshi_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('总镖师', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '1':
                    if tianjiangxiangrui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('天降祥瑞', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '2':
                    if mukui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('木魁', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '3':
                    if wokouxiaotoumu_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('倭寇小头目', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '4':
                    if jiutianxuannv_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('九天玄女', int(zuobiao[-2]), int(zuobiao[-1]))
        jiutianxuannv1 = dm.FindPicEx(int(zuobiao[-2]) - 100, int(zuobiao[-1]) - 100, int(zuobiao[-2]) + 100,
                                      int(zuobiao[-1]) + 100,
                                      'zongbiaoshi3.bmp|tianjiangxiangrui3.bmp|mukui3.bmp|wokouxiaotoumu3.bmp|jiutianxuannv3.bmp',
                                      '050505', 0.98, 0)
        if len(jiutianxuannv1) != 0:
            strlist = jiutianxuannv1.split('|')
            for guai in strlist:
                # print('点怪')
                zuobiao = guai.split(',')
                if zuobiao[0] == '0':
                    if zongbiaoshi_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('总镖师', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '1':
                    if tianjiangxiangrui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('天降祥瑞', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '2':
                    if mukui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('木魁', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '3':
                    if wokouxiaotoumu_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('倭寇小头目', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '4':
                    if jiutianxuannv_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('九天玄女', int(zuobiao[-2]), int(zuobiao[-1]))
        jiutianxuannv1 = dm.FindPicEx(int(zuobiao[-2]) - 100, int(zuobiao[-1]) - 100, int(zuobiao[-2]) + 100,
                                      int(zuobiao[-1]) + 100,
                                      'zongbiaoshi4.bmp|tianjiangxiangrui4.bmp|mukui1.bmp|wokouxiaotoumu4.bmp|jiutianxuannv4.bmp',
                                      '050505', 0.98, 0)
        if len(jiutianxuannv1) != 0:
            strlist = jiutianxuannv1.split('|')
            for guai in strlist:
                # print('点怪')
                zuobiao = guai.split(',')
                if zuobiao[0] == '0':
                    if zongbiaoshi_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('总镖师', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '1':
                    if tianjiangxiangrui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('天降祥瑞', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '2':
                    if mukui_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('木魁', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '3':
                    if wokouxiaotoumu_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('倭寇小头目', int(zuobiao[-2]), int(zuobiao[-1]))
                elif zuobiao[0] == '4':
                    if jiutianxuannv_num > 0:
                        dm.MoveTo(int(zuobiao[-2]), int(zuobiao[-1]))
                        dm.LeftClick()
                        dm.MoveTo(280, 30)
                        time.sleep(1)
                        zuorenwu('九天玄女', int(zuobiao[-2]), int(zuobiao[-1]))
    move_to()


if __name__ == '__main__':
    # pyinstaller -F -w main.py
    dm = Dispatch('dm.dmsoft')
    ret = dm.reg('hokki198785057a83d7c6d9c0417a65d06e7a32de', 'FwE0fqI')
    hwnd = dm.EnumWindow(0, '桃源二区   各位都是垃圾 ID:225', 'SunAwtFrame', 1 + 2)
    dm.BindWindow(hwnd, 'gdi', 'windows2', 'windows', 0)
    # dm.BindWindow(hwnd, 'gdi', 'normal', 'windows', 0)
    pash = os.path.join(sys.path[1], '') + 'pic\\'
    dm.SetPath(pash)
    dm.SetDict(0, '12.txt')
    dm.MoveWindow(hwnd, 0, 0)
    va = zongbiaoshi_num > 0 or tianjiangxiangrui_num > 0 or mukui_num > 0 or wokouxiaotoumu_num > 0 or jiutianxuannv_num > 0
    while va:
        zuorensdfsdfwu()
        va = zongbiaoshi_num > 0 or tianjiangxiangrui_num > 0 or mukui_num > 0 or wokouxiaotoumu_num > 0 or jiutianxuannv_num > 0
        print('总镖师:' + str(100 - zongbiaoshi_num) + ' 天降祥瑞:' + str(100 - tianjiangxiangrui_num) + ' 木魁:' + str(
            100 - mukui_num) + ' 倭寇小头目:' + str(100 - wokouxiaotoumu_num) + ' 九天玄女:' + str(100 - jiutianxuannv_num))
    print('程序结束')

    # renwuzuobiao = dm.FindPicEx(0, 0, 956, 700, 'haigui1.bmp|haigui2.bmp|haigui3.bmp|haigui4.bmp', '050505', 0.95, 0)
    # if len(renwuzuobiao) != 0:
    #     zuobiao = renwuzuobiao.split(',')
    #     print(zuobiao[-2])
    #     print(zuobiao[-1])
    #     dm.Capture(int(zuobiao[-2]) - 100, int(zuobiao[-1]) - 100, int(zuobiao[-2]) + 100, int(zuobiao[-1]) + 100, '1111111.bmp')

    # dm.Capture(667, 343, 667+100, 343+100, '1111111.bmp')

    # jiutianxuannv1 = dm.FindPicEx(150, 80, 900, 610,
    #                               'jiutianxuannv1.bmp|wokouxiaotoumu1.bmp',
    #                               '050505', 0.9, 0)
    # print(jiutianxuannv1)
    # dm.MoveTo(616, 282)

    # dm.Capture(110, 75, 900, 590,'1111111.bmp')
    # dm.MoveWindow(hwnd, 0, 0)
    # dm.MoveTo(490, 350)
    # dm.RightClick()
    # va = zongbiaoshi_num > 0 and tianjiangxiangrui_num > 0 and mukui_num > 0 and wokouxiaotoumu_num > 0 and jiutianxuannv_num > 0
    # while va:
    #     zuorensdfsdfwu()
    #     va = zongbiaoshi_num > 0 and tianjiangxiangrui_num > 0 and mukui_num > 0 and wokouxiaotoumu_num > 0 and jiutianxuannv_num > 0
    #     print('总镖师:' + str(zongbiaoshi_num) + ' 天降祥瑞:' + str(tianjiangxiangrui_num) + ' 木魁:' + str(
    #         tianjiangxiangrui_num) + ' 倭寇小头目:' + str(wokouxiaotoumu_num) + ' 九天玄女:' + str(jiutianxuannv_num))

    # print('程序结束')
