echo off
cd /d %~dp0
for /d %%i in (*) do (
  rmdir /s/q %%i
)
for %%i in (*.py*) do (
  del /s/q %%i
)
