from pywinauto.application import Application
import time
import subprocess
import os
from pywinauto import Desktop

# Path to your installer
installer_path = os.path.abspath("installer/Carbonite-personal-client.exe")

# Use PowerShell to run the installer with elevated privileges
# command = f'powershell Start-Process "{installer_path}" -Verb RunAs'
# subprocess.call(command, shell=True)
# Launch the installer with elevation
subprocess.Popen([
    "powershell", 
    "Start-Process", 
    f'"{installer_path}"', 
    "-Verb", 
    "RunAs"
], shell=True)

# Wait for the window to appear
time.sleep(20)  # Increase if needed

# # Launch installer and Connect to the window
# app = Application(backend="win32").connect(path="Carbonite-personal-client.exe")
# dlg = app.window(title_re=".*Setup.*")
for w in Desktop(backend="uia").windows():
    print(w.window_text())

# command = f'powershell Start-Process "{installer_path}" -Verb RunAs'
# subprocess.call(command, shell=True)
#app = Application(backend="uia").start(installer_path)

# dlg = Desktop(backend='uia').ProgramManager
# dlg.wait('visible')
app = Application(backend="uia").connect(path=installer_path)
# dlg = app.top_window()
# dlg.wait('visible', timeout=15)
# print("Installer window found.")

# Wait until the window is ready
# dlg.wait('visible', timeout=2)

# Example installation steps (may vary depending on installer)
#dlg.print_control_identifiers()
# time.sleep(1)
# dlg.Agree.click_input()
# time.sleep(1)
# dlg.Install.click_input()
# dlg.Finish.wait('visible', timeout=60)
# dlg.Finish.click_input()

print("✅ Installation completed successfully.")
