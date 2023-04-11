# -*- coding: utf-8 -*- 
""" ++++++++++++++++++++++++++++++++++++++
@product->name PyCharm
@project->name growth_analysis
@editor->name Sanliy
@file->name auth_check.py
@create->time 2023/4/11-14:50
@desc->
++++++++++++++++++++++++++++++++++++++ """
import base64
import datetime
import os
import uuid
import json
from PyQt5.QtWidgets import QWidget, QMessageBox
from datetime import datetime


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('授权检查')
        self.resize(400, 300)
        self.show()


class AuthCheckUI:

    def __init__(self):
        self.license_file_with_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "lic", "license.lic")
        self.user = None
        self.start_date = None
        self.end_date = None

    def check_auth_file(self):
        if not os.path.exists(self.license_file_with_path):
            msg_box = QMessageBox()
            msg_box.setText(
                '您的授权文件不存在，请联系管理员获取授权文件。'
                '如果未获得授权许可，点击确定后，您还可以免费使用该软件5分钟，五分钟之后软件将会自动关闭！')
            msg_box.setWindowTitle('授权文件错误')
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()
            return False
        else:
            # 检查授权文件是否是符合规范的，是否到期，等等
            with open(self.license_file_with_path, "r") as f:
                encrypt_license = f.read()
            decrypt_license = base64.b64decode(encrypt_license).decode("utf8")
            result = self.check_valid(decrypt_license)
            if result:
                return True
            else:
                msg_box = QMessageBox()
                msg_box.setText(
                    '您的授权文件无效，请联系管理员获取授权文件。'
                    '如果未获得授权许可，点击确定后，您还可以免费使用该软件5分钟，五分钟之后软件将会自动关闭！')
                msg_box.setWindowTitle('授权文件无效')
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
                return False

    def get_mac_address(self):
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

    def check_valid(self, decrypt_license):
        decrypt_license_eval = json.loads(decrypt_license)
        self.user = decrypt_license_eval["user"]
        self.start_date = datetime.strptime(decrypt_license_eval["start_date"], "%Y-%m-%d")
        self.end_date = datetime.strptime(decrypt_license_eval["end_date"], "%Y-%m-%d")
        real_mac_address = self.get_mac_address()
        now = datetime.now()

        if self.user == real_mac_address or now <= self.start_date or now >= self.end_date:
            return False
        else:
            return True

