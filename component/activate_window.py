import pyautogui
import pygetwindow as gw
import time


#--------------------------------------------
#--------指定したウィンドウをアクティブにする関数
#--------------------------------------------

def activate_window():
    #アクティブにしたいアプリケーションの名前を指定
    window_title = "NIKKE"
    print(f"{window_title}のアクティブONの関数実行")
    #マウスが画面の隅に移動すると強制的に停止する機能OFF
    pyautogui.FAILSAFE = False 

    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()
        print(f"{window_title}のウィンドウがアクティブになりました")
        print("")
        time.sleep(1)   #アクティブ後1秒待機
    else:
        print(f"{window_title}のウィンドウが見つかりません")
        print("")