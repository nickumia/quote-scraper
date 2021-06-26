##  Quote-scraper and sender
#   Developer: nickumia


import json
import socket

import gather


if __name__=="__main__":
    print("Quote Scraper UP")
    quote_server = socket.socket()
    quote_server.bind(('', 5555))
    quote_server.listen(20)

    while True:
        connection,addr = quote_server.accept()
        msg = connection.recv(1024)
        quote = gather.get_quote(img=msg)
        connection.send(json.dumps(quote).encode('utf-8'))
        connection.close()
