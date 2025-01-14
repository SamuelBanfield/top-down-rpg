from .backend import back_requests as bk
from .backend import processing as pr

if __name__ == '__main__':
    requester = bk.Requests(bk.TurnNotificationSubscription())
    requester.init(1)
    if 0 in requester.functions.chart.characters:
        print('hello')


