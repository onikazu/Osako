from socket import *
import threading
import sys
import os
import csv

import analyze
import generate_command as gc
import base_client


class OsakoGoalKeeper(base_client.BaseClient, threading.Thread):
    def __init__(self):
        super(Osako, self).__init__()
        self.neck_flag = 1
        
    def play(self, result):
        super().play(result)
