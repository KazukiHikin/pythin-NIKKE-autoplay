import threading
from component import overlay
from component.listen_for_key import listen_for_key
from component.singleton_flag import ProgramInterrupted
from order.order_interception import order_interception


# -----vscode起動時に右クリック→管理者として実行すること------------
# -----管理者じゃないとguiのclickが反応しない----------------------


if __name__ == "__main__":
    # listen_for_keyをバックグラウンドスレッドで実行
    thread = threading.Thread(target=listen_for_key, daemon=True)
    thread.start()  # スレッドを開始

    #----「自動操作中」の案内を表示（正常終了・中断・エラーのどれでも必ず消す）
    overlay_process = overlay.start()

    #----orderで画像クリック処理の開始
    try:
        order_interception()
        print("メインスクリプトの処理が終了しました")
    except ProgramInterrupted as e:
        print(f"キー入力により処理を中断しました:{e}")
    finally:
        overlay.stop(overlay_process)
