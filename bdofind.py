import requests
import asyncio
import datetime
import time
import random
import math
import urllib
import json
import io
import discord

from jshbot.utilities import future
from jshbot import data, utilities, configurations, logger, plugins, parser
from jshbot.exceptions import BotException, ConfiguredBotException, ErrorTypes
from jshbot.commands import (
    Command, SubCommand, Shortcut, ArgTypes, Attachment, Arg, Opt, MessageTypes, Response)
    
__version__ = '0.1.0'
CBException = ConfiguredBotException('BDO Find Plugin')
uses_configuration = True


def get_commands(bot):
    new_commands = []
    
    new_commands.append(Command(
        'find', subcommands=[
            SubCommand(
                Opt('start'),
                Arg('character_name'),
                Arg('bell'),
                doc='Initalizes the search for a given user.',
                function=to_be_named),
            SubCommand(
                Opt('stop'),
                Arg('character_name'),
                doc='Stops searching for a given user.',
                function=to_be_stopped),
            SubCommand(
                Opt('clear'),
                Arg('character_name'),
                Arg('server'), # optional all
                doc='Resets a server or the entire search',
                function=to_be_cleared),
            SubCommand(
                Opt('call'),
                Arg('character_name'),
                Arg('server'),
                Arg('status'),
                doc='Calls wether or not a user has been found to be there or not',
                function=to_be_called),
            SubCommand(
                Opt('bell'),
                Arg('server'),
                Arg('bell_minutes'),
                doc='Calls out a server for having a bell.',
                function=to_be_belled),
            SubCommand(
                Opt('clearbell'),
                Arg('server'),
                doc='Clears a bell from a server',
                function=to_be_bellcleared)],
        description='Keep track of what servers has been searched in BDO'))
        
        return new_commands

class BDOFind():

    def __init__(self, character_name, bell):
        self.character_name = character_name
        self.bell = bell
        self.servers = SERVERS
        self.bell_servers = BELL_SERVERS
    
    def _get_server_list(self):
        if not self.bell.upper() == '?': 
            # this will only set SERVERS to YES or ?, doesn't make sense to update bells to NO
            for bell_server in BELL_SERVERS:
                if BELL_SERVERS[bell_server][0] == self.bell.upper():
                    self.servers[bell_server] == self.bell.upper()

async def to_be_belled(bot, context):
    server = context.arguments[0]
    bell_minutes = context.arguments[1]
    
    response = Response()
    
    # check inputs
    if server not in SERVERS:
        response.content = '{} is not a valid server.'.format(server)
        return response
    if bell_minutes < 1 or bell_minutes > 60:
        response.content = 'The bell time must be between 1 and 60 minutes.'
        return response
    
    # passes checks, update BELL_SERVERS
    BELL_SERVERS[server] = ['YES', bell_minutes, round(time.time())]
    
        
async def _update_bell():
    for bell_server in BELL_SERVERS:
        if BELL_SERVERS[bell_server][0] == 'YES':
            if round(time.time()) - BELL_SERVERS[bell_server][2] > 
            BELL_SERVERS[bell_server][1] * 60:
                BELL_SERVERS[bell_server] == ['?', 0, 0]
            else:
                # called minutes - current time - called time
                BELL_SERVERS[bell_server] == ['YES', round(BELL_SERVERS[bell_server][1] - 
                (time.time() - BELL_SERVERS[bell_server][2]) / 60), round(time.time)]
                
async def _bell_loop():
    while True:
        if 'YES' in str(BELL_SERVERS):
            _update_bell()
        await asyncio.sleep(60)

        

SERVERS = {
    'bal1': '?',
    'bal2': '?',
    'bal3': '?',
    'bal4': '?',
    'bal5': '?',
    'bal6': '?',
    'val1': '?',
    'val2': '?',
    'val3': '?',
    'val4': '?',
    'val5': '?',
    'val6': '?',
    'cal1': '?',
    'cal2': '?',
    'cal3': '?',
    'cal4': '?',
    'cal5': '?',
    'cal6': '?',
    'ser1': '?',
    'ser2': '?',
    'ser3': '?',
    'ser4': '?',
    'ser5': '?',
    'ser6': '?',
    'med1': '?',
    'med2': '?',
    'med3': '?',
    'med4': '?',
    'med5': '?',
    'med6': '?',
    'kam1': '?',
    'kam2': '?',
    'kam3': '?',
    'kam4': '?',
    'arsha': '?'
}
    
# BELL_STATUS, CALLED_MINUTES_LEFT, CALLED_TIME (EPOCH)
BELL_SERVERS = {
    'bal1': ['?', 30, 0],
    'bal2': ['?', 0, 0],
    'bal3': ['?', 0, 0],
    'bal4': ['?', 0, 0],
    'bal5': ['?', 0, 0],
    'bal6': ['?', 0, 0],
    'val1': ['?', 0, 0],
    'val2': ['?', 0, 0],
    'val3': ['?', 0, 0],
    'val4': ['?', 0, 0],
    'val5': ['?', 0, 0],
    'val6': ['?', 0, 0],
    'cal1': ['?', 0, 0],
    'cal2': ['?', 0, 0],
    'cal3': ['?', 0, 0],
    'cal4': ['?', 0, 0],
    'cal5': ['?', 0, 0],
    'cal6': ['?', 0, 0],
    'ser1': ['?', 0, 0],
    'ser2': ['?', 0, 0],
    'ser3': ['?', 0, 0],
    'ser4': ['?', 0, 0],
    'ser5': ['?', 0, 0],
    'ser6': ['?', 0, 0],
    'med1': ['?', 0, 0],
    'med2': ['?', 0, 0],
    'med3': ['?', 0, 0],
    'med4': ['?', 0, 0],
    'med5': ['?', 0, 0],
    'med6': ['?', 0, 0],
    'kam1': ['?', 0, 0],
    'kam2': ['?', 0, 0],
    'kam3': ['?', 0, 0],
    'kam4': ['?', 0, 0],
    'arsha': ['?', 0, 0]
}

    