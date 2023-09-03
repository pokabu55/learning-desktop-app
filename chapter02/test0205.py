import PySimpleGUI as sg

# sg.theme("BrightColors")
sg.theme("DarkTeal2")

layout = [
    [sg.I("フタバ", k="in")],
    [sg.B("実行", k="btn")],
    [sg.T(k="txt")],
]
window = sg.Window("テスト", layout, font=(None, 12), size=(250, 120))


def execute():
    txt = "こんにちは" + v["in"] + "さん！"
    window["txt"].update(txt)


while True:
    e, v = window.read()
    if e == "btn":
        execute()
    if e == None:
        break
window.close()
