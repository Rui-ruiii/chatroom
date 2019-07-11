"""
功能
1.发送信息
2.接收信息
3.退出系统

框架设计
1.发送信息send_msg()
2.接收信息recv_msg()
3.程序的主入口main()
4.当程序独立运行的时候，才启动聊天器

步骤
1.发送信息send_msg()
--定义变量接收用户与输入的接收方的地址，端口号，内容
--使用socket的sentto()发送信息
2.接收信息recv_msg()
--使用socket接收数据，解码数据，输出显示
3.程序的主入口main()
--创建socket套接字，绑定端口，打印菜单（循环），接收用户输入的选项，判断用户的选择，并且调用对应的函数，关闭套接字
4.当程序独立运行的时候，才启动聊天器

"""
import socket
def send_msg(udp_socket):

    recv_ipaddress = input("请输入对方IP地址:\n")
    recv_portaddress = input("请输入对方端口号：\n")
    send_content = input("请输入聊天内容：\n")
    udp_socket.sendto(send_content.encode(),(recv_ipaddress,int(recv_portaddress)))


def recv_msg(udp_socket):

    recv_data,recv_ipport = udp_socket.recvfrom(1024)
    recv_text = recv_data.decode()
    print("接收到来自%s的消息为：%s" %(str(recv_ipport),recv_data))



def main():

    while True:
        udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        udp_socket.bind(("",8080))
        print("*" * 40)
        print("*****          1.发送信息          *****")
        print("*****          2.接收信息          *****")
        print("*****          3.退出系统          *****")
        print("*" * 40)
        sel_num = int(input("请输入选项"))
        if sel_num == 1:
            send_msg(udp_socket)
        elif sel_num == 2:
            recv_msg(udp_socket)
        elif sel_num == 3:
            print("系统退出")
            break
    udp_socket.close()

if __name__ == '__main__':

    main()

