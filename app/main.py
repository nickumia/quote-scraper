##  Quote-scraper and sender
#   Developer: nickumia


from datetime import datetime
import json
import pytz
import socket
import time

import gather
import sender

EXECUTED = False

if __name__=="__main__":
    print("Quote Scraper UP")

    quote = gather.get_quote()
    s = socket.socket()
    s.connect(('mail', 4444))
    s.send(json.dumps(quote).encode('utf-8'))
    s.close()

    while True:
        time.sleep(5)
        current_time = datetime.now().astimezone(
                        pytz.timezone('US/Eastern'))
        action_time = current_time.replace(hour=7, minute=0,
                                            second=0, microsecond=0)
        reset_time = current_time.replace(hour=0, minute=5,
                                            second=0, microsecond=0)
        print(current_time)
        print(action_time)
        if current_time >= action_time and not EXECUTED:
            print("should run")
            quote = gather.get_quote()
            print(quote)
            EXECUTED = True
            gather.IMG = not gather.IMG
        elif current_time >= action_time and EXECUTED:
            print("already ran")
        elif current_time <= reset_time:
            print("reset for the new day")
            EXECUTED = False
        else:
            print("not ready")
