# this is server code using socket programming
from socket import *

serverPort = 9966  # define the port of our server        allow ==> (larger than 1400 integer number)
serverSocket = socket(AF_INET,
                      SOCK_STREAM)  # creat object from socket (serverSocket),(AF_INET => Address family), (SOCK_STREAM =>  means TCP)
serverSocket.bind(('', serverPort))  # bind 2 string with each ather
serverSocket.listen(1)  # Start listen to the incoming connections
print("The server is ready to receive\n\n")


#####################################
while True:
    connectionSocket, addr = serverSocket.accept()  # open a new socket  to connect on it

    # 2048 is 2KByte stored data on buffer
    sentence = connectionSocket.recv(2048).decode()  # read the sentence  => (what the client send -on server-)
    # print (sentence)
    # print(addr)
    IPAddress = addr[0]
    PortNumber = addr[1]
    print('\n\nClient  IP Address : ' + addr[0] + '\nClient Port Number : ' + str(addr[1]) + "\n\n")

    # capitalizedSentence = sentence.upper()   # conver the sentance on Capetall-Latter
    # connectionSocket.send(capitalizedSentence.encode())  # to send the sentance
    ##################################################

    # print(sentence)
    request_list = sentence.split(' ')  # Split requestMessage by spaces
    GET = request_list[0]
    try:
        requestedFile = request_list[1]
        f_name = requestedFile.split('?')[0]  # effectively removes any query parameters or additional information #This is presumably a string variable containing a file name or a URL
        f_name = f_name.lstrip('/') # after the first question mark
        #print(requestedFile)
    except IndexError:
        print(f"requestedFile Error: list index out of range")

    print(sentence)
    #####################################################
    # Now we will handle each request case
    #####################################################
    # part3 branch 1
    if requestedFile == '/' or requestedFile == '/index.html' or requestedFile == '/main_en.html' or \
            requestedFile == '/en' or requestedFile == ' ':
        try:
            #print(requestedFile)
            main_en_path = "main_en.html"
            main_en_file = open(main_en_path, "r")
            html_msg = main_en_file.read()

            response = "HTTP/1.1 200 OK\r\n"  # http response
            response += "Content-Type: text/html\r\n"  # the kind of masseg is html masseg or text/plain or imag/png
            response += "\r\n"
            response += html_msg
            connectionSocket.send(response.encode())
            connectionSocket.close()  # to close the sentance => (close Connection)

        except FileNotFoundError:
            print(f"Error: '{main_en_path}' not found. Please check the file path.")
        except IOError as e:
            print(f"Error reading file: {e}")
        ############################


    ############ part3 branch 2 ###########
    # "main_ar.html" is the Arabic Version html file
    elif requestedFile == '/ar' or requestedFile == '/main_ar.html':
        try:
            print("hi in arrrrr")

            main_ar_path = "main_ar.html"
            main_ar_file = open(main_ar_path, encoding='utf-8') #  encoding='utf-8' means read file with utf-8 encoding
            html_msg = main_ar_file.read()

            # print(html_msg)
            response = "HTTP/1.1 200 OK\r\n"  # http response
            response += "Content-Type: text/html\r\n"  # the kind of masseg is html masseg or text/plain or imag/png
            response += "\r\n"
            response += html_msg # eeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrooooooooooooooooorrrrrrrrrrrrrrrr
            connectionSocket.send(response.encode())
            connectionSocket.close()  # to close the sentance => (close Connection)

        except FileNotFoundError:
            print(f"Error: '{main_ar_path}' not found. Please check the file path.")
        except IOError as e:
            print(f"Error reading file: {e}")
    ############################
    ############ part3 branch 3 ###########
    elif requestedFile.endswith(".html"):
        try:
            print("hiiii in .html case")
            #print(requestedFile)

            htmlf_path = str(f_name)
            with open(htmlf_path, "r") as html_file:
                html_msg = html_file.read()

                response = "HTTP/1.1 200 OK\r\n"  # http response
                response += "Content-Type: text/html\r\n"  # the kind of masseg is html masseg or text/plain or imag/png
                response += html_msg
                response += "\r\n"
                connectionSocket.send(response.encode())
                connectionSocket.close()  # to close the sentance => (close Connection)

        except FileNotFoundError:
            print(f"Error: '{htmlf_path}' not found. Please check the file path.")
        except IOError as e:
            print(f"Error reading file: {e}")
        ################
    ############ part3 branch 4 ###########
    elif requestedFile.endswith(".css"):
        try:
            # print(requestedFile)
            style_path = str(f_name)
            with open(style_path, "r") as style_file:
                style_msg = style_file.read()

                response = "HTTP/1.1 200 OK\r\n"  # http response
                response += "Content-Type: text/css\r\n"  # the kind of masseg is html masseg or text/plain or imag/png
                response += "\r\n"
                response += style_msg
                connectionSocket.send(response.encode())
                connectionSocket.close()  # to close the sentance => (close Connection)

        except FileNotFoundError:
            print(f"Error: '{style_path}' not found. Please check the file path.")
        except IOError as e:
            print(f"Error reading file: {e}")
    ##############################################
    ############ part3 branch 5 ###########
    elif requestedFile.endswith(".png"):
        try:
            png_path = str(f_name)
            with open(png_path, "rb") as png_file:
                png_msg = png_file.read()

            response = "HTTP/1.1 200 OK\r\n"  # http response
            response += "Content-Type: image/png\r\n"  # the kind of masseg is html masseg or text/plain or imag/png
            response += "\r\n"
            connectionSocket.send(response.encode())
            connectionSocket.send(png_msg)
            connectionSocket.close()  # to close the sentance => (close Connection)

        except FileNotFoundError:
            print(f"Error: '{png_path}' not found. Please check the file path.")
        except IOError as e:
            print(f"Error reading file: {e}")
    ######################################
    ############ part3 branch 6 ###########
    elif requestedFile.endswith(".jpg"):
        try:
            jpg_path = str(f_name)
            with open(jpg_path, "rb") as jpg_file:
                jpj_msg = jpg_file.read()

            response = "HTTP/1.1 200 OK\r\n"  # http response
            response += "Content-Type: image/jpg\r\n"  # the kind of masseg is html masseg or text/plain or imag/png
            response += "\r\n"
            connectionSocket.send(response.encode())
            connectionSocket.send(jpj_msg)
            connectionSocket.close()  # to close the sentance => (close Connection)

        except FileNotFoundError:
            print(f"Error: '{jpg_path}' not found. Please check the file path.")
        except IOError as e:
            print(f"Error reading file: {e}")


    ################# part 3 branch 7 ##############
    elif requestedFile == "/cr":
        connectionSocket.send(f"HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(f"Location: https://www.cornell.edu/ \r\n".encode())
    elif requestedFile == "/so":
        connectionSocket.send(f"HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(f"Location: https://stackoverflow.com/ \r\n".encode())
    elif requestedFile == "/rt":
        connectionSocket.send(f"HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send(f"Location: https://ritaj.birzeit.edu/register/ \r\n".encode())
    ############### part 3 branch 8 ##############
    else:
        connectionSocket.send(f"HTTP/1.1 404 Not Found\r\n".encode())
        responseMessage = (
                '<html><title>Error 404</title><body><center><h1 style = "color : red ;">The file is not '
                'found => Error 404 <= </h1><hr><p style= '
                '"font-weight: '
                'bold;">Afaf Amwas: 1203359 </p><p style="font-weight: bold;"> Mohammed Salem: 1200651 '
                '</p><p style="font-weight: bold;"> Dana Asfour: 1211924 '
                '</p><hr><h2>IP: ' + str(IPAddress) + ', Port: ' + str(PortNumber) +
                '</h2></center></body></html>').encode('utf-8')
        connectionSocket.send(f"\r\n".encode())
        connectionSocket.send(responseMessage)
        connectionSocket.close()
