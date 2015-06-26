#!/usr/bin/env python

# code taken from the examples from the Python documentation on SocketServer
# brother3 returns base64'd message, which is xxd'ed

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
    	data = """
0000000: 5347 5673 6247 3873 4948 4e30 636d 4675  SGVsbG8sIHN0cmFu
0000010: 5a32 5679 4951 6f4b 5757 3931 4947 5276  Z2VyIQoKWW91IGRv
0000020: 4947 3576 6443 427a 5a57 5674 4948 4a6c  IG5vdCBzZWVtIHJl
0000030: 5957 5235 4948 5276 4947 7475 6233 6367  YWR5IHRvIGtub3cg
0000040: 6233 5679 4948 4e6c 5933 4a6c 0a64 4334  b3VyIHNlY3Jl.dC4
0000050: 4b43 6b4e 7662 5755 6759 6d46 6a61 7942  KCkNvbWUgYmFjayB
0000060: 3361 4756 7549 486c 7664 5342 6863 6d55  3aGVuIHlvdSBhcmU
0000070: 6763 6d56 685a 486b 7543 6770 4862 3239  gcmVhZHkuCgpHb29
0000080: 6b59 6e6c 6c4c 4342 7a64 484a 6862 6d64  kYnllLCBzdHJhbmd
0000090: 6c63 6945 4b43 673d 3d0a                 lciEKCg==.
"""
        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 32136

    # Create the server, binding to localhost on port 32136
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
