# Python stubs generated by omniidl from idl/TaskList.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"idl/TaskList.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"idl/TaskList.idl")


# #include "BasicDataType.idl"
import BasicDataType_idl
_0_RTC = omniORB.openModule("RTC")
_0_RTC__POA = omniORB.openModule("RTC__POA")

# struct TaskList
_0__GlobalIDL.TaskList = omniORB.newEmptyClass()
class TaskList (omniORB.StructBase):
    _NP_RepositoryId = "IDL:TaskList:1.0"

    def __init__(self, tm, task_id, start_time, finish_time, target, status, title, discription):
        self.tm = tm
        self.task_id = task_id
        self.start_time = start_time
        self.finish_time = finish_time
        self.target = target
        self.status = status
        self.title = title
        self.discription = discription

_0__GlobalIDL.TaskList = TaskList
_0__GlobalIDL._d_TaskList  = (omniORB.tcInternal.tv_struct, TaskList, TaskList._NP_RepositoryId, "TaskList", "tm", omniORB.typeMapping["IDL:RTC/Time:1.0"], "task_id", omniORB.tcInternal.tv_long, "start_time", (omniORB.tcInternal.tv_string,0), "finish_time", (omniORB.tcInternal.tv_string,0), "target", (omniORB.tcInternal.tv_string,0), "status", omniORB.tcInternal.tv_boolean, "title", (omniORB.tcInternal.tv_string,0), "discription", (omniORB.tcInternal.tv_string,0))
_0__GlobalIDL._tc_TaskList = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_TaskList)
omniORB.registerType(TaskList._NP_RepositoryId, _0__GlobalIDL._d_TaskList, _0__GlobalIDL._tc_TaskList)
del TaskList

#
# End of module "_GlobalIDL"
#
__name__ = "TaskList_idl"

_exported_modules = ( "_GlobalIDL", )

# The end.