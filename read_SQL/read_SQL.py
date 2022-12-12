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

import pathlib
import sqlite3

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
read_sql_spec = ["implementation_id", "read_SQL", 
         "type_name",         "read_SQL", 
         "description",       "ModuleDescription", 
         "version",           "1.2.0", 
         "vendor",            "Tsukasa Takahashi", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "0", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.database_conf", "../tasklist.db', 'task",
         "conf.default.sort", "start_time', 'ASC",

         "conf.__widget__.database_conf", "text",
         "conf.__widget__.sort", "text",

         "conf.__type__.database_conf", "string",
         "conf.__type__.sort", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class read_SQL
# @brief ModuleDescription
# 
# SQLite3からデータを取得するコンポーネント
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

        self._d_db_out = OpenRTM_aist.instantiateDataType(_GlobalIDL.TaskListSeq(tm=0, task_id=[], start_time=[], finish_time=[], target=[], status=[], title=[], discription=[]))
        """
        SQLite3 Database
		SELECT * FROM {table_name}
        """
        self._db_outOut = OpenRTM_aist.OutPort("db_out", self._d_db_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        データベースの相対パス, データベース内のテーブル名
         - Name:  database_conf
         - DefaultValue: ../tasklist.db', 'task
        """
        self._database_conf = ['../tasklist.db', 'task']
        """
        db_outの並べ替え
         - Name: sort sort
         - DefaultValue: start_time', 'ASC
         - Range: {coloum name}', '{ASC or DSC}
        """
        self._sort = ['start_time', 'ASC']
		
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
        self.bindParameter("database_conf", self._database_conf, "../tasklist.db', 'task")
        self.bindParameter("sort", self._sort, "start_time', 'ASC")
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("db_out",self._db_outOut)
		
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
        global db_table
        global conn
        global cur

        if not pathlib.Path(self._database_conf[0].split('\'')[0]).is_absolute():
            db = pathlib.Path(self._database_conf[0].split('\'')[0]).resolve()
        else :
            db = pathlib.Path(self._database_conf[0].split('\'')[0])

        db_table = self._database_conf[1]                           # the database table-name

        conn = sqlite3.connect('file:'+ pathlib.PureWindowsPath(db).as_posix() +'?mode=ro', uri=True)   # read only mode
        cur = conn.cursor()

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
    
        # latest task data
        cur.execute('SELECT * FROM '+ db_table +' ORDER BY '+ self._sort[0].split('\'')[0] +' ' + self._sort[1] + ';')
        data_list = cur.fetchall()

        if len(data_list) != 0:
            # get data from database
            cur.execute('SELECT * FROM ' + db_table + ';')
            task_list = cur.fetchall()

            task_list_task_id = []
            task_list_start_time=[]
            task_list_finish_time=[]
            task_list_target=[]
            task_list_status=[]
            task_list_title=[]
            task_list_discription=[]

            for i in range(len(data_list)):
                task_list_task_id.append(int(task_list[i][0]))
                task_list_start_time.append(task_list[i][1])
                task_list_finish_time.append(task_list[i][2])
                task_list_target.append(task_list[i][3])

                # change type from SQLite-string to boolean
                if task_list[i][3] == 1:
                    task_list_status.append(True)
                elif task_list[i][4] == 0:
                    task_list_status.append(False)

                task_list_title.append(task_list[i][5])
                task_list_discription.append(task_list[i][6])

            # set and send data
            self._d_db_out.task_id = task_list_task_id
            self._d_db_out.start_time = task_list_start_time
            self._d_db_out.finish_time = task_list_finish_time
            self._d_db_out.target = task_list_target
            self._d_db_out.status = task_list_status
            self._d_db_out.title = task_list_title
            self._d_db_out.discription = task_list_discription

            self._db_outOut.write()

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

