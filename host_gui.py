# -*- coding: shift_jis -*-

import tkinter as tk
from tkinter import ttk
import time
import threading
from datetime import datetime

def main():
    root = tk.Tk()
    root.title(u'Manange Task')
    root.geometry('1133x700')
    def get_time():
        while True:
            now = datetime.now()
            tm = u'{:02}月{:02}日{:02}:{:02}:{:02}'.format(now.month,now.day,now.hour,now.minute,now.second)
            clock.delete('all')
            clock.create_text(320,50,text=tm,font=(None,36))
            t1 = now-start_time
            t2 = finish_time-start_time
            progress_per = t1.total_seconds()/t2.total_seconds()
            progress.delete('all')
            progress.create_rectangle(0,0,int(1000*progress_per),60,fill='green')
            progress.create_rectangle(int(1000*progress_per),0,1000,60,fill='orange')
            time.sleep(1)

    app_title = u'タスク管理'
    app_title_label = tk.Label(
        root,text=app_title,
        font=(None,30)
    )
    app_title_label.grid(column=1,row=0,sticky=tk.W)

    clock = tk.Canvas(root,width=500,height=100)
    clock.grid(column=3,row=0)

    blank = tk.Canvas(root,width=50,height=1)
    blank.grid(column=0,row=0)

    start_time = datetime(2022,10,17,13,7,20)
    finish_time = datetime(2022,10,17,13,9,0)

    time_label = tk.Label(
        root,text=u'開始　{:02}/{:02}　{:02}:{:02}\n終了　{:02}/{:02}　{:02}:{:02}'.format(start_time.month,start_time.day,start_time.hour,start_time.minute,finish_time.month,finish_time.day,finish_time.hour,finish_time.minute),
        font=(None,'16')
    )
    time_label.grid(column=1,row=1,padx=15,sticky=tk.W)

    task_name = u'タスク名'
    if len(task_name.encode('shift_jis'))<30:
        task_name = task_name+' '*(30-len(task_name.encode('shift_jis')))
    task_name_label = tk.Label(
        root,text=task_name,
        font=(None,'20')
        )
    task_name_label.grid(column=2,row=1,padx=15,sticky=tk.W)

    person_name = u'芝浦太郎'
    person_name_label = tk.Label(
        root,text = 'by {0}'.format(person_name),
        font=(None,'16')
    )
    person_name_label.grid(column=3,row=1,padx=15)

    explanation = u'説明'
    explanation_label = tk.Label(
        root,text = explanation,
        font=(None,'12'),
    )
    explanation_label.grid(column=1,row=2,padx=15,pady=10,sticky=tk.W)

    progress = tk.Canvas(root,width=1000,height=60)
    progress.grid(column=1,row=3,padx=15,columnspan=3)

    next_task_title_label = tk.Label(
        root,text=u'次のタスク',
        font=(None,'16')
    )
    next_task_title_label.grid(column=1,row=4,padx=15,pady=30,sticky=tk.W)

    taskList = [
        ['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),u'人1',u'タスク1'],
        ['10C8',datetime(2022,10,17,10,30,0),datetime(2022,10,17,10,50,0),u'人2',u'タスク2'],
        ['10C9',datetime(2022,10,17,11,0,0),datetime(2022,10,17,11,20,0),u'人3',u'タスク3'],
        ['10CA',datetime(2022,10,17,11,30,0),datetime(2022,10,17,11,50,0),u'人4',u'タスク4'],
        ['10CB',datetime(2022,10,17,12,0,0),datetime(2022,10,17,12,20,0),u'人5',u'タスク5'],
        ['10CC',datetime(2022,10,17,12,30,0),datetime(2022,10,17,12,50,0),u'人6',u'タスク6'],
        ['10CD',datetime(2022,10,17,13,0,0),datetime(2022,10,17,13,20,0),u'人7',u'タスク7'],
        ['10CE',datetime(2022,10,17,13,30,0),datetime(2022,10,17,10,50,0),u'人8',u'タスク8']
    ]
    
    # 列の識別名の指定
    taskList_column = ('ID',u'開始',u'終了',u'人',u'名前')
    # Treeviewの生成
    taskList_tree = ttk.Treeview(root,columns=taskList_column)
    # 列の設定
    taskList_tree.column('#0',width=0,stretch='no')
    taskList_tree.column('ID',anchor='center',width=50)
    taskList_tree.column(u'開始',anchor='center',width=50)
    taskList_tree.column(u'終了',anchor='center',width=50)
    taskList_tree.column(u'人',anchor='center',width=100)
    taskList_tree.column(u'名前',anchor='w',width=200)
    # 列の見出し設定
    taskList_tree.heading('#0',text='')
    taskList_tree.heading('ID',text='ID',anchor='center')
    taskList_tree.heading(u'開始',text=u'開始',anchor='center')
    taskList_tree.heading(u'終了',text=u'終了',anchor='center')
    taskList_tree.heading(u'人',text=u'人',anchor='center')
    taskList_tree.heading(u'名前',text=u'名前',anchor='center')
    # レコードの追加
    for i in range(8):
        taskList_tree.insert(parent='',index='end',iid=i,values=(
            taskList[i][0],
            '{:02}:{:02}'.format(taskList[i][1].hour,taskList[i][1].minute),
            '{:02}:{:02}'.format(taskList[i][2].hour,taskList[i][2].minute),
            taskList[i][3],
            taskList[i][4]
        ))
    # 表の配置
    taskList_tree.grid(column=1,row=5,padx=15,pady=10,sticky=tk.W,columnspan=3)

    task_edit_title_label = tk.Label(
        root,text=u'タスク編集',
        font=(None,16)
    )
    task_edit_title_label.grid(column=3,row=4,padx=15,pady=10,sticky=tk.W)
    
    edit_textbox = tk.Text(height=10,width=68)
    edit_textbox.grid(column=3,row=5,padx=15,pady=10,sticky=tk.NW,rowspan=8)

    thread = threading.Thread(target=get_time,daemon=True)
    thread.start()
    root.mainloop()

if __name__ == '__main__':
    main()
