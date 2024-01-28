import subprocess
import pyautogui
import time

def main():
    path = r'C:\Users\kyoto\digitizer\WaveDump.exe'
    subprocess.Popen(path)
    time.sleep(10)
    pyautogui.press('s')
    time.sleep(5)
    pyautogui.press('W')
    time.sleep(30)
    pyautogui.press('W')
    time.sleep(5)
    pyautogui.press('s')
    time.sleep(1)
    pyautogui.press('q')

if __name__ == '__main__':
    main()