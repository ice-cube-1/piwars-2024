import controller
import manual3
import wall2
import robot2
pwm,sensors=robot2.initialise()
remote=controller.initialize()
while True:
    if controller.get('A',remote) == 1:
        wall2.run(remote,pwm,sensors)
    if controller.get('B',remote) == 1:
        manual3.run(remote,pwm,sensors)