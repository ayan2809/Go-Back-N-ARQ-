# Go-Back-N-ARQ
Implementation of Go Back N ARQ protocol in Python

The two codes Sender and Receiver are the implementation of Go Back N ARQ protocol of networking. It will convert the inputted message in the sender into binary and then ask for the window size. It will then send bit by bit to the receiver which will then send the acknowledgement back to the sender. The sender can simulate whether the packet will be lost or received and will retransmit if the acknowledgment is lost. If the acknowledgement is not lost then the next bit is sent to the receiver. This process will continue until the entire message is received. 
