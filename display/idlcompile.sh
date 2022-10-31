#!/bin/sh
IDL_PATH=`rtm-config --rtm-idldir`
omniidl -bpython -I$IDL_PATH idl/TaskList.idl idl/TaskListSeq.idl 