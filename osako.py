"""
コマンド決定機能を備えたクライアント
"""

from socket import *
import threading
import sys
import os
import csv

from analyze import *
import base_client


class Osako(base_client.BaseClient, threading.Thread):
    def __init__(self):
        super(Osako, self).__init__()


    def play(self, init_result, visual_result, aural_result, physical_result, player_type_result):
        super().play(init_result, visual_result, aural_result, physical_result, player_type_result)