from component.activate_window import activate_window
from component.click_image import click_image
from component.wait_for_image import wait_for_image
import keyboard

#--------------
#--迎撃戦を自動化
#--------------

def order_interception():
    #----ウィンドウを検索してアクティブにする----
    activate_window()
    #----「アーク」の画像をクリック----
    wait_for_image(image_path="img/arc.png",image_name="アーク",pass_confidence=0.8)
    #----「迎撃戦の画像」をクリック----
    wait_for_image(image_path="img/interception.png",image_name="迎撃戦",pass_confidence=0.8)
    #----「迎撃戦-特殊個体」の画像をクリック----
    wait_for_image(image_path="img/interception_special.png",image_name="迎撃戦-特殊個体",pass_confidence=0.8)
    #----「戦闘突入の画像」をクリック----
    wait_for_image(image_path="img/Entering_battle.png",image_name="戦闘突入",pass_confidence=0.8)
    #----「空いてるところをタップ」の画像をクリック----
    wait_for_image(image_path="img/tap_empty_space.png",image_name="空いてるところをタップ",pass_confidence=0.8,retry_maxcount=180)

