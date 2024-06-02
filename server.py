import socket
import time
import ctypes

import subprocess
import platform



def lock_screen():#actual locking of the screen is done
    # Function to lock the screen - OS specific implementation
    # Lock screen for Windows
    system_platform = platform.system()

    if system_platform == 'Windows':
         # Lock screen for Windows
        ctypes.windll.user32.LockWorkStation()

    elif system_platform == 'Linux':
        # Lock screen for Linux
        subprocess.run(['xdg-screensaver', 'lock'])

    elif system_platform == 'Darwin':
        # Lock screen for macOS
        subprocess.run(['pmset', 'displaysleepnow'])
    else:
        print("Unsupported operating system.")

####################################################################################################
def handle_client(client_socket, data):

    #student IDs  valid
    print("Received data:", data)

    student_id1_Dana = '1211924'
    student_id2_Mohammad = '1200651'
    student_id3_Masa = '1203359'

    students_ids = [student_id1_Dana, student_id2_Mohammad, student_id3_Masa ]

    for i in students_ids:
        # اذا كانت الرسالة المرسلة من ""الكلاينت"" تحمل رقم طالب الفعلي فسيدخل الى جمل الشرط هذه
        # 1.	display a message on the server side that the OS will lock screen after 10 seconds
        if data in i:

            print("Received student ID:",
                  data)  # The server prints "Received student ID:" to indicate that it has received a valid student ID
            client_socket.send(
                "Server: Locking screen in 10 seconds...".encode())  # It sends a message to the client using client_socket.send
            # 3.	then wait 10 seconds
            time.sleep(10)
            print("Locking screen...")
            lock_screen()
            # print("dana ")
            # 2.	send a message to the client that the sever will lock screen after 10 seconds
            # notify the client that the server has completed the screen-locking process
            client_socket.send("Server: Screen locked.".encode())


        else:
            # Invalid student ID or text received.
            print("Invalid student ID or text received.")


##################################################################################################
# localhost = '127.0.0.1'
portnumber = 9955
# Main server code
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', portnumber))
server_socket.listen(1)
print("Server listening on port 9955...")

###################################################################################################
while True:
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024).decode()
    handle_client(client_socket, data)
    client_socket.close()
