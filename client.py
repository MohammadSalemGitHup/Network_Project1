import socket

server_address = ('127.0.0.1', 9955)

# Replace 'YOUR_STUDENT_ID' with a valid student ID
# student_id1_Dana = '1211924'
student_id2_Mohammad = '1200651'
# student_id3_Masa = '1203359'

#test_str = "\r\n"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_socket.connect((server_address))

    client_socket.send(student_id2_Mohammad.encode())

    #receives a response from the server
    response = client_socket.recv(1024).decode()
    print(response)