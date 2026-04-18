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







def receive_messages(client):
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if not data or data.lower() == 'exit':
                print("\n[!]🔌⛔ Server disconnected.")
                break
            print(f"\n[Server]: {data}")
            print("client: ", end="")
        except:
            break





def start_chatting(client):
    print("\n--- Chat Started (Type 'exit' to stop) ---")
    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:
        message = input("✅client: ")
        client.send(message.encode('utf-8'))
        if message.lower() == 'exit' :
            break






client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
print("Connected to Server!✅✅")





while True:
    print("\n1. Start Chatting")
    print("0. Exit Program")
    choice = input("Enter your choice: ")

    if choice == '1':
        start_chatting(client_socket)
    elif choice == '0':
        break
    else:
        print("Invalid choice!")






client_socket.close()










