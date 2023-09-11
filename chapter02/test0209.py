import PySimpleGUI as sg

sg.theme("DarkBrown3")

layout = [
    [sg.T("１行１列目"), sg.T("１行２列目")],
    [sg.T("２行１列目"), sg.T("２行２列目")],
    [sg.T("３行１列目"), sg.B("ボタン")],
]

win = sg.Window("要素レイアウトテスト", layout, font=(None, 14), size=(300, 120))

e, v = win.read()
win.close()
