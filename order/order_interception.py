from component.activate_window import activate_window
from component.click_image import click_image
from component.wait_for_image import wait_for_image

#--------------
#--迎撃戦を自動化
#--------------

def order_interception():
    #----ウィンドウを検索してアクティブにする----
    activate_window()
    #----アークの画像をクリック----
    # click_image(image_path="img/arc.png",pass_confidence=0.8)
    wait_for_image(image_path="img/arc.png",image_name="アーク",pass_confidence=0.8)
    #----迎撃戦の画像をクリック----
    # click_image(image_path="img/interception.png",pass_confidence=0.8)
    wait_for_image(image_path="img/interception.png",image_name="迎撃戦",pass_confidence=0.8)