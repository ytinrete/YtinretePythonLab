# using monkey runner to auto screen shot app
# useful for archive messages

# 0.1 make sure you have jdk1.8 in your env
# brew install openjdk@8
# ~/.bash_profile -> export PATH=/usr/local/opt/openjdk@8/bin:$PATH
# java -version

# 0.2 make sure monkey runner in the env variables
# export PATH=/path to android sdk/tools/bin:$PATH
# make sure you can call monkeyrunner on command line

# 1. navigate to message app, better make your phone in airplane mode to avoid accident

# 1.1 if you feel to long to scroll to top can run help_to_scroll method

# 2. the auto_shot method will get screenshot, can change the params to fit your phone

# 3. command line go to a empty folder, run: monkeyrunner "path to this script/AndroidAutoScreenShot.py"

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


def help_to_scroll():
    # connect to android phone
    print("start connection")
    device = MonkeyRunner.waitForConnection()
    print("done connection")

    # perform drag 5000 times, you can change this until it satisfy you
    for i in range(5000):
        start_pos = (500, 400)  # dragging start pos
        end_pos = (500, 1800)  # dragging end pos
        drag_duration = 0.5
        drag_step = 50
        device.drag(start_pos, end_pos, drag_duration, drag_step)
        # for android screen the (0, 0) is on top left so, the drag above is tended to scrolling up

        # wait a little bit
        MonkeyRunner.sleep(0.5)


def auto_shot():
    # connect to android phone
    print("start connection")
    device = MonkeyRunner.waitForConnection()
    print("done connection")

    # perform drag 5000 times, you can change this until it satisfy you
    for i in range(5000):
        img = device.takeSnapshot()
        img.writeToFile("ScreenShot_2021_03_21-" + str(i) + ".png", "png")

        start_pos = (500, 1800)  # dragging start pos
        end_pos = (500, 400)  # dragging end pos
        drag_duration = 0.5
        drag_step = 50
        device.drag(start_pos, end_pos, drag_duration, drag_step)
        # for android screen the (0, 0) is on top left so, the drag above is tended to scrolling up

        # wait a little bit
        MonkeyRunner.sleep(0.5)


if __name__ == '__main__':
    help_to_scroll()
    # auto_shot()
    print("done")
