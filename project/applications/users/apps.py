#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'project.applications.users'

    def ready(self):
        from project.applications.users import signals
