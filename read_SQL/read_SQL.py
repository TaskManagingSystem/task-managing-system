#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file read_SQL.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

import sqlite3

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
read_sql_spec = ["implementation_id", "read_SQL", 
         "type_name",         "read_SQL", 
         "description",       "ModuleDescription", 
         "version",           "1.1.0", 
         "vendor",            "Tsukasa Takahashi", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.database_path", "../tasklist.db",

         "conf.__widget__.database_path", "text",

         "conf.__type__.database_path", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class read_SQL
# @brief ModuleDescription
# 
# 
# </rtc-template>
class read_SQL(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_task_list = OpenRTM_aist.instantiateDataType(RTC.TimedLongSeq)
        """
        """
        self._task_task_idOut = OpenRTM_aist.OutPort("task_task_id", self._d_task_list)
        self._d_latest_task = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._latest_taskOut = OpenRTM_aist.OutPort("latest_task", self._d_latest_task)
        self._d_task_start_time = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_start_timeOut = OpenRTM_aist.OutPort("task_start_time", self._d_task_start_time)
        self._d_task_finish_time = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_finish_timeOut = OpenRTM_aist.OutPort("task_finish_time", self._d_task_finish_time)
        self._d_task_target = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_targetOut = OpenRTM_aist.OutPort("task_target", self._d_task_target)
        self._d_task_status = OpenRTM_aist.instantiateDataType(RTC.TimedBooleanSeq)
        """
        """
        self._task_statusOut = OpenRTM_aist.OutPort("task_status", self._d_task_status)
        self._d_task_title = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_titleOut = OpenRTM_aist.OutPort("task_title", self._d_task_title)
        self._d_task_explanation = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_explanationOut = OpenRTM_aist.OutPort("task_explanation", self._d_task_explanation)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  database_path
         - DefaultValue: ../tasklist.db
        """
        self._database_path = ['../tasklist.db']
		
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
        self.bindParameter("database_path", self._database_path, "../tasklist.db")
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("task_task_id",self._task_task_idOut)
        self.addOutPort("latest_task",self._latest_taskOut)
        self.addOutPort("task_start_time",self._task_start_timeOut)
        self.addOutPort("task_finish_time",self._task_finish_timeOut)
        self.addOutPort("task_target",self._task_targetOut)
        self.addOutPort("task_status",self._task_statusOut)
        self.addOutPort("task_title",self._task_titleOut)
        self.addOutPort("task_explanation",self._task_explanationOut)
		
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
        
        # connect task database
        global db
        global conn
        global cur
        db = self._database_path[0]
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        # create table
        cur.execute('CREATE TABLE IF NOT EXISTS task(id integer primary key autoincrement, start_time text, finish_time text, target text, status integer, title text, discription text)')

        # disconnect the task database
        # cur.close()
        # conn.close()

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
    
        # disconnect the task database
        cur.close()
        conn.close()

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
        # connect task database
        # conn = sqlite3.connect(db)
        # cur = conn.cursor()


        # latest task data
        cur.execute('SELECT * FROM task ORDER BY start_time asc;')
        task_list = cur.fetchall()
        if len(task_list) != 0:
            self._d_latest_task.data = task_list[0]
            self._latest_taskOut.write()


        # all task data
        # get data from database
        cur.execute('SELECT * FROM task;')
        task_list = cur.fetchall()

        for i in range(len(task_list)):
            self._d_task_list.data = int(task_list[i][0])
            self._task_task_idOut.write()
            self._d_task_start_time.data = task_list[i][1]
            self._task_start_timeOut.write()
            self._d_task_finish_time.data = task_list[i][2]
            self._task_finish_timeOut.write()
            self._d_task_target.data = task_list[i][2]
            self._task_targetOut.write()

            # SQLiteのstring型をboolean型に変換
            if task_list[i][3] == 1:
                self._d_task_status.data = True
            elif task_list[i][4] == 0:
                self._d_task_status.data == False
            self._task_statusOut.write()

            self._d_task_title.data = task_list[i][5]
            self._task_titleOut.write()
            self._d_task_target.data = task_list[i][6]
            self._task_targetOut.write()

    
        # disconnect the task database
        # cur.close()
        # conn.close()

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
	



def read_SQLInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=read_sql_spec)
    manager.registerFactory(profile,
                            read_SQL,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    read_SQLInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("read_SQL" + args)

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

