# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

import os
from shutil import copy

from aion.microservice import main_decorator, Options
from aion.kanban import Kanban
from aion.logger import lprint, initialize_logger


SERVICE_NAME = os.environ.get("SERVICE", "sample-microservice")
initialize_logger(SERVICE_NAME)


@main_decorator(SERVICE_NAME)
def main_without_kanban(opt: Options):
    lprint("start main_without_kanban()")
    # get cache kanban
    conn = opt.get_conn()
    num = opt.get_number()
    kanban: Kanban = conn.set_kanban(SERVICE_NAME, num)

    copy(
        './json/C_MongoBackup.json',
        '/var/lib/aion/Data/direct-next-service_1/C_MongoBackup.json')
