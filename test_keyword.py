# -*- coding: utf-8 -*-

from uiautomator import Device
# from robot.libraries.BuiltIn import BuiltIn

d1 = Device('4d00af1dd460408d')
d2 = Device('FA357PN01129')

def asynchronously_start_system_1():
    print '1 starting'
    print '1 set_serial_number'
#     d1 = Device('0123456789ABCDEF')
    print '1 swipe_left_by_class_name 1111'
    d1(className='android.view.View').swipe.left(steps=10)
    print '1 swipe_left_by_class_name 2222'
    d1(className='android.view.View').swipe.left(steps=10)
    print '1 swipe_left_by_class_name 3333'
    d1(className='android.view.View').swipe.left(steps=10)
    print '1 swipe_left_by_class_name 4444'
    d1(className='android.view.View').swipe.left(steps=10)

def asynchronously_start_system_2():
    print '2 starting'
    print '2 set_serial_number'
#     d2 = Device('HYZPLVR48T6TS8LV')
    print '2 swipe_right_by_class_name 1111'
    d2(className='android.view.View').swipe.right(steps=10)
    print '2 swipe_right_by_class_name 2222'
    d2(className='android.view.View').swipe.right(steps=10)
    print '2 swipe_right_by_class_name 3333'
    d2(className='android.view.View').swipe.right(steps=10)
    print '2 swipe_right_by_class_name 4444'
    d2(className='android.view.View').swipe.right(steps=10)

def connect_to_wifi_d1():
    d1.press.menu()
    d1(text = '系統設定').wait.exists(timeout=10000)
    d1(text = '系統設定').click()
    d1(text = 'Wi-Fi').wait.exists(timeout=10000)
    d1(text = 'Wi-Fi').click()
    d1(text = '關閉').wait.exists(timeout=10000)
    d1(text = '關閉').click()