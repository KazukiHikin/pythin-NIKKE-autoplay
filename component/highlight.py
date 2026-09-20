import ctypes
import time
import tkinter as tk

#--------------------------------------------------------------
#--画像が見つかった位置を、クリック前に赤枠で画面に表示する
#--確認用の機能なので、表示に失敗しても自動化処理は止めない
#--------------------------------------------------------------

ENABLED = True          #Falseにすると枠を出さなくなる
BORDER_COLOR = "red"
BORDER_WIDTH = 4
TRANSPARENT_COLOR = "magenta"   #この色の部分が透明になる(枠以外を見えなくするため)

GWL_EXSTYLE = -20
WS_EX_TRANSPARENT = 0x00000020  #クリックが枠を素通りしてゲームに届くようにする
WS_EX_NOACTIVATE = 0x08000000   #枠がフォーカスを奪ってゲームが非アクティブになるのを防ぐ
WS_EX_TOOLWINDOW = 0x00000080   #タスクバーに出さない


def _make_overlay_non_interactive(window):
    hwnd = ctypes.windll.user32.GetParent(window.winfo_id()) or window.winfo_id()
    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(
        hwnd, GWL_EXSTYLE, style | WS_EX_TRANSPARENT | WS_EX_NOACTIVATE | WS_EX_TOOLWINDOW
    )


def show_box(left, top, width, height, seconds=0.6):
    if not ENABLED:
        return

    root = None
    try:
        root = tk.Tk()
        root.overrideredirect(True)      #タイトルバーや枠を消す
        root.attributes("-topmost", True)
        root.attributes("-transparentcolor", TRANSPARENT_COLOR)
        root.geometry(f"{width}x{height}+{left}+{top}")

        canvas = tk.Canvas(root, width=width, height=height,
                           bg=TRANSPARENT_COLOR, highlightthickness=0)
        canvas.pack()
        half = BORDER_WIDTH // 2
        canvas.create_rectangle(half, half, width - half, height - half,
                                outline=BORDER_COLOR, width=BORDER_WIDTH)

        root.update()
        _make_overlay_non_interactive(root)
        root.update()
        time.sleep(seconds)
    except Exception as e:
        print(f"(枠の表示に失敗しましたが処理は続行します: {e})")
    finally:
        if root is not None:
            try:
                root.destroy()
            except Exception:
                pass
