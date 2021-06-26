##  Main Scheduler to coordinate when quote is reteived and sent
#   Developer: nickumia


from datetime import datetime
import json
import pytz
import random
import socket
import time

EXECUTED = False

if __name__ == "__main__":
    print("Scheduler UP")
    random.seed()

    while True:
        time.sleep(5)
        current_time = datetime.now().astimezone(
                        pytz.timezone('US/Eastern'))
        action_time = current_time.replace(hour=7, minute=0,
                                            second=0, microsecond=0)
        reset_time = current_time.replace(hour=0, minute=5,
                                            second=0, microsecond=0)

        if current_time >= action_time and not EXECUTED:
            # print("should run")
            s = socket.socket()
            s.connect(('quotes', 5555))
            s.send((lambda: "img" if 
                        random.randint(1,1024) % 2 == 0 else "none")()
                        .encode("utf-8"))
            quote = s.recv(4096)
            s.close()
            s = socket.socket()
            s.connect(('mail', 4444))
            s.send(quote)
            s.close()
            EXECUTED = True
            print(current_time, "Quote Sent")

        elif current_time >= action_time and EXECUTED:
            # print("already ran")
            pass
        elif current_time <= reset_time:
            # print("reset for the new day")
            EXECUTED = False
        else:
            # print("not ready")
            pass
