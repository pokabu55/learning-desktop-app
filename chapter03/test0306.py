import PySimpleGUI as sg

sg.theme("DarkBrown3")

layout = [
    [sg.T("金額と人数を入力してください")],
    [sg.T("金額"), sg.I("1000", k="totalCost")],
    [sg.T("人数"), sg.I("4", k="number")],
    [sg.B("実行", k="calcBtn")],
    [sg.T("答え", k="outputTxt")],
]

win = sg.Window("割り勘アプリ", layout, font=(None, 14), size=(500, 300))


def execute():
    print("test")
    cost = int(v["totalCost"])
    num = int(v["number"])

    # 端数を別途計算したい
    payment = int(cost / num)
    fraction = cost - payment * num

    txt = f"１人あたりの金額は{payment:.0f}円で、端数は{fraction:.0f}円です。"
    win["outputTxt"].update(txt)


while True:
    e, v = win.read()

    if e == "calcBtn":
        execute()
    else:
        break


win.close()
