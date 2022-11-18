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
write_sql_spec = ["implementation_id", "write_SQL", 
         "type_name",         "write_SQL", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
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
        self._d_change_task = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._change_taskIn = OpenRTM_aist.InPort("change_task", self._d_change_task)
        self._d_add_task = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._add_taskIn = OpenRTM_aist.InPort("add_task", self._d_add_task)


		


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
        self.addInPort("complete_task_id",self._complete_task_idIn)
        self.addInPort("change_task",self._change_taskIn)
        self.addInPort("add_task",self._add_taskIn)
		
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
        db = self._database_path[0]
        global conn
        global cur
        conn = sqlite3.connect(db)
        cur = conn.cursor()

        # create table
        cur.execute('CREATE TABLE IF NOT EXISTS task(id integer primary key autoincrement, start_time text, finish_time text, target text, status integer, title text, discription text)')
    
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
            add_task = self._add_taskIn.read().data

            # insert SQL statement
            cur.execute("insert into values(null, " + add_task[1] + ", " + add_task[2] + "," + add_task[3] + "," + int(add_task[4]) + "," + add_task[5] + ", " + add_task[6] + ")")


        # change data "status" value from False "0" to True "1"
        if self._complete_task_idIn.isNew():
            complete_task_id = self._complete_task_idIn.read().data

            # SQL statuement
            cur.execute('UPDATE task SET status = 1 where id =' + complete_task_id)

        
        if self._change_taskIn.isNew():
            change_task = self._change_taskIn.read().data


    
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

