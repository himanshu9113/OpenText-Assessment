import time
from pywinauto import Application, timings
from pywinauto.findwindows import ElementNotFoundError
import os
import subprocess


# --- Configuration ---
# Path to Carbonite installer executable
INSTALLER_PATH = os.path.abspath("installer/Carbonite-personal-client.exe")
INSTALLER_WINDOW_TITLE = "Installing Carbonite" 
# Timeout for finding window
TIMEOUT = 30


def automate_carbonite_installation():
   
   print(f"Starting Carbonite installer: {INSTALLER_PATH}")


   try:
       # Start the application
       # If UAC prompt appears, you will need to manually click 'Yes'.
       proc = subprocess.Popen(f'"{INSTALLER_PATH}"', shell=True)
       time.sleep(5)

       app = Application(backend="uia").start(INSTALLER_PATH)
       print("Application started. Waiting for installer window...")


       # Connect to the installer window
       timings.wait_until_passes(TIMEOUT, 1, lambda: app.window(title_re=INSTALLER_WINDOW_TITLE).exists())
       main_window = app.window(title_re=INSTALLER_WINDOW_TITLE)
       main_window.wait('ready', timeout=TIMEOUT)
       print(f"Connected to installer window: '{main_window.window_text()}'")

       try:
           
           agree_checkbox = main_window.child_window(title = "I agree", control_type="CheckBox")
           agree_checkbox.click()
           continue_button = main_window.child_window(title="Continue", control_type="Button")
           print("Found 'Continue' button. Clicking it...")
           continue_button.click()
           print("'Continue' button clicked.")
           time.sleep(2) # Give some time for the next screen to load
       except ElementNotFoundError:
           print("Warning: 'Continue' button not found. Assuming it's not present or already clicked.")


       # Find and click the 'Next' button
       try:
           timings.wait_until_passes(TIMEOUT, 1, lambda: main_window.child_window(title_re=INSTALLER_WINDOW_TITLE, control_type="Button").exists())
           next_button = main_window.child_window(title="Next", control_type="Button")
           print("Found 'Next' button. Clicking it...")
           next_button.click()
           print("'Next' button clicked.")
           time.sleep(5) # Give time for the installer to close
       except ElementNotFoundError:
           print("Error: 'Next' button not found. The installation might not have completed as expected.")


       print("Automation complete. Verifying application closure...")
       # Check if the application process is still running
       try:
           app.kill()
           print("Installer process terminated.")
       except Exception as e:
           print(f"Could not kill installer process (it might have already closed): {e}")


   except ElementNotFoundError as e:
       print(f"Error: Could not find a required UI element. Please check window titles and control identifiers. Details: {e}")
       print("Tip: Use 'pywinauto.inspect.exe' to inspect the application's UI elements.")
   except Exception as e:
       print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
   automate_carbonite_installation()

