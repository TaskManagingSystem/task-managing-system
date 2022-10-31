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
# @class read_SQLTest
# @brief ModuleDescription
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

        self._d_task_list = OpenRTM_aist.instantiateDataType(RTC.TimedLongSeq)
        """
        """
        self._task_task_idIn = OpenRTM_aist.InPort("task_task_id", self._d_task_list)
        self._d_latest_task = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._latest_taskIn = OpenRTM_aist.InPort("latest_task", self._d_latest_task)
        self._d_task_start_time = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_start_timeIn = OpenRTM_aist.InPort("task_start_time", self._d_task_start_time)
        self._d_task_finish_time = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_finish_timeIn = OpenRTM_aist.InPort("task_finish_time", self._d_task_finish_time)
        self._d_task_target = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_targetIn = OpenRTM_aist.InPort("task_target", self._d_task_target)
        self._d_task_status = OpenRTM_aist.instantiateDataType(RTC.TimedBooleanSeq)
        """
        """
        self._task_statusIn = OpenRTM_aist.InPort("task_status", self._d_task_status)
        self._d_task_title = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_titleIn = OpenRTM_aist.InPort("task_title", self._d_task_title)
        self._d_task_explanation = OpenRTM_aist.instantiateDataType(RTC.TimedStringSeq)
        """
        """
        self._task_explanationIn = OpenRTM_aist.InPort("task_explanation", self._d_task_explanation)


        


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
        self.addInPort("task_task_id",self._task_task_idIn)
        self.addInPort("latest_task",self._latest_taskIn)
        self.addInPort("task_start_time",self._task_start_timeIn)
        self.addInPort("task_finish_time",self._task_finish_timeIn)
        self.addInPort("task_target",self._task_targetIn)
        self.addInPort("task_status",self._task_statusIn)
        self.addInPort("task_title",self._task_titleIn)
        self.addInPort("task_explanation",self._task_explanationIn)
        
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

