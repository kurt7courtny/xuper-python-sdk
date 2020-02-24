# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:50:38 2020

@author: kurt
"""

from tkinter import *
from tkinter import ttk
import xuper
import json

class cbchot_bc_sdk:
    def __init__(self):
        self.bc_nginxgw  = StringVar() # 区块链入口地址，python-sdk使用nginxgw
        self.bc_nginxgw.set("http://106.14.180.178:8098")
        self.bc_username = StringVar() # 区块链名称
        self.bc_username.set("xuper")
        self.myaddr = StringVar()      # 管理员地址    
    
   
def make_menus():
    menubar = Menu(r)

    bc_info = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="区块链信息", menu=bc_info)
    bc_info.add_command(label="New Keys")
    bc_info.add_command(label="Load Keys")
    bc_info.add_command(label="New Account")
    

    content_owner = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="内容版权方", menu=content_owner)
    content_owner.add_command(label="Deploy")
    content_owner.add_command(label="Invoke")
    

    video_ws = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="播放方平台", menu=video_ws)
    video_ws.add_command(label="All")
    video_ws.add_command(label="Query")
    

    video_history = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="播放信息查询平台", menu=video_history)
    video_history.add_command(label="All")
    video_history.add_command(label="Query")
    
    r.config(menu = menubar)
    
def make_front():
    Label(r, text = "My Address", font='Helvetica 14 bold').grid(row=0, column=0,sticky=W, padx=5, pady=2)
    Label(r, textvariable=sdk.bc_nginxgw).grid(row=0, column=1,sticky=E)
    Label(r, text = "Balance", font='Helvetica 14 bold').grid(row=1, column=0, sticky=W,  padx=5, pady=2)
    Label(r, textvariable=sdk.bc_username).grid(row=1, column=1,sticky=E)
 
r = Tk()
sdk = cbchot_bc_sdk()

r.geometry("720x640")
r.title("区块链内容版权管理平台演示版")
make_menus()
make_front()
r.mainloop()   