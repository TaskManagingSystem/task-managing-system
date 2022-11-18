#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file display.py
 @brief DisplayTaskLists
 @date $Date$


"""
# </rtc-template>

import sys
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


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
         "description",       "DisplayTaskLists", 
         "version",           "1.0.0", 
         "vendor",            "HarutoFuruyama", 
         "category",          "User Interface", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class display
# @brief DisplayTaskLists
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

        self._d_latest_task = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._latest_taskIn = OpenRTM_aist.InPort("latest_task", self._d_latest_task)
        self._d_id = OpenRTM_aist.instantiateDataType(RTC.TimedLongSeq)
        """
        """
        self._idIn = OpenRTM_aist.InPort("id", self._d_id)
        self._d_start_time = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._start_timeIn = OpenRTM_aist.InPort("start_time", self._d_start_time)
        self._d_finish_time = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._finish_timeIn = OpenRTM_aist.InPort("finish_time", self._d_finish_time)
        self._d_target = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._targetIn = OpenRTM_aist.InPort("target", self._d_target)
        self._d_status = OpenRTM_aist.instantiateDataType(RTC.TimedBooleanSeq)
        """
        """
        self._statusIn = OpenRTM_aist.InPort("status", self._d_status)
        self._d_title = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._titleIn = OpenRTM_aist.InPort("title", self._d_title)
        self._d_description = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._descriptionIn = OpenRTM_aist.InPort("description", self._d_description)
        self._d_change_task = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._change_taskOut = OpenRTM_aist.OutPort("change_task", self._d_change_task)
        self._d_complete_task_id = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._complete_task_idOut = OpenRTM_aist.OutPort("complete_task_id", self._d_complete_task_id)

    def select_record(self,event):
        taskList_column = ('ID','開始','終了','人','名前')
        record_id = self.taskList_tree.focus()
        task_edit_title_label = tk.Label(
        self.root,text='タスク編集',
        font=(None,16)
        )
        task_edit_title_label.grid(column=3,row=4,padx=15,pady=10,sticky=tk.W,columnspan=3)
        task_edit_table_label = tk.Label(
            self.root,text='項目',
            font=(None,12)
        )
        task_edit_table_label.grid(column=3,row=5,pady=3,sticky=tk.W)
        task_edit_table_label = tk.Label(
            self.root,text='編集前',
            font=(None,12)
        )
        task_edit_table_label.grid(column=4,row=5,pady=3,sticky=tk.W)
        task_edit_table_label = tk.Label(
            self.root,text='編集後',
            font=(None,12)
        )
        task_edit_table_label.grid(column=5,row=5,pady=3,sticky=tk.W)
        for i in range(5):
            edit_record_label_0 = tk.Label(
                self.root,text=taskList_column[i],
                font=(None,12)
            )
            edit_record_label_0.grid(column=3,row=6+i,pady=3,sticky=tk.W)
            values = [""] * 5
            if i==1 or i==2:
                edit_record_label_1_text = self.taskList_tree.item(record_id, 'values')[i]
            else :
                edit_record_label_1_text = self.taskList_tree.item(record_id, 'values')[i]
            edit_record_label_1 = tk.Label(
                    self.root,text=edit_record_label_1_text,
                    font=(None,12)
                )
            edit_record_label_1.grid(column=4,row=6+i,pady=3,sticky=tk.W)
            edit_record_textbox = tk.Entry(width=30)
            edit_record_textbox.insert(tk.END,edit_record_label_1_text)
            edit_record_textbox.grid(column=5,row=6+i,pady=3,sticky=tk.W)

        # 編集完了ボタン押下時の処理
        def edit_finish_fanc():
            self.taskList_edited=[]
            
        edit_finish_button = tk.Button(self.root,text='編集完了',command=edit_finish_fanc)
        edit_finish_button.grid(column=3,row=11,pady=3,sticky=tk.W)
		


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
        self.addInPort("latest_task",self._latest_taskIn)
        self.addInPort("id",self._idIn)
        self.addInPort("start_time",self._start_timeIn)
        self.addInPort("finish_time",self._finish_timeIn)
        self.addInPort("target",self._targetIn)
        self.addInPort("status",self._statusIn)
        self.addInPort("title",self._titleIn)
        self.addInPort("description",self._descriptionIn)
		
        # Set OutPort buffers
        self.addOutPort("change_task",self._change_taskOut)
        self.addOutPort("complete_task_id",self._complete_task_idOut)
		
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
        blank = tk.Canvas(self.root,width=50,height=1)
        blank.grid(column=0,row=0)

        # アプリケーションタイトルの表示
        app_title = 'タスク管理'
        app_title_label = tk.Label(
            self.root,text=app_title,
            font=(None,30)
        )
        app_title_label.grid(column=1,row=0,sticky=tk.W)

        # 時計の表示
        self.clock = tk.Canvas(self.root,width=500,height=100)
        self.clock.grid(column=3,row=0,columnspan=3)

        # 進捗バーの表示
        self.progress = tk.Canvas(self.root,width=1000,height=60)
        self.progress.grid(column=1,row=3,padx=15,columnspan=6)

        # 次のタスク一覧表示
        next_task_title_label = tk.Label(
            self.root,text='次のタスク',
            font=(None,'16')
        )
        next_task_title_label.grid(column=1,row=4,padx=15,pady=30,sticky=tk.W)

        # 全てのタスクの表の作成
        # 列の識別名の指定
        taskList_column = ('ID','開始','終了','実行者','タイトル')

        # Treeviewの生成
        self.taskList_tree = ttk.Treeview(self.root,columns=taskList_column)

        # 列選択時の関数の紐づけ
        self.taskList_tree.bind('<<TreeviewSelect>>',self.select_record)

        # 列の設定
        self.taskList_tree.column('#0',width=0,stretch='no')
        self.taskList_tree.column('ID',anchor='center',width=50)
        self.taskList_tree.column('開始',anchor='center',width=50)
        self.taskList_tree.column('終了',anchor='center',width=50)
        self.taskList_tree.column('実行者',anchor='center',width=100)
        self.taskList_tree.column('タイトル',anchor='w',width=200)
        # 列の見出し設定
        self.taskList_tree.heading('#0',text='')
        self.taskList_tree.heading('ID',text='ID',anchor='center')
        self.taskList_tree.heading('開始',text='開始',anchor='center')
        self.taskList_tree.heading('終了',text='終了',anchor='center')
        self.taskList_tree.heading('実行者',text='実行者',anchor='center')
        self.taskList_tree.heading('タイトル',text='タイトル',anchor='center')

        self.taskList_tree.grid(column=1,row=5,padx=15,pady=10,sticky=tk.W,columnspan=3,rowspan=8)

        self.latest_task = ['','0-0-0 0:0:0','0-0-0 0:0:0','','','','']
        
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
        now_str = '{:02}月{:02}日{:02}:{:02}:{:02}'.format(now.month,now.day,now.hour,now.minute,now.second)
        self.clock.delete('all')
        self.clock.create_text(250,50,text=now_str,font=(None,36))

        # 最新のタスクを取得する
        start_time = datetime(2022,10,24,21,10,0)
        finish_time = datetime(2022,10,24,22,10,0)
        task_name = 'タスク名'
        person_name = '人'
        description = '説明'
        if self._latest_taskIn.isNew():
            self.latest_task = self._latest_taskIn.read().data
            if len(self.latest_task) != 0:
                start_time = datetime.strptime(self.latest_task[1],'%Y-%m-%d %H:%M:%S')
                finish_time = datetime.strptime(self.latest_task[2],'%Y-%m-%d %H:%M:%S')
                task_name = self.latest_task[4]
                person_name = self.latest_task[3]
                description = self.latest_task[5]

        # 最新のタスクの開始・終了時刻を表示する
        time_label = tk.Label(
            self.root,text='開始　{:02}/{:02}　{:02}:{:02}\n終了　{:02}/{:02}　{:02}:{:02}'.format(start_time.month,start_time.day,start_time.hour,start_time.minute,finish_time.month,finish_time.day,finish_time.hour,finish_time.minute),
            font=(None,16)
        )
        time_label.grid(column=1,row=1,padx=15,sticky=tk.W)

        # 最新のタスクのタイトルを表示する
        if len(task_name.encode('utf-8'))<30:
            task_name = task_name+' '*(30-len(task_name.encode('utf-8')))
        task_name_label = tk.Label(
            self.root,text=task_name,
            font=(None,'20')
        )
        task_name_label.grid(column=2,row=1,padx=15,sticky=tk.W)

        # 最新のタスクの実行者を表示する
        task_target_label = tk.Label(
            self.root,text='by {0}'.format(person_name),
            font=(None,'16')
        )
        task_target_label.grid(column=3,row=1,padx=15,columnspan=3)

        # 最新のタスクの説明を表示する
        task_description_label = tk.Label(
            self.root,text = description,
            font=(None,'12')
        )
        task_description_label.grid(column=1,row=2,padx=15,pady=10,sticky=tk.W)

        # 進捗バーの更新
        t1 = now-start_time
        t2 = finish_time-start_time
        progress_per = t1.total_seconds()/t2.total_seconds()
        self.progress.delete('all')
        self.progress.create_rectangle(0,0,int(1000*progress_per),60,fill='green')
        self.progress.create_rectangle(int(1000*progress_per),0,1000,60,fill='orange')

        # 全てのタスクのデータを取得する
        task_list = [
            ['id'],
            ['start_time'],
            ['finish_time'],
            ['target'],
            ['status'],
            ['title'],
            ['description']
        ]
        if self._idIn.isNew():
            task_list[0] = self._idIn.read().data
        if self._start_timeIn.isNew():
            task_list[1] = self._start_timeIn.read().data
        if self._finish_timeIn.isNew():
            task_list[2] = self._finish_timeIn.read().data
        if self._targetIn.isNew():
            task_list[3] = self._targetIn.read().data
        if self._statusIn.isNew():
            task_list[4] = self._statusIn.read().data
        if self._titleIn.isNew():
            task_list[5] = self._titleIn.read().data
        if self._descriptionIn.isNew():
            task_list[6] = self._descriptionIn.read().data

        for i in self.taskList_tree.get_children():
            self.taskList_tree.delete(i)
        # for i in range(len(task_list[0])):
        #     #print(i)
        #     self.taskList_tree.insert(parent='',index='end',values=(
        #         task_list[0:4][i]
        #     ))

        # TODO TODO TODO 仮 TODO TODO TODO
        taskList = [['10C7',datetime(2022,10,17,10,0,0),datetime(2022,10,17,10,20,0),'人1','タスク1']]
        for i in range(len(taskList)):
            self.taskList_tree.insert(parent='',index='end',iid=i,values=(
            taskList[i][0],
            '{:02}:{:02}'.format(taskList[i][1].hour,taskList[i][1].minute),
            '{:02}:{:02}'.format(taskList[i][2].hour,taskList[i][2].minute),
            taskList[i][3],
            taskList[i][4]
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

