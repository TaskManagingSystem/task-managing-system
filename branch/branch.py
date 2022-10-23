#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file branch.py
 @brief HardwareControl
 @date $Date$


"""
# </rtc-template>

import sys
import time
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
branch_spec = ["implementation_id", "branch", 
         "type_name",         "branch", 
         "description",       "HardwareControl", 
         "version",           "1.0.0", 
         "vendor",            "Haruto Furuyama", 
         "category",          "Controller", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class branch
# @brief HardwareControl
# 
# 
# </rtc-template>
class branch(OpenRTM_aist.DataFlowComponentBase):
	
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
        self._d_input_button = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._input_buttonIn = OpenRTM_aist.InPort("input_button", self._d_input_button)
        self._d_LCD_strings = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._LCD_stringsOut = OpenRTM_aist.OutPort("LCD_strings", self._d_LCD_strings)
        self._d_complete_task_id = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._complete_task_idOut = OpenRTM_aist.OutPort("complete_task_id", self._d_complete_task_id)


		


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
        self.addInPort("input_button",self._input_buttonIn)
		
        # Set OutPort buffers
        self.addOutPort("LCD_strings",self._LCD_stringsOut)
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
        print(Deactivated)
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
        # latest_taskにデータが送信されてきたときの処理
        if self._latest_taskIn.isNew():
            # latest_taskのデータを取得
            latest_task = self._latest_taskIn.read().data

            # I2C_2_LCDから送信するための文字列を生成
            display_str = '{0}\n{1} ﾏﾃﾞ'.format(latest_task[4],latest_task[2].split(' ')[1])
            self._d_I2C_to_LCD.data = display_str
            self._I2C_to_LCDOut.write()
            print(display_str)

        # input_buttonにデータが送信されてきたときの処理
        if self._input_buttonIn.isNew():
            button_data = self._input_buttonIn.read().data
            if button_data == 1:
                self._d_complete_task_id.data = latest_task[0]
                self._complete_task_idOut.write()
                print('pushed!')
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
	



def branchInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=branch_spec)
    manager.registerFactory(profile,
                            branch,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    branchInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("branch" + args)

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

