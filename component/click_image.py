import pyautogui
import time
import traceback

#----------------------------------------------------------
#--image_pathの画像が画面上で画像認識OKなら画像クリックする処理
#---------------------------------------------------------

def click_image(image_path, pass_confidence):
    # 
    # 指定した画像を検索し、見つかればクリックする関数
    # 
    image_location = None
    try:
        image_location = pyautogui.locateOnScreen(image_path,confidence=pass_confidence)
    except Exception as e :
        print("エラーが発生しました")
        print(traceback.format_exc())   #今回のtry-exceptのエラーをコンソールに表示
    
    if image_location:
        #画像が見つかった場合、中央をクリック
        pyautogui.click(pyautogui.center(image_location),duration=1)
        print(f"OK:{image_path}のセンター位置に移動、クリック")
        time.sleep(3.0)     #1.0秒待機
    else:
        print(f"{image_path}が見つかりません")