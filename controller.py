import pygame

def initialize():
    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() > 0:
        controller = pygame.joystick.Joystick(0)
        controller.init()
        print("Controller connected:",controller.get_name())
        return controller
    else:
        print("Initialization failed")



map = {
    "LX": ["A",0],
    "LY": ["A",1],
    "RX": ["A",2],
    "RY": ["A",3],
    "RTRIG": ["A",4],
    "LTRIG": ["A",5],

    "A": ["B",0],
    "B": ["B",1],
    "X": ["B",3],
    "Y": ["B",4],

    "LBUMP": ["B",6],
    "RBUMP": ["B",7],

    "LMENU": ["B",10],
    "RMENU": ["B",11],
    "XLOGO": ["B",12],

    "HAT": ["H",0]  

}

def get(toget, controller):
    pygame.event.get()
    if map[toget][0] == "A":
        return controller.get_axis(map[toget][1])
    if map[toget][0] == "B":
        return controller.get_button(map[toget][1])
    return controller.get_hat(map[toget][1])
