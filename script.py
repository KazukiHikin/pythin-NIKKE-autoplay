import pyautogui
import sys
import threading
from component.activate_window import activate_window
from component.click_image import click_image
from component.listen_for_key import listen_for_key
from component.listen_for_key import stop_flag
from order.order_interception import order_interception


# -----vscode起動時に右クリック→管理者として実行すること------------
# -----管理者じゃないとguiのclickが反応しない----------------------


#キーボードの入力を監視するコンポーネントを別で作成する
#それをorder_inberceptionやwait_for_imageに組めるようにする


if __name__ == "__main__":
    # listen_for_keyをバックグラウンドスレッドで実行
    thread = threading.Thread(target=listen_for_key, daemon=True)
    thread.start()  # スレッドを開始


order_interception()
print("メインスクリプトの処理が終了しました")