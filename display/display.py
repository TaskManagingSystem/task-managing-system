#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file display.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from distutils.util import strtobool

# Import RTM module
import RTC
import OpenRTM_aist

import _GlobalIDL

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
display_spec = ["implementation_id", "display", 
         "type_name",         "display", 
         "description",       "ModuleDescription", 
         "version",           "1.1.0", 
         "vendor",            "Tsukasa Takahashi", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class display
# @brief ModuleDescription
# 
# 
# </rtc-template>
class display(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_task_list = OpenRTM_aist.instantiateDataType(_GlobalIDL.TaskListSeq(tm=0, task_id=[], start_time=[], finish_time=[], target=[], status=False, title=[], discription=[]))
        """
        """
        self._task_listIn = OpenRTM_aist.InPort("task_list", self._d_task_list)
        self._d_change_task = OpenRTM_aist.instantiateDataType(_GlobalIDL.TaskList(tm=0, task_id=-1, start_time="", finish_time="", target="", status=False, title="", discription=""))
        """
        """
        self._change_taskOut = OpenRTM_aist.OutPort("change_task", self._d_change_task)
        self._d_complete_task_id = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._complete_task_idOut = OpenRTM_aist.OutPort("complete_task_id", self._d_complete_task_id)
        self._d_add_task = OpenRTM_aist.instantiateDataType(_GlobalIDL.TaskList(tm=0, task_id=-1, start_time="", finish_time="", target="", status=False, title="", discription=""))
        """
        """
        self._add_taskOut = OpenRTM_aist.OutPort("add_task", self._d_add_task)
        self._d_delete_task_id = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._delete_task_idOut = OpenRTM_aist.OutPort("delete_task_id", self._d_delete_task_id)


        self.edit_record_textboxes = []

        self.edit_record_textboxes_sub = []

    def select_record(self, event):
        print("select_record()")
        taskList_column = ('ID', '開始', '終了', '実行者', 'ステータス', 'タイトル', '説明')
        record_id = self.taskList_tree.focus()
        task_edit_title_label = tk.Label(
            self.root, text='タスク編集',
            font=(None, 16)
        )
        task_edit_title_label.grid(
            column=3, row=4, padx=15, pady=10, sticky=tk.W, columnspan=3)
        task_edit_table_label = tk.Label(
            self.root, text='項目',
            font=(None, 12)
        )
        task_edit_table_label.grid(column=3, row=5, pady=3, sticky=tk.W)
        task_edit_table_label = tk.Label(
            self.root, text='編集前',
            font=(None, 12)
        )
        task_edit_table_label.grid(column=4, row=5, pady=3, sticky=tk.W)
        task_edit_table_label = tk.Label(
            self.root, text='編集後',
            font=(None, 12)
        )
        task_edit_table_label.grid(column=5, row=5, pady=3, sticky=tk.W)

        print("\n\nBefore for loop")
        print(taskList_column)
        print()
        for i in range(7):
            print("TaskList_column[i]:" + taskList_column[i])
            edit_record_label_0 = tk.Label(                     # 項目名
                self.root, text=taskList_column[i],
                font=(None, 12)
            )
            edit_record_label_0.grid(column=3, row=6+i, pady=3, sticky=tk.W)
            values = [""] * 5

            print(self.taskList_tree.item(record_id, 'values'))
            print(i)
            edit_record_label_1_text = self.taskList_tree.item(record_id, 'values')[i]
            edit_record_label_1 = tk.Label(
                self.root, text=edit_record_label_1_text,
                font=(None, 12)
            )
            edit_record_label_1.grid(column=4, row=6+i, pady=3, sticky=tk.W)
            self.edit_record_textboxes.append(tk.Entry(width=30))
            self.edit_record_textboxes[i].delete(0, tk.END)
            self.edit_record_textboxes[i].insert(tk.END, edit_record_label_1_text)
            self.edit_record_textboxes[i].grid(column=5, row=6+i, pady=3, sticky=tk.W)

        edit_finish_button = tk.Button(
            self.root, text='編集完了', command=self.edit_finish_fanc)
        edit_finish_button.grid(column=3, row=13, pady=3, sticky=tk.W)

    # 編集完了ボタン押下時の処理
    def edit_finish_fanc(self):
        print("edit_finish_fanc")
        taskList_edited = []
        for i in range(5):
            taskList_edited.append(self.edit_record_textboxes[i].get())

        self._d_change_task.task_id = self.edit_record_textboxes[0].get()
        self._d_change_task.start_time = taskList_edited[1].get()
        self._d_change_task.finish_time = taskList_edited[2].get()
        self._d_change_task.target = taskList_edited[3].get()
        self._d_change_task.status = taskList_edited[4].get()
        self._d_change_task.title = taskList_edited[5].get()
        self._d_change_task.discription = taskList_edited[6].get()
        self._change_taskOut.write()
        print(taskList_edited)

    def edit_fin_new(self):
            print('edit_fin_new()')
            self._d_add_task.task_id = self.edit_record_textboxes_sub[0].get()
            self._d_add_task.start_time = self.edit_record_textboxes_sub[1].get()
            self._d_add_task.finish_time = self.edit_record_textboxes_sub[2].get()
            self._d_add_task.target = self.edit_record_textboxes_sub[3].get()
            self._d_add_task.status = self.edit_record_textboxes_sub[4].get()
            self._d_add_task.title = self.edit_record_textboxes_sub[5].get()
            self._d_add_task.discription = self.edit_record_textboxes_sub[6].get()


            self._add_taskOut.write()

    def make_newtask_func(self):
        root_new = tk.Tk()
        root_new.title('新規作成')
        root_new.geometry('400x400')
        taskList_column = ('ID', '開始', '終了', '実行者', 'ステータス', 'タイトル', '説明')
        self.edit_record_textboxes_sub = []
        for i in range(7):
            edit_record_label_0 = tk.Label(                     # 項目名
                root_new, text=taskList_column[i],
                font=(None, 12)
            )
            edit_record_label_0.grid(column=0, row=i, pady=3, sticky=tk.W)
            self.edit_record_textboxes_sub.append(tk.Entry(root_new, width=30))
            self.edit_record_textboxes_sub[i].delete(0, tk.END)
            self.edit_record_textboxes_sub[i].grid(column=1, row=i, pady=3, sticky=tk.W)
        edit_finish_new_butoon = tk.Button(root_new,text='新規作成完了',command=self.edit_fin_new)
        edit_finish_new_butoon.grid(column=0,row=8)



        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("task_list",self._task_listIn)
		
        # Set OutPort buffers
        self.addOutPort("change_task",self._change_taskOut)
        self.addOutPort("complete_task_id",self._complete_task_idOut)
        self.addOutPort("add_task",self._add_taskOut)
        self.addOutPort("delete_task_id",self._delete_task_idOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        print('Activated')

        # tkinterの初期設定
        self.root = tk.Tk()
        self.root.title('Manage Task')
        self.root.geometry('1133x700')
        self.root.update_idletasks()

        # 余白
        blank = tk.Canvas(self.root, width=50, height=1)
        blank.grid(column=0, row=0)

        # アプリケーションタイトルの表示
        app_title = 'タスク管理'
        app_title_label = tk.Label(
            self.root, text=app_title,
            font=(None, 30)
        )
        app_title_label.grid(column=1, row=0, sticky=tk.W)

        # 時計の表示
        self.clock = tk.Canvas(self.root, width=500, height=100)
        self.clock.grid(column=3, row=0, columnspan=3)

        # 進捗バーの表示
        self.progress = tk.Canvas(self.root, width=1000, height=60)
        self.progress.grid(column=1, row=3, padx=15, columnspan=6)

        # 次のタスク一覧表示
        next_task_title_label = tk.Label(
            self.root, text='次のタスク',
            font=(None, '16')
        )
        next_task_title_label.grid(
            column=1, row=4, padx=15, pady=30, sticky=tk.W)

        # 全てのタスクの表の作成
        # 列の識別名の指定
        taskList_column = ('ID', '開始', '終了', '実行者', 'ステータス', 'タイトル', '説明')

        # Treeviewの生成
        self.taskList_tree = ttk.Treeview(self.root, columns=taskList_column)

        # 列選択時の関数の紐づけ
        self.taskList_tree.bind('<<TreeviewSelect>>', self.select_record)

        # 列の設定
        self.taskList_tree.column('#0', width=0, stretch='no')
        self.taskList_tree.column('ID', anchor='center', width=30)
        self.taskList_tree.column('開始', anchor='center', width=35)
        self.taskList_tree.column('終了', anchor='center', width=35)
        self.taskList_tree.column('実行者', anchor='center', width=75)
        self.taskList_tree.column('ステータス', anchor='center', width=40)
        self.taskList_tree.column('タイトル', anchor='w', width=130)
        self.taskList_tree.column('説明', anchor='w', width=130)
        # 列の見出し設定
        self.taskList_tree.heading('#0', text='')
        self.taskList_tree.heading('ID', text='ID', anchor='center')
        self.taskList_tree.heading('開始', text='開始', anchor='center')
        self.taskList_tree.heading('終了', text='終了', anchor='center')
        self.taskList_tree.heading('実行者', text='実行者', anchor='center')
        self.taskList_tree.heading('ステータス', text='ステータス', anchor='center')
        self.taskList_tree.heading('タイトル', text='タイトル', anchor='center')
        self.taskList_tree.heading('説明', text='説明', anchor='center')

        self.taskList_tree.grid(column=1, row=5, padx=15,
                                pady=10, sticky=tk.W, columnspan=3, rowspan=10)

        self.make_newtask_button = tk.Button(self.root,text='新規作成',command=self.make_newtask_func)
        self.make_newtask_button.grid(column=4, row=13, padx=15,pady=10, sticky=tk.W)

        self.latest_task = ['', '0-0-0 0:0:0', '0-0-0 0:0:0', '', '', '', '']

        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
        self.root.destroy()
        print('Deactivated')

        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        # 現在時刻を取得し、時計に表示
        now = datetime.now()
        now_str = '{:02}月{:02}日{:02}:{:02}:{:02}'.format(
            now.month, now.day, now.hour, now.minute, now.second)
        self.clock.delete('all')
        self.clock.create_text(250, 50, text=now_str, font=(None, 36))


        # 全てのタスクのデータを取得する
        task_list = [
            ['id'],
            ['2020-8-12 6:45:0'],
            ['2021-1-13 7:40:0'],
            ['target'],
            ['status'],
            ['title'],
            ['description']
        ]
            


        # 最新のタスクを取得する
        self.latest_task = ['123', '2022-11-17 7:18:0',
                            '2022-11-18 23:59:59', 'person', 'False', 'title', 'description']
        start_time = datetime(2022, 11, 17, 7, 18, 0)
        finish_time = datetime(2022, 11, 18, 23, 59, 59)
        task_name = 'タスク名'
        person_name = '人'
        description = '説明'

        if self._task_listIn.isNew():
            # task_listから直近かつ未完了のものを選択
            # for i in range(len(task_list[0])):
            #     if not task_list[4][i]:
            #         self.latest_task = [task_list[0][i], task_list[1][i], task_list[2][i], task_list[3][i], task_list[4][i], task_list[5][i], task_list[6][i]]
            #     else:
            #         break

            task_list[0] = self._idIn.read().task_id
            task_list[1] = self._idIn.read().start_time
            task_list[2] = self._idIn.read().finish_time
            task_list[3] = self._idIn.read().target
            task_list[4] = self._idIn.read().status
            task_list[5] = self._idIn.read().title
            task_list[6] = self._idIn.read().discription
            try:
                if strtobool(self.latest_task[4]) == 0:
                    start_time = datetime.strptime(
                        self.latest_task[1], '%Y-%m-%d %H:%M:%S')
                    finish_time = datetime.strptime(
                        self.latest_task[2], '%Y-%m-%d %H:%M:%S')
                    task_name = self.latest_task[4]
                    person_name = self.latest_task[3]
                    description = self.latest_task[5]
            except:
                self.latest_task = ['123', '2022-11-17 7:18:0',
                                    '2022-11-18 23:59:59', 'person', 'False', 'title', 'description']
                start_time = datetime.strptime(
                    self.latest_task[1], '%Y-%m-%d %H:%M:%S')
                finish_time = datetime.strptime(
                    self.latest_task[2], '%Y-%m-%d %H:%M:%S')
                task_name = self.latest_task[5]
                person_name = self.latest_task[3]
                description = self.latest_task[6]

        # 最新のタスクの開始・終了時刻を表示する
        time_label = tk.Label(
            self.root, text='開始　{:02}/{:02}　{:02}:{:02}\n終了　{:02}/{:02}　{:02}:{:02}'.format(
                start_time.month, start_time.day, start_time.hour, start_time.minute, finish_time.month, finish_time.day, finish_time.hour, finish_time.minute),
            font=(None, 16)
        )
        time_label.grid(column=1, row=1, padx=15, sticky=tk.W)

        # 最新のタスクのタイトルを表示する
        if len(task_name.encode('utf-8')) < 30:
            task_name = task_name+' '*(30-len(task_name.encode('utf-8')))
        task_name_label = tk.Label(
            self.root, text=task_name,
            font=(None, '20')
        )
        task_name_label.grid(column=2, row=1, padx=15, sticky=tk.W)

        # 最新のタスクの実行者を表示する
        task_target_label = tk.Label(
            self.root, text='by {0}'.format(person_name),
            font=(None, '16')
        )
        task_target_label.grid(column=3, row=1, padx=15, columnspan=3)

        # 最新のタスクの説明を表示する
        task_description_label = tk.Label(
            self.root, text=description,
            font=(None, '12')
        )
        task_description_label.grid(
            column=1, row=2, padx=15, pady=10, sticky=tk.W)

        # 進捗バーの更新
        t1 = now-start_time
        t2 = finish_time-start_time
        progress_per = t1.total_seconds()/t2.total_seconds()
        self.progress.delete('all')
        self.progress.create_rectangle(
            0, 0, int(1000*progress_per), 60, fill='green')
        self.progress.create_rectangle(
            int(1000*progress_per), 0, 1000, 60, fill='orange')

        for i in self.taskList_tree.get_children():
            self.taskList_tree.delete(i)
        # for i in range(len(task_list[0])):
        #     #print(i)
        #     self.taskList_tree.insert(parent='',index='end',values=(
        #         task_list[0:4][i]
        #     ))

        # TODO TODO TODO 仮 TODO TODO TODO
        # taskList = [['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),'人1','タスク1']]

        # タスク一覧のテーブル表示
        for i in range(min([len(task_list[j]) for j in range(7)])):
            self.taskList_tree.insert(parent='', index='end', iid=i, values=(
                task_list[0][i],
                '{:02}:{:02}'.format(datetime.strptime(
                    task_list[1][i], '%Y-%m-%d %H:%M:%S').hour, datetime.strptime(task_list[1][i], '%Y-%m-%d %H:%M:%S').minute),
                '{:02}:{:02}'.format(datetime.strptime(
                    task_list[2][i], '%Y-%m-%d %H:%M:%S').hour, datetime.strptime(task_list[2][i], '%Y-%m-%d %H:%M:%S').minute),
                task_list[3][i],
                task_list[4][i],
                task_list[5][i],
                task_list[6][i]
            ))

        self.root.update_idletasks()
        self.root.update()
 
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def displayInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=display_spec)
    manager.registerFactory(profile,
                            display,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    displayInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("display" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

