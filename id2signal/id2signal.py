#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file id2signal.py
 @brief ChangeIdIntoSignal
 @date $Date$


"""
# </rtc-template>

import sys
import time
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
id2signal_spec = ["implementation_id", "id2signal", 
         "type_name",         "id2signal", 
         "description",       "ChangeIdIntoSignal", 
         "version",           "1.0.0", 
         "vendor",            "Haruto Furuyama", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.machine_id", "'0'",

         "conf.__widget__.machine_id", "text",

         "conf.__type__.machine_id", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class id2signal
# @brief ChangeIdIntoSignal
# 
# 
# </rtc-template>
class id2signal(OpenRTM_aist.DataFlowComponentBase):
	
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
        self._d_signal_out = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
        """
        """
        self._signal_outOut = OpenRTM_aist.OutPort("signal_out", self._d_signal_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  machine_id
         - DefaultValue: '0'
        """
        self._machine_id = ['0']
		
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
        self.bindParameter("machine_id", self._machine_id, "'0'")
		
        # Set InPort buffers
        self.addInPort("latest_task",self._latest_taskIn)
		
        # Set OutPort buffers
        self.addOutPort("signal_out",self._signal_outOut)
		
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
        # latest_taskにデータが来たときの処理
        if self._latest_taskIn.isNew():
            latest_task = self._latest_taskIn.read().data
            # 実行対象のターゲットがコンフィグレーション変数で設定したものと同じだったときの処理
            if latest_task[3] == self._machine_id[0]:
                # 開始時刻の取得
                start_time = datetime.strptime(latest_task[1],'%Y-%m-%d %H:%M:%S')
                # 開始時刻になった時に信号を送信する処理
                if  (start_time-datetime.now()).total_seconds() > 0:
                    self._d_signal_out.data = True
                    self._signal_outOut.write()
                    print(self._d_signal_out.data)
                    time.sleep(1)
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
	



def id2signalInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=id2signal_spec)
    manager.registerFactory(profile,
                            id2signal,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    id2signalInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("id2signal" + args)

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

