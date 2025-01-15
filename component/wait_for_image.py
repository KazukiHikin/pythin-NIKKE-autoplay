import pyautogui
import time
import traceback
from component.listen_for_key import stop_flag


#指定された画像が見つかるまで待機し、見つかったらクリック。
#最大試行回数に達したら例外をスローする。
#image_path (str): 検索する画像ファイルのパス
#confidence (float): 画像検索の信頼度 (0.0~1.0)。
#max_retries (int): 最大試行回数。
#image_locationは画像が見つかった場合見つかった画像の位置とサイズを表す辞書 (Dictionary) 形式のオブジェクトです。
# 以下のキーを含んでいます：
#left: 画像の左端のX座標,top: 画像の上端のY座標,width: 画像の幅,height: 画像の高さ


#重要
#pyautogui.locateOnScreenの画像判定はNGだとエラーを返し処理が中団する為、try-except文じゃないと処理が進まない

#関数に初期値を設定することで呼び出し時に引数を設定しない場合にデフォルトで関数で設定した値が使われる
def wait_for_image (image_path,image_name, pass_confidence, retry_maxcount=10) :
    time_count = 1.0
    retry_count = 0
    # retry_maxcount = 10
    image_location = None

    #whileの前にプログラム中断flagの追加
    
    while retry_count < retry_maxcount:
        #locateOnScreenでimage_pathの画像が画面上にあるか判定
        try:
            image_location = pyautogui.locateOnScreen(image_path,confidence=pass_confidence)
        except Exception as e :
            #time関数で1秒待ってから再度処理が流れる
            retry_count += 1
            print(f"画像、{image_name}が見つかりません。画像パス、{image_path}。{retry_count}/{retry_maxcount}回目の再確認。{time_count}秒後に再確認します")
            # print(traceback.format_exc())   #今回のtry-exceptのエラーをコンソールに表示、画像の一致率見れる
            time.sleep(time_count)

        if image_location:
            
            pyautogui.click(pyautogui.center(image_location),duration=1)
            print("")
            print(f"OK:{image_name}のセンター位置にマウス移動＋クリックが完了しました")
            print("")
            time.sleep(time_count)     #1.0秒待機
            #関数処理終了させるためreturnを使う
            return image_location
        
            
    
    raise RuntimeError(f"画像{image_path}が見つかりませんでした。最大試行回数{retry_maxcount}回に到達しました。raise呼び出しの為処理を中断します")