"""
コマンド決定機能を備えたクライアント
"""

from socket import *
import threading
import sys
import os
import csv

import analyze
import generate_command as gc
import base_client


class Osako(base_client.BaseClient, threading.Thread):
    def __init__(self):
        super(Osako, self).__init__()
        self.neck_flag = 1

    def play(self, result):
        super().play(result)
        if self.neck_flag:
            self.m_strCommand = gc.turn_neck(90)
            self.neck_flag = 0
        else:
            self.m_strCommand = gc.turn_neck(-90)
            self.neck_flag = 1
