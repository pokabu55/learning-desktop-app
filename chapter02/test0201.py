import PySimpleGUI as sg

# fmt:off
layout = [[sg.Input("ふたば")],
          [sg.Button("実行")], 
          [sg.Text("こんにちは")]]
# fmg:on
window = sg.Window("テスト", layout)

event, values = window.read()
window.close()
