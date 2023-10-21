import PySimpleGUI as sg
sg.theme("LightGray6")
but_col1 = sg.Column([[sg.Slider(range=(0, 1), key="-AND1-", size=(4, 30), expand_x=True, pad=(0, 5))],
                      [sg.Slider(range=(0, 1), key="-AND2-", size=(4, 30), expand_x=True, pad=(0, 5))]])
but_col2 = sg.Column([[sg.Slider(range=(0, 1), key="-OR1-", size=(4, 30), expand_x=True, pad=(0, 5))],
                      [sg.Slider(range=(0, 1), key="-OR2-", size=(4, 30), expand_x=True, pad=(0, 5))]])
but_col3 = sg.Column([[sg.Slider(range=(0, 1), key="-NOT1-", size=(4, 30), expand_x=True, pad=0)]])
but_col4 = sg.Column([[sg.Slider(range=(0, 1), key="-NOTNOT1-", size=(4, 30), expand_x=True, pad=0)]])
but_col5 = sg.Column([[sg.Slider(range=(0, 1), key="-XOR1-", size=(4, 30), expand_x=True, pad=(0, 5))],
                      [sg.Slider(range=(0, 1), key="-XOR2-", size=(4, 30), expand_x=True, pad=(0, 5))]])
but_col6 = sg.Column([[sg.Slider(range=(0, 1), key="-XNOR1-", size=(4, 30), expand_x=True, pad=(0, 5))],
                      [sg.Slider(range=(0, 1), key="-XNOR2-", size=(4, 30), expand_x=True, pad=(0, 5))]])
first_lay = [
    [sg.Text("Welcome To Gate Tutorial App", font="Calibre 30", text_color="Red", expand_x=True, justification="center")],
    [sg.Text("Click On The Tabs To Get Started", font="Calibre 20", text_color="Black", expand_x=True,
             justification="center")],
     [sg.Image("pic/start.png", expand_x=True, expand_y=True)],
    [sg.Text("By Mohammad Ali Haririan", font="Calibre 10", text_color="Black", expand_x=True, justification="center")]
]
and_lay = [
    [sg.Column([
        [sg.Text("AND GATE", justification="center", font="Calibre 15", text_color="Black", expand_x=True,
                 pad=(5, 10))],
        [but_col1, sg.Image("pic/and.png", expand_x=True, expand_y=True, pad=0),
         sg.Image("pic/off.png", key="-ANDIMAGE-", expand_x=True, expand_y=True, pad=0)],
    ],justification="center")],
    [sg.Column([
        [sg.Image("pic/and_table.png", expand_x=True, expand_y=True, pad=(130, 0))]
    ])]
]
or_lay = [
    [sg.Column([
        [sg.Text("OR GATE", justification="center", font="Calibre 15", text_color="Black", expand_x=True, pad=(5, 10))],
        [but_col2, sg.Image("pic/or.png", expand_x=True, expand_y=True, pad=0),
         sg.Image("pic/off.png", key="-ORDIMAGE-", expand_x=True, expand_y=True, pad=0)],
    ],justification="center")],
    [sg.Column([
        [sg.Image("pic/or_table.png", expand_x=True, expand_y=True, pad=(130, 0))]
    ])]
]
not_lay = [
    [sg.Column([
        [sg.Text("NOT GATE", justification="center", font="Calibre 15", text_color="Black", expand_x=True,
                 pad=(5, 10))],
        [but_col3, sg.Image("pic/not.png", expand_x=True, expand_y=True, pad=0),
         sg.Image("pic/on.png", key="-NOTIMAGE-", expand_x=True, expand_y=True, pad=0)],
    ],justification="center")],
    [sg.Column([
        [sg.Image("pic/not_table.png", expand_x=True, expand_y=True, pad=(130, 40))]
    ])]
]
notnot_lay = [
    [sg.Column([
        [sg.Text("NOT NOT GATE", justification="center", font="Calibre 15", text_color="Black", expand_x=True,
                 pad=(5, 10))],
        [but_col4, sg.Image("pic/notnot.png", expand_x=True, expand_y=True, pad=0),
         sg.Image("pic/off.png", key="-NOTNOTIMAGE-", expand_x=True, expand_y=True, pad=0)],
    ],justification="center")],
    [sg.Column([
        [sg.Image("pic/notnot_table.png", expand_x=True, expand_y=True, pad=(130, 40))]
    ])]
]
xor_lay = [
    [sg.Column([
        [sg.Text("XOR GATE", justification="center", font="Calibre 15", text_color="Black", expand_x=True,
                 pad=(5, 10))],
        [but_col5, sg.Image("pic/xor.png", expand_x=True, expand_y=True, pad=0),
         sg.Image("pic/off.png", key="-XORIMAGE-", expand_x=True, expand_y=True, pad=0)],
    ],justification="center"), ],
    [sg.Column([
        [sg.Image("pic/xor_table.png", expand_x=True, expand_y=True, pad=(130, 0))]
    ])]

]
xnor_lay = [
    [sg.Column([
        [sg.Text("XNOR GATE", justification="center", font="Calibre 15", text_color="Black", expand_x=True,
                 pad=(5, 10))],
        [but_col6, sg.Image("pic/xnor.png", expand_x=True, expand_y=True, pad=0),
         sg.Image("pic/off.png", key="-XNORIMAGE-", expand_x=True, expand_y=True, pad=0)],
    ],justification="center")],
    [sg.Column([
        [sg.Image("pic/xnor_table.png", expand_x=True, expand_y=True, pad=(130, 0))]
    ])]
]
about_tab = [
    [sg.Text("֍ Ver 2", font="Calibre 15", text_color="Red", expand_x=True, justification="left")],
    [sg.Text("1-Optimize The Code", font="Calibre 15", text_color="Blue", expand_x=True, justification="left")],
    [sg.Text("2-Quality Images", font="Calibre 15", text_color="Blue", expand_x=True, justification="left")],
    [sg.Text("3-Add Start And About Tabs", font="Calibre 15", text_color="Blue", expand_x=True, justification="left")],
    [sg.Text("-----------------------------------------------------------------", font="Calibre 15", text_color="Black",
             expand_x=True, justification="left")],
    [sg.Image("pic/instagram.png", pad=0), sg.Text("@maharirian", font="Calibre 15",text_color="black", pad=0)],
    [sg.Image("pic/telegram.png", pad=0), sg.Text("@ma_haririan", font="Calibre 15",text_color="black", pad=0)],
    [sg.Image("pic/site.png", pad=0), sg.Text("haririan.ir", font="Calibre 15",text_color="black", pad=0)],
]
tab_group = [[
    sg.TabGroup(
        [[
            sg.Tab("START", first_lay),
            sg.Tab("AND", and_lay),
            sg.Tab("OR", or_lay),
            sg.Tab("NOT", not_lay),
            sg.Tab("NOTNOT", notnot_lay),
            sg.Tab("XOR", xor_lay),
            sg.Tab("XNOR", xnor_lay),
            sg.Tab("ABOUT", about_tab)
        ]],
        tab_location="centertop",
        title_color="White",
        tab_background_color="Black",
        selected_title_color="Red",
        selected_background_color="White"
    )
]]
window = sg.Window("Gate", tab_group)
while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break
    # and sec
    if values["-AND1-"] == 1 and values["-AND2-"] == 1:
        window["-ANDIMAGE-"].update("pic/on.png")
    else:
        window["-ANDIMAGE-"].update("pic/off.png")
    # or sec
    if values["-OR1-"] == 1 or values["-OR2-"] == 1:
        window["-ORDIMAGE-"].update("pic/on.png")
    else:
        window["-ORDIMAGE-"].update("pic/off.png")
    # not sec
    if values["-NOT1-"] == 0:
        window["-NOTIMAGE-"].update("pic/on.png")
    else:
        window["-NOTIMAGE-"].update("pic/off.png")
    # not not sec
    if values["-NOTNOT1-"] == 0:
        window["-NOTNOTIMAGE-"].update("pic/off.png")
    else:
        window["-NOTNOTIMAGE-"].update("pic/on.png")
    # xor sec
    if values["-XOR1-"] != values["-XOR2-"]:
        window["-XORIMAGE-"].update("pic/on.png")
    else:
        window["-XORIMAGE-"].update("pic/off.png")
    # xnor sec
    if values["-XNOR1-"] == values["-XNOR2-"]:
        window["-XNORIMAGE-"].update("pic/on.png")
    else:
        window["-XNORIMAGE-"].update("pic/off.png")
window.close()
