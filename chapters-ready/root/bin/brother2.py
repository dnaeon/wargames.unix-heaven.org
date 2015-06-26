#!/usr/bin/env python

# code taken from the examples from the Python documentation on SocketServer
# brother2 returns gzip'ed message, which is base64'd and xxd'ed
# brother2 holds the key to the next chapter

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
0000000: 4834 7349 414b 6b32 3956 4541 4131 5751  H4sIAKk29VEAA1WQ
0000010: 7357 3744 4d41 7845 6433 3046 6d36 564c  sW7DMAxEd30Fm6VL
0000020: 3449 2f6f 4544 5244 7479 3464 4666 7353  4I/oEDRDty4dFfsS
0000030: 4358 5a4a 6736 4a69 364f 394c 4b56 4d58  CXZJg6Ji6O9LKVMX
0000040: 5163 4478 3368 3335 6957 3254 0a4d 7858  QcDx3h35iW2T.MxX
0000050: 5479 412f 6f57 7768 586f 7851 4c33 5143  TyA/oWwhXoxQL3QC
0000060: 6d53 4566 4b47 317a 5050 494f 7572 6a7a  mSEfKG1zPPIOurjz
0000070: 4237 305a 6c6c 3956 3145 3472 6368 4446  B70Zll9V1E4rchDF
0000080: 4e55 776a 2b55 4758 4c47 7a57 706a 7052  NUwj+UGXLGzWpjpR
0000090: 3978 304b 334e 6c45 490a 4839 5863 5873  9x0K3NlEI.H9XcXs
00000a0: 4146 5a43 6e61 4749 6b4b 5976 4538 2b4f  AFZCnaGIkKYvE8+O
00000b0: 6375 366e 6c7a 3179 4976 5138 7539 5161  cu6nlz1yIvQ8u9Qa
00000c0: 7171 7a65 6b2f 6275 6a78 684b 6a73 5845  qqzek/bujxhKjsXE
00000d0: 7367 7a59 396b 7663 584b 6370 4255 3959  sgzY9kvcXKcpBU9Y
00000e0: 525a 5954 372b 0a37 664b 4b39 716f 4372  RZYT7+.7fKK9qoCr
00000f0: 4750 2b56 3470 524c 6e54 3679 705a 3834  GP+V4pRLnT6ypZ84
0000100: 7958 7261 526f 7248 3735 7939 792f 5632  yXraRorH75y9y/V2
0000110: 6741 432b 3742 3078 6773 3647 7335 6771  gAC+7B0xgs6Gs5gq
0000120: 3570 527a 7451 6a38 3842 3568 6859 2f33  5pRztQj88B5hhY/3
0000130: 6356 4c0a 4833 3751 662f 6638 4132 7952  cVL.H37Qf/f8A2yR
0000140: 384a 5a69 4151 4141 0a                   8JZiAQAA.
"""
        self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 31579

    # Create the server, binding to localhost on port 31579
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
