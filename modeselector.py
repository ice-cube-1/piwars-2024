import controller
import manual3
#import wallfollower

remote=controller.initialize()
while True:
    # if controller.get('A',remote) == 1:
    #     wallfollower.run()
    if controller.get('B',remote) == 1:
        manual3.run(remote)