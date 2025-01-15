import keyboard
import sys
import time

stop_flag = False

def listen_for_key():
    global stop_flag
    print("キー入力を監視中-----（Escキーを押すと終了）")
    while not stop_flag:
        if keyboard.is_pressed("w"):
            print("Escキーが押されました。pythonプログラムを強制終了します。")
            stop_flag = True
            print(f"stop_flag:{stop_flag}")
            break
        time.sleep(0.5) #0.5秒毎にwhileを実行