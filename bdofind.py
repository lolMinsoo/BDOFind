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
		# if self.bell.upper() == 'YES':
		if not self.bell.upper() == '?': 
			for bell_server in BELL_SERVERS:
				if BELL_SERVERS[bell_server] == self.bell.upper():
					self.servers[bell_server] == self.bell.upper()
					
			
	
SERVERS = {
	'bal1':	'?',
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
	
BELL_SERVERS = {
	'bal1':	'?',
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
	

	