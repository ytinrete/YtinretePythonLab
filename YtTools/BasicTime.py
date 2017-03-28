import datetime
import pytz

if __name__ == '__main__':
    tz = pytz.timezone('Asia/Shanghai')

    timestamp = int('1490714537')
    timeStr = datetime.datetime.fromtimestamp(timestamp, tz=tz).strftime('%Y-%m-%d %H:%M:%S:%f')
    print(timeStr)

    timestamp = (float('1490177910052')/1000)
    timeStr = datetime.datetime.fromtimestamp(timestamp, tz=tz).strftime('%Y-%m-%d %H:%M:%S:%f')
    print(timeStr[0:-3])

    time_str_now = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S:%f')
    print(time_str_now)


    timestamp = int(datetime.datetime.now().timestamp())
    print(timestamp)#1490715003

    pass
