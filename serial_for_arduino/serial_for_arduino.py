#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file serial_for_arduino.py
 @brief SerialCommunicationWithArduino.
 @date $Date$


"""
# </rtc-template>

import sys
import time
import serial
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
serial_for_arduino_spec = ["implementation_id", "serial_for_arduino", 
         "type_name",         "serial_for_arduino", 
         "description",       "SerialCommunicationWithArduino.", 
         "version",           "1.1.1", 
         "vendor",            "HarutoFuruyama", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.com_port", "COM3",

         "conf.__widget__.com_port", "text",

         "conf.__type__.com_port", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class serial_for_arduino
# @brief SerialCommunicationWithArduino.
# 
# 
# </rtc-template>
class serial_for_arduino(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_LCD_strings = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._LCD_stringsIn = OpenRTM_aist.InPort("LCD_strings", self._d_LCD_strings)
        self._d_button_result = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        """
        self._button_resultOut = OpenRTM_aist.OutPort("button_result", self._d_button_result)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        シリアル通信ポート
         - Name: com_port com_port
         - DefaultValue: COM3
        """
        self._com_port = ['COM3']
		
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
        self.bindParameter("com_port", self._com_port, "COM3")
		
        # Set InPort buffers
        self.addInPort("LCD_strings",self._LCD_stringsIn)
		
        # Set OutPort buffers
        self.addOutPort("button_result",self._button_resultOut)
		
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
        self.ser = serial.Serial(self._com_port[0],9600)

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
        self.ser.close()
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
        if self._LCD_stringsIn.isNew():
            LCD_strings = self._LCD_stringsIn.read().data
            self.ser.write(LCD_strings+'.')

        if self.ser.read_all() == b'1':
            self._d_button_result.data = 1
            self._button_resultOut.write()
            print('button_on')

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
	



def serial_for_arduinoInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=serial_for_arduino_spec)
    manager.registerFactory(profile,
                            serial_for_arduino,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    serial_for_arduinoInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("serial_for_arduino" + args)

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

