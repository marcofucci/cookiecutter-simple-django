#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil

with open('./requirements/local.txt', 'r') as f:
    if 'Sphinx' not in f.read():
        shutil.rmtree('./docs')
