@echo off
echo Restarting Python Service...
python service_wrapper.py stop
python service_wrapper.py start
