import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import sys
import subprocess

class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonService"
    _svc_display_name_ = "Python Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        # Specify the path to your Python script
        script_path = r"S:\Coding\python\withSQL\coral_ai\app.py"

        # Run the Python script in a subprocess with the console window
        process = subprocess.Popen(["C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\python.exe", script_path])

        # Wait for the service to be stopped
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        process.terminate()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PythonService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PythonService)
