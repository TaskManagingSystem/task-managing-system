#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file write_SQL.py
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
write_sql_spec = ["implementation_id", "write_SQL", 
         "type_name",         "write_SQL", 
         "description",       "ModuleDescription", 
         "version",           "1.2.0", 
         "vendor",            "Tsukasa Takahashi", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.database_conf", "../tasklist.db', 'task",
         "conf.default.data_type", "id integer primarykey autoincrement, start_time text, finish_time text, target text, status integer, title text, discription text",

         "conf.__widget__.database_conf", "spin",
         "conf.__widget__.data_type", "text",

         "conf.__type__.database_conf", "string",
         "conf.__type__.data_type", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class write_SQL
# @brief ModuleDescription
# 
# 
# </rtc-template>
class write_SQL(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_complete_task_id = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._complete_task_idIn = OpenRTM_aist.InPort("complete_task_id", self._d_complete_task_id)
        self._d_change_task = OpenRTM_aist.instantiateDataType(_GlobalIDL.TaskList(tm=0, task_id=-1, start_time="", finish_time="", target="", status=False, title="", discription=""))
        """
        """
        self._change_taskIn = OpenRTM_aist.InPort("change_task", self._d_change_task)
        self._d_add_task = OpenRTM_aist.instantiateDataType(_GlobalIDL.TaskList(tm=0, task_id=-1, start_time="", finish_time="", target="", status=False, title="", discription=""))
        """
        """
        self._add_taskIn = OpenRTM_aist.InPort("add_task", self._d_add_task)
        self._d_delete_task_id = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._delete_task_idIn = OpenRTM_aist.InPort("delete_task_id", self._d_delete_task_id)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        データベースの相対パス, データベース内のテーブル名
         - Name:  database_conf
         - DefaultValue: ../tasklist.db', 'task
        """
        self._database_conf = ['../tasklist.db', 'task']
        """
        databaseのカラム名、カラムのデータ型
         - Name: data_type data_type
         - DefaultValue: id integer primarykey autoincrement, start_time text, finish_time text, target text, status integer, title text, discription text
         - Range: {variable name} + {"null" or "integer" or "real" or "text" or
		          "blob"} + {option}, ...
        """
        self._data_type = ['id integer primarykey autoincrement, start_time text, finish_time text, target text, status integer, title text, discription text']
		
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
        self.bindParameter("data_type", self._data_type, "id integer primarykey autoincrement, start_time text, finish_time text, target text, status integer, title text, discription text")
		
        # Set InPort buffers
        self.addInPort("complete_task_id",self._complete_task_idIn)
        self.addInPort("change_task",self._change_taskIn)
        self.addInPort("add_task",self._add_taskIn)
        self.addInPort("delete_task_id",self._delete_task_idIn)
		
        # Set OutPort buffers
		
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

        db_table = self._database_conf[1]                                # the database table-name

        conn = sqlite3.connect(pathlib.PureWindowsPath(db).as_posix())   # write mode
        cur = conn.cursor()

 
        # create table

        print('CREATE TABLE IF NOT EXISTS ' + db_table + '(' + self._data_type[0] + ')')
        #cur.execute('CREATE TABLE IF NOT EXISTS ' + db_table + '(' + self._data_type[0] + ')')
    
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

        # insert task data into the database table
        if self._add_taskIn.isNew():
            add_task = self._add_taskIn.read()

            # insert SQL statement
            print("insert into " + db_table +" values(null, " + add_task.data[1] + ", " + add_task.data[2] + "," + add_task.data[3] + "," + int(add_task.data[4]) + "," + add_task.data[5] + ", " + add_task.data[6] + ");")
            cur.execute("insert into " + db_table +" values(null, " + add_task.data[1] + ", " + add_task.data[2] + "," + add_task.data[3] + "," + int(add_task.data[4]) + "," + add_task.data[5] + ", " + add_task.data[6] + ");")

        # change data "status" value from False "0" to True "1"
        if self._complete_task_idIn.isNew():
            complete_task_id = self._complete_task_idIn.read()

            # SQL statuement
            print('UPDATE ' + db_table + ' SET status = 1 where id =' + complete_task_id.data + ';')
            cur.execute('UPDATE ' + db_table + ' SET status = 1 where id =' + complete_task_id.data + ';')

        
        # update data
        if self._change_taskIn.isNew():
            change_task = self._change_taskIn.read()
            print(f'UPDATE task SET start_time = \"{change_task.start_time}\", finish_time = \"{change_task.finish_time}\", target = \"{change_task.target}\", status = {change_task.status}, title = \"{change_task.title}\", discription = \"{change_task.discription}\" where id =' + change_task.data[0] + ';')
            cur.execute(f'UPDATE task SET start_time = \"{change_task.start_time}\", finish_time = \"{change_task.finish_time}\", target = \"{change_task.target}\", status = {change_task.status}, title = \"{change_task.title}\", discription = \"{change_task.discription}\" where id =' + change_task.data[0] + ';')


        # delete data
        if self._delete_task_idIn.isNew():
            delete_id = self._delete_task_idIn.read()
            print('DELETE from ' + db_table + 'WHERE id = ' + delete_id +';')
            cur.execute('DELETE from ' + db_table + 'WHERE id = ' + delete_id +';')

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
	



def write_SQLInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=write_sql_spec)
    manager.registerFactory(profile,
                            write_SQL,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    write_SQLInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("write_SQL" + args)

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

