import pyautogui
from component.activate_window import activate_window
from component.click_image import click_image
from order.order_interception import order_interception

# -----vscode起動時に右クリック→管理者として実行すること------------
# -----管理者じゃないとguiのclickが反応しない----------------------


#キーボードの入力を監視するコンポーネントを別で作成する
#それをorder_inberceptionやwait_for_imageに組めるようにする
order_interception()

print("メインスクリプトの処理が終了しました")


