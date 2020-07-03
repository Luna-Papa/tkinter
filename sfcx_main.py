import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox
from datetime import datetime
from sfcx import sfcx, open_date_query


def frame1_sfcx():
    account = frame1_account.get()
    begin_date = frame1_date1.get()
    end_date = frame1_date2.get()
    if not account.strip():
        messagebox.showerror('', '未输入账号！')
    elif not begin_date.strip():
        messagebox.showerror('', '未输入查询日期')
    else:
        sfcx(account, begin_date, end_date)
        messagebox.showinfo('', '请求已提交后台')


def frame2_sfcx():
    id_no = frame2_identity.get()
    org_no = frame2_organization.get()
    account = frame2_account.get()
    if not (id_no.strip() or org_no.strip() or account.strip()):
        messagebox.showerror('', '未输入任何值！')
    else:
        open_date_query(id_no, org_no, account)
        messagebox.showinfo('', '请求已提交后台')


# ==============================================
# GUI Layout
# ==============================================

# Create instance
win = tk.Tk()

# Add a title
win.title("司法查询")

# ==============================================
# 根据账号和日期查询交易对手信息
# ==============================================

# Create a container to hold labels
frame1 = ttk.LabelFrame(win, text="根据账号日期查交易对手")
frame1.grid(column=0, row=0, padx=10, pady=5)

# Adding Labels
frame1_label_account = ttk.Label(frame1, text="请输入23位外部账号或卡号：       ")
frame1_label_account.grid(column=0, row=0, sticky='W', pady=2, padx=5)

# Adding Text boxes Entry widget
frame1_account = tk.StringVar()
frame1_account_entered = ttk.Entry(frame1, width=30, textvariable=frame1_account)
frame1_account_entered.grid(column=0, row=1, pady=2, padx=5, sticky='W')

# Adding Labels
frame1_label_date = ttk.Label(frame1, text="请输入起始日期：       ")
frame1_label_date.grid(column=0, row=2, sticky='W', pady=2, padx=5)

# Adding  Text boxes Entry widget
frame1_date1 = tk.StringVar()
frame1_date1_entered = ttk.Entry(frame1, width=30, textvariable=frame1_date1)
frame1_date1_entered.grid(column=0, row=3, pady=2, padx=5, sticky='W')

# Adding Labels
frame1_label_date2 = ttk.Label(frame1, text="请输入结束日期：       ")
frame1_label_date2.grid(column=0, row=4, sticky='W', pady=2, padx=5)

# Adding  Text boxes Entry widget
frame1_date2 = tk.StringVar()
frame1_date2_entered = ttk.Entry(frame1, width=30, textvariable=frame1_date2)
frame1_date2_entered.grid(column=0, row=5, pady=2, padx=5, sticky='W')

# Adding a Button
frame1_action = ttk.Button(frame1, text="开始查询", command=frame1_sfcx)
frame1_action.grid(column=0, row=6, pady=5)

# ==============================================
# 根据证件号码或账号查询开户日期
# ==============================================

# Create a container to hold labels
frame2 = ttk.LabelFrame(win, text="根据证件号码或账号查开户日期")
frame2.grid(column=1, row=0, padx=10, pady=5)

# Adding Labels
frame2_label_identity = ttk.Label(frame2, text="请输入个人客户证件号码：       ")
frame2_label_identity.grid(column=1, row=0, sticky='W', pady=2, padx=5)

# Adding Text boxes Entry widget
frame2_identity = tk.StringVar()
frame2_identity_entered = ttk.Entry(frame2, width=30, textvariable=frame2_identity)
frame2_identity_entered.grid(column=1, row=1, pady=2, padx=5, sticky='W')

# Adding Labels
frame2_label_organization = ttk.Label(frame2, text="请输入组织机构代码：       ")
frame2_label_organization.grid(column=1, row=2, sticky='W', pady=2, padx=5)

# Adding  Text boxes Entry widget
frame2_organization = tk.StringVar()
frame2_organization_entered = ttk.Entry(frame2, width=30, textvariable=frame2_organization)
frame2_organization_entered.grid(column=1, row=3, pady=2, padx=5, sticky='W')

# Adding Labels
frame2_label_account = ttk.Label(frame2, text="请输入23位账号或卡号：       ")
frame2_label_account.grid(column=1, row=4, sticky='W', pady=2, padx=5)

# Adding  Text boxes Entry widget
frame2_account = tk.StringVar()
frame2_account_entered = ttk.Entry(frame2, width=30, textvariable=frame2_account)
frame2_account_entered.grid(column=1, row=5, pady=2, padx=5, sticky='W')

# Adding a Button
frame2_action = ttk.Button(frame2, text="开始查询", command=frame2_sfcx)
frame2_action.grid(column=1, row=6, pady=5)
# =====================================
# MENU GUI
# =====================================
# ADD a Menu
menu_bar = Menu(win)
win.config(menu=menu_bar)


def _aboutmsg():
    messagebox.showinfo('开发信息', '开发人员：胡鹏\n版本：V1.1\n发版日期：2020-7-2')


def _info():
    messagebox.showinfo('使用说明', '增加查询客户开户信息的功能')


help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="帮助", menu=help_menu)
help_menu.add_command(label="关于", command=_aboutmsg)
help_menu.add_command(label="使用说明", command=_info)

# =====================================
# Start GUI
# =====================================
win.mainloop()
# =====================================
