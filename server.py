import socket
import sys
import select
import json
from _thread import *
from config_setup import config
#from client import Client



class ServerCommunication:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.IP_address = config.WebServer_IP_address
        self.Port = config.WebServer_Port
        self.socket.connect((self.IP_address, self.Port))
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
                message_bulk = last_message
                message_bulk += bytes_message.decode("utf-8")
                print(message_bulk)
                message_list = message_bulk.split('$')
                if message_list[len(message_list) - 1] != "-" or message_list[len(message_list) - 1] != "--":
                    last_message = message_list[len(message_list) - 1]
                    message_list = message_list[:-1]
                else:
                    last_message = ""
                print(message_list)
                for message in message_list:
                    if message == "-" or message == "--":
                        continue
                    if message == "":
                        print("[Web Server] Broken connection")
                        #self.remove_potential_player(player)
                        terminate_thread_flag = True
                    #terminate_thread_flag = self.execute_command(message)
                    self.execute_command(message)
            except: 
                print("[Web Server] Exceptie in WebClient")
                #return
                #print("Lobby Thread terminated for address: " + str(player["address"]))

    def execute_command(self, message):
        message = json.loads(message)
        values = json.loads(message["values"])
        if message["command_type"] == "ROOM_CREATED":
            self.game_master_ref.add_room(values["room_code"])

    def send_message_to_server(self, message_json):
        string_message = "-$"
        string_message += json.dumps(message_json)
        string_message += "$-"
        self.socket.sendall(bytes(string_message, 'UTF-8'))