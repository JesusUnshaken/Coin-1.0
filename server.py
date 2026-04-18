#---------------------------------------------
#=-------------=> 🪙 COIN 1.0 <=-------------=
#---------------------------------------------
# As You can see dear Wizard 🧙‍♂️🪄
# This is a simple chat server that allows you to communicate with a client
# The Difference beteen this and the previous releas is :
# Now you can send and receive messages at the same time )Full-Duplex in the engineer's language((The previous release was like a turn based indie rpg game)
# Now you have a minu to chose from (Start chatting or exit program )Or if you are acting funny you can type anything and the program will react the proper way( )

# In the next release I will try to add a clouring method so you won't suffer trying to see where your messages 
# And I'll try to add encryption to make it more secure and private (I know it's not the best but it's a start)







import socket
import threading







def receive_messages(server):
    while True:
        try:
            data = server.recv(1024).decode('utf-8')
            if not data or data.lower() == 'exit':
                print("\n[!]🔌⛔ Client disconnected.")
                break
            print(f"\n[Client]: {data}")
            print("(server): ", end="")
        except:
            break



      


def start_chatting(server):
    print("\n--- Chat Started (Type 'exit' to stop) ---")
    
    recv_thread = threading.Thread(target=receive_messages, args=(server,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:
        reply = input("✅(server): ")
        server.send(reply.encode('utf-8'))
        if reply.lower() == 'exit':
            break


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(1)
print("Waiting for connection.....")
conn, addr = server_socket.accept()
print(f"Connected to {addr}✅✅")


while True:
    print("\n1. Start Chatting")
    print("0. Exit Program")
    choice = input("Enter your choice: ")

    if choice == '1':
        start_chatting(conn)
    elif choice == '0':
        print("Closing server...")
        break
    else:
        print("Try-hard🤡")

conn.close()







