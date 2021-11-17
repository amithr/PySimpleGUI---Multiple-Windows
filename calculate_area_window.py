import PySimpleGUI as sg
import math

def create():
    calculate_area_layout = [[sg.Text("Enter radius in centimeters"), sg.Input(key='-RADIUS-', do_not_clear=True, size=(5, 1))],
          [sg.Text(size=(20, 1), justification='right', key='-OUT-AREA-CALCULATION-'),
           sg.Text(' centimeters squared')],
          [sg.Button("Calculate Area"), sg.Button('Quit')]
    ]  

    calculate_area_window = sg.Window('Calculate Circle Area', calculate_area_layout)

    while True:
        event, values = calculate_area_window.read()
        if event in (None, 'Quit'):
            break
        elif event == 'Calculate Volume':
            radius = float(values['-RADIUS-'])
            area = math.pi*(radius**2)
            calculate_area_window['-OUT-AREA-CALCULATION-'].Update(area)
    
    calculate_area_window.close()