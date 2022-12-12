#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file read_SQLTest.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import _GlobalIDL

# Import Service implementation class
# <rtc-template block="service_impl">

import read_SQL

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
read_sqltest_spec = ["implementation_id", "read_SQLTest", 
         "type_name",         "read_SQLTest", 
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
# @class read_SQLTest
# @brief ModuleDescription
# 
# SQLite3からデータを取得するコンポーネント
# 
# 
# </rtc-template>
class read_SQLTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_db_out = OpenRTM_aist.instantiateDataType(TaskListSeq())
        """
        SQLite3 Database
		SELECT * FROM {table_name}
        """
        self._db_outIn = OpenRTM_aist.InPort("db_out", self._d_db_out)


        


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
        self.addInPort("db_out",self._db_outIn)
        
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
    
    #    ##
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
    
        return RTC.RTC_OK
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
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
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("read_SQLTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def read_SQLTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=read_sqltest_spec)
    manager.registerFactory(profile,
                            read_SQLTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    read_SQLTestInit(manager)
    read_SQL.read_SQLInit(manager)

    # Create a component
    comp = manager.createComponent("read_SQLTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

