# UDP
# User Datagram Protocol
# Un-Reliable Connection-less based protocol
# Low Overhead
# Used for VOIP, Online Games, Streaming.

# UDP Capitalize
# Lets create the same program as before this time using a UDP connection.
# udpServer.py and udpClient.py
# You will notice we use recvfrom() and sendto()This is because UDP is Connectionless, we need to tell the data where to go when we send it.

# Non Blocking
# It is possible and often needed, to set a socket to non blocking. This means that the program will not sit and wait for data to be received.
# Often used in Real-time programs.
# When a task cannot be spread over threads.
# Always throws an error if there is nothing in the buffer!!!

import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    # 这里如果是 TCP 连接，应该监听(listen())端口是否有客户机申请加入
    # 并且在获得申请并‘接受’的时候获得客户机的 端口 和 ip： c, addr = s.accept()

    print("Server Started")

    while True:
        # 如果是TCP链接，那是一对一的稳定链接,或者是封闭的
        # 一旦一条线路建立，那么这条先就只有他们俩，不需要指明谁接受or发给谁
        # 而 UDP 链接是开放式的，所以每一条信息都有可能来自不同的人，所以要
        # 捕获每一条信息的地址
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message From: " + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        # 同理，发送信息也需要指定是发给谁
        s.sendto(data.encode('utf-8'), addr)
    c.close()

if __name__ == "__main__":
    Main()
