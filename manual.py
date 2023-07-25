import controller

remote=controller.initialize()

while True:
    print(controller.get("HAT",remote))