"""
基本的な機能(メッセージの受信と解析，コマンドの送信機能)を備えたサッカーエージェント
戦略等は未実装
"""

from socket import *
import threading
import sys
import os
import csv

import analyze
import robo_tools


class BaseClient(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # サーバ接続のための変数
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.HOSTNAME = "localhost"
        self.PORT = 6000
        self.ADDRESS = gethostbyname(self.HOSTNAME)

        # クライアントの基本情報を代入する変数
        self.m_iNumber = 0
        self.m_strTeamName = ""
        self.m_strHostName = ""
        self.m_kick_off_x = 0
        self.m_kick_off_y = 0

        # メッセージの解析結果を代入する変数
        self.analyze_result = {
            "side": "",
            "number": 0,
            "play_mode": "",
            "neck": 0,
            "x": 0,
            "y": 0,
            "ball_x": 0,
            "ball_y": 0,
            "time": 0,
            "stamina": 0,
            "speaker": "",
            "content": "",
            "server_param": "",
            "player_param": "",
            "id": 0,
            "player_type": ""
        }
        print("__init__:self.analyze_result", self.analyze_result)

        # コマンドを代入する変数
        self.m_strCommand = ""

    # コマンドの送信
    def send(self, command):
        if len(command) == 0:
            return
        command = command + "\0"
        try:
            to_byte_command = command.encode(encoding='utf_8')
            self.socket.sendto(to_byte_command, (self.ADDRESS, self.PORT))
        except OSError:
            print("送信失敗")
            sys.exit()

    # メッセージの受信を行う関数
    def receive(self):
        try:
            message, arr = self.socket.recvfrom(4096)
            message = message.decode("UTF-8")
            self.PORT = arr[1]
            # if self.m_iNumber == 1:
            #     print(message)
            return message
        except OSError:
            print("受信失敗")
            sys.exit()

    # クライアントの登録を行う関数
    def initialize(self, number, team_name, server_name, server_port):
        self.m_iNumber = number
        self.m_strTeamName = team_name
        self.m_strHostName = server_name
        self.PORT = server_port
        if self.m_iNumber == 1:
            command = "(init " + self.m_strTeamName + "(goalie)(version 15.40))"
        else:
            command = "(init " + self.m_strTeamName + "(version 15.40))"
        self.send(command)

    # thread を動かしている最中に行われる関数
    def run(self):
        while True:
            message = self.receive()
            # print(message)
            self.analyze_message(message)

    # messageの解析を行う関数
    def analyze_message(self, message):
        if message.startswith("(init "):
            self.analyze_result = analyze.analyze_initial_message(message, self.analyze_result)
            print("init:self.analyze_result", self.analyze_result)
        # 視覚メッセージの処理
        elif message.startswith("(see "):
            self.analyze_result = analyze.analyze_visual_message(message, self.analyze_result, self.m_kick_off_x,
                                                                 self.m_kick_off_y)
            print("see:self.analyze_result", self.analyze_result)
        # 体調メッセージの処理
        elif message.startswith("(sense_body "):
            self.analyze_result = analyze.analyze_physical_message(message, self.analyze_result)
            self.play(self.analyze_result)
            print("sense body: self.analyze_result", self.analyze_result)
        # 聴覚メッセージの処理
        elif message.startswith("(hear "):
            self.analyze_result = analyze.analyze_aural_message(message, self.analyze_result)
            # プレイモードが観測できたら更新
            self.play_mode = self.analyze_result["play_mode"]
            print("hear: self.analyze_result", self.analyze_result)
        # サーバパラメータの処理
        elif message.startswith("(server_param"):
            self.analyze_result = analyze.analyze_server_param(message, self.analyze_result)
        # プレーヤーパラメータの処理
        elif message.startswith("(player_param"):
            self.analyze_result = analyze.analyze_player_param(message, self.analyze_result)
        # プレーヤータイプの処理
        elif message.startswith("(player_type"):
            self.analyze_result = analyze.analyze_player_type(message, self.analyze_result)
        # エラーの処理
        else:
            pass
            # print("サーバーからエラーが伝えられた:", message)
            # print("エラー発生原因のコマンドは右記の通り :", self.m_strCommand)

    def play(self, result):
        if robo_tools.checkInitialMode(result["play_mode"]):
            self.set_kick_off_position()
            command = "(move " + str(self.m_kick_off_x) + " " \
                      + str(self.m_kick_off_y) + ")"
            print(command)
            self.send(command)

        # デバッグ
        if self.m_iNumber == 1:
            print(result)
            print("===================")

    def set_kick_off_position(self):
        with open("./formation/init.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if self.m_iNumber == int(row[0]):
                    self.m_kick_off_x = int(row[1])
                    self.m_kick_off_y = int(row[2])


if __name__ == "__main__":
    players = []
    for i in range(22):
        p = BaseClient()
        players.append(p)
        if i < 11:
            team_name = "Left"
        else:
            team_name = "Right"
        players[i].initialize(i % 11 + 1, team_name, "localhost", 6000)
        players[i].start()
    print("試合登録完了")
