Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pynput
>>> from pynput.mouse import Button, Controller
>>> mouse = Controller()
>>> mouse.position
(1281, 229)
>>> mouse.position
(1290, 237)
>>> mouse.move(100, 200)
>>> mouse.click(Button.right, 1)
>>> mouse.click(Button.right, 2)
>>> mouse.press(Button.right)
>>> mouse.release(Button.right)
>>> mouse.press(Button.right)
>>> mouse.scroll(0,-111)
>>> 
