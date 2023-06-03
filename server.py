import socket
import sys
import select
import json
from _thread import *
from fix_fields import Fix
#from client import Client



class ServerCommunication:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.IP_address = 
        self.Port = 
        self.socket.connect((self.IP_address, self.Port))
        self.msg_generator = Fix()
        start_new_thread(self.listen_thread, ())

    def set_game_master_ref(self, game_master_ref):
        self.game_master_ref = game_master_ref

    def listen_thread(self):
        terminate_thread_flag = False
        last_message = ""
        while True:
            try:
                if terminate_thread_flag == True:
                    print("Lobby Thread terminated")
                    return
                bytes_message = self.socket.recv(1024)
                message_bulk = bytes_message.decode("utf-8")
                self.execute_command()
            except: 
                print("[Web Server] Exceptie in WebClient")
                #return
                #print("Lobby Thread terminated for address: " + str(player["address"]))

    def execute_command(self):
        self.msg_generator.make_login()
        self.socket.sendall(bytes(self.msg_generator.make_login(), 'UTF-8'))
        file1 = open('myfile.txt', 'r')
        Lines = file1.readlines()
         
        count = 0
        # Strips the newline character
        for line in Lines:
            #count += 1
            #print("Line{}: {}".format(count, line.strip()))
            self.socket.sendall(bytes(self.msg_generator.make_msg(line), 'UTF-8'))
