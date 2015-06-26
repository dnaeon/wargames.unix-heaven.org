#!/usr/bin/env python

# code taken from the examples from the Python documentation on SocketServer
# daemon1 returns base64'd message, which is xxd'ed

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
0000000: 5157 6773 4947 4675 6233 526f 5a58 4967  QWgsIGFub3RoZXIg
0000010: 6333 5279 5957 356e 5a58 4967 6347 467a  c3RyYW5nZXIgcGFz
0000020: 6332 6c75 5a79 4269 6553 454b 436c 6c76  c2luZyBieSEKCllv
0000030: 6453 4268 636d 5567 6247 3976 6132 6c75  dSBhcmUgbG9va2lu
0000040: 5a79 426d 6233 4967 6447 686c 0a49 484e  ZyBmb3IgdGhl.IHN
0000050: 6c59 334a 6c64 4342 725a 586b 7349 4746  lY3JldCBrZXksIGF
0000060: 795a 5734 6e64 4342 3562 3355 6763 3352  yZW4ndCB5b3Ugc3R
0000070: 7959 5735 6e5a 5849 2f43 6770 4a4a 3230  yYW5nZXI/CgpJJ20
0000080: 6763 3239 7963 6e6b 7349 474a 3164 4342  gc29ycnksIGJ1dCB
0000090: 4a49 474e 6862 6d35 760a 6443 426f 5a57  JIGNhbm5v.dCBoZW
00000a0: 7877 4948 6c76 6453 3475 4c67 6f4b 5432  xwIHlvdS4uLgoKT2
00000b0: 3573 6553 4276 626d 5567 6232 5967 5957  5seSBvbmUgb2YgYW
00000c0: 7873 4948 567a 4948 526f 636d 566c 4947  xsIHVzIHRocmVlIG
00000d0: 6876 6247 527a 4948 526f 5a53 4272 5a58  hvbGRzIHRoZSBrZX
00000e0: 6b75 4c69 344b 0a43 6c6c 7664 5342 755a  kuLi4K.CllvdSBuZ
00000f0: 5756 6b49 4852 7649 475a 7062 6d51 6762  WVkIHRvIGZpbmQgb
0000100: 586b 6759 6e4a 7664 4768 6c63 6977 6761  XkgYnJvdGhlciwga
0000110: 4755 6764 326c 7362 4342 6f5a 5778 7749  GUgd2lsbCBoZWxwI
0000120: 486c 7664 5345 4b43 6b35 7664 7942 4a49  HlvdSEKCk5vdyBJI
0000130: 4735 6c0a 5a57 5167 6447 3867 636d 567a  G5l.ZWQgdG8gcmVz
0000140: 6443 7767 5a32 3976 5a47 4a35 5a53 427a  dCwgZ29vZGJ5ZSBz
0000150: 6448 4a68 626d 646c 6369 454b 4367 3d3d  dHJhbmdlciEKCg==
0000160: 0a                                       .
"""

        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 31123

    # Create the server, binding to localhost on port 31123
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
