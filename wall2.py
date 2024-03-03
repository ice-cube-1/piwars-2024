import robot2
import settings
import controller
import time
#BL - 0
#BR - 1
#FL - 2
#FR - 3
name2idx={'BL':0, 'BR':1,'FL':2,'FR':3}
t=5
mindistance=20
left=-0.75
right=0.75

def update(pwm,sensors):
    readings = robot2.getToFReadings(sensors)
    print('readings',readings)
    bl=readings[name2idx['BL']]
    if bl == 0:
        bl=1000
    br=readings[name2idx['BR']]
    if br==0:
        br=1000
    fl=readings[name2idx['FL']]
    if fl==0:
        fl=1000
    fr=readings[name2idx['FR']]
    if fr==0:
        fr=1000
    if fl<fr:
        if fl<mindistance:
            robot2.turn(right,0,pwm)
        else:
            if fl+t<bl:
                robot2.turn(right,0,pwm)
            elif bl+t<fl:
                robot2.turn(left,0,pwm)
            else:
                robot2.turn(0,100,pwm)
    else:
        if fr<mindistance:
            robot2.turn(left,0,pwm)
        else:
            if fr+t<br:
                robot2.turn(left,0,pwm)
            elif br+t<fr:
                robot2.turn(right,0,pwm)
            else:
                robot2.turn(0,100,pwm)
    #if readings[name2idx['BL']]+t<readings[name2idx["FL"]] or readings[name2idx['FR']]+t<readings[name2idx["BR"]]:
        #print('-0.5')
        #robot2.turn(-1,0,pwm)
    #elif readings[name2idx['FL']]+t<readings[name2idx["BL"]] or readings[name2idx['BR']]+t<readings[name2idx["FR"]]:
        #print('0.5')
        #robot2.turn(1,0,pwm)
    #else:
        #print('-0')
        #robot2.turn(0,1,pwm)

    # if readings[name2idx["FR"]] > readings[name2idx["BR"]]+t or readings[name2idx["FL"]]+t < readings[name2idx["BL"]]:
    #     robot2.turn(-0.5,0,pwm)
    #     print('1aaa')
    # elif readings[name2idx["FL"]] > readings[name2idx["BL"]] +t or readings[name2idx["FR"]]+t < readings[name2idx["BR"]]:
    #     robot2.turn(0.5,0,pwm)
    #     print('2')
    # else:
    #     robot2.turn(0,1,pwm)
    #     print('3')
    # if readings[name2idx["FL"]]-readings[name2idx["FR"]] > 10:
    #     robot2.turn(0.5,0,pwm)
    #     print('4')
    # if readings[name2idx["FR"]]-readings[name2idx["FL"]] > 10:
    #     robot2.turn(-0.5,0,pwm)
    #     print('5')
    # if readings[name2idx["FR"]]>60 or readings[name2idx["FL"]] > 60:
    #     print('6')
    #     return True

def run(remote,pwm,sensors):
    time.sleep(1)
    print('hello ')
    robot2.forwards(-1)
    while True:
        update(pwm,sensors)
        if controller.get('A',remote) == 1:
            robot2.forwards(0)
            time.sleep(1)
            print('quit')
            return
