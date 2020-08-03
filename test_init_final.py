# -*- coding: utf-8 -*- 

################ Server Ver. 18 (2020. 7. 4.) #####################

import os
import sys
import asyncio
import discord
import datetime
import random
import math
import logging
from discord.ext import tasks, commands
from discord.ext.commands import CommandNotFound, MissingRequiredArgument
from gtts import gTTS
from github import Github
import base64
import re #정산
import gspread #정산
from oauth2client.service_account import ServiceAccountCredentials #정산
from io import StringIO
import urllib.request
from math import ceil, floor
import aiohttp
from pymongo import MongoClient
import pymongo, ssl, traceback, random

##################### 로깅 ###########################
log_stream = StringIO()    
logging.basicConfig(stream=log_stream, level=logging.WARNING)

#ilsanglog = logging.getLogger('discord')
#ilsanglog.setLevel(level = logging.WARNING)
#handler = logging.StreamHandler()
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#ilsanglog.addHandler(handler)
#####################################################

basicSetting = []
bossData = []
fixed_bossData = []

bossNum = 0
fixed_bossNum = 0
chkvoicechannel = 0
chkrelogin = 0
chflg = 0
LoadChk = 0

bossTime = []
tmp_bossTime = []

fixed_bossTime = []

bossTimeString = []
bossDateString = []
tmp_bossTimeString = []
tmp_bossDateString = []

bossFlag = []
bossFlag0 = []
fixed_bossFlag = []
fixed_bossFlag0 = []
bossMungFlag = []
bossMungCnt = []

channel_info = []
channel_name = []
channel_id = []
channel_voice_name = []
channel_voice_id = []
channel_type = []

FixedBossDateData = []
indexFixedBossname = []

client = discord.Client()
client = commands.Bot(command_prefix="", help_command = None, description='일상디코봇')

access_token = os.environ["BOT_TOKEN"]			
git_access_token = os.environ["GIT_TOKEN"]			
git_access_repo = os.environ["GIT_REPO"]			
git_access_repo_restart = os.environ["GIT_REPO_RESTART"]		
mongoDB_HOST = os.environ["MONGODB_HOST"]
user_ID = os.environ["USER_ID"]
user_PASSWORD = os.environ["USER_PW"]
time_Zone = os.environ["TIME_ZONE"]	

g = Github(git_access_token)
repo = g.get_repo(git_access_repo)
repo_restart = g.get_repo(git_access_repo_restart)

def init():
	global basicSetting
	global bossData
	global fixed_bossData

	global bossNum
	global fixed_bossNum
	global chkvoicechannel
	global chkrelogin

	global bossTime
	global tmp_bossTime

	global fixed_bossTime

	global bossTimeString
	global bossDateString
	global tmp_bossTimeString
	global tmp_bossDateString

	global bossFlag
	global bossFlag0
	global fixed_bossFlag
	global fixed_bossFlag0
	global bossMungFlag
	global bossMungCnt
	
	global voice_client1
	
	global channel_info
	global channel_name
	global channel_voice_name
	global channel_voice_id
	global channel_id
	global channel_type
	global LoadChk
	
	global indexFixedBossname
	global FixedBossDateData

	global endTime
	
	global gc #정산
	global credentials #정산
	
	global regenembed
	global command
	global kill_Data
	global kill_Time
	global item_Data

	global tmp_racing_unit

	global commandSetting_jungsan
	global basicSetting_jungsan

	command = []
	tmp_bossData = []
	tmp_fixed_bossData = []
	FixedBossDateData = []
	indexFixedBossname = []
	kill_Data = {}
	tmp_kill_Data = []
	item_Data = {}
	tmp_item_Data = []
	f = []
	fb = []
	fk = []
	fc = []
	fi = []
	tmp_racing_unit = []
	basicSetting_jungsan = []
	commandSetting_jungsan = []
	
	inidata = repo.get_contents("test_setting.ini")
	file_data1 = base64.b64decode(inidata.content)
	file_data1 = file_data1.decode('utf-8')
	inputData = file_data1.split('\n')

	command_inidata = repo.get_contents("command.ini")
	file_data4 = base64.b64decode(command_inidata.content)
	file_data4 = file_data4.decode('utf-8')
	command_inputData = file_data4.split('\n')

	command_inidata_jungsan = repo.get_contents("command_jungsan.ini")
	file_data7 = base64.b64decode(command_inidata_jungsan.content)
	file_data7 = file_data7.decode('utf-8')
	commandData_jungsan = file_data7.split('\n')
	
	boss_inidata = repo.get_contents("boss.ini")
	file_data3 = base64.b64decode(boss_inidata.content)
	file_data3 = file_data3.decode('utf-8')
	boss_inputData = file_data3.split('\n')

	fixed_inidata = repo.get_contents("fixed_boss.ini")
	file_data2 = base64.b64decode(fixed_inidata.content)
	file_data2 = file_data2.decode('utf-8')
	fixed_inputData = file_data2.split('\n')

	kill_inidata = repo.get_contents("kill_list.ini")
	file_data5 = base64.b64decode(kill_inidata.content)
	file_data5 = file_data5.decode('utf-8')
	kill_inputData = file_data5.split('\n')

	item_inidata = repo.get_contents("item_list.ini")
	file_data6 = base64.b64decode(item_inidata.content)
	file_data6 = file_data6.decode('utf-8')
	item_inputData = file_data6.split('\n')

	for i in range(len(fixed_inputData)):
		FixedBossDateData.append(fixed_inputData[i])

	index_fixed = 0

	for value in FixedBossDateData:
		if value.find('bossname') != -1:
			indexFixedBossname.append(index_fixed)
		index_fixed = index_fixed + 1

	for i in range(inputData.count('\r')):
		inputData.remove('\r')

	for i in range(command_inputData.count('\r')):
		command_inputData.remove('\r')

	for i in range(commandData_jungsan.count('\r')):
		commandData_jungsan.remove('\r')
		
	for i in range(boss_inputData.count('\r')):
		boss_inputData.remove('\r')

	for i in range(fixed_inputData.count('\r')):
		fixed_inputData.remove('\r')
	
	for i in range(kill_inputData.count('\r')):
		kill_inputData.remove('\r')

	for i in range(item_inputData.count('\r')):
		item_inputData.remove('\r')

	del(command_inputData[0])
	del(commandData_jungsan[0])
	del(boss_inputData[0])
	del(fixed_inputData[0])
	del(kill_inputData[0])
	del(item_inputData[0])
	
	############## 보탐봇 초기 설정 리스트 #####################
	basicSetting.append(inputData[0][11:])     #basicSetting[0] : timezone
	basicSetting.append(inputData[8][15:])     #basicSetting[1] : before_alert
	basicSetting.append(inputData[10][10:])     #basicSetting[2] : mungChk
	basicSetting.append(inputData[9][16:])     #basicSetting[3] : before_alert1
	basicSetting.append(inputData[13][14:16])  #basicSetting[4] : restarttime 시
	basicSetting.append(inputData[13][17:])    #basicSetting[5] : restarttime 분
	basicSetting.append(inputData[1][15:])     #basicSetting[6] : voice채널 ID
	basicSetting.append(inputData[2][14:])     #basicSetting[7] : text채널 ID
	basicSetting.append(inputData[3][16:])     #basicSetting[8] : 사다리 채널 ID
	basicSetting.append(inputData[12][14:])    #basicSetting[9] : !ㅂ 출력 수
	basicSetting.append(inputData[16][11:])    #basicSetting[10] : json 파일명
	basicSetting.append(inputData[4][17:])     #basicSetting[11] : 정산 채널 ID
	basicSetting.append(inputData[15][12:])    #basicSetting[12] : sheet 이름
	basicSetting.append(inputData[14][16:])    #basicSetting[13] : restart 주기
	basicSetting.append(inputData[17][12:])    #basicSetting[14] : 시트 이름
	basicSetting.append(inputData[18][12:])    #basicSetting[15] : 입력 셀
	basicSetting.append(inputData[19][13:])    #basicSetting[16] : 출력 셀
	basicSetting.append(inputData[11][13:])     #basicSetting[17] : 멍삭제횟수
	basicSetting.append(inputData[5][14:])     #basicSetting[18] : kill채널 ID
	basicSetting.append(inputData[6][16:])     #basicSetting[19] : racing 채널 ID
	basicSetting.append(inputData[7][14:])     #basicSetting[20] : item 채널 ID

	############## 보탐봇 명령어 리스트 #####################
	for i in range(len(command_inputData)):
		tmp_command = command_inputData[i][12:].rstrip('\r')
		fc = tmp_command.split(', ')
		command.append(fc)
		fc = []
		#command.append(command_inputData[i][12:].rstrip('\r'))     #command[0] ~ [24] : 명령어

	############## 분배봇 초기 설정 리스트 #####################
	basicSetting_jungsan.append(access_token)
	basicSetting_jungsan.append(mongoDB_HOST)
	basicSetting_jungsan.append(user_ID)
	basicSetting_jungsan.append(user_PASSWORD)

	# basicSetting_jungsan[0] = bot_token
	# basicSetting_jungsan[1] = host
	# basicSetting_jungsan[2] = user_ID
	# basicSetting_jungsan[3] = user_PASSWORD
	# basicSetting_jungsan[4] = backup_period
	# basicSetting_jungsan[5] = checktime
	# basicSetting_jungsan[6] = distributionchannel
	# basicSetting_jungsan[7] = tax
	# basicSetting_jungsan[8] = timezone

	############## 보탐봇 명령어 리스트 #####################
	for i in range(len(commandData_jungsan)):
		tmp_command = commandData_jungsan[i][(commandData_jungsan[0].find("="))+2:].rstrip('\r')
		fc = tmp_command.split(', ')
		commandSetting_jungsan.append(fc)
		fc = []

	################## 척살 명단 ###########################
	for i in range(len(kill_inputData)):
		tmp_kill_Data.append(kill_inputData[i].rstrip('\r'))
		fk.append(tmp_kill_Data[i][:tmp_kill_Data[i].find(' ')])
		fk.append(tmp_kill_Data[i][tmp_kill_Data[i].find(' ')+1:])
		try:
			kill_Data[fk[0]] = int(fk[1])
		except:
			pass
		fk = []

	for i in range(len(item_inputData)):
		tmp_item_Data.append(item_inputData[i].rstrip('\r'))
		fi.append(tmp_item_Data[i][:tmp_item_Data[i].find(' ')])
		fi.append(tmp_item_Data[i][tmp_item_Data[i].find(' ')+1:])
		try:
			item_Data[fi[0]] = int(fi[1])
		except:
			pass
		fi = []


	tmp_killtime = datetime.datetime.now().replace(hour=int(5), minute=int(0), second = int(0))
	kill_Time = datetime.datetime.now()

	if tmp_killtime < kill_Time :
		kill_Time = tmp_killtime + datetime.timedelta(days=int(1))
	else:
		kill_Time = tmp_killtime
	
	for i in range(len(basicSetting)):
		basicSetting[i] = basicSetting[i].strip()
	
	if basicSetting[6] != "":
		basicSetting[6] = int(basicSetting[6])
		
	if basicSetting[7] != "":
		basicSetting[7] = int(basicSetting[7])
	
	if basicSetting[8] != "":
		basicSetting[8] = int(basicSetting[8])
		
	if basicSetting[11] != "":
		basicSetting[11] = int(basicSetting[11])

	if basicSetting[18] != "":
		basicSetting[18] = int(basicSetting[18])

	if basicSetting[19] != "":
		basicSetting[19] = int(basicSetting[19])

	if basicSetting[20] != "":
		basicSetting[20] = int(basicSetting[20])

	tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
	
	if int(basicSetting[13]) == 0 :
		endTime = tmp_now.replace(hour=int(basicSetting[4]), minute=int(basicSetting[5]), second = int(0))
		endTime = endTime + datetime.timedelta(days=int(1000))
	else :
		endTime = tmp_now.replace(hour=int(basicSetting[4]), minute=int(basicSetting[5]), second = int(0))
		if endTime < tmp_now :			
			endTime = endTime + datetime.timedelta(days=int(basicSetting[13]))
	
	bossNum = int(len(boss_inputData)/5)

	fixed_bossNum = int(len(fixed_inputData)/6) 
	
	for i in range(bossNum):
		tmp_bossData.append(boss_inputData[i*5:i*5+5])

	for i in range(fixed_bossNum):
		tmp_fixed_bossData.append(fixed_inputData[i*6:i*6+6]) 
		
	#print (tmp_bossData)
		
	for j in range(bossNum):
		for i in range(len(tmp_bossData[j])):
			tmp_bossData[j][i] = tmp_bossData[j][i].strip()

	for j in range(fixed_bossNum):
		for i in range(len(tmp_fixed_bossData[j])):
			tmp_fixed_bossData[j][i] = tmp_fixed_bossData[j][i].strip()

	############## 일반보스 정보 리스트 #####################
	for j in range(bossNum):
		tmp_len = tmp_bossData[j][1].find(':')
		f.append(tmp_bossData[j][0][11:])         #bossData[0] : 보스명
		f.append(tmp_bossData[j][1][10:tmp_len])  #bossData[1] : 시
		f.append(tmp_bossData[j][2][13:])         #bossData[2] : 멍/미입력
		f.append(tmp_bossData[j][3][20:])         #bossData[3] : 분전 알림멘트
		f.append(tmp_bossData[j][4][13:])         #bossData[4] : 젠 알림멘트
		f.append(tmp_bossData[j][1][tmp_len+1:])  #bossData[5] : 분
		f.append('')                              #bossData[6] : 메세지
		bossData.append(f)
		f = []
		bossTime.append(datetime.datetime.now()+datetime.timedelta(days=365, hours = int(basicSetting[0])))
		tmp_bossTime.append(datetime.datetime.now()+datetime.timedelta(days=365, hours = int(basicSetting[0])))
		bossTimeString.append('99:99:99')
		bossDateString.append('9999-99-99')
		tmp_bossTimeString.append('99:99:99')
		tmp_bossDateString.append('9999-99-99')
		bossFlag.append(False)
		bossFlag0.append(False)
		bossMungFlag.append(False)
		bossMungCnt.append(0)
		
	tmp_fixed_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))

	############## 고정보스 정보 리스트 #####################	
	for j in range(fixed_bossNum):
		tmp_fixed_len = tmp_fixed_bossData[j][1].find(':')
		tmp_fixedGen_len = tmp_fixed_bossData[j][2].find(':')
		fb.append(tmp_fixed_bossData[j][0][11:])                  #fixed_bossData[0] : 보스명
		fb.append(tmp_fixed_bossData[j][1][11:tmp_fixed_len])     #fixed_bossData[1] : 시
		fb.append(tmp_fixed_bossData[j][1][tmp_fixed_len+1:])     #fixed_bossData[2] : 분
		fb.append(tmp_fixed_bossData[j][4][20:])                  #fixed_bossData[3] : 분전 알림멘트
		fb.append(tmp_fixed_bossData[j][5][13:])                  #fixed_bossData[4] : 젠 알림멘트
		fb.append(tmp_fixed_bossData[j][2][12:tmp_fixedGen_len])  #fixed_bossData[5] : 젠주기-시
		fb.append(tmp_fixed_bossData[j][2][tmp_fixedGen_len+1:])  #fixed_bossData[6] : 젠주기-분
		fb.append(tmp_fixed_bossData[j][3][12:16])                #fixed_bossData[7] : 시작일-년	
		fb.append(tmp_fixed_bossData[j][3][17:19])                #fixed_bossData[8] : 시작일-월
		fb.append(tmp_fixed_bossData[j][3][20:22])                #fixed_bossData[9] : 시작일-일
		fixed_bossData.append(fb)
		fb = []
		fixed_bossFlag.append(False)
		fixed_bossFlag0.append(False)
		fixed_bossTime.append(tmp_fixed_now.replace(year = int(fixed_bossData[j][7]), month = int(fixed_bossData[j][8]), day = int(fixed_bossData[j][9]), hour=int(fixed_bossData[j][1]), minute=int(fixed_bossData[j][2]), second = int(0)))
		if fixed_bossTime[j] < tmp_fixed_now :
			while fixed_bossTime[j] < tmp_fixed_now :
				fixed_bossTime[j] = fixed_bossTime[j] + datetime.timedelta(hours=int(fixed_bossData[j][5]), minutes=int(fixed_bossData[j][6]), seconds = int(0))

	################# 이모지 로드 ######################

	emo_inidata = repo.get_contents("emoji.ini")
	emoji_data1 = base64.b64decode(emo_inidata.content)
	emoji_data1 = emoji_data1.decode('utf-8')
	emo_inputData = emoji_data1.split('\n')

	for i in range(len(emo_inputData)):
		tmp_emo = emo_inputData[i][8:].rstrip('\r')
		if tmp_emo != "":
			tmp_racing_unit.append(tmp_emo)
	
	################# 리젠보스 시간 정렬 ######################
	regenData = []
	regenTime = []
	regenbossName = []
	outputTimeHour = []
	outputTimeMin = []

	for i in range(bossNum):
		if bossData[i][2] == "1":
			f.append(bossData[i][0] + "R")
		else:
			f.append(bossData[i][0])
		f.append(bossData[i][1] + bossData[i][5])
		regenData.append(f)
		regenTime.append(bossData[i][1] + bossData[i][5])
		f = []
		
	regenTime = sorted(list(set(regenTime)))
	
	for j in range(len(regenTime)):
		for i in range(len(regenData)):
			if regenTime[j] == regenData[i][1] :
				f.append(regenData[i][0])
		regenbossName.append(f)
		outputTimeHour.append(int(regenTime[j][:2]))
		outputTimeMin.append(int(regenTime[j][2:]))
		f = []

	regenembed = discord.Embed(
			title='----- 보스별 리스폰 시간 -----',
			description= ' ')
	for i in range(len(regenTime)):
		if outputTimeMin[i] == 0 :
			regenembed.add_field(name=str(outputTimeHour[i]) + '시간', value= '```'+ ', '.join(map(str, sorted(regenbossName[i]))) + '```', inline=False)
		else :
			regenembed.add_field(name=str(outputTimeHour[i]) + '시간' + str(outputTimeMin[i]) + '분', value= '```' + ','.join(map(str, sorted(regenbossName[i]))) + '```', inline=False)
	regenembed.set_footer(text = 'R : 멍 보스')

	##########################################################

	if basicSetting[10] !="":
		scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #정산
		credentials = ServiceAccountCredentials.from_json_keyfile_name(basicSetting[10], scope) #정산

init()

channel = ''

async def task():
	await client.wait_until_ready()

	global channel
	global endTime
		
	global basicSetting
	global bossData
	global fixed_bossData

	global bossNum
	global fixed_bossNum
	global chkvoicechannel
	global chkrelogin

	global bossTime
	global tmp_bossTime
	
	global fixed_bossTime

	global bossTimeString
	global bossDateString
	global tmp_bossTimeString
	global tmp_bossDateString

	global bossFlag
	global bossFlag0
	global fixed_bossFlag
	global fixed_bossFlag0
	global bossMungFlag
	global bossMungCnt
	
	global voice_client1
	
	global channel_info
	global channel_name
	global channel_id
	global channel_voice_name
	global channel_voice_id
	global channel_type
	
	global endTime
	global kill_Time
	
	if chflg == 1 : 
		if voice_client1.is_connected() == False :
			voice_client1 = await self.get_channel(basicSetting[6]).connect(reconnect=True)
			if voice_client1.is_connected() :
				await dbLoad()
				await self.get_channel(channel).send( '< 다시 왔습니다! >', tts=False)
				print("명치복구완료!")

	while not client.is_closed():
		############ 워닝잡자! ############
		if log_stream.getvalue().find("Awaiting") != -1:
			log_stream.truncate(0)
			log_stream.seek(0)
			await self.get_channel(channel).send( '< 디코접속에러! 잠깐 나갔다 올께요! >', tts=False)
			await dbSave()
			raise SystemExit
		
		log_stream.truncate(0)
		log_stream.seek(0)
		##################################

		now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
		priv0 = now+datetime.timedelta(minutes=int(basicSetting[3]))
		priv = now+datetime.timedelta(minutes=int(basicSetting[1]))
		aftr = now+datetime.timedelta(minutes=int(0-int(basicSetting[2])))

		if channel != '':			
			################ 보탐봇 재시작 ################ 
			if endTime.strftime('%Y-%m-%d ') + endTime.strftime('%H:%M:%S') == now.strftime('%Y-%m-%d ') + now.strftime('%H:%M:%S'):
				await dbSave()
				await FixedBossDateSave()
				await data_list_Save("kill_list.ini", "-----척살명단-----", kill_Data)
				await data_list_Save("item_list.ini", "-----아이템목록-----", item_Data)
				#await self.get_channel(channel).send('<갑자기 인사해도 놀라지마세요!>', tts=False)
				print("보탐봇재시작!")
				endTime = endTime + datetime.timedelta(days = int(basicSetting[13]))
				await voice_client1.disconnect()
				await asyncio.sleep(2)

				inidata_restart = repo_restart.get_contents("restart.txt")
				file_data_restart = base64.b64decode(inidata_restart.content)
				file_data_restart = file_data_restart.decode('utf-8')
				inputData_restart = file_data_restart.split('\n')

				if len(inputData_restart) < 3:	
					contents12 = repo_restart.get_contents("restart.txt")
					repo_restart.update_file(contents12.path, "restart_0", "restart\nrestart\nrestrat\n", contents12.sha)
				else:
					contents12 = repo_restart.get_contents("restart.txt")
					repo_restart.update_file(contents12.path, "restart_1", "", contents12.sha)
			
			################ 킬 목록 초기화 ################ 
			if kill_Time.strftime('%Y-%m-%d ') + kill_Time.strftime('%H:%M') == now.strftime('%Y-%m-%d ') + now.strftime('%H:%M'):
				kill_Time = kill_Time + datetime.timedelta(days=int(1))
				await init_data_list('kill_list.ini', '-----척살명단-----')

			################ 고정 보스 확인 ################ 
			for i in range(fixed_bossNum):
				################ before_alert1 ################ 
				if fixed_bossTime[i] <= priv0 and fixed_bossTime[i] > priv:
					if basicSetting[3] != '0':
						if fixed_bossFlag0[i] == False:
							fixed_bossFlag0[i] = True
							await self.get_channel(channel).send("```" + fixed_bossData[i][0] + ' ' + basicSetting[3] + '분 전 ' + fixed_bossData[i][3] +' [' +  fixed_bossTime[i].strftime('%H:%M:%S') + ']```', tts=False)
							await PlaySound(voice_client1, './sound/' + fixed_bossData[i][0] + '알림1.mp3')

				################ before_alert ################ 
				if fixed_bossTime[i] <= priv and fixed_bossTime[i] > now:
					if basicSetting[1] != '0' :
						if fixed_bossFlag[i] == False:
							fixed_bossFlag[i] = True
							await self.get_channel(channel).send("```" + fixed_bossData[i][0] + ' ' + basicSetting[1] + '분 전 ' + fixed_bossData[i][3] +' [' +  fixed_bossTime[i].strftime('%H:%M:%S') + ']```', tts=False)
							await PlaySound(voice_client1, './sound/' + fixed_bossData[i][0] + '알림.mp3')
				
				################ 보스 젠 시간 확인 ################
				if fixed_bossTime[i] <= now :
					fixed_bossTime[i] = fixed_bossTime[i]+datetime.timedelta(hours=int(fixed_bossData[i][5]), minutes=int(fixed_bossData[i][6]), seconds = int(0))
					fixed_bossFlag0[i] = False
					fixed_bossFlag[i] = False
					embed = discord.Embed(
							description= "```" + fixed_bossData[i][0] + fixed_bossData[i][4] + "```" ,
							color=0x00ff00
							)
					await self.get_channel(channel).send(embed=embed, tts=False)
					await PlaySound(voice_client1, './sound/' + fixed_bossData[i][0] + '젠.mp3')

			################ 일반 보스 확인 ################ 
			for i in range(bossNum):
				################ before_alert1 ################ 
				if bossTime[i] <= priv0 and bossTime[i] > priv:
					if basicSetting[3] != '0':
						if bossFlag0[i] == False:
							bossFlag0[i] = True
							if bossData[i][6] != '' :
								await self.get_channel(channel).send("```" + bossData[i][0] + ' ' + basicSetting[3] + '분 전 ' + bossData[i][3] + " [" +  bossTimeString[i] + "]" + '\n<' + bossData[i][6] + '>```', tts=False)
							else :
								await self.get_channel(channel).send("```" + bossData[i][0] + ' ' + basicSetting[3] + '분 전 ' + bossData[i][3] + " [" +  bossTimeString[i] + "]```", tts=False)
							await PlaySound(voice_client1, './sound/' + bossData[i][0] + '알림1.mp3')

				################ before_alert ################
				if bossTime[i] <= priv and bossTime[i] > now:
					if basicSetting[1] != '0' :
						if bossFlag[i] == False:
							bossFlag[i] = True
							if bossData[i][6] != '' :
								await self.get_channel(channel).send("```" + bossData[i][0] + ' ' + basicSetting[1] + '분 전 ' + bossData[i][3] + " [" +  bossTimeString[i] + "]" + '\n<' + bossData[i][6] + '>```', tts=False)
							else :
								await self.get_channel(channel).send("```" + bossData[i][0] + ' ' + basicSetting[1] + '분 전 ' + bossData[i][3] + " [" +  bossTimeString[i] + "]```", tts=False)
							await PlaySound(voice_client1, './sound/' + bossData[i][0] + '알림.mp3')

				################ 보스 젠 시간 확인 ################ 
				if bossTime[i] <= now :
					#print ('if ', bossTime[i])
					bossMungFlag[i] = True
					tmp_bossTime[i] = bossTime[i]
					tmp_bossTimeString[i] = tmp_bossTime[i].strftime('%H:%M:%S')
					tmp_bossDateString[i] = tmp_bossTime[i].strftime('%Y-%m-%d')
					bossTimeString[i] = '99:99:99'
					bossDateString[i] = '9999-99-99'
					bossTime[i] = now+datetime.timedelta(days=365)
					if bossData[i][6] != '' :
						embed = discord.Embed(
								description= "```" + bossData[i][0] + bossData[i][4] + '\n<' + bossData[i][6] + '>```' ,
								color=0x00ff00
								)
					else :
						embed = discord.Embed(
								description= "```" + bossData[i][0] + bossData[i][4] + "```" ,
								color=0x00ff00
								)
					await self.get_channel(channel).send(embed=embed, tts=False)
					await PlaySound(voice_client1, './sound/' + bossData[i][0] + '젠.mp3')

				################ 보스 자동 멍 처리 ################ 
				if bossMungFlag[i] == True:
					if (bossTime[i]+datetime.timedelta(days=-365)) <= aftr:
						if basicSetting[2] != '0':
							if int(basicSetting[17]) <= bossMungCnt[i] and int(basicSetting[17]) != 0:
								bossTime[i] = datetime.datetime.now()+datetime.timedelta(days=365, hours = int(basicSetting[0]))
								tmp_bossTime[i] =  datetime.datetime.now()+datetime.timedelta(days=365, hours = int(basicSetting[0]))
								bossTimeString[i] = '99:99:99'
								bossDateString[i] = '9999-99-99'
								tmp_bossTimeString[i] = '99:99:99'
								tmp_bossDateString[i] = '9999-99-99'
								bossFlag[i] = False
								bossFlag0[i] = False
								bossMungFlag[i] = False
								bossMungCnt[i] = 0
								if bossData[i][2] == '0':
									await self.get_channel(channel).send(f'```자동 미입력 횟수 {basicSetting[17]}회 초과! [{bossData[i][0]}] 삭제!```', tts=False)
									print ('자동미입력 횟수초과 <' + bossData[i][0] + ' 삭제완료>')
								else:
									await self.get_channel(channel).send(f'```자동 멍처리 횟수 {basicSetting[17]}회 초과! [{bossData[i][0]}] 삭제!```', tts=False)
									print ('자동멍처리 횟수초과 <' + bossData[i][0] + ' 삭제완료>')
								#await dbSave()
								
							else:
								################ 미입력 보스 ################
								if bossData[i][2] == '0':
									bossFlag[i] = False
									bossFlag0[i] = False
									bossMungFlag[i] = False
									bossMungCnt[i] = bossMungCnt[i] + 1
									tmp_bossTime[i] = bossTime[i] = nextTime = tmp_bossTime[i]+datetime.timedelta(hours=int(bossData[i][1]), minutes=int(bossData[i][5]))
									tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
									tmp_bossDateString[i] = bossDateString[i] = nextTime.strftime('%Y-%m-%d')
									await self.get_channel(channel).send("```" +  bossData[i][0] + ' 미입력 됐습니다.```', tts=False)
									embed = discord.Embed(
										description= '```다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.```',
										color=0xff0000
										)
									await self.get_channel(channel).send(embed=embed, tts=False)
									await PlaySound(voice_client1, './sound/' + bossData[i][0] + '미입력.mp3')
								################ 멍 보스 ################
								else :
									bossFlag[i] = False
									bossFlag0[i] = False
									bossMungFlag[i] = False
									bossMungCnt[i] = bossMungCnt[i] + 1
									tmp_bossTime[i] = bossTime[i] = nextTime = tmp_bossTime[i]+datetime.timedelta(hours=int(bossData[i][1]), minutes=int(bossData[i][5]))
									tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
									tmp_bossDateString[i] = bossDateString[i] = nextTime.strftime('%Y-%m-%d')
									await self.get_channel(channel).send("```" + bossData[i][0] + ' 멍 입니다.```')
									embed = discord.Embed(
										description= '```다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.```',
										color=0xff0000
										)
									await self.get_channel(channel).send(embed=embed, tts=False)
									await PlaySound(voice_client1, './sound/' + bossData[i][0] + '멍.mp3')

		await asyncio.sleep(1) # task runs every 60 seconds

#mp3 파일 생성함수(gTTS 이용, 남성목소리)
async def MakeSound(saveSTR, filename):
	
	tts = gTTS(saveSTR, lang = 'ko')
	tts.save('./' + filename + '.wav')
	
	'''
	try:
		encText = urllib.parse.quote(saveSTR)
		urllib.request.urlretrieve("https://clova.ai/proxy/voice/api/tts?text=" + encText + "%0A&voicefont=1&format=wav",filename + '.wav')
	except Exception as e:
		print (e)
		tts = gTTS(saveSTR, lang = 'ko')
		tts.save('./' + filename + '.wav')
		pass
	'''
#mp3 파일 재생함수	
async def PlaySound(voiceclient, filename):
	source = discord.FFmpegPCMAudio(filename)
	try:
		voiceclient.play(source)
	except discord.errors.ClientException:
		while voiceclient.is_playing():
			await asyncio.sleep(1)
	while voiceclient.is_playing():
		await asyncio.sleep(1)
	voiceclient.stop()
	source.cleanup()

#my_bot.db 저장하기
async def dbSave():
	global bossData
	global bossNum
	global bossTime
	global bossTimeString
	global bossDateString
	global bossMungFlag
	global bossMungCnt

	for i in range(bossNum):
		for j in range(bossNum):
			if bossTimeString[i] and bossTimeString[j] != '99:99:99':
				if bossTimeString[i] == bossTimeString[j] and i != j:
					tmp_time1 = bossTimeString[j][:6]
					tmp_time2 = (int(bossTimeString[j][6:]) + 1)%100
					if tmp_time2 < 10 :
						tmp_time22 = '0' + str(tmp_time2)
					elif tmp_time2 == 60 :
						tmp_time22 = '00'
					else :
						tmp_time22 = str(tmp_time2)
					bossTimeString[j] = tmp_time1 + tmp_time22
					
	datelist1 = bossTime
	
	datelist = list(set(datelist1))

	information1 = '----- 보스탐 정보 -----\n'
	for timestring in sorted(datelist):
		for i in range(bossNum):
			if timestring == bossTime[i]:
				if bossTimeString[i] != '99:99:99' or bossMungFlag[i] == True :
					if bossMungFlag[i] == True :
						if bossData[i][2] == '0' :
							information1 += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + tmp_bossTime[i].strftime('%H:%M:%S') + ' @ ' + tmp_bossTime[i].strftime('%Y-%m-%d') + ' (미입력 ' + str(bossMungCnt[i]) + '회)' + ' * ' + bossData[i][6] + '\n'
						else : 
							information1 += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + tmp_bossTime[i].strftime('%H:%M:%S') + ' @ ' + tmp_bossTime[i].strftime('%Y-%m-%d') + ' (멍 ' + str(bossMungCnt[i]) + '회)' + ' * ' + bossData[i][6] + '\n'
					else:
						if bossData[i][2] == '0' :
							information1 += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + bossTimeString[i] + ' @ ' + bossDateString[i] + ' (미입력 ' + str(bossMungCnt[i]) + '회)' + ' * ' + bossData[i][6] + '\n'
						else : 
							information1 += ' - ' + bossData[i][0] + '(' + bossData[i][1] + '.' + bossData[i][5] + ') : ' + bossTimeString[i] + ' @ ' + bossDateString[i] + ' (멍 ' + str(bossMungCnt[i]) + '회)' + ' * ' + bossData[i][6] + '\n'
						
	try :
		contents = repo.get_contents("my_bot.db")
		repo.update_file(contents.path, "bossDB", information1, contents.sha)
	except GithubException as e :
		print ('save error!!')
		print(e.args[1]['message']) # output: This repository is empty.
		errortime = datetime.datetime.now()
		print (errortime)
		pass

#my_bot.db 불러오기
async def dbLoad():
	global LoadChk
	
	contents1 = repo.get_contents("my_bot.db")
	file_data = base64.b64decode(contents1.content)
	file_data = file_data.decode('utf-8')
	beforeBossData = file_data.split('\n')
	
	if len(beforeBossData) > 1:	
		for i in range(len(beforeBossData)-1):
			for j in range(bossNum):
				startPos = beforeBossData[i+1].find('-')
				endPos = beforeBossData[i+1].find('(')
				if beforeBossData[i+1][startPos+2:endPos] == bossData[j][0] :
				#if beforeBossData[i+1].find(bossData[j][0]) != -1 :
					tmp_mungcnt = 0
					tmp_len = beforeBossData[i+1].find(':')
					tmp_datelen = beforeBossData[i+1].find('@')
					tmp_msglen = beforeBossData[i+1].find('*')

					
					years1 = beforeBossData[i+1][tmp_datelen+2:tmp_datelen+6]
					months1 = beforeBossData[i+1][tmp_datelen+7:tmp_datelen+9]
					days1 = beforeBossData[i+1][tmp_datelen+10:tmp_datelen+12]
					
					hours1 = beforeBossData[i+1][tmp_len+2:tmp_len+4]
					minutes1 = beforeBossData[i+1][tmp_len+5:tmp_len+7]
					seconds1 = beforeBossData[i+1][tmp_len+8:tmp_len+10]
					
					now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))

					tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
					tmp_now = tmp_now.replace(year = int(years1), month = int(months1), day = int(days1), hour=int(hours1), minute=int(minutes1), second = int(seconds1))

					tmp_now_chk = tmp_now + datetime.timedelta(minutes = int(basicSetting[2]))

					if tmp_now_chk < now2 : 
						deltaTime = datetime.timedelta(hours = int(bossData[j][1]), minutes = int(bossData[j][5]))
						while tmp_now_chk < now2 :
							tmp_now_chk = tmp_now_chk + deltaTime
							tmp_now = tmp_now + deltaTime
							tmp_mungcnt = tmp_mungcnt + 1

					if tmp_now_chk > now2 > tmp_now: #젠중.
						bossMungFlag[j] = True
						tmp_bossTime[j] = tmp_now
						tmp_bossTimeString[j] = tmp_bossTime[j].strftime('%H:%M:%S')
						tmp_bossDateString[j] = tmp_bossTime[j].strftime('%Y-%m-%d')
						bossTimeString[j] = '99:99:99'
						bossDateString[j] = '9999-99-99'
						bossTime[j] = tmp_bossTime[j] + datetime.timedelta(days=365)
					else:
						tmp_bossTime[j] = bossTime[j] = tmp_now
						tmp_bossTimeString[j] = bossTimeString[j] = bossTime[j].strftime('%H:%M:%S')
						tmp_bossDateString[j] = bossDateString[j] = bossTime[j].strftime('%Y-%m-%d')
						
					bossData[j][6] = beforeBossData[i+1][tmp_msglen+2:len(beforeBossData[i+1])]

					if beforeBossData[i+1][tmp_msglen-4:tmp_msglen-3] != 0 and beforeBossData[i+1][tmp_msglen-5:tmp_msglen-4] == ' ':
						bossMungCnt[j] = int(beforeBossData[i+1][tmp_msglen-4:tmp_msglen-3]) + tmp_mungcnt
					elif beforeBossData[i+1][tmp_msglen-5:tmp_msglen-4] != ' ':
						bossMungCnt[j] = int(beforeBossData[i+1][tmp_msglen-5:tmp_msglen-4] + beforeBossData[i+1][tmp_msglen-4:tmp_msglen-3]) + tmp_mungcnt
					else:
						bossMungCnt[j] = 0
		LoadChk = 0
		print ("<불러오기 완료>")
	else:
		#await self.get_channel(channel).send('<보스타임 정보가 없습니다.>', tts=False)
		LoadChk = 1
		print ("보스타임 정보가 없습니다.")

#고정보스 날짜저장
async def FixedBossDateSave():
	global fixed_bossData
	global fixed_bossTime
	global fixed_bossNum
	global FixedBossDateData
	global indexFixedBossname

	for i in range(fixed_bossNum):
		FixedBossDateData[indexFixedBossname[i] + 3] = 'startDate = '+ fixed_bossTime[i].strftime('%Y-%m-%d') + '\n'

	FixedBossDateDataSTR = ""
	for j in range(len(FixedBossDateData)):
		pos = len(FixedBossDateData[j])
		tmpSTR = FixedBossDateData[j][:pos-1] + '\r\n'
		FixedBossDateDataSTR += tmpSTR

	contents = repo.get_contents("fixed_boss.ini")
	repo.update_file(contents.path, "bossDB", FixedBossDateDataSTR, contents.sha)

#사다리함수		
async def LadderFunc(number, ladderlist, channelVal):
	if number < len(ladderlist):
		result_ladder = random.sample(ladderlist, number)
		result_ladderSTR = ','.join(map(str, result_ladder))
		embed = discord.Embed(
			title = "----- 당첨! -----",
			description= '```' + result_ladderSTR + '```',
			color=0xff00ff
			)
		await channelVal.send(embed=embed, tts=False)
	else:
		await channelVal.send('```추첨인원이 총 인원과 같거나 많습니다. 재입력 해주세요```', tts=False)

#data초기화
async def init_data_list(filename, first_line : str = "-----------"):
	try :
		contents = repo.get_contents(filename)
		repo.update_file(contents.path, "deleted list " + str(filename), first_line, contents.sha)
		print ('< 데이터 초기화 >')
	except GithubException as e :
		print ('save error!!')
		print(e.args[1]['message']) # output: This repository is empty.
		errortime = datetime.datetime.now()
		print (errortime)
		pass

#data저장
async def data_list_Save(filename, first_line : str = "-----------",  save_data : dict = {}):

	output_list = first_line+ '\n'
	for key, value in save_data.items():
		output_list += str(key) + ' ' + str(value) + '\n'

	try :
		contents = repo.get_contents(filename)
		repo.update_file(contents.path, "updated " + str(filename), output_list, contents.sha)
	except GithubException as e :
		print ('save error!!')
		print(e.args[1]['message']) # output: This repository is empty.
		errortime = datetime.datetime.now()
		print (errortime)
		pass

#서버(길드) 정보 
def get_guild_channel_info(bot):
	text_channel_name : list = []
	text_channel_id : list = []
	voice_channel_name : list = []
	voice_channel_id : list = []
	
	for guild in bot.guilds:
		for text_channel in guild.text_channels:
			text_channel_name.append(text_channel.name)
			text_channel_id.append(str(text_channel.id))
		for voice_channel in guild.voice_channels:
			voice_channel_name.append(voice_channel.name)
			voice_channel_id.append(str(voice_channel.id))
	return text_channel_name, text_channel_id, voice_channel_name, voice_channel_id

#서버(길드) 정보 
def get_guild_channel_info_sungsan(bot):
	text_channel_name : list = []
	text_channel_id : list = []
	
	for guild in bot.guilds:
		for text_channel in guild.text_channels:
			text_channel_name.append(text_channel.name)
			text_channel_id.append(str(text_channel.id))

	return text_channel_name, text_channel_id

#초성추출 함수
def convertToInitialLetters(text):
	CHOSUNG_START_LETTER = 4352
	JAMO_START_LETTER = 44032
	JAMO_END_LETTER = 55203
	JAMO_CYCLE = 588

	def isHangul(ch):
		return ord(ch) >= JAMO_START_LETTER and ord(ch) <= JAMO_END_LETTER
	
	def isBlankOrNumber(ch):
		return ord(ch) == 32 or ord(ch) >= 48 and ord(ch) <= 57

	def convertNomalInitialLetter(ch):
		dic_InitalLetter = {4352:"ㄱ"
							,4353:"ㄲ"
							,4354:"ㄴ"
							,4355:"ㄷ"
							,4356:"ㄸ"
							,4357:"ㄹ"
							,4358:"ㅁ"
							,4359:"ㅂ"
							,4360:"ㅃ"
							,4361:"ㅅ"
							,4362:"ㅆ"
							,4363:"ㅇ"
							,4364:"ㅈ"
							,4365:"ㅉ"
							,4366:"ㅊ"
							,4367:"ㅋ"
							,4368:"ㅌ"
							,4369:"ㅍ"
							,4370:"ㅎ"
							,32:" "
							,48:"0"
							,49:"1"
							,50:"2"
							,51:"3"
							,52:"4"
							,53:"5"
							,54:"6"
							,55:"7"
							,56:"8"
							,57:"9"
		}
		return dic_InitalLetter[ord(ch)]

	result = ""
	for ch in text:
		if isHangul(ch): #한글이 아닌 글자는 걸러냅니다.
			result += convertNomalInitialLetter(chr((int((ord(ch)-JAMO_START_LETTER)/JAMO_CYCLE))+CHOSUNG_START_LETTER))
		elif isBlankOrNumber(ch):
			result += convertNomalInitialLetter(chr(int(ord(ch))))

	return result

## 명치 예외처리	
def handle_exit():
	#print("Handling")
	client.loop.run_until_complete(client.logout())

	for t in asyncio.Task.all_tasks(loop=client.loop):
		if t.done():
		#t.exception()
			try:
			#print ('try :   ', t)
				t.exception()
			except asyncio.CancelledError:
			#print ('cancel :   ', t)
				continue
			continue
		t.cancel()
		try:
			client.loop.run_until_complete(asyncio.wait_for(t, 5, loop=client.loop))
			t.exception()
		except asyncio.InvalidStateError:
			pass
		except asyncio.TimeoutError:
			pass
		except asyncio.CancelledError:
			pass

def is_manager():
	async def pred(ctx : commands.Context) -> bool:
		user_info : dict = ctx.bot.db.jungsan.member.find_one({"_id":ctx.author.id})
		if not user_info:
			return False
		if "manager" in user_info["permissions"]:
			return True
		return False
	return commands.check(pred)

#detail embed
def get_detail_embed(info : dict = {}):
	# "_id" : int = 순번
	# "regist_ID" : str = 등록자ID
	# "regist" : str = 등록자 겜 ID
	# "getdate" : datetime = 등록날짜
	# "boss" : str = 보스명
	# "item" : str = 아이템명
	# "toggle" : str = 루팅자 게임 ID
	# "toggle_ID" : str = 루팅자ID
	# "itemstatus" : str = 아이템상태(미판매, 분배중, 분배완료)
	# "price" : int = 가격
	# "each_price" : int = 분배가격
	# "before_jungsan_ID" : list = 참석명단(분배전)
	# "after_jungsan_ID" : list = 참석명단(분배후)
	# "modifydate" : datetime = 수정날짜
	# "gulid_money_insert" : bool = 혈비등록여부
	# "bank_money_insert" : bool = 은행입금여부
	# "image_url":""

	embed = discord.Embed(
			title = "📜 등록 정보",
			description = "",
			color=0x00ff00
			)
	embed.add_field(name = "[ 순번 ]", value = f"```{info['_id']}```")
	embed.add_field(name = "[ 등록 ]", value = f"```{info['regist']}```")
	embed.add_field(name = "[ 일시 ]", value = f"```{info['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
	embed.add_field(name = "[ 보스 ]", value = f"```{info['boss']}```")
	embed.add_field(name = "[ 아이템 ]", value = f"```{info['item']}```")
	embed.add_field(name = "[ 루팅 ]", value = f"```{info['toggle']}```")
	embed.add_field(name = "[ 상태 ]", value = f"```{info['itemstatus']}```")
	embed.add_field(name = "[ 판매금 ]", value = f"```{info['price']}```")
	embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(info['before_jungsan_ID']+info['after_jungsan_ID'])}```")
	if 'image_url' in info.keys():
		if info['image_url'] is not None:
			embed.set_image(url = info['image_url'])
	return embed

class IlsangDistributionBot(commands.AutoShardedBot):
	def __init__(self):
		self.cog_list : list = ["admin", "manage", "member", "bank"]
		self.db = None

		self.mongoDB_connect_info : dict = {
			"host" : basicSetting_jungsan[1],
			"username" : basicSetting_jungsan[2],
			"password" : basicSetting_jungsan[3]
			}

		super().__init__(command_prefix=[""], help_command=None)
		self.session = aiohttp.ClientSession(loop=self.loop)

		# db 설정
		self.db = None
		try:
			self.db = MongoClient(ssl=True, ssl_cert_reqs=ssl.CERT_NONE, **self.mongoDB_connect_info)
			self.db.admin.command("ismaster") # 연결 완료되었는지 체크
			print(f"db 연결 완료. 아이디:{self.mongoDB_connect_info['username']}")
		except pymongo.errors.ServerSelectionTimeoutError:
			return print("db 연결 실패! host 리스트를 확인할 것.")
		except pymongo.errors.OperationFailure:
			return print("db 로그인 실패! username과 password를 확인할 것.")
		except:
			return print("db 연결 실패! 오류 발생:")

		guild_data : dict = self.db.jungsan.guild.find_one({"_id":"guild"})

		if not guild_data:
			init_guild_data : dict = {
				"guild_money":0,
				"back_up_period":14,
				"checktime":15,
				"distributionchannel":0,
				"tax":5
				}
			update_guild_data : dict = self.db.jungsan.guild.update_one({"_id":"guild"}, {"$set":init_guild_data}, upsert = True)

			basicSetting_jungsan.append(init_guild_data['back_up_period'])
			basicSetting_jungsan.append(init_guild_data['checktime'])
			basicSetting_jungsan.append(init_guild_data['distributionchannel'])
			basicSetting_jungsan.append(init_guild_data['tax'])			
		else:
			basicSetting_jungsan.append(guild_data['back_up_period'])
			basicSetting_jungsan.append(guild_data['checktime'])
			basicSetting_jungsan.append(guild_data['distributionchannel'])
			basicSetting_jungsan.append(guild_data['tax'])

		basicSetting_jungsan.append(time_Zone)

		# basicSetting_jungsan[4] = backup_period
		# basicSetting_jungsan[5] = checktime
		# basicSetting_jungsan[6] = distributionchannel		
		# basicSetting_jungsan[7] = tax
		# basicSetting_jungsan[8] = timezone			

		self.backup_data.start()

	def run(self):
		super().run(basicSetting_jungsan[0], reconnect=True)

	@tasks.loop(hours=12.0)
	async def backup_data(self):
		await self.wait_until_ready()
		if basicSetting_jungsan[6] != "" and basicSetting_jungsan[6] != 0 :
			backup_date = datetime.datetime.now() - datetime.timedelta(days = int(basicSetting_jungsan[4])) + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
			log_delete_date = datetime.datetime.now() - datetime.timedelta(days = int(30))
			
			jungsan_document :list = []
			delete_jungsan_id : list = []
			backup_jungsan_document : list = []
			total_save_money : int = 0
			cnt : int = 0

			jungsan_document = list(self.db.jungsan.jungsandata.find({"modifydate":{"$lt":backup_date}, "itemstatus":"분배중"}))

			for jungsan_data in jungsan_document:
				cnt += 1
				total_save_money += int(jungsan_data['each_price']*len(jungsan_data['before_jungsan_ID'])*(1-(basicSetting_jungsan[7]/100)))
				delete_jungsan_id.append(jungsan_data['_id'])
				del jungsan_data['_id']
				backup_jungsan_document.append(jungsan_data)

			self.db.jungsan.guild_log.delete_many({'log_date':{"$lt":log_delete_date}})
			self.db.jungsan.jungsandata.delete_many({"$and": [{'modifydate':{"$lt":log_delete_date}}, {"itemstatus":"분배완료"}]})
			self.db.jungsan.jungsandata.delete_many({'_id':{'$in':delete_jungsan_id}})

			if len(backup_jungsan_document) > 0:
				tmp : list = list(map(str,delete_jungsan_id))
				self.db.backup.backupdata.insert_many(backup_jungsan_document)

				result_guild_update : dict = self.db.jungsan.guild.update_one({"_id":"guild"}, {"$inc":{"guild_money":total_save_money}}, upsert = True)
				total_guild_money : dict = self.db.jungsan.guild.find_one({"_id":"guild"})

				insert_log_data = {
							"in_out_check":True, # True : 입금, False : 출금
							"log_date":datetime.datetime.now(),
							"money":str(total_save_money),
							"member_list":[],
							"reason":"정산 자동 삭제 후 적립"
				}
				result_guild_log = self.db.jungsan.guild_log.insert_one(insert_log_data)

				embed = discord.Embed(
						title = f"💰  혈비 자동 적립 ({(datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))).strftime('%y-%m-%d %H:%M:%S')})",
						description = f"",
						color=0x00ff00
						)
				embed.add_field(name = f"**삭제순번**", value = f"**```fix\n{' '.join(tmp)}```**", inline = False)
				embed.add_field(name = f"**적립**", value = f"**```fix\n{total_save_money}```**")
				embed.add_field(name = f"**혈비**", value = f"**```fix\n{total_guild_money['guild_money']}```**")
				embed.set_footer(text = f"기간({basicSetting_jungsan[4]}일) 경과로 인하여 총 {cnt}건 혈비 자동적립 완료\n(총 혈비 {total_guild_money['guild_money']})")

				await self.get_channel(int(basicSetting_jungsan[6])).send(embed = embed)

	async def on_ready(self):
		global basicSetting

		global channel
		
		global voice_client1

		global channel_info
		global channel_name
		global channel_id
		global channel_voice_name
		global channel_voice_id
		global channel_type
		
		global chkvoicechannel
		global chflg
		
		global endTime
		global setting_channel_name

		print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
		print(self.user.name)
		print(self.user.id)
		print("===========")

		jungsan_channel_name, jungsan_channel_id = get_guild_channel_info_sungsan(self)
		channel_name, channel_id, channel_voice_name, channel_voice_id = get_guild_channel_info(self)

		await dbLoad()

		if str(basicSetting[6]) in channel_voice_id and str(basicSetting[7]) in channel_id:
			voice_client1 = await self.get_channel(basicSetting[6]).connect(reconnect=True)
			channel = basicSetting[7]

			setting_channel_name = self.get_channel(basicSetting[7]).name

			now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))

			print('< 접속시간 [' + now.strftime('%Y-%m-%d ') + now.strftime('%H:%M:%S') + '] >')
			print('< 텍스트채널 [' + self.get_channel(basicSetting[7]).name + '] 접속완료>')
			print('< 음성채널 [' + self.get_channel(basicSetting[6]).name + '] 접속완료>')
			if basicSetting[8] != "":
				if str(basicSetting[8]) in channel_id:
					print('< 사다리채널 [' + self.get_channel(int(basicSetting[8])).name + '] 접속완료 >')
				else:
					basicSetting[8] = ""
					print(f"사다리채널 ID 오류! [{command[28][0]} 사다리] 명령으로 재설정 바랍니다.")
			if basicSetting[11] != "":
				if str(basicSetting[11]) in channel_id:
					print('< 정산채널 [' + self.get_channel(int(basicSetting[11])).name + '] 접속완료>')
				else:
					basicSetting[11] = ""
					print(f"정산채널 ID 오류! [{command[28][0]} 정산] 명령으로 재설정 바랍니다.")
			if basicSetting[18] != "":
				if str(basicSetting[18]) in channel_id:
					print('< 척살채널 [' + self.get_channel(int(basicSetting[18])).name + '] 접속완료>')
				else:
					basicSetting[18] = ""
					print(f"척살채널 ID 오류! [{command[28][0]} 척살] 명령으로 재설정 바랍니다.")
			if basicSetting[19] != "":
				if str(basicSetting[19]) in channel_id:
					print('< 경주채널 [' + self.get_channel(int(basicSetting[19])).name + '] 접속완료>')
				else:
					basicSetting[19] = ""
					print(f"경주채널 ID 오류! [{command[28][0]} 경주] 명령으로 재설정 바랍니다.")
			if basicSetting[20] != "":
				if str(basicSetting[20]) in channel_id:
					print('< 아이템채널 [' + self.get_channel(int(basicSetting[20])).name + '] 접속완료>')
				else:
					basicSetting[20] = ""
					print(f"아이템채널 ID 오류! [{command[28][0]} 아이템] 명령으로 재설정 바랍니다.")
			if int(basicSetting[13]) != 0 :
				print('< 보탐봇 재시작 시간 ' + endTime.strftime('%Y-%m-%d ') + endTime.strftime('%H:%M:%S') + ' >')
				print('< 보탐봇 재시작 주기 ' + basicSetting[13] + '일 >')
			else :
				print('< 보탐봇 재시작 설정안됨 >')
			chflg = 1
		else:
			basicSetting[6] = ""
			basicSetting[7] = ""
			print(f"설정된 채널 값이 없거나 잘못 됐습니다. **[{command[0][0]}]** 명령어 먼저 입력하여 사용해주시기 바랍니다.")

		if str(basicSetting_jungsan[6]) in jungsan_channel_id:
			print(f"< 분배 텍스트채널 [{self.get_channel(int(basicSetting_jungsan[6])).name}] 접속완료 >")
		else:
			basicSetting_jungsan[6] = 0
			print(f"분배 설정된 채널 값이 없거나 잘못 됐습니다. [{commandSetting_jungsan[36][0]}] 명령어를 먼저 입력하여 사용해주시기 바랍니다.")
		
		# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
		# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
		await self.change_presence(status=discord.Status.dnd, activity=discord.Game(name=command[1][0], type=1), afk=False)

	async def on_command_error(self, ctx : commands.Context, error : commands.CommandError):
		if isinstance(error, CommandNotFound):
			return
		elif isinstance(error, MissingRequiredArgument):
			return
		elif isinstance(error, discord.ext.commands.MissingPermissions):
			return await ctx.send(f"**[{ctx.message.content.split()[0]}]** 명령을 사용할 권한이 없습니다.!")
		elif isinstance(error, discord.ext.commands.CheckFailure):
			return await ctx.send(f"**[{ctx.message.content.split()[0]}]** 명령을 사용할 권한이 없습니다.!")
		raise error

	async def close(self):
		await self.session.close()
		await super().close()
		print("일상분배봇 종료 완료.")

class settingCog(commands.Cog): 
	def __init__(self, bot):
		self.bot = bot

		self.member_db = self.bot.db.jungsan.member
		self.jungsan_db = self.bot.db.jungsan.jungsandata
		self.guild_db = self.bot.db.jungsan.guild
		self.guild_db_log = self.bot.db.jungsan.guild_log

	################ 채널등록 ################ 
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[36][0], aliases=commandSetting_jungsan[36][1:])
	async def join_channel(self, ctx, *, args : str = None):
		global basicSetting_jungsan

		if basicSetting_jungsan[6] == "" or basicSetting_jungsan[6] == 0:
			channel = ctx.message.channel.id #메세지가 들어온 채널 ID

			print (f"[ {basicSetting_jungsan[6]} ]")
			print (f"] {ctx.message.channel.name} [")

			basicSetting_jungsan[6] = str(channel)

			result = self.guild_db.update_one({"_id":"guild"}, {"$set":{"distributionchannel":str(channel)}}, upsert = True)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 내역 삭제 주기 설정 실패.")   

			await ctx.send(f"< 텍스트채널 [{ctx.message.channel.name}] 접속완료 >", tts=False)
			
			print(f"< 텍스트채널 [ {self.bot.get_channel(int(basicSetting_jungsan[6])).name} ] 접속완료>")
		else:
			for guild in self.bot.guilds:
				for text_channel in guild.text_channels:
					if basicSetting_jungsan[6] == str(text_channel.id):
						curr_guild_info = guild
						print(curr_guild_info.name, guild.name, curr_guild_info.get_channel(int(basicSetting_jungsan[6])).name)

			emoji_list : list = ["⭕", "❌"]
			guild_error_message = await ctx.send(f"이미 **[{curr_guild_info.name}]** 서버 **[{curr_guild_info.get_channel(int(basicSetting_jungsan[6])).name}]** 채널이 명령어 채널로 설정되어 있습니다.\n해당 채널로 명령어 채널을 변경 하시려면 ⭕ 그대로 사용하시려면 ❌ 를 눌러주세요.\n({basicSetting_jungsan[5]}이내 미입력시 기존 설정 그대로 설정됩니다.)", tts=False)

			for emoji in emoji_list:
				await guild_error_message.add_reaction(emoji)

			def reaction_check(reaction, user):
				return (reaction.message.id == guild_error_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)
			try:
				reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
			except asyncio.TimeoutError:
				return await ctx.send(f"시간이 초과됐습니다. **[{curr_guild_info.name}]** 서버 **[{curr_guild_info.get_channel(basicSetting_jungsan[6]).name}]** 채널에서 사용해주세요!")
			
			if str(reaction) == "⭕":
				basicSetting_jungsan[6] = str(ctx.message.channel.id)

				print ('[ ', basicSetting_jungsan[6], ' ]')
				print ('] ', ctx.message.channel.name, ' [')
			
				result = self.guild_db.update_one({"_id":"guild"}, {"$set":{"distributionchannel":str(basicSetting_jungsan[6])}}, upsert = True)
				if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
					return await ctx.send(f"{ctx.author.mention}, 정산 내역 삭제 주기 설정 실패.")

				return await ctx.send(f"명령어 채널이 **[{ctx.author.guild.name}]** 서버 **[{ctx.message.channel.name}]** 채널로 새로 설정되었습니다.")
			else:
				return await ctx.send(f"명령어 채널 설정이 취소되었습니다.\n**[{curr_guild_info.name}]** 서버 **[{curr_guild_info.get_channel(int(basicSetting_jungsan[6])).name}]** 채널에서 사용해주세요!")

	################ 백업주기 설정 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[40][0], aliases=commandSetting_jungsan[40][1:])
	async def set_backup_time(self, ctx, *, args : str = None):
		global basicSetting_jungsan

		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[40][0]} [숫자]** 양식으로 등록 해주세요")
		
		try:
			args = int(args)
		except ValueError:
			return await ctx.send(f"**정산 내역 삭제 주기는 [숫자]** 로 입력 해주세요")

		basicSetting_jungsan[4] = args
		result = self.guild_db.update_one({"_id":"guild"}, {"$set":{"back_up_period":args}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 정산 내역 삭제 주기 설정 실패.")   

		return  await ctx.send(f"정산 내역 삭제 주기를 **[{args}]**일로 설정 하였습니다.")

	################ 확인시간 설정 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[41][0], aliases=commandSetting_jungsan[41][1:])
	async def set_check_time(self, ctx, *, args : str = None):
		global basicSetting_jungsan

		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[41][0]} [숫자]** 양식으로 등록 해주세요")
		
		try:
			args = int(args)
		except ValueError:
			return await ctx.send(f"**이모지 확인 시간은 [숫자]** 로 입력 해주세요")

		basicSetting_jungsan[5] = args
		result = self.guild_db.update_one({"_id":"guild"}, {"$set":{"checktime":args}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 이모지 확인 시간 설정 실패.")   

		return  await ctx.send(f"이모지 확인 시간을 **[{args}]**초로 설정 하였습니다.")

	################ 세금 설정 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[42][0], aliases=commandSetting_jungsan[42][1:])
	async def set_tax(self, ctx, *, args : str = None):
		global basicSetting_jungsan

		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[42][0]} [숫자]** 양식으로 등록 해주세요")
		
		try:
			args = int(args)
		except ValueError:
			return await ctx.send(f"**세율은 시간은 [숫자]** 로 입력 해주세요")

		basicSetting_jungsan[7] = args
		result = self.guild_db.update_one({"_id":"guild"}, {"$set":{"tax":args}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 세율 설정 실패.")   

		return  await ctx.send(f"세율을 **[{args}]**%로 설정 하였습니다.")

class adminCog(commands.Cog): 
	def __init__(self, bot):
		self.bot = bot
		
		self.member_db = self.bot.db.jungsan.member
		self.jungsan_db = self.bot.db.jungsan.jungsandata
		self.guild_db = self.bot.db.jungsan.guild
		self.guild_db_log = self.bot.db.jungsan.guild_log
		self.backup_db = self.bot.db.backup.backupdata

	################ 기본설정확인 ################ 
	@commands.command(name=commandSetting_jungsan[46][0], aliases=commandSetting_jungsan[46][1:])
	async def setting_info(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		embed = discord.Embed(
			title = f"⚙️ 기본 설정(v4)",
			color=0xff00ff
			)
		embed.add_field(name = f"🚫 삭제 주기", value = f"```{basicSetting_jungsan[4]} 일```")
		embed.add_field(name = f"⌛ 체크 시간", value = f"```{basicSetting_jungsan[5]} 초```")
		embed.add_field(name = f"⚖️ 수수료", value = f"```{basicSetting_jungsan[7]} %```")
		embed.add_field(name = f"🗨️ 명령 채널", value = f"```{ctx.message.channel.name}```")
		return await ctx.send(embed = embed, tts=False)

	################ 현재시간 확인 ################ 
	@commands.command(name=commandSetting_jungsan[37][0], aliases=commandSetting_jungsan[37][1:])
	async def current_time_check(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return
		now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		embed = discord.Embed(
			title = f"현재시간은 {now.strftime('%H')}시 {now.strftime('%M')}분 {now.strftime('%S')}초 입니다.",
			color=0xff00ff
			)
		return await ctx.send(embed = embed, tts=False)

	################ 상태메세지 변경 ################ 
	@commands.command(name=commandSetting_jungsan[38][0], aliases=commandSetting_jungsan[38][1:])
	async def status_modify(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[38][0]} [내용]** 양식으로 변경 해주세요")

		await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=args, type=1), afk = False)
		return await ctx.send(f"< 상태메세지 **[ {args} ]**로 변경완료 >", tts=False)

	################ 도움말 ################ 
	@commands.command(name=commandSetting_jungsan[39][0], aliases=commandSetting_jungsan[39][1:])
	async def command_help(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return
		
		if args:
			return await ctx.send(f"**{commandSetting_jungsan[39][0]}만 입력 해주세요!**", tts=False)
		else:
			admin_command_list : str = ""
			admin_command_list += f"{','.join(commandSetting_jungsan[36])}\n"   # 분배채널설정
			admin_command_list += f"{','.join(commandSetting_jungsan[4])} [아이디]\n"   # 총무등록
			admin_command_list += f"{','.join(commandSetting_jungsan[5])} [아이디]\n"   # 총무삭제
			
			manager_command_list : str = ""
			manager_command_list += f"{','.join(commandSetting_jungsan[0])}  ※ 관리자권한도 필요\n"   # 혈원데이터초기화
			manager_command_list += f"{','.join(commandSetting_jungsan[1])}  ※ 관리자권한도 필요\n"   # 정산데이터초기화
			manager_command_list += f"{','.join(commandSetting_jungsan[2])}  ※ 관리자권한도 필요\n"   # 혈비데이터초기화
			manager_command_list += f"{','.join(commandSetting_jungsan[3])}  ※ 관리자권한도 필요\n"   # 백업데이터초기화
			manager_command_list += f"{','.join(commandSetting_jungsan[40])}\n"   # 삭제주기설정
			manager_command_list += f"{','.join(commandSetting_jungsan[41])}\n"   # 확인시간설정
			manager_command_list += f"{','.join(commandSetting_jungsan[42])}\n"   # 세금설정
			manager_command_list += f"{','.join(commandSetting_jungsan[47])}  ※ 30일 이후 데이터는 삭제됨\n"   # 혈비로그확인
			manager_command_list += f"{','.join(commandSetting_jungsan[43])} (상세)\n"   # 전체확인
			manager_command_list += f"{','.join(commandSetting_jungsan[43])} (상세) (검색조건) (검색값)\n"   # 전체확인
			manager_command_list += f"{','.join(commandSetting_jungsan[9])} [아이디] [디스코드ID]\n"   # 혈원입력
			manager_command_list += f"{','.join(commandSetting_jungsan[10])} [아이디]\n"   # 혈원삭제
			manager_command_list += f"{','.join(commandSetting_jungsan[30])} [금액] [아이디1] [아이디2]...\n"   # 은행입금
			manager_command_list += f"{','.join(commandSetting_jungsan[31])} [금액] [아이디1] [아이디2]...\n"   # 은행출금
			manager_command_list += f"{','.join(commandSetting_jungsan[32])} [금액]\n"   # 혈비입금
			manager_command_list += f"{','.join(commandSetting_jungsan[49])} [금액] *[사유]\n"   # 혈비출금
			manager_command_list += f"{','.join(commandSetting_jungsan[33])} [금액] [아이디1] [아이디2]... *[사유]\n"   # 혈비지원

			member_command_list : str = ""
			member_command_list += f"{','.join(commandSetting_jungsan[6])}\n"   # 혈원
			member_command_list += f"{','.join(commandSetting_jungsan[7])} [아이디]\n"   # 혈원등록
			member_command_list += f"{','.join(commandSetting_jungsan[8])} [아이디]\n\n"   # 혈원수정
			
			member_command_list += f"{','.join(commandSetting_jungsan[28])}\n"   # 계좌
			member_command_list += f"{','.join(commandSetting_jungsan[44])}\n"   # 창고
			member_command_list += f"{','.join(commandSetting_jungsan[11])}\n\n"   # 정산확인
			
			member_command_list += f"{','.join(commandSetting_jungsan[12])} [보스명] [아이템] [루팅자] [아이디1] [아이디2] ... (참고이미지 url)\n\n"   # 등록
			member_command_list += f"----- 등록자만 가능 -----\n"   # 등록자
			member_command_list += f"{','.join(commandSetting_jungsan[13])} (상세)\n"   # 등록확인1
			member_command_list += f"{','.join(commandSetting_jungsan[13])} (상세) (검색조건) (검색값)\n"   # 등록확인2
			member_command_list += f"{','.join(commandSetting_jungsan[14])} [보스명] [순번] [아이템] [루팅자] [아이디1] [아이디2] ...\n"   # 등록수정
			member_command_list += f"{','.join(commandSetting_jungsan[15])} [순번]\n\n"   # 등록삭제
			member_command_list += f"----- 루팅자만 가능 -----\n"   # 루팅자
			member_command_list += f"{','.join(commandSetting_jungsan[16])} (상세)\n"   # 루팅확인1
			member_command_list += f"{','.join(commandSetting_jungsan[16])} (상세) (검색조건) (검색값)\n"   # 루팅확인2
			member_command_list += f"{','.join(commandSetting_jungsan[17])} [보스명] [순번] [아이템] [루팅자] [아이디1] [아이디2] ...\n"   # 루팅수정
			member_command_list += f"{','.join(commandSetting_jungsan[18])} [순번]\n\n"   # 루팅삭제
			member_command_list += f"----- 등록자, 루팅자만 가능 -----\n"   # 등록자, 루팅자
			member_command_list += f"{','.join(commandSetting_jungsan[19])} [순번] [변경보스명]\n"   # 보스수정
			member_command_list += f"{','.join(commandSetting_jungsan[20])} [순번] [변경아이템명]\n"   # 템수정
			member_command_list += f"{','.join(commandSetting_jungsan[21])} [순번] [변경아이디]\n"   # 템수정
			member_command_list += f"{','.join(commandSetting_jungsan[22])} [순번] [추가아이디]\n"   # 참여자추가
			member_command_list += f"{','.join(commandSetting_jungsan[23])} [순번] [삭제아이디]\n"   # 참여자삭제
			member_command_list += f"{','.join(commandSetting_jungsan[50])} [순번] [수정이미지 url]\n"   # 이미지수정
			member_command_list += f"{','.join(commandSetting_jungsan[24])} [순번] [금액]\n"   # 판매
			member_command_list += f"{','.join(commandSetting_jungsan[45])} [순번] [금액] [인원]\n"   # 뽑기판매
			member_command_list += f"{','.join(commandSetting_jungsan[29])} [순번] [금액]\n"   # 저축
			member_command_list += f"{','.join(commandSetting_jungsan[48])} [순번] [금액] [인원]\n"   # 뽑기저축
			member_command_list += f"{','.join(commandSetting_jungsan[25])} [순번] [아이디]\n"   # 정산
			member_command_list += f"{','.join(commandSetting_jungsan[26])} [순번] [아이디]\n"   # 정산취소
			member_command_list += f"{','.join(commandSetting_jungsan[27])}\n"   # 일괄정산1
			member_command_list += f"{','.join(commandSetting_jungsan[27])} (검색조건) (검색값)\n"   # 일괄정산2

			etc_command_list : str = ""
			etc_command_list += f"{','.join(commandSetting_jungsan[46])}\n"   # 기본설정확인
			etc_command_list += f"{','.join(commandSetting_jungsan[37])}\n"   # 현재시간
			etc_command_list += f"{','.join(commandSetting_jungsan[38])} [변경메세지]\n"   # 상태
			etc_command_list += f"{','.join(commandSetting_jungsan[34])} [금액] (거래소세금)\n"   # 수수료
			etc_command_list += f"{','.join(commandSetting_jungsan[35])} [거래소금액] [실거래가] (거래소세금)\n"   # 페이백
			
			embed = discord.Embed(
					title = "🕹️ 분배봇 사용법",
					description= f"```득템 → 정산등록 → 판매입력 → 정산처리 → 끝!```",
					color=0xff00ff
					)
			embed.add_field(name = f"⚙️ [ 관리자 전용 명령어 ]", value = f"```css\n{admin_command_list}```", inline = False)
			embed.add_field(name = f"🤴 [ 총무 전용 명령어 ]", value = f"```css\n{manager_command_list}```", inline = False)
			embed.add_field(name = f"🧑 [ 일반 명령어 ]", value = f"```css\n{member_command_list}```", inline = False)
			embed.add_field(name = f"🔧 [ 기타 명령어 ]", value = f"```css\n{etc_command_list}```", inline = False)
			embed.set_footer(text = f"※ '분배완료'된 것 중 30일이 지난 건은 자동으로 삭제\n    '미입력' 상태의 등록건만 수정 가능\n    '분배중' 상태의 등록건만 정산 가능\n    거래소세금 : 미입력시 {basicSetting_jungsan[7]}%")
			return await ctx.send( embed=embed, tts=False)

	################ member_db초기화 ################ .
	@is_manager()
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[0][0], aliases=commandSetting_jungsan[0][1:])
	async def initialize_all_member_data(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		emoji_list : list = ["⭕", "❌"]

		delete_warning_message = await ctx.send(f"**혈원데이터를 초기화 하시면 다시는 복구할 수 없습니다. 정말로 초기화하시겠습니까?**\n**초기화 : ⭕ 취소: ❌**\n({int(basicSetting_jungsan[5])*2}초 동안 입력이 없을시 초기화가 취소됩니다.)", tts=False)
		
		for emoji in emoji_list:
			await delete_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == delete_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5])*2)
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **초기화**를 취소합니다!")

		if str(reaction) == "⭕":
			self.member_db.delete_many({})
			print(f"< 혈원데이터 초기화 완료 >")
			return await ctx.send(f"☠️ 혈원데이터 초기화 완료! ☠️")
		else:
			return await ctx.send(f"**초기화**가 취소되었습니다.\n")		

	################ jungsan_db초기화 ################
	@is_manager()
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[1][0], aliases=commandSetting_jungsan[1][1:])
	async def initialize_all_jungsan_data(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		emoji_list : list = ["⭕", "❌"]

		delete_warning_message = await ctx.send(f"**정산데이터를 초기화 하시면 다시는 복구할 수 없습니다. 정말로 초기화하시겠습니까?**\n**초기화 : ⭕ 취소: ❌**\n({int(basicSetting_jungsan[5])*2}초 동안 입력이 없을시 초기화가 취소됩니다.)", tts=False)
		
		for emoji in emoji_list:
			await delete_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == delete_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5])*2)
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **초기화**를 취소합니다!")

		if str(reaction) == "⭕":
			self.jungsan_db.delete_many({})
			print(f"< 정산데이터 초기화 완료 >")
			return await ctx.send(f"☠️ 정산데이터 초기화 완료! ☠️")
		else:
			return await ctx.send(f"**초기화**가 취소되었습니다.\n")		

	################ guild_db초기화 ################
	@is_manager()
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[2][0], aliases=commandSetting_jungsan[2][1:])
	async def initialize_all_guild_data(self, ctx):
		global basicSetting_jungsan
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		emoji_list : list = ["⭕", "❌"]

		delete_warning_message = await ctx.send(f"**혈비데이터를 초기화 하시면 다시는 복구할 수 없습니다. 정말로 초기화하시겠습니까?**\n**초기화 : ⭕ 취소: ❌**\n({int(basicSetting_jungsan[5])*2}초 동안 입력이 없을시 초기화가 취소됩니다.)", tts=False)
		
		for emoji in emoji_list:
			await delete_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == delete_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5])*2)
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **초기화**를 취소합니다!")

		if str(reaction) == "⭕":
			self.guild_db.delete_many({})
			self.guild_db_log.delete_many({})
			init_guild_data : dict = {
				"guild_money":0,
				"back_up_period":14,
				"checktime":15,
				"distributionchannel":0,
				"tax":5
				}
			update_guild_data : dict = self.guild_db.update_one({"_id":"guild"}, {"$set":init_guild_data}, upsert = True)

			basicSetting_jungsan[4] = init_guild_data['back_up_period']
			basicSetting_jungsan[5] = init_guild_data['checktime']
			basicSetting_jungsan[6] = init_guild_data['distributionchannel']
			basicSetting_jungsan[7] = init_guild_data['tax']
			
			# basicSetting_jungsan[4] = backup_period
			# basicSetting_jungsan[5] = checktime
			# basicSetting_jungsan[6] = distributionchannel
			# basicSetting_jungsan[7] = tax

			print(f"< 혈비/로그 데이터 초기화 완료 >")
			return await ctx.send(f"☠️ 혈비/로그 데이터 초기화 완료! ☠️\n**[{commandSetting_jungsan[36][0]}]** 명령어를 입력하신 후 사용해주시기 바랍니다.")
		else:
			return await ctx.send(f"**초기화**가 취소되었습니다.\n")	

	################ backup_db초기화 ################
	@is_manager()
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[3][0], aliases=commandSetting_jungsan[3][1:])
	async def initialize_all_backup_data(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		emoji_list : list = ["⭕", "❌"]

		delete_warning_message = await ctx.send(f"**백업데이터를 초기화 하시면 다시는 복구할 수 없습니다. 정말로 초기화하시겠습니까?**\n**초기화 : ⭕ 취소: ❌**\n({int(basicSetting_jungsan[5])*2}초 동안 입력이 없을시 초기화가 취소됩니다.)", tts=False)
		
		for emoji in emoji_list:
			await delete_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == delete_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5])*2)
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **초기화**를 취소합니다!")

		if str(reaction) == "⭕":
			self.backup_db.delete_many({})
			print(f"< 백업데이터 초기화 완료 >")
			return await ctx.send(f"☠️ 백업데이터 초기화 완료! ☠️")
		else:
			return await ctx.send(f"**초기화**가 취소되었습니다.\n")

	################ 혈비로그확인 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[47][0], aliases=commandSetting_jungsan[47][1:])
	async def guild_log_load(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if args:
			return await ctx.send(f"**{commandSetting_jungsan[47][0]}** 양식으로 등록 해주세요")

		result : list = []

		result = list(self.guild_db_log.find({}))

		if len(result) == 0:
			return await ctx.send(f"```혈비 로그가 없습니다!```")

		sorted_result = sorted(list([result_data['log_date'] for result_data in result]))

		log_date_list : list = []
		log_date_list = sorted(list(set([result_data['log_date'].strftime('%y-%m-%d') for result_data in result])))
		
		total_distribute_money : int = 0
		embed_list : list = []
		embed_limit_checker : int = 0
		embed_cnt : int = 0
		detail_title_info	: str = ""
		detail_info	: str = ""
		
		embed = discord.Embed(
					title = f"📜 혈비 로그",
					description = "",
					color=0x00ff00
					)
		embed_list.append(embed)
		for date in log_date_list:
			embed_limit_checker = 0
			detail_info	: str = ""
			for result_data1 in result:
				if embed_limit_checker == 50:
					embed_limit_checker = 0
					embed_cnt += 1
					tmp_embed = discord.Embed(
						title = "",
						description = "",
						color=0x00ff00
						)
					embed_list.append(tmp_embed)
				if result_data1['log_date'].strftime('%y-%m-%d') == date:
					embed_limit_checker += 1
					if result_data1['in_out_check']:
						if result_data1['reason'] != "":
							detail_info += f"+ 💰 {result_data1['money']} : {', '.join(result_data1['member_list'])} (사유:{result_data1['reason']})\n"
						else:
							detail_info += f"+ 💰 {result_data1['money']} : 혈비 입금\n"
					else:
						if result_data1['reason'] != "":
							detail_info += f"- 💰 {result_data1['money']} : {', '.join(result_data1['member_list'])} (사유:{result_data1['reason']})\n"
						else:
							detail_info += f"- 💰 {result_data1['money']} : {', '.join(result_data1['member_list'])}\n"
				
				embed_list[embed_cnt].title = f"🗓️ {date}"
				embed_list[embed_cnt].description = f"```diff\n{detail_info}```"

			if len(embed_list) > 1:
				for embed_data in embed_list:
					await asyncio.sleep(0.1)
					await ctx.send(embed = embed_data)
			else:
				await asyncio.sleep(0.1)
				await ctx.send(embed = embed)

class memberCog(commands.Cog): 
	def __init__(self, bot):
		self.bot = bot	

		self.member_db = self.bot.db.jungsan.member
		self.jungsan_db = self.bot.db.jungsan.jungsandata
		self.guild_db = self.bot.db.jungsan.guild
		self.guild_db_log = self.bot.db.jungsan.guild_log

	################ 총무등록 ################ 
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[4][0], aliases=commandSetting_jungsan[4][1:])
	async def set_manager(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"game_ID":args})

		if not member_data:
			return await ctx.send(f"**[{args}]**님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[4][0]} [아이디]** 양식으로 등록 해주세요")

		result = self.member_db.update_one({"game_ID":member_data["game_ID"]}, {"$set":{"permissions":"manager"}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 총무 등록 실패.")   

		return  await ctx.send(f"**[{args}]**님을 총무로 등록 하였습니다.")

	################ 총무삭제 ################ 
	@commands.has_permissions(manage_nicknames=True)
	@commands.command(name=commandSetting_jungsan[5][0], aliases=commandSetting_jungsan[5][1:])
	async def delete_manager(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"game_ID":args})

		if not member_data:
			return await ctx.send(f"**[{args}]**님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[5][0]} [아이디]** 양식으로 삭제 해주세요")

		result = self.member_db.update_one({"game_ID":member_data["game_ID"]}, {"$set":{"permissions":"member"}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 총무 삭제 실패.")   

		return  await ctx.send(f"**[{args}]**님을 총무에서 삭제 하였습니다.")

	################ 혈원목록 확인 ################ 
	@commands.command(name=commandSetting_jungsan[6][0], aliases=commandSetting_jungsan[6][1:])
	async def member_list(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		remain_guild_money : int = 0

		guild_data : dict = self.guild_db.find_one({"_id":"guild"})

		if not guild_data:
			remain_guild_money = 0
		else:
			remain_guild_money = guild_data["guild_money"]
			
		member_list : str = ""
		manager_list : str = ""

		member_document : list = list(self.member_db.find({}))

		sorted_member_document : dict = sorted(member_document, key=lambda member_document:member_document['account'], reverse = True)

		total_account : int = sum(member['account'] for member in sorted_member_document)

		for member_info in sorted_member_document:
			if member_info["permissions"] == "manager":
				if member_info['account'] != 0:
					manager_list += f"{member_info['game_ID']}({member_info['account']}) "
				else:
					manager_list += f"{member_info['game_ID']} "
			else:
				if member_info['account'] != 0:
					member_list += f"{member_info['game_ID']}({member_info['account']}) "
				else:
					member_list += f"{member_info['game_ID']} "

		embed = discord.Embed(
		title = "👥  혈원 목록",
		description = "",
		color=0x00ff00
		)
		if len(manager_list) == 0:
			embed.add_field(name = f"**🤴 총무**",value = f"**```cs\n등록된 총무가 없습니다.```**")
		else:
			embed.add_field(name = f"**🤴 총무**",value = f"**```cs\n{manager_list}```**")
		if len(member_list) == 0:
			embed.add_field(name = f"**🧑 혈원**",value = f"**```cs\n등록된 혈원이 없습니다.```**", inline = False)
		else:
			embed.add_field(name = f"**🧑 혈원**",value = f"**```cs\n{member_list}```**", inline = False)
		embed.add_field(name = f"**👤 혈원수**",value = f"**```fix\n{len(sorted_member_document)}```**")
		embed.add_field(name = f"**🏦 잔고**",value = f"**```fix\n{total_account}```**")
		embed.add_field(name = f"**💰 혈비**",value = f"**```fix\n{remain_guild_money}```**")
		#embed.set_footer(text = f"👑 표시는 총무!")
		return await ctx.send(embed = embed)

	################ 혈원아이디 등록 ################ 
	@commands.command(name=commandSetting_jungsan[7][0], aliases=commandSetting_jungsan[7][1:])
	async def member_add(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[7][0]} [아이디]** 양식으로 추가 해주세요")

		member_document : dict = self.member_db.find_one({ "_id":ctx.author.id})
		member_game_ID_document : dict = self.member_db.find_one({ "game_ID":args})

		if member_document:
			return await ctx.send(f"```이미 등록되어 있습니다!```")

		if member_game_ID_document:
			return await ctx.send(f"```이미 등록된 [아이디]입니다!```")

		result = self.member_db.update_one({"_id":ctx.author.id}, {"$set":{"game_ID":args, "discord_name":self.bot.get_user(ctx.author.id).display_name, "permissions":"member", "account":0}}, upsert = True)

		# "_id" : int = discord_ID
		# "game_ID" : str = game_ID
		# "discord_name" : str = discord_nickname
		# "permissiotns" : str = 권한 ["manager", "member"]
		# "account" : int = 은행잔고

		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 혈원 등록 실패.")   

		return await ctx.send(f"{ctx.author.mention}님! **[{args}] [{ctx.author.id}]**(으)로 혈원 등록 완료!")

	################ 혈원아이디 수정 ################ 
	@commands.command(name=commandSetting_jungsan[8][0], aliases=commandSetting_jungsan[8][1:])
	async def member_modify(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({ "_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[8][0]} [아이디]** 양식으로 수정 해주세요")

		jungsan_document = list(self.jungsan_db.find({"$and" : [{"$or" : [{"before_jungsan_ID" : member_data['game_ID']}, {"after_jungsan_ID" : member_data['game_ID']}, {"toggle" : member_data['game_ID']}, {"regist" : member_data['game_ID']}]}, {"$or" : [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]}))
		len_jungsan_document : int = len(jungsan_document)
		tmp_before_data : list = []
		tmp_after_data : list = []
		tmp_toggle_data : str = ""
		tmp_regist_data : str = ""
		
		if len_jungsan_document != 0:
			for jungsan_data in jungsan_document:
				if member_data['game_ID'] in jungsan_data["before_jungsan_ID"]:
					jungsan_data["before_jungsan_ID"].remove(member_data['game_ID'])
					jungsan_data["before_jungsan_ID"].append(args)
					tmp_before_data = jungsan_data["before_jungsan_ID"]
					result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":{"before_jungsan_ID":jungsan_data["before_jungsan_ID"]}}, upsert = False)
				
				if member_data['game_ID'] in jungsan_data["after_jungsan_ID"]:
					jungsan_data["after_jungsan_ID"].remove(member_data['game_ID'])
					jungsan_data["after_jungsan_ID"].append(args)
					tmp_after_data = jungsan_data["after_jungsan_ID"]
					result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":{"after_jungsan_ID":jungsan_data["after_jungsan_ID"]}}, upsert = False)
				
				if member_data['game_ID'] in jungsan_data["toggle"]:
					tmp_toggle_data = args
					result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":{"toggle":args}}, upsert = False)

				if member_data['game_ID'] in jungsan_data["regist"]:
					tmp_regist_data = args
				
				result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":{"regist":tmp_regist_data, "toggle":tmp_toggle_data,"before_jungsan_ID":tmp_before_data , "after_jungsan_ID":tmp_after_data}}, upsert = False)

		result = self.member_db.update_one({"_id":ctx.author.id}, {"$set":{"game_ID":args}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 아이디 수정 실패.")   

		return await ctx.send(f"{ctx.author.mention}님, 아이디를 **[{member_data['game_ID']}]**에서 **[{args}]**로 변경하였습니다.")

	################ 혈원아이디 등록 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[9][0], aliases=commandSetting_jungsan[9][1:])
	async def member_input_add(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[9][0]} [아이디] [디코ID]** 양식으로 추가 해주세요")

		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data < 2:
			return await ctx.send(f"**{commandSetting_jungsan[9][0]} [아이디] [디코ID]** 양식으로 추가 해주세요")

		member_document : dict = self.member_db.find_one({ "_id":input_regist_data[1]})
		member_game_ID_document : dict = self.member_db.find_one({ "game_ID":input_regist_data[0]})

		if member_document:
			return await ctx.send(f"```이미 등록되어 있습니다!```")

		if member_game_ID_document:
			return await ctx.send(f"```이미 등록된 [ 아이디 ] 입니다!```")

		result = self.member_db.update_one({"_id":int(input_regist_data[1])}, {"$set":{"game_ID":input_regist_data[0], "discord_name":self.bot.get_user(int(input_regist_data[1])).display_name, "permissions":"member", "account":0}}, upsert = True)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"**[{input_regist_data[0]}] [{input_regist_data[1]}]**(으)로 혈원 등록 실패.")   

		return await ctx.send(f"**[{input_regist_data[0]}] [{input_regist_data[1]}]**(으)로 혈원 등록 완료!")

	################ 혈원아이디 삭제 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[10][0], aliases=commandSetting_jungsan[10][1:])
	async def member_delete(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return
			
		member_data : dict = self.member_db.find_one({"game_ID":args})

		if not member_data:
			return await ctx.send(f"**[{args}]**님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[10][0]} [아이디]** 양식으로 삭제 해주세요")

		jungsan_document = list(self.jungsan_db.find({"$and" : [{"$or": [{"before_jungsan_ID" : args}, {"toggle": args}]}, {"$or": [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]}))
		len_jungsan_document : int = len(jungsan_document)
		
		if len_jungsan_document != 0:
			remain_jungsan_info : str = ""
			total_remain_money : int = 0
			for jungsan_data in jungsan_document:
				if jungsan_data["toggle"] == args:
					if jungsan_data['each_price'] != 0 and args in jungsan_data['before_jungsan_ID']:
						total_remain_money += jungsan_data['each_price']
						remain_jungsan_info += f"**[ 순번 : {jungsan_data['_id']}]** 루팅  💰 {jungsan_data['each_price']}\n"
					else:
						remain_jungsan_info += f"**[ 순번 : {jungsan_data['_id']}]** 루팅\n"
				else: 
					if jungsan_data['each_price'] != 0:
						total_remain_money += jungsan_data['each_price']
						remain_jungsan_info += f"**[ 순번 : {jungsan_data['_id']}]** 참여 💰 {jungsan_data['each_price']}\n"
					else:
						remain_jungsan_info += f"**[ 순번 : {jungsan_data['_id']}]** 참여\n"
						

			await ctx.send(f"```잔여 루팅/정산 목록이 있어 혈원을 삭제할 수 없습니다.```")
			embed = discord.Embed(
				title = "📜 잔여 루팅/정산 목록",
				description = remain_jungsan_info,
				color=0x00ff00
				)
			embed.add_field(name = "\u200b", value = f"잔여 정산 금액 : 💰 {total_remain_money}")
			return await ctx.send(embed = embed)

		result = self.member_db.delete_one({"game_ID":args})
		
		return  await ctx.send(f"**[{args}]**님을 혈원에서 삭제 하였습니다.")

class manageCog(commands.Cog): 
	def __init__(self, bot):
		self.bot = bot
		self.index_value = 0
				
		self.member_db = self.bot.db.jungsan.member
		self.jungsan_db = self.bot.db.jungsan.jungsandata
		self.guild_db = self.bot.db.jungsan.guild
		self.guild_db_log = self.bot.db.jungsan.guild_log

		try:
			self.db_index = self.jungsan_db.find().sort([("_id",-1)]).limit(1)
			self.index_value = list(self.db_index)[0]["_id"]
		except:
			pass

	################ 참여자 ################ 
	################ 참여내역 및 정산금 확인 ################ 
	@commands.command(name=commandSetting_jungsan[11][0], aliases=commandSetting_jungsan[11][1:])
	async def participant_data_check(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		jungsan_document : list = []
		if not args:
			jungsan_document = list(self.jungsan_db.find({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"$or" : [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]}))
		else:
			input_distribute_all_finish : list = args.split()
			len_input_distribute_all_finish = len(input_distribute_all_finish)

			if len_input_distribute_all_finish != 2:
				return await ctx.send(f"**{commandSetting_jungsan[11][0]} [검색조건] [검색값]** 형식으로 입력 해주세요! **[검색조건]**은 **[순번, 보스명, 아이템, 날짜, 분배상태]** 다섯가지 중 **1개**를 입력 하셔야합니다!")
			else:
				if input_distribute_all_finish[0] == "순번":
					try:
						input_distribute_all_finish[1] = int(input_distribute_all_finish[1])
					except:
						return await ctx.send(f"**[순번] [검색값]**은 \"숫자\"로 입력 해주세요!")
					jungsan_document : dict = self.jungsan_db.find_one({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"_id":input_distribute_all_finish[1]}, {"$or" : [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]})
					if not jungsan_document:
						return await ctx.send(f"{ctx.author.mention}님! 수령할 정산 내역이 없습니다.")
					embed = get_detail_embed(jungsan_document)
					try:
						return await ctx.send(embed = embed)
					except Exception:
						embed.add_field(name = "🚫  이미지 링크 확인 필요  🚫", value = f"```저장된 이미지가 삭제됐습니다.```")
						embed.set_image(url = "")
						result1 = self.jungsan_db.update_one({"_id":input_distribute_all_finish[1]}, {"$set":{"image_url":""}}, upsert = True)
						if result1.raw_result["nModified"] < 1 and "upserted" not in result1.raw_result:
							return await ctx.send(f"{ctx.author.mention}, 정산 등록 실패.") 
						return await ctx.send(embed = embed)
				elif input_distribute_all_finish[0] == "보스명":
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"boss":input_distribute_all_finish[1]}, {"$or" : [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]}))
				elif input_distribute_all_finish[0] == "아이템":
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"item":input_distribute_all_finish[1]}, {"$or" : [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]}))
				elif input_distribute_all_finish[0] == "날짜":
					try:
						start_search_date : str = (datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))).replace(year = int(input_distribute_all_finish[1][:4]), month = int(input_distribute_all_finish[1][5:7]), day = int(input_distribute_all_finish[1][8:10]), hour = 0, minute = 0, second = 0)
						end_search_date : str = start_search_date + datetime.timedelta(days = 1)
					except:
						return await ctx.send(f"**[날짜] [검색값]**은 0000-00-00 형식으로 입력 해주세요!")
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"getdate":{"$gte":start_search_date, "$lt":end_search_date}}, {"$or" : [{"itemstatus" : "분배중"}, {"itemstatus" : "미판매"}]}]}))
				elif input_distribute_all_finish[0] == "분배상태":
					if input_distribute_all_finish[1] == "분배중":
						jungsan_document = list(self.jungsan_db.find({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"itemstatus" : "분배중"}]}))
					elif input_distribute_all_finish[1] == "미판매":
						jungsan_document = list(self.jungsan_db.find({"$and" : [{"before_jungsan_ID" : member_data['game_ID']}, {"itemstatus" : "미판매"}]}))
					else:
						return await ctx.send(f"**[분배상태] [검색값]**은 \"미판매\" 혹은 \"분배중\"로 입력 해주세요!")
				else:
					return await ctx.send(f"**[검색조건]**이 잘못 됐습니다. **[검색조건]**은 **[순번, 보스명, 아이템, 날짜, 분배상태]** 다섯가지 중 **1개**를 입력 하셔야합니다!")

		if len(jungsan_document) == 0:
			return await ctx.send(f"{ctx.author.mention}님! 수령할 정산 내역이 없습니다.")

		total_money : int = 0
		toggle_list : list = []
		toggle_list = sorted(list(set([jungsan_data['toggle'] for jungsan_data in jungsan_document])))

		if "혈비" in toggle_list:
			toggle_list.remove("혈비")

		embed = discord.Embed(
				title = f"📜 [{member_data['game_ID']}]님 정산 내역",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = f"🏦 **[ 은행 ]**", value = f"**```fix\n {member_data['account']}```**")
		for game_id in toggle_list:
			each_price : int = 0
			info_cnt : int = 0
			tmp_info : list = []
			tmp_info.append("")
			for jungsan_data in jungsan_document:
				if jungsan_data['toggle'] == game_id:
					if len(tmp_info[info_cnt]) > 900:
						tmp_info.append("")
						info_cnt += 1
					if jungsan_data['itemstatus'] == "미판매":
						tmp_info[info_cnt] += f"-[순번:{jungsan_data['_id']}]|{jungsan_data['getdate'].strftime('%y-%m-%d')}|{jungsan_data['boss']}|{jungsan_data['item']}|{jungsan_data['itemstatus']}\n"
					else:
						each_price += jungsan_data['each_price']
						if jungsan_data["ladder_check"]:
							tmp_info[info_cnt] += f"+[순번:{jungsan_data['_id']}]|{jungsan_data['getdate'].strftime('%y-%m-%d')}|{jungsan_data['boss']}|{jungsan_data['item']}|🌟|💰{jungsan_data['each_price']}\n"
						else:
							tmp_info[info_cnt] += f"+[순번:{jungsan_data['_id']}]|{jungsan_data['getdate'].strftime('%y-%m-%d')}|{jungsan_data['boss']}|{jungsan_data['item']}|💰{jungsan_data['each_price']}\n"
			total_money += each_price
			if len(tmp_info) > 1:
				embed.add_field(
					name = f"[ {game_id} ]님께 받을 내역 (총 💰 {each_price} )",
					value = f"```diff\n{tmp_info[0]}```",
					inline = False
					)
				for i in range(len(tmp_info)-1):
					embed.add_field(
						name = f"\u200b",
						value = f"```diff\n{tmp_info[i+1]}```",
						inline = False
						)
			else:
				embed.add_field(
						name = f"[ {game_id} ]님께 받을 내역 (총 💰 {each_price} )",
						value = f"```diff\n{tmp_info[0]}```",
						inline = False
						)
		await ctx.send(embed = embed)
		if int(total_money) == 0:
			return
		else:
			embed1 = discord.Embed(
				title = f"총 수령 예정 금액 : 💰 {total_money}",
				description = "",
				color=0x00ff00
				)
			return await ctx.send(embed = embed1)

	################ 등록자 ################ 
	################ 분배등록 ################ 
	@commands.command(name=commandSetting_jungsan[12][0], aliases=commandSetting_jungsan[12][1:])
	async def regist_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[12][0]} [보스명] [아이템명] [루팅자] [참여자1] [참여자2]...** 양식으로 등록 해주세요")

		tmp_args : str = ""
		tmp_image_url : str = ""

		if args.find("https://") != -1:
			tmp_data = args.split("https://")
			tmp_args = tmp_data[0]
			tmp_image_url = f"https://{tmp_data[1]}"
		else:
			tmp_args = args
		
		input_regist_data : list = tmp_args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data < 4:
			return await ctx.send(f"**{commandSetting_jungsan[12][0]} [보스명] [아이템명] [루팅자] [참여자1] [참여자2]...** 양식으로 등록 해주세요")

		check_member_data : list = []
		check_member_list : list = []
		wrong_input_id : list = []
		gulid_money_insert_check : bool = False
		loot_member_data : dict = {}

		if input_regist_data[2] == "혈비":
			gulid_money_insert_check = True
			loot_member_data = {"_id":ctx.author.id}
		else:
			gulid_money_insert_check = False
			loot_member_data = self.member_db.find_one({"game_ID":input_regist_data[2]})
			if not loot_member_data:
				wrong_input_id.append(f"💥{input_regist_data[2]}")
				#return await ctx.send(f"```루팅자 [{input_regist_data[2]}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			check_member_list.append(game_id['game_ID'])

		for game_id in input_regist_data[3:]:
			if game_id not in check_member_list:
				wrong_input_id.append(game_id)

		if len(wrong_input_id) > 0:
			return await ctx.send(f"```[{', '.join(wrong_input_id)}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")
		
		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = {"regist_ID":str(ctx.author.id),
					"regist":member_data["game_ID"],
					"getdate":input_time,
					"boss":input_regist_data[0],
					"item":input_regist_data[1],
					"toggle":input_regist_data[2],
					"toggle_ID":str(loot_member_data["_id"]),
					"itemstatus":"미판매",
					"price":0,
					"each_price":0,
					"before_jungsan_ID":list(set(input_regist_data[3:])),
					"after_jungsan_ID":[],
					"modifydate":input_time,
					"gulid_money_insert":gulid_money_insert_check,
					"bank_money_insert":False,
					"ladder_check":False,
					"image_url":tmp_image_url
					}
		
		# "_id" : int = 순번
		# "regist_ID" : str = 등록자ID
		# "regist" : str = 등록자 겜 ID
		# "getdate" : datetime = 등록날짜
		# "boss" : str = 보스명
		# "item" : str = 아이템명
		# "toggle" : str = 루팅자 게임 ID
		# "toggle_ID" : str = 루팅자ID
		# "itemstatus" : str = 아이템상태(미판매, 분배중, 분배완료)
		# "price" : int = 가격
		# "each_price" : int = 분배가격
		# "before_jungsan_ID" : list = 참석명단(분배전)
		# "after_jungsan_ID" : list = 참석명단(분배후)
		# "modifydate" : datetime = 수정날짜
		# "gulid_money_insert" : bool = 혈비등록여부
		# "bank_money_insert" : bool = 은행입금여부
		# "ladder_check":False
		# "image_url":이미지 url

		embed = discord.Embed(
				title = "📜 등록 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 일시 ]", value = f"```{insert_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{insert_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{insert_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{insert_data['toggle']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(insert_data['before_jungsan_ID'])}```")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 등록 내역을 확인해 보세요!**\n**등록 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 등록이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]

		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **등록**를 취소합니다!")

		if str(reaction) == "⭕":
			self.index_value += 1
			result = self.jungsan_db.update_one({"_id":self.index_value}, {"$set":insert_data}, upsert = True)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 실패.") 

			return await ctx.send(f"📥 **[ 순번 : {self.index_value} ]** 정산 등록 완료! 📥")
		else:
			return await ctx.send(f"**등록**이 취소되었습니다.\n")

	################ 전체내역확인 ################ 
	@is_manager()
	@commands.command(name=commandSetting_jungsan[43][0], aliases=commandSetting_jungsan[43][1:])
	async def all_distribute_check(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		visual_flag : int = 0

		jungsan_document : list = []
		if not args:
			jungsan_document : list = list(self.jungsan_db.find({}))
		else:
			input_distribute_all_finish : list = args.split()
			
			if input_distribute_all_finish[0] == "상세":
				visual_flag = 1
				del(input_distribute_all_finish[0])
			
			len_input_distribute_all_finish = len(input_distribute_all_finish)

			if len_input_distribute_all_finish == 0:
				jungsan_document : list = list(self.jungsan_db.find({}))
			elif len_input_distribute_all_finish != 2:
				return await ctx.send(f"**{commandSetting_jungsan[43][0]} (상세) [검색조건] [검색값]** 형식으로 입력 해주세요! **[검색조건]**은 **[순번, 보스명, 아이템, 루팅, 등록, 날짜, 분배상태]** 일곱가지 중 **1개**를 입력 하셔야합니다!")
			else:
				if input_distribute_all_finish[0] == "순번":
					try:
						input_distribute_all_finish[1] = int(input_distribute_all_finish[1])
					except:
						return await ctx.send(f"**[순번] [검색값]**은 \"숫자\"로 입력 해주세요!")
					jungsan_document : dict = self.jungsan_db.find_one({"_id":input_distribute_all_finish[1]})
					if not jungsan_document:
						return await ctx.send(f"{ctx.author.mention}님! 등록된 정산 목록이 없습니다.")
					embed = get_detail_embed(jungsan_document)
					try:
						return await ctx.send(embed = embed)
					except Exception:
						embed.add_field(name = "🚫  이미지 링크 확인 필요  🚫", value = f"```저장된 이미지가 삭제됐습니다.```")
						embed.set_image(url = "")
						result1 = self.jungsan_db.update_one({"_id":input_distribute_all_finish[1]}, {"$set":{"image_url":""}}, upsert = True)
						if result1.raw_result["nModified"] < 1 and "upserted" not in result1.raw_result:
							return await ctx.send(f"{ctx.author.mention}, 정산 등록 실패.") 
						return await ctx.send(embed = embed)
				elif input_distribute_all_finish[0] == "보스명":
					jungsan_document : list = list(self.jungsan_db.find({"boss":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "아이템":
					jungsan_document : list = list(self.jungsan_db.find({"item":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "루팅":
					jungsan_document : list = list(self.jungsan_db.find({"toggle":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "등록":
					jungsan_document : list = list(self.jungsan_db.find({"regist":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "날짜":
					try:
						start_search_date : str = datetime.datetime.now().replace(year = int(input_distribute_all_finish[1][:4]), month = int(input_distribute_all_finish[1][5:7]), day = int(input_distribute_all_finish[1][8:10]), hour = 0, minute = 0, second = 0)
						end_search_date : str = start_search_date + datetime.timedelta(days = 1)
					except:
						return await ctx.send(f"**[날짜] [검색값]**은 0000-00-00 형식으로 입력 해주세요!")
					jungsan_document : list = list(self.jungsan_db.find({"getdate":{"$gte":start_search_date, "$lt":end_search_date}}))
				elif input_distribute_all_finish[0] == "분배상태":
					if input_distribute_all_finish[1] == "분배중":
						jungsan_document : list = list(self.jungsan_db.find({"itemstatus" : "분배중"}))
					elif input_distribute_all_finish[1] == "미판매":
						jungsan_document : list = list(self.jungsan_db.find({"itemstatus" : "미판매"}))
					else:
						return await ctx.send(f"**[분배상태] [검색값]**은 \"미판매\" 혹은 \"분배중\"로 입력 해주세요!")
				else:
					return await ctx.send(f"**[검색조건]**이 잘못 됐습니다. **[검색조건]**은 **[순번, 보스명, 아이템, 루팅, 등록, 날짜, 분배상태]** 일곱가지 중 **1개**를 입력 하셔야합니다!")
		
		if len(jungsan_document) == 0:
			return await ctx.send(f"{ctx.author.mention}님! 등록된 정산 목록이 없습니다.")

		total_distribute_money : int = 0
		embed_list : list = []
		embed_limit_checker : int = 0
		embed_cnt : int = 0
		detail_title_info	: str = ""
		detail_info	: str = ""
		
		embed = discord.Embed(
					title = f"📜 [{member_data['game_ID']}]님 등록 내역",
					description = "",
					color=0x00ff00
					)
		embed_list.append(embed)
		for jungsan_data in jungsan_document:
			embed_limit_checker += 1
			if embed_limit_checker == 20:
				embed_limit_checker = 0
				embed_cnt += 1
				tmp_embed = discord.Embed(
					title = "",
					description = "",
					color=0x00ff00
					)
				embed_list.append(tmp_embed)

			if jungsan_data['gulid_money_insert']:
				if jungsan_data['itemstatus'] == "미판매":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 혈비적립예정\n[ 등록자 : {jungsan_data['regist']} ]"
					detail_info = f"```fix\n[ 혈비적립 ]```"
				else:
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 혈비적립완료\n[ 등록자 : {jungsan_data['regist']} ]"
					detail_info = f"~~```fix\n[ 혈비적립 ]```~~"
			elif jungsan_data['bank_money_insert']:
				detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 은행저축완료\n[ 등록자 : {jungsan_data['regist']} ]"
				detail_info = f"~~```fix\n[ 은행저축 ]```~~"
			else:
				if jungsan_data['itemstatus'] == "분배중":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} : 1인당 💰{jungsan_data['each_price']}\n[ 등록자 : {jungsan_data['regist']} ]"
					if visual_flag == 0:
						detail_info = f"```fix\n[ 분배중 ] : {len(jungsan_data['before_jungsan_ID'])}명   [ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명```"
					else:
						detail_info = f"```diff\n+ 분 배 중 : {len(jungsan_data['before_jungsan_ID'])}명 (💰{len(jungsan_data['before_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['before_jungsan_ID'])}\n- 분배완료 : {len(jungsan_data['after_jungsan_ID'])}명  (💰{len(jungsan_data['after_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['after_jungsan_ID'])}```"
					total_distribute_money += len(jungsan_data['before_jungsan_ID'])*int(jungsan_data['each_price'])
				elif jungsan_data['itemstatus'] == "미판매":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']}\n[ 등록자 : {jungsan_data['regist']} ]"
					if visual_flag == 0:
						detail_info = f"```ini\n[ 참여자 ] : {len(jungsan_data['before_jungsan_ID'])}명```"
					else:
						detail_info = f"```ini\n[ 참여자 ] : {len(jungsan_data['before_jungsan_ID'])}명\n{', '.join(jungsan_data['before_jungsan_ID'])}```"
				else:
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} | 💰~~{jungsan_data['price']}~~\n[ 등록자 : {jungsan_data['regist']} ]"
					if visual_flag == 0:
						detail_info = f"~~```yaml\n[ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명```~~"
					else:
						detail_info = f"~~```yaml\n[ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명\n{', '.join(jungsan_data['after_jungsan_ID'])}```~~"

			if 'image_url' in jungsan_data.keys():
				if jungsan_data['image_url'] != "":
					detail_title_info += " 📸"
			
			if jungsan_data['ladder_check']:
				detail_title_info += " 🌟"

			embed_list[embed_cnt].add_field(name = detail_title_info,
							value = detail_info,
							inline = False)

		if len(embed_list) > 1:
			for embed_data in embed_list:
				await asyncio.sleep(0.1)
				await ctx.send(embed = embed_data)
		else:
			await ctx.send(embed = embed)

		embed1 = discord.Embed(
			title = f"총 정산 금액 : 💰 {str(total_distribute_money)}",
			description = "",
			color=0x00ff00
			)
		return await ctx.send(embed = embed1)

	################ 등록내역확인 ################ 
	@commands.command(name=commandSetting_jungsan[13][0], aliases=commandSetting_jungsan[13][1:])
	async def distribute_check(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		visual_flag : int = 0

		jungsan_document : list = []
		if not args:
			jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id)}))
		else:
			input_distribute_all_finish : list = args.split()
			
			if input_distribute_all_finish[0] == "상세":
				visual_flag = 1
				del(input_distribute_all_finish[0])
			
			len_input_distribute_all_finish = len(input_distribute_all_finish)

			if len_input_distribute_all_finish == 0:
				jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id)}))
			elif len_input_distribute_all_finish != 2:
				return await ctx.send(f"**{commandSetting_jungsan[13][0]} (상세) [검색조건] [검색값]** 형식으로 입력 해주세요! **[검색조건]**은 **[순번, 보스명, 아이템, 날짜, 분배상태]** 다섯가지 중 **1개**를 입력 하셔야합니다!")
			else:
				if input_distribute_all_finish[0] == "순번":
					try:
						input_distribute_all_finish[1] = int(input_distribute_all_finish[1])
					except:
						return await ctx.send(f"**[순번] [검색값]**은 \"숫자\"로 입력 해주세요!")
					jungsan_document : dict = self.jungsan_db.find_one({"regist_ID":str(ctx.author.id), "_id":input_distribute_all_finish[1]})
					if not jungsan_document:
						return await ctx.send(f"{ctx.author.mention}님! 등록된 정산 목록이 없습니다.")
					embed = get_detail_embed(jungsan_document)
					try:
						return await ctx.send(embed = embed)
					except Exception:
						embed.add_field(name = "🚫  이미지 링크 확인 필요  🚫", value = f"```저장된 이미지가 삭제됐습니다.```")
						embed.set_image(url = "")
						result1 = self.jungsan_db.update_one({"_id":input_distribute_all_finish[1]}, {"$set":{"image_url":""}}, upsert = True)
						if result1.raw_result["nModified"] < 1 and "upserted" not in result1.raw_result:
							return await ctx.send(f"{ctx.author.mention}, 정산 등록 실패.") 
						return await ctx.send(embed = embed)
				elif input_distribute_all_finish[0] == "보스명":
					jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id), "boss":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "아이템":
					jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id), "item":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "날짜":
					try:
						start_search_date : str = (datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))).replace(year = int(input_distribute_all_finish[1][:4]), month = int(input_distribute_all_finish[1][5:7]), day = int(input_distribute_all_finish[1][8:10]), hour = 0, minute = 0, second = 0)
						end_search_date : str = start_search_date + datetime.timedelta(days = 1)
					except:
						return await ctx.send(f"**[날짜] [검색값]**은 0000-00-00 형식으로 입력 해주세요!")
					jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id), "getdate":{"$gte":start_search_date, "$lt":end_search_date}}))
				elif input_distribute_all_finish[0] == "분배상태":
					if input_distribute_all_finish[1] == "분배중":
						jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id), "itemstatus" : "분배중"}))
					elif input_distribute_all_finish[1] == "미판매":
						jungsan_document : list = list(self.jungsan_db.find({"regist_ID":str(ctx.author.id), "itemstatus" : "미판매"}))
					else:
						return await ctx.send(f"**[분배상태] [검색값]**은 \"미판매\" 혹은 \"분배중\"로 입력 해주세요!")
				else:
					return await ctx.send(f"**[검색조건]**이 잘못 됐습니다. **[검색조건]**은 **[순번, 보스명, 아이템, 날짜, 분배상태]** 다섯가지 중 **1개**를 입력 하셔야합니다!")
		
		if len(jungsan_document) == 0:
			return await ctx.send(f"{ctx.author.mention}님! 등록된 정산 목록이 없습니다.")

		total_distribute_money : int = 0
		embed_list : list = []
		embed_limit_checker : int = 0
		embed_cnt : int = 0
		detail_title_info	: str = ""
		detail_info	: str = ""
		
		embed = discord.Embed(
					title = f"📜 [{member_data['game_ID']}]님 등록 내역",
					description = "",
					color=0x00ff00
					)
		embed_list.append(embed)
		for jungsan_data in jungsan_document:
			embed_limit_checker += 1
			if embed_limit_checker == 20:
				embed_limit_checker = 0
				embed_cnt += 1
				tmp_embed = discord.Embed(
					title = "",
					description = "",
					color=0x00ff00
					)
				embed_list.append(tmp_embed)

			if jungsan_data['gulid_money_insert']:
				if jungsan_data['itemstatus'] == "미판매":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 혈비적립예정"
					detail_info = f"```fix\n[ 혈비적립 ]```"
				else:
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 혈비적립완료"
					detail_info = f"~~```fix\n[ 혈비적립 ]```~~"
			elif jungsan_data['bank_money_insert']:
				detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 은행저축완료"
				detail_info = f"~~```fix\n[ 은행저축 ]```~~"
			else:
				if jungsan_data['itemstatus'] == "분배중":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} : 1인당 💰{jungsan_data['each_price']}"
					if visual_flag == 0:
						detail_info = f"```fix\n[ 분배중 ] : {len(jungsan_data['before_jungsan_ID'])}명   [ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명```"
					else:
						detail_info = f"```diff\n+ 분 배 중 : {len(jungsan_data['before_jungsan_ID'])}명 (💰{len(jungsan_data['before_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['before_jungsan_ID'])}\n- 분배완료 : {len(jungsan_data['after_jungsan_ID'])}명  (💰{len(jungsan_data['after_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['after_jungsan_ID'])}```"
					total_distribute_money += len(jungsan_data['before_jungsan_ID'])*int(jungsan_data['each_price'])
				elif jungsan_data['itemstatus'] == "미판매":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']}"
					if visual_flag == 0:
						detail_info = f"```ini\n[ 참여자 ] : {len(jungsan_data['before_jungsan_ID'])}명```"
					else:
						detail_info = f"```ini\n[ 참여자 ] : {len(jungsan_data['before_jungsan_ID'])}명\n{', '.join(jungsan_data['before_jungsan_ID'])}```"
				else:
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} | 💰~~{jungsan_data['price']}~~"
					if visual_flag == 0:
						detail_info = f"~~```yaml\n[ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명```~~"
					else:
						detail_info = f"~~```yaml\n[ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명\n{', '.join(jungsan_data['after_jungsan_ID'])}```~~"

			if 'image_url' in jungsan_data.keys():
				if jungsan_data['image_url'] != "":
					detail_title_info += " 📸"
			
			if jungsan_data['ladder_check']:
				detail_title_info += " 🌟"

			embed_list[embed_cnt].add_field(name = detail_title_info,
							value = detail_info,
							inline = False)

		if len(embed_list) > 1:
			for embed_data in embed_list:
				await asyncio.sleep(0.1)
				await ctx.send(embed = embed_data)
		else:
			await ctx.send(embed = embed)

		embed1 = discord.Embed(
			title = f"총 정산 금액 : 💰 {str(total_distribute_money)}",
			description = "",
			color=0x00ff00
			)
		return await ctx.send(embed = embed1)

	################ 등록내역수정 ################ 
	@commands.command(name=commandSetting_jungsan[14][0], aliases=commandSetting_jungsan[14][1:])
	async def modify_regist_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[14][0]} [순번] [보스명] [아이템명] [루팅자] [참여자1] [참여자2]...** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data < 5:
			return await ctx.send(f"**{commandSetting_jungsan[14][0]} [순번] [보스명] [아이템명] [루팅자] [참여자1] [참여자2]...** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"_id":int(input_regist_data[0]), "regist_ID":str(member_data['_id']), "itemstatus":"미판매"})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		del(input_regist_data[0])

		check_member_data : list = []
		check_member_list : list = []
		check_member_id_list : list = []
		wrong_input_id : list = []
		gulid_money_insert_check : bool = False
		loot_member_data : dict = {}

		if input_regist_data[2] == "혈비":
			gulid_money_insert_check = True
			loot_member_data["_id"] = ctx.author.id
		else:
			gulid_money_insert_check = False
			loot_member_data = self.member_db.find_one({"game_ID":input_regist_data[2]})
			if not loot_member_data:
				wrong_input_id.append(f"💥{input_regist_data[2]}")
				#return await ctx.send(f"```루팅자 [{input_regist_data[2]}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			check_member_list.append(game_id['game_ID'])
			if game_id['game_ID'] == input_regist_data[2]:
				loot_member_data["_id"] = game_id['_id']

		for game_id in input_regist_data[3:]:
			if game_id not in check_member_list:
				wrong_input_id.append(game_id)
		
		if len(wrong_input_id) > 0:
			return await ctx.send(f"```[{', '.join(wrong_input_id)}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")
		
		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["boss"] = input_regist_data[0]
		insert_data["item"] = input_regist_data[1]
		insert_data["toggle"] = input_regist_data[2]
		insert_data["toggle_ID"] = str(loot_member_data["_id"])
		insert_data["before_jungsan_ID"] = list(set(input_regist_data[3:]))
		insert_data["modifydate"] = input_time
		insert_data["gulid_money_insert"] = gulid_money_insert_check
		
		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		if jungsan_data['boss'] == insert_data['boss']:
			embed.add_field(name = "[ 보스 ]", value = f"```{insert_data['boss']}```")
		else:
			embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']} → {insert_data['boss']}```")
		if jungsan_data['item'] == insert_data['item']:
			embed.add_field(name = "[ 아이템 ]", value = f"```{insert_data['item']}```")
		else:
			embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']} → {insert_data['item']}```")
		if jungsan_data['toggle'] == insert_data['toggle']:
			embed.add_field(name = "[ 루팅 ]", value = f"```{insert_data['toggle']}```")
		else:
			embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']} → {insert_data['toggle']}```")
		if jungsan_data['before_jungsan_ID'] == insert_data['before_jungsan_ID']:
			embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(insert_data['before_jungsan_ID'])}```")
		else:
			embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])} → {', '.join(insert_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 등록삭제 ################ 
	@commands.command(name=commandSetting_jungsan[15][0], aliases=commandSetting_jungsan[15][1:])
	async def distribute_delete(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[15][0]} [순번]** 양식으로 확인 해주세요")

		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"regist_ID":str(ctx.author.id)}, {"_id":int(args)}, {"$or" : [{"itemstatus" : "분배완료"}, {"itemstatus" : "미판매"}]}]})

		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 분배중 ]**이거나 없습니다. **[ {commandSetting_jungsan[13][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 삭제는 **[ 분배상태 ]**가 **[ 미판매/분배완료 ]** 인 등록건만 수정 가능합니다!")
		
		embed = discord.Embed(
					title = "⚠️☠️⚠️ 삭제 내역 ⚠️☠️⚠️",
					description = "",
					color=0x00ff00
					)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID']+jungsan_data['after_jungsan_ID'])}```")
		await ctx.send(embed = embed)
		
		delete_warning_message = await ctx.send(f"**등록 내역을 삭제하시면 다시는 복구할 수 없습니다. 정말로 삭제하시겠습니까?**\n**삭제 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 삭제가 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await delete_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == delete_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **삭제**를 취소합니다!")

		if str(reaction) == "⭕":
			self.jungsan_db.delete_one({"_id":int(args)})
			return await ctx.send(f"☠️ 정산 내역 삭제 완료! ☠️")
		else:
			return await ctx.send(f"**삭제**가 취소되었습니다.\n")

	################ 루팅자 ################ 
	@commands.command(name=commandSetting_jungsan[16][0], aliases=commandSetting_jungsan[16][1:])
	async def loot_distribute_check(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		visual_flag : int = 0

		jungsan_document : list = []
		if not args:
			jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id)}))
		else:
			input_distribute_all_finish : list = args.split()
			
			if input_distribute_all_finish[0] == "상세":
				visual_flag = 1
				del(input_distribute_all_finish[0])
			
			len_input_distribute_all_finish = len(input_distribute_all_finish)

			if len_input_distribute_all_finish == 0:
				jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id)}))
			elif len_input_distribute_all_finish != 2:
				return await ctx.send(f"**{commandSetting_jungsan[16][0]} (상세) [검색조건] [검색값]** 형식으로 입력 해주세요! **[검색조건]**은 **[순번, 보스명, 아이템, 날짜, 분배상태]** 다섯가지 중 **1개**를 입력 하셔야합니다!")
			else:
				if input_distribute_all_finish[0] == "순번":
					try:
						input_distribute_all_finish[1] = int(input_distribute_all_finish[1])
					except:
						return await ctx.send(f"**[순번] [검색값]**은 \"숫자\"로 입력 해주세요!")
					jungsan_document : dict = self.jungsan_db.find_one({"toggle_ID":str(ctx.author.id), "_id":input_distribute_all_finish[1]})
					if not jungsan_document:
						return await ctx.send(f"{ctx.author.mention}님! 등록된 정산 목록이 없습니다.")
					embed = get_detail_embed(jungsan_document)
					try:
						return await ctx.send(embed = embed)
					except Exception:
						embed.add_field(name = "🚫  이미지 링크 확인 필요  🚫", value = f"```저장된 이미지가 삭제됐습니다.```")
						embed.set_image(url = "")
						result1 = self.jungsan_db.update_one({"_id":input_distribute_all_finish[1]}, {"$set":{"image_url":""}}, upsert = True)
						if result1.raw_result["nModified"] < 1 and "upserted" not in result1.raw_result:
							return await ctx.send(f"{ctx.author.mention}, 정산 등록 실패.") 
						return await ctx.send(embed = embed)
				elif input_distribute_all_finish[0] == "보스명":
					jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id), "boss":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "아이템":
					jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id), "item":input_distribute_all_finish[1]}))
				elif input_distribute_all_finish[0] == "날짜":
					try:
						start_search_date : str = (datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))).replace(year = int(input_distribute_all_finish[1][:4]), month = int(input_distribute_all_finish[1][5:7]), day = int(input_distribute_all_finish[1][8:10]), hour = 0, minute = 0, second = 0)
						end_search_date : str = start_search_date + datetime.timedelta(days = 1)
					except:
						return await ctx.send(f"**[날짜] [검색값]**은 0000-00-00 형식으로 입력 해주세요!")
					jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id), "getdate":{"$gte":start_search_date, "$lt":end_search_date}}))
				elif input_distribute_all_finish[0] == "분배상태":
					if input_distribute_all_finish[1] == "분배중":
						jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id), "itemstatus" : "분배중"}))
					elif input_distribute_all_finish[1] == "미판매":
						jungsan_document : list = list(self.jungsan_db.find({"toggle_ID":str(ctx.author.id), "itemstatus" : "미판매"}))
					else:
						return await ctx.send(f"**[분배상태] [검색값]**은 \"미판매\" 혹은 \"분배중\"로 입력 해주세요!")
				else:
					return await ctx.send(f"**[검색조건]**이 잘못 됐습니다. **[검색조건]**은 **[순번, 보스명, 아이템, 날짜, 분배상태]** 다섯가지 중 **1개**를 입력 하셔야합니다!")
		
		if len(jungsan_document) == 0:
			return await ctx.send(f"{ctx.author.mention}님! 루팅한 정산 목록이 없습니다.")

		total_distribute_money : int = 0
		embed_list : list = []
		embed_limit_checker : int = 0
		embed_cnt : int = 0
		detail_title_info	: str = ""
		detail_info	: str = ""
		
		embed = discord.Embed(
					title = f"📜 [{member_data['game_ID']}]님 루팅 내역",
					description = "",
					color=0x00ff00
					)
		embed_list.append(embed)
		for jungsan_data in jungsan_document:
			embed_limit_checker += 1
			if embed_limit_checker == 20:
				embed_limit_checker = 0
				embed_cnt += 1
				tmp_embed = discord.Embed(
					title = "",
					description = "",
					color=0x00ff00
					)
				embed_list.append(tmp_embed)
			
			if jungsan_data['gulid_money_insert']:
				if jungsan_data['itemstatus'] == "미판매":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 혈비적립예정"
					detail_info = f"```fix\n[ 혈비적립 ]```"
				else:
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 혈비적립완료"
					detail_info = f"~~```fix\n[ 혈비적립 ]```~~"
			elif jungsan_data['bank_money_insert']:
				detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | 은행저축"
				detail_info = f"```fix\n[ 은행저축 ]```"
			else:			
				if jungsan_data['itemstatus'] == "분배중":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} : 1인당 💰{jungsan_data['each_price']}"
					if visual_flag == 0:
						detail_info = f"```fix\n[ 분배중 ] : {len(jungsan_data['before_jungsan_ID'])}명   [ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명```"
					else:
						detail_info = f"```diff\n+ 분 배 중 : {len(jungsan_data['before_jungsan_ID'])}명 (💰{len(jungsan_data['before_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['before_jungsan_ID'])}\n- 분배완료 : {len(jungsan_data['after_jungsan_ID'])}명  (💰{len(jungsan_data['after_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['after_jungsan_ID'])}```"
					total_distribute_money += len(jungsan_data['before_jungsan_ID'])*int(jungsan_data['each_price'])
				elif jungsan_data['itemstatus'] == "미판매":
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']}"
					if visual_flag == 0:
						detail_info = f"```ini\n[ 참여자 ] : {len(jungsan_data['before_jungsan_ID'])}명```"
					else:
						detail_info = f"```ini\n[ 참여자 ] : {len(jungsan_data['before_jungsan_ID'])}명\n{', '.join(jungsan_data['before_jungsan_ID'])}```"
				else:
					detail_title_info = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} | 💰~~{jungsan_data['price']}~~"
					if visual_flag == 0:
						detail_info = f"~~```yaml\n[ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명```~~"
					else:
						detail_info = f"~~```yaml\n[ 분배완료 ] : {len(jungsan_data['after_jungsan_ID'])}명\n{', '.join(jungsan_data['after_jungsan_ID'])}```~~"

			if 'image_url' in jungsan_data.keys():
				if jungsan_data['image_url'] != "":
					detail_title_info += " 📸"
			
			if jungsan_data['ladder_check']:
				detail_title_info += " 🌟"

			embed_list[embed_cnt].add_field(name = detail_title_info,
							value = detail_info,
							inline = False)

		if len(embed_list) > 1:
			for embed_data in embed_list:
				await asyncio.sleep(0.1)
				await ctx.send(embed = embed_data)
		else:
			await ctx.send(embed = embed)

		embed1 = discord.Embed(
			title = f"총 정산 금액 : 💰 {str(total_distribute_money)}",
			description = "",
			color=0x00ff00
			)
		return await ctx.send(embed = embed1)

	################ 루팅내역수정 ################ 
	@commands.command(name=commandSetting_jungsan[17][0], aliases=commandSetting_jungsan[17][1:])
	async def loot_modify_regist_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[17][0]} [순번] [보스명] [아이템명] [루팅자] [참여자1] [참여자2]...** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data < 5:
			return await ctx.send(f"**{commandSetting_jungsan[17][0]} [순번] [보스명] [아이템명] [루팅자] [참여자1] [참여자2]...** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"_id":int(input_regist_data[0]), "toggle_ID":str(member_data['_id']), "itemstatus":"미판매"})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 루팅하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 루팅건만 수정 가능합니다!")

		del(input_regist_data[0])

		check_member_data : list = []
		check_member_list : list = []
		check_member_id_list : list = []
		wrong_input_id : list = []
		gulid_money_insert_check : bool = False
		loot_member_data : dict = {}

		if input_regist_data[2] == "혈비":
			gulid_money_insert_check = True
			loot_member_data["_id"] = ctx.author.id
		else:
			gulid_money_insert_check = False
			loot_member_data = self.member_db.find_one({"game_ID":input_regist_data[2]})
			if not loot_member_data:
				wrong_input_id.append(f"💥{input_regist_data[2]}")
				#return await ctx.send(f"```루팅자 [{input_regist_data[2]}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			check_member_list.append(game_id['game_ID'])
			if game_id['game_ID'] == input_regist_data[2]:
				loot_member_data["_id"] = game_id['_id']

		for game_id in input_regist_data[3:]:
			if game_id not in check_member_list:
				wrong_input_id.append(game_id)

		if len(wrong_input_id) > 0:
			return await ctx.send(f"```[{', '.join(wrong_input_id)}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")
		
		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["boss"] = input_regist_data[0]
		insert_data["item"] = input_regist_data[1]
		insert_data["toggle"] = input_regist_data[2]
		insert_data["toggle_ID"] = str(loot_member_data["_id"])
		insert_data["before_jungsan_ID"] = list(set(input_regist_data[3:]))
		insert_data["modifydate"] = input_time
		insert_data["gulid_money_insert"] = gulid_money_insert_check
		
		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		if jungsan_data['boss'] == insert_data['boss']:
			embed.add_field(name = "[ 보스 ]", value = f"```{insert_data['boss']}```")
		else:
			embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']} → {insert_data['boss']}```")
		if jungsan_data['item'] == insert_data['item']:
			embed.add_field(name = "[ 아이템 ]", value = f"```{insert_data['item']}```")
		else:
			embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']} → {insert_data['item']}```")
		if jungsan_data['toggle'] == insert_data['toggle']:
			embed.add_field(name = "[ 루팅 ]", value = f"```{insert_data['toggle']}```")
		else:
			embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']} → {insert_data['toggle']}```")
		if jungsan_data['before_jungsan_ID'] == insert_data['before_jungsan_ID']:
			embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(insert_data['before_jungsan_ID'])}```")
		else:
			embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])} → {', '.join(insert_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = True)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 루팅삭제 ################ 
	@commands.command(name=commandSetting_jungsan[18][0], aliases=commandSetting_jungsan[18][1:])
	async def loot_distribute_delete(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[18][0]} [순번]** 양식으로 확인 해주세요")

		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"toggle_ID":str(ctx.author.id)}, {"_id":int(args)}, {"$or" : [{"itemstatus" : "분배완료"}, {"itemstatus" : "미판매"}]}]})

		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 분배중 ]**이거나 없습니다. **[ {commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 삭제는 **[ 분배상태 ]**가 **[ 미판매/분배완료 ]** 인 등록건만 수정 가능합니다!")
		
		embed = discord.Embed(
					title = "⚠️☠️⚠️ 삭제 내역 ⚠️☠️⚠️",
					description = "",
					color=0x00ff00
					)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID']+jungsan_data['after_jungsan_ID'])}```")
		await ctx.send(embed = embed)
		
		delete_warning_message = await ctx.send(f"**정산 내역을 삭제하시면 다시는 복구할 수 없습니다. 정말로 삭제하시겠습니까?**\n**삭제 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 삭제가 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await delete_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == delete_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **삭제**를 취소합니다!")

		if str(reaction) == "⭕":
			self.jungsan_db.delete_one({"_id":int(args)})
			return await ctx.send(f"☠️ 정산 내역 삭제 완료! ☠️")
		else:
			return await ctx.send(f"**삭제**가 취소되었습니다.\n")

	################ 보스수정 ################ 
	@commands.command(name=commandSetting_jungsan[19][0], aliases=commandSetting_jungsan[19][1:])
	async def modify_regist_boss_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[19][0]} [순번] [보스명]** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[19][0]} [순번] [보스명]** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_regist_data[0])}, {"itemstatus":"미판매"}]})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]}/{commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		if jungsan_data['boss'] == input_regist_data[1]:
			return await ctx.send(f"```수정하려는 [보스명:{input_regist_data[1]}](이)가 등록된 [보스명]과 같습니다!```")
		
		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["boss"] = input_regist_data[1]
		insert_data["modifydate"] = input_time
		
		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']} → {insert_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 템수정 ################ 
	@commands.command(name=commandSetting_jungsan[20][0], aliases=commandSetting_jungsan[20][1:])
	async def modify_regist_item_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[20][0]} [순번] [아이템명]** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[20][0]} [순번] [아이템명]** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_regist_data[0])}, {"itemstatus":"미판매"}]})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]}/{commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		if jungsan_data['item'] == input_regist_data[1]:
			return await ctx.send(f"```수정하려는 [아이템명:{input_regist_data[1]}](이)가 등록된 [아이템명]과 같습니다!```")
		
		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["item"] = input_regist_data[1]
		insert_data["modifydate"] = input_time
		
		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']} → {insert_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 토글수정 ################ 
	@commands.command(name=commandSetting_jungsan[21][0], aliases=commandSetting_jungsan[21][1:])
	async def modify_regist_toggle_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[21][0]} [순번] [아이디]** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[21][0]} [순번] [아이디]** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_regist_data[0])}, {"itemstatus":"미판매"}]})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]}/{commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		if jungsan_data['toggle'] == input_regist_data[1]:
			return await ctx.send(f"```수정하려는 [토글자:{input_regist_data[1]}](이)가 등록된 [토글자]과 같습니다!```")

		check_member_data : list = []
		gulid_money_insert_check : bool = False
		loot_member_data : dict = {}

		if input_regist_data[1] == "혈비":
			gulid_money_insert_check = True
			loot_member_data["_id"] = ctx.author.id
		else:
			gulid_money_insert_check = False
			loot_member_data = self.member_db.find_one({"game_ID":input_regist_data[1]})
			if not loot_member_data:
				return await ctx.send(f"```루팅자 [{input_regist_data[1]}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			if game_id['game_ID'] == input_regist_data[1]:
				loot_member_data["_id"] = game_id['_id']
		
		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["toggle"] = input_regist_data[1]
		insert_data["toggle_ID"] = str(loot_member_data["_id"])
		insert_data["gulid_money_insert"] = gulid_money_insert_check
		insert_data["modifydate"] = input_time

		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']} → {insert_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 참여자추가 ################ 
	@commands.command(name=commandSetting_jungsan[22][0], aliases=commandSetting_jungsan[22][1:])
	async def modify_regist_add_member_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[22][0]} [순번] [아이디]** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[22][0]} [순번] [아이디]** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_regist_data[0])}, {"itemstatus":"미판매"}]})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]}/{commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		if input_regist_data[1] in jungsan_data['before_jungsan_ID']:
			return await ctx.send(f"```수정하려는 [참여자:{input_regist_data[1]}](이)가 등록된 [참여자] 목록에 있습니다!```")

		check_member_data : dict = {}

		tmp_member_list : list = []

		check_member_data = self.member_db.find_one({"game_ID":input_regist_data[1]})
		if not check_member_data:
			return await ctx.send(f"```참여자 [{input_regist_data[1]}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")
		
		tmp_member_list = jungsan_data["before_jungsan_ID"].copy()
		tmp_member_list.append(check_member_data["game_ID"])

		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["before_jungsan_ID"] = tmp_member_list

		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])} → {', '.join(insert_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 참여자삭제 ################ 
	@commands.command(name=commandSetting_jungsan[23][0], aliases=commandSetting_jungsan[23][1:])
	async def modify_regist_remove_member_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[23][0]} [순번] [아이디]** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[23][0]} [순번] [아이디]** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_regist_data[0])}, {"itemstatus":"미판매"}]})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]}/{commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		if input_regist_data[1] not in jungsan_data['before_jungsan_ID']:
			return await ctx.send(f"```삭제하려는 [참여자:{input_regist_data[1]}](이)가 등록된 [참여자] 목록에 없습니다!```")

		check_member_data : dict = {}

		tmp_member_list : list = []

		check_member_data = self.member_db.find_one({"game_ID":input_regist_data[1]})
		if not check_member_data:
			return await ctx.send(f"```참여자 [{input_regist_data[1]}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")
		
		tmp_member_list = jungsan_data["before_jungsan_ID"].copy()
		tmp_member_list.remove(check_member_data["game_ID"])

		if len(tmp_member_list) <= 0:
			return await ctx.send(f"```참여자 [{input_regist_data[1]}]를 삭제하면 참여자가 [0]명이 되므로 삭제할 수 없습니다!```")

		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["before_jungsan_ID"] = tmp_member_list

		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])} → {', '.join(insert_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		await ctx.send(embed = embed)

		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 이미지 수정 ################ 
	@commands.command(name=commandSetting_jungsan[50][0], aliases=commandSetting_jungsan[50][1:])
	async def modify_regist_image_data(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[50][0]} [순번] [수정이미지 url]** 양식으로 등록 해주세요")
		
		input_regist_data : list = args.split()
		len_input_regist_data = len(input_regist_data)

		if len_input_regist_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[50][0]} [순번] [수정이미지 url]** 양식으로 등록 해주세요")
		
		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_regist_data[0])}, {"itemstatus":"미판매"}]})
		
		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]**중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]}/{commandSetting_jungsan[16][0]} ]** 명령을 통해 확인해주세요.\n※정산 등록 내역 수정은 **[ 분배상태 ]**가 **[ 미판매 ]** 중인 등록건만 수정 가능합니다!")

		input_time : datetime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))
		insert_data : dict = {}
		insert_data = jungsan_data.copy()
		insert_data["image_url"] = input_regist_data[1]
		insert_data["modifydate"] = input_time
		
		embed = discord.Embed(
				title = "📜 수정 정보",
				description = "",
				color=0x00ff00
				)
		embed.add_field(name = "[ 순번 ]", value = f"```{jungsan_data['_id']}```", inline = False)
		embed.add_field(name = "[ 일시 ]", value = f"```{jungsan_data['getdate'].strftime('%y-%m-%d %H:%M:%S')}```", inline = False)
		embed.add_field(name = "[ 보스 ]", value = f"```{jungsan_data['boss']}```")
		embed.add_field(name = "[ 아이템 ]", value = f"```{jungsan_data['item']}```")
		embed.add_field(name = "[ 루팅 ]", value = f"```{jungsan_data['toggle']}```")
		embed.add_field(name = "[ 상태 ]", value = f"```{jungsan_data['itemstatus']}```")
		embed.add_field(name = "[ 판매금 ]", value = f"```{jungsan_data['price']}```")
		embed.add_field(name = "[ 참여자 ]", value = f"```{', '.join(jungsan_data['before_jungsan_ID'])}```")
		embed.set_footer(text = f"{insert_data['modifydate'].strftime('%y-%m-%d %H:%M:%S')} 수정!")
		embed.set_image(url = insert_data["image_url"])
		try:
			await ctx.send(embed = embed)
		except Exception:
			embed.add_field(name = "🚫  이미지 링크 확인 필요  🚫", value = f"```저장된 이미지가 삭제됩니다.```")
			insert_data["image_url"] = ""
			embed.set_image(url = insert_data["image_url"])
			await ctx.send(embed = embed)
		
		data_regist_warning_message = await ctx.send(f"**입력하신 수정 내역을 확인해 보세요!**\n**수정 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 수정이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await data_regist_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == data_regist_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **수정**을 취소합니다!")

		if str(reaction) == "⭕":
			result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":insert_data}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 등록 내역 수정 실패.") 

			return await ctx.send(f"📥 정산 등록 내역 수정 완료! 📥")
		else:
			return await ctx.send(f"**수정**이 취소되었습니다.\n")

	################ 판매입력 ################ 
	@commands.command(name=commandSetting_jungsan[24][0], aliases=commandSetting_jungsan[24][1:])
	async def input_sell_price(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[24][0]} [순번] [금액]** 양식으로 입력 해주세요")
		
		input_sell_price_data : list = args.split()
		len_input_sell_price_data = len(input_sell_price_data)

		if len_input_sell_price_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[24][0]} [순번] [금액]** 양식으로 입력 해주세요")
		
		try:
			input_sell_price_data[0] = int(input_sell_price_data[0])
			input_sell_price_data[1] = int(input_sell_price_data[1])
		except ValueError:
			return await ctx.send(f"**[순번]** 및 **[금액]**은 숫자로 입력 해주세요")

		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_sell_price_data[0])}, {"itemstatus":"미판매"}]})

		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]** 중이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]} ]** 명령을 통해 확인해주세요")

		result_each_price = int(input_sell_price_data[1]//len(jungsan_data["before_jungsan_ID"]))   # 혈비일 경우 수수로 계산 입력 예정

		if jungsan_data["gulid_money_insert"]:
			after_tax_price : int = int(input_sell_price_data[1]*(1-(basicSetting_jungsan[7]/100)))
			result_each_price : int = int(after_tax_price//len(jungsan_data["before_jungsan_ID"]))
			result = self.jungsan_db.update_one({"_id":input_sell_price_data[0]}, {"$set":{"price":after_tax_price, "each_price":result_each_price, "before_jungsan_ID":[], "after_jungsan_ID":jungsan_data["before_jungsan_ID"], "itemstatus":"분배완료"}}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 혈비 등록 실패.")
			result_guild = self.guild_db.update_one({"_id":"guild"}, {"$inc":{"guild_money":after_tax_price}}, upsert = True)
			if result_guild.raw_result["nModified"] < 1 and "upserted" not in result_guild.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 혈비 적립 실패.")
			insert_log_data = {
						"in_out_check":True,  # True : 입금, False : 출금
						"log_date":datetime.datetime.now(),
						"money":str(after_tax_price),
						"member_list":jungsan_data["before_jungsan_ID"],
						"reason":"정산금 혈비 적립"
			}
			result_guild_log = self.guild_db_log.insert_one(insert_log_data)
			return await ctx.send(f"**[ 순번 : {input_sell_price_data[0]} ]**   💰판매금 **[ {after_tax_price} ]**(세율 {basicSetting_jungsan[7]}% 적용) 혈비 적립 완료!")
		
		result = self.jungsan_db.update_one({"_id":input_sell_price_data[0]}, {"$set":{"price":input_sell_price_data[1], "each_price":result_each_price, "itemstatus":"분배중"}}, upsert = False)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 판매 등록 실패.") 			

		return await ctx.send(f"**[ 순번 : {input_sell_price_data[0]} ]**   💰판매금 **[ {input_sell_price_data[1]} ]** 등록 완료! 분배를 시작합니다.")

	################ 뽑기판매입력 ################ 
	@commands.command(name=commandSetting_jungsan[45][0], aliases=commandSetting_jungsan[45][1:])
	async def input_ladder_sell_price(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[45][0]} [순번] [금액] [인원]** 양식으로 입력 해주세요")
		
		input_sell_price_data : list = args.split()
		len_input_sell_price_data = len(input_sell_price_data)

		if len_input_sell_price_data != 3:
			return await ctx.send(f"**{commandSetting_jungsan[45][0]} [순번] [금액] [인원]** 양식으로 입력 해주세요")
		
		try:
			input_sell_price_data[0] = int(input_sell_price_data[0])
			input_sell_price_data[1] = int(input_sell_price_data[1])
			input_sell_price_data[2] = int(input_sell_price_data[2])
		except ValueError:
			return await ctx.send(f"**[순번]**, **[금액]** 및 **[인원]**은 숫자로 입력 해주세요")

		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_sell_price_data[0])}, {"itemstatus":"미판매"}]})

		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]** 중이 아니거나 없습니다. **[ {commandSetting_jungsan[45][0]} ]** 명령을 통해 확인해주세요")

		if input_sell_price_data[2] < 1:
			return await ctx.send(f"{ctx.author.mention}님! 추첨인원이 0보다 작거나 같습니다. 재입력 해주세요")

		ladder_check : bool = False

		if len(jungsan_data["before_jungsan_ID"]) > input_sell_price_data[2]:
			result_ladder = random.sample(jungsan_data["before_jungsan_ID"], input_sell_price_data[2])
			await ctx.send(f"**[ {', '.join(jungsan_data['before_jungsan_ID'])} ]** 중 **[ {', '.join(result_ladder)} ]** 당첨! 분배를 시작합니다.")
			result_each_price = int(input_sell_price_data[1]//input_sell_price_data[2])   # 혈비일 경우 수수로 계산 입력 예정
			ladder_check = True
		else:
			return await ctx.send(f"{ctx.author.mention}님! 추첨인원이 총 인원과 같거나 많습니다. 재입력 해주세요")

		if jungsan_data["gulid_money_insert"]:
			after_tax_price : int = int(input_sell_price_data[1]*(1-(basicSetting_jungsan[7]/100)))
			result_each_price : int = int(after_tax_price//input_sell_price_data[2])
			result = self.jungsan_db.update_one({"_id":input_sell_price_data[0]}, {"$set":{"price":after_tax_price, "each_price":result_each_price, "before_jungsan_ID":[], "after_jungsan_ID":result_ladder, "itemstatus":"분배완료", "ladder_check":ladder_check}}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 혈비 등록 실패.")
			result_guild = self.guild_db.update_one({"_id":"guild"}, {"$inc":{"guild_money":after_tax_price}}, upsert = True)
			if result_guild.raw_result["nModified"] < 1 and "upserted" not in result_guild.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 혈비 적립 실패.")
			insert_log_data = {
						"in_out_check":True,  # True : 입금, False : 출금
						"log_date":datetime.datetime.now(),
						"money":str(after_tax_price),
						"member_list":result_ladder,
						"reason":"정산금 혈비 적립"
			}
			result_guild_log = self.guild_db_log.insert_one(insert_log_data)
			return await ctx.send(f"**[ 순번 : {input_sell_price_data[0]} ]**   💰판매금 **[ {after_tax_price} ]**(세율 {basicSetting_jungsan[7]}% 적용) 혈비 적립 완료!")
		
		result = self.jungsan_db.update_one({"_id":input_sell_price_data[0]}, {"$set":{"price":input_sell_price_data[1], "each_price":result_each_price, "before_jungsan_ID":result_ladder, "itemstatus":"분배중", "ladder_check":ladder_check}}, upsert = False)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 판매 등록 실패.") 			

		return await ctx.send(f"**[ 순번 : {input_sell_price_data[0]} ]**   💰판매금 **[ {input_sell_price_data[1]} ]** 등록 완료! 분배를 시작합니다.")

	################ 정산 처리 입력 ################ 
	@commands.command(name=commandSetting_jungsan[25][0], aliases=commandSetting_jungsan[25][1:])
	async def distribute_finish(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[25][0]} [순번] [아이디]** 양식으로 정산 해주세요")

		input_distribute_finish_data : list = args.split()
		len_input_distribute_finish_data = len(input_distribute_finish_data)

		if len_input_distribute_finish_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[25][0]} [순번] [아이디]** 양식으로 정산 해주세요")

		try:
			input_distribute_finish_data[0] = int(input_distribute_finish_data[0])
		except ValueError:
			return await ctx.send(f"**[순번]**은 숫자로 입력 해주세요")

		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_distribute_finish_data[0])}, {"itemstatus":"분배중"}]})

		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 분배중 ]**이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]} ]** 명령을 통해 확인해주세요")
		else:
			if input_distribute_finish_data[1] in jungsan_data["after_jungsan_ID"]:
				return await ctx.send(f"**[ {input_distribute_finish_data[1]} ]**님은 **[ 순번 : {input_distribute_finish_data[0]} ]**의 정산 내역에 대하여 이미 💰**[ {jungsan_data['each_price']} ]** 정산 받았습니다!")
			elif input_distribute_finish_data[1] not in jungsan_data["before_jungsan_ID"]:
				return await ctx.send(f"**[ {input_distribute_finish_data[1]} ]**님은 **[ 순번 : {input_distribute_finish_data[0]} ]**의 정산 전 명단에 존재하지 않습니다!")
			else:
				pass
				
		jungsan_data["before_jungsan_ID"].remove(input_distribute_finish_data[1])
		jungsan_data["after_jungsan_ID"].append(input_distribute_finish_data[1])

		len_before_jungsan_data :int = 0
		len_before_jungsan_data = len(jungsan_data["before_jungsan_ID"])

		if len_before_jungsan_data == 0:
			result = self.jungsan_db.update_one({"_id":int(input_distribute_finish_data[0])}, {"$set":{"before_jungsan_ID":jungsan_data["before_jungsan_ID"], "after_jungsan_ID":jungsan_data["after_jungsan_ID"], "itemstatus" : "분배완료"}}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 실패.") 		
			return await ctx.send(f"**[ 순번 : {input_distribute_finish_data[0]} ]** : **[ {input_distribute_finish_data[1]} ]**님 정산 완료!\n**[ 순번 : {input_distribute_finish_data[0]} ]** 분배 완료!🎉")
		else:
			result = self.jungsan_db.update_one({"_id":int(input_distribute_finish_data[0])}, {"$set":{"before_jungsan_ID":jungsan_data["before_jungsan_ID"], "after_jungsan_ID":jungsan_data["after_jungsan_ID"]}}, upsert = False)
			if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
				return await ctx.send(f"{ctx.author.mention}, 정산 실패.") 		
			return await ctx.send(f"**[ 순번 : {input_distribute_finish_data[0]} ]** : **[ {input_distribute_finish_data[1]} ]**님 정산 완료!")
	
	################ 정산 처리 취소 ################ 
	@commands.command(name=commandSetting_jungsan[26][0], aliases=commandSetting_jungsan[26][1:])
	async def cancel_distribute_finish(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[26][0]} [순번] [아이디]** 양식으로 정산 해주세요")

		input_distribute_finish_data : list = args.split()
		len_input_distribute_finish_data = len(input_distribute_finish_data)

		if len_input_distribute_finish_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[26][0]} [순번] [아이디]** 양식으로 정산 해주세요")

		try:
			input_distribute_finish_data[0] = int(input_distribute_finish_data[0])
		except ValueError:
			return await ctx.send(f"**[순번]**은 숫자로 입력 해주세요")

		jungsan_data : dict = self.jungsan_db.find_one({"$and" : [{"$or" : [{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_distribute_finish_data[0])}, {"itemstatus":"분배중"}]})

		if not jungsan_data:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 분배중 ]**이 아니거나 없습니다. **[ {commandSetting_jungsan[13][0]} ]** 명령을 통해 확인해주세요")
		else:
			if input_distribute_finish_data[1] in jungsan_data["before_jungsan_ID"]:
				return await ctx.send(f"**[ {input_distribute_finish_data[1]} ]**님은 **[ 순번 : {input_distribute_finish_data[0]} ]**의 정산 내역에 대하여 아직 정산 받지 않았습니다!")
			elif input_distribute_finish_data[1] not in jungsan_data["after_jungsan_ID"]:
				return await ctx.send(f"**[ {input_distribute_finish_data[1]} ]**님은 **[ 순번 : {input_distribute_finish_data[0]} ]**의 정산 후 명단에 존재하지 않습니다!")
			else:
				pass
				
		jungsan_data["after_jungsan_ID"].remove(input_distribute_finish_data[1])
		jungsan_data["before_jungsan_ID"].append(input_distribute_finish_data[1])

		result = self.jungsan_db.update_one({"_id":int(input_distribute_finish_data[0])}, {"$set":{"before_jungsan_ID":jungsan_data["before_jungsan_ID"], "after_jungsan_ID":jungsan_data["after_jungsan_ID"]}}, upsert = False)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 정산 취소 실패.") 		
		return await ctx.send(f"**[ 순번 : {input_distribute_finish_data[0]} ]** : **[ {input_distribute_finish_data[1]} ]**님 정산 취소 완료!")

	################ 일괄정산 ################ 
	@commands.command(name=commandSetting_jungsan[27][0], aliases=commandSetting_jungsan[27][1:])
	async def distribute_all_finish(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		jungsan_document : list = []

		if not args:
			jungsan_document : list = list(self.jungsan_db.find({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"itemstatus":"분배중"}]}))
		else:
			input_distribute_all_finish : list = args.split()
			len_input_distribute_all_finish = len(input_distribute_all_finish)

			if len_input_distribute_all_finish != 2:
				return await ctx.send(f"**{commandSetting_jungsan[27][0]} [검색조건] [검색값]** 형식으로 입력 해주세요! **[검색조건]**은 **[순번, 보스명, 아이템, 날짜]** 다섯가지 중 **1개**를 입력 하셔야합니다!")
			else:
				if input_distribute_all_finish[0] == "순번":
					try:
						input_distribute_all_finish[1] = int(input_distribute_all_finish[1])
					except:
						return await ctx.send(f"**[순번] [검색값]**은 숫자로 입력 해주세요!")
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":input_distribute_all_finish[1]}, {"itemstatus":"분배중"}]}))
				elif input_distribute_all_finish[0] == "보스명":
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"boss":input_distribute_all_finish[1]}, {"itemstatus":"분배중"}]}))
				elif input_distribute_all_finish[0] == "아이템":
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"item":input_distribute_all_finish[1]}, {"itemstatus":"분배중"}]}))
				elif input_distribute_all_finish[0] == "날짜":
					try:
						start_search_date : str = (datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting_jungsan[8]))).replace(year = int(input_distribute_all_finish[1][:4]), month = int(input_distribute_all_finish[1][5:7]), day = int(input_distribute_all_finish[1][8:10]), hour = 0, minute = 0, second = 0)
						end_search_date : str = start_search_date + datetime.timedelta(days = 1)
					except:
						return await ctx.send(f"**[날짜] [검색값]**은 0000-00-00 형식으로 입력 해주세요!")
					jungsan_document = list(self.jungsan_db.find({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"getdate":{"$gte":start_search_date, "$lt":end_search_date}}, {"itemstatus":"분배중"}]}))
				else:
					return await ctx.send(f"**[검색조건]**이 잘못 됐습니다. **[검색조건]**은 **[순번, 보스명, 아이템, 날짜]** 네가지 중 **1개**를 입력 하셔야합니다!")

		if len(jungsan_document) == 0:
			return await ctx.send(f"{ctx.author.mention}님! **[ 분배중 ]**인 정산 내역이 없거나 등록된 정산 내역이 없습니다. **[ {commandSetting_jungsan[13][0]} ]** 명령을 통해 확인해주세요")

		total_distribute_money : int = 0
		detail_info_ing : str = ""
		embed_list : list = []
		embed_limit_checker : int = 0
		embed_cnt : int = 0
		init_data : dict = {}

		embed = discord.Embed(
					title = f"📜 [{member_data['game_ID']}]님 등록 내역",
					description = "",
					color=0x00ff00
					)

		embed_list.append(embed)
		for jungsan_data in jungsan_document:
			embed_limit_checker += 1
			if embed_limit_checker == 20:
				embed_limit_checker = 0
				embed_cnt += 1
				tmp_embed = discord.Embed(
					title = "",
					description = "",
					color=0x00ff00
					)
				embed_list.append(tmp_embed)
			detail_info_ing = f"```diff\n+ 분 배 중 : {len(jungsan_data['before_jungsan_ID'])}명 (💰{len(jungsan_data['before_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['before_jungsan_ID'])}\n- 분배완료 : {len(jungsan_data['after_jungsan_ID'])}명  (💰{len(jungsan_data['after_jungsan_ID'])*jungsan_data['each_price']})\n{', '.join(jungsan_data['after_jungsan_ID'])}```"
			embed_list[embed_cnt].add_field(name = f"[ 순번 : {jungsan_data['_id']} ] | {jungsan_data['getdate'].strftime('%y-%m-%d')} | {jungsan_data['boss']} | {jungsan_data['item']} | {jungsan_data['toggle']} | {jungsan_data['itemstatus']} : 1인당 💰{jungsan_data['each_price']}",
							value = detail_info_ing,
							inline = False)
			total_distribute_money += len(jungsan_data['before_jungsan_ID'])*int(jungsan_data['each_price'])
			init_data[jungsan_data['_id']] = jungsan_data['after_jungsan_ID']

		if len(embed_list) > 1:
			for embed_data in embed_list:
				await asyncio.sleep(0.1)
				await ctx.send(embed = embed_data)
		else:
			await ctx.send(embed = embed)

		embed1 = discord.Embed(
			title = f"일괄정산 예정 금액 : 💰 {str(total_distribute_money)}",
			description = "",
			color=0x00ff00
			)
		await ctx.send(embed = embed1)

		distribute_all_finish_warning_message = await ctx.send(f"**일괄 정산 예정인 등록 내역을 확인해 보세요!**\n**일괄정산 : ⭕ 취소: ❌**\n({basicSetting_jungsan[5]}초 동안 입력이 없을시 일괄정산이 취소됩니다.)", tts=False)

		emoji_list : list = ["⭕", "❌"]
		for emoji in emoji_list:
			await distribute_all_finish_warning_message.add_reaction(emoji)

		def reaction_check(reaction, user):
			return (reaction.message.id == distribute_all_finish_warning_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)

		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = reaction_check, timeout = int(basicSetting_jungsan[5]))
		except asyncio.TimeoutError:
			for emoji in emoji_list:
				await data_regist_warning_message.remove_reaction(emoji, self.bot.user)
			return await ctx.send(f"시간이 초과됐습니다. **일괄정산**을 취소합니다!")

		if str(reaction) == "⭕":
			for jungsan_data in jungsan_document:
				result = self.jungsan_db.update_one({"_id":jungsan_data['_id']}, {"$set":{"before_jungsan_ID":[], "after_jungsan_ID":init_data[jungsan_data['_id']]+jungsan_data['before_jungsan_ID'], "itemstatus":"분배완료"}}, upsert = True)
				if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
					await ctx.send(f"{ctx.author.mention}, 일괄정산 실패.") 

			return await ctx.send(f"📥 일괄정산 완료! 📥")
		else:
			return await ctx.send(f"**일괄정산**이 취소되었습니다.\n")

class bankCog(commands.Cog): 
	def __init__(self, bot):
		self.bot = bot	

		self.member_db = self.bot.db.jungsan.member
		self.jungsan_db = self.bot.db.jungsan.jungsandata
		self.guild_db = self.bot.db.jungsan.guild
		self.guild_db_log = self.bot.db.jungsan.guild_log

	################ 수수료 계산기 ################ 
	@commands.command(name=commandSetting_jungsan[34][0], aliases=commandSetting_jungsan[34][1:])
	async def tax_check(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[34][0]} [판매금액] (거래소세금)** 양식으로 입력 해주세요\n※ 거래소세금은 미입력시 {basicSetting_jungsan[7]}%입니다.")
		
		input_money_data : list = args.split()
		len_input_money_data = len(input_money_data)

		try:
			for i in range(len_input_money_data):
				input_money_data[i] = int(input_money_data[i])
		except ValueError:
			return await ctx.send(f"**[판매금액] (거래소세금)**은 숫자로 입력 해주세요.")

		if len_input_money_data < 1 or len_input_money_data > 3:
			return await ctx.send(f"**{commandSetting_jungsan[34][0]} [판매금액] (거래소세금)** 양식으로 입력 해주세요\n※ 거래소세금은 미입력시 {basicSetting_jungsan[7]}%입니다.")
		elif len_input_money_data == 2:
			tax = input_money_data[1]
		else:
			tax = basicSetting_jungsan[7]

		price_first_tax = int(input_money_data[0] * ((100-tax)/100))
		price_second_tax = int(price_first_tax * ((100-tax)/100))
		price_rev_tax = int((input_money_data[0] * 100)/(100-tax)+0.5)

		embed = discord.Embed(
				title = f"🧮  수수료 계산결과 (세율 {tax}% 기준) ",
				description = f"",
				color=0x00ff00
				)
		embed.add_field(name = "⚖️ 수수료 지원", value = f"```등록가 : {price_rev_tax}\n수령가 : {input_money_data[0]}\n세 금 : {price_rev_tax-input_money_data[0]}```")
		embed.add_field(name = "⚖️ 1차 거래", value = f"```등록가 : {input_money_data[0]}\n정산가 : {price_first_tax}\n세 금 : {input_money_data[0]-price_first_tax}```")
		embed.add_field(name = "⚖️ 2차 거래", value = f"```등록가 : {price_first_tax}\n정산가 : {price_second_tax}\n세 금 : {price_first_tax-price_second_tax}```")
		return await ctx.send(embed = embed)

	################ 페이백 계산기 ################ 
	@commands.command(name=commandSetting_jungsan[35][0], aliases=commandSetting_jungsan[35][1:])
	async def payback_check(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[35][0]} 거래소가격] [실거래가] (거래소세금)** 양식으로 입력 해주세요\n※ 거래소세금은 미입력시 {basicSetting_jungsan[7]}%입니다.")
		
		input_money_data : list = args.split()
		len_input_money_data = len(input_money_data)

		try:
			for i in range(len_input_money_data):
				input_money_data[i] = int(input_money_data[i])
		except ValueError:
			return await ctx.send(f"**[판매금액] (거래소세금)**은 숫자로 입력 해주세요.")

		if len_input_money_data < 2 or len_input_money_data > 4:
			return await ctx.send(f"**{commandSetting_jungsan[35][0]} [거래소가격] [실거래가] (거래소세금)** 양식으로 입력 해주세요\n※ 거래소세금은 미입력시 {basicSetting_jungsan[7]}%입니다.")
		elif len_input_money_data == 3:
			tax = input_money_data[2]
		else:
			tax = basicSetting_jungsan[7]

		price_reg_tax = int(input_money_data[0] * ((100-tax)/100))
		price_real_tax = int(input_money_data[1] * ((100-tax)/100))

		reault_payback = price_reg_tax - price_real_tax
		reault_payback1= price_reg_tax - input_money_data[1]

		embed = discord.Embed(
				title = f"🧮  페이백 계산결과1 (세율 {tax}% 기준) ",
				description = f"**```fix\n{reault_payback}```**",
				color=0x00ff00
				)
		embed.add_field(name = "⚖️ 거래소", value = f"```등록가 : {input_money_data[0]}\n정산가 : {price_reg_tax}\n세 금 : {input_money_data[0]-price_reg_tax}```")
		embed.add_field(name = "🕵️ 실거래", value = f"```등록가 : {input_money_data[1]}\n정산가 : {price_real_tax}\n세 금 : {input_money_data[1]-price_real_tax}```")
		await ctx.send(embed = embed)

		embed2 = discord.Embed(
				title = f"🧮  페이백 계산결과2 (세율 {tax}% 기준) ",
				description = f"**```fix\n{reault_payback1}```**",
				color=0x00ff00
				)
		embed2.add_field(name = "⚖️ 거래소", value = f"```등록가 : {input_money_data[0]}\n정산가 : {price_reg_tax}\n세 금 : {input_money_data[0]-price_reg_tax}```")
		embed2.add_field(name = "🕵️ 실거래", value = f"```내판가 : {input_money_data[1]}```")
		return await ctx.send(embed = embed2)

	################ 계좌확인 ################ 
	@commands.command(name=commandSetting_jungsan[28][0], aliases=commandSetting_jungsan[28][1:])
	async def account_check(self, ctx):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		embed = discord.Embed(
				title = f"[{member_data['game_ID']}]님 은행 잔고 📝",
				description = f"**```diff\n{member_data['account']}```**",
				color=0x00ff00
				)
		embed.set_thumbnail(url = ctx.author.avatar_url)
		return await ctx.send(embed = embed)

	################ 저축 ################ 
	@commands.command(name=commandSetting_jungsan[29][0], aliases=commandSetting_jungsan[29][1:])
	async def bank_save_money(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]):
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[29][0]} [순번] [금액]** 양식으로 입력 해주세요")
		
		input_sell_price_data : list = args.split()
		len_input_sell_price_data = len(input_sell_price_data)

		if len_input_sell_price_data != 2:
			return await ctx.send(f"**{commandSetting_jungsan[29][0]} [순번] [금액]** 양식으로 입력 해주세요")
		
		try:
			input_sell_price_data[0] = int(input_sell_price_data[0])
			input_sell_price_data[1] = int(input_sell_price_data[1])
		except ValueError:
			return await ctx.send(f"**[순번]** 및 **[금액]**은 숫자로 입력 해주세요")

		jungsan_document : dict = self.jungsan_db.find_one({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_sell_price_data[0])}, {"itemstatus":"미판매"}]})
		if not jungsan_document:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]** 중이 아니거나 없습니다. **[ {commandSetting_jungsan[13]}/{commandSetting_jungsan[16]} ]** 명령을 통해 확인해주세요")
		
		after_tax_price : int = int(input_sell_price_data[1]*(1-(basicSetting_jungsan[7]/100)))
		result_each_price : int = int(after_tax_price//len(jungsan_document["before_jungsan_ID"]))

		participant_list : list = jungsan_document["before_jungsan_ID"]

		self.member_db.update_many({"game_ID":{"$in":participant_list}}, {"$inc":{"account":result_each_price}})

		insert_data : dict = {}
		insert_data = {
					"itemstatus":"분배완료",
					"price":after_tax_price,
					"each_price":result_each_price,
					"before_jungsan_ID":[],
					"after_jungsan_ID":jungsan_document["before_jungsan_ID"],
					"bank_money_insert":True
					}

		result = self.jungsan_db.update_one({"_id":input_sell_price_data[0]}, {"$set":insert_data}, upsert = False)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 은행 저축 실패.")		

		return await ctx.send(f"**[ 순번 : {input_sell_price_data[0]} ]**   💰판매금 **[ {after_tax_price} ]**(세율 {basicSetting_jungsan[7]}% 적용)\n**{jungsan_document['before_jungsan_ID']}**계좌로 인당 **💰 [ {result_each_price} ]** 은행 저축 완료!")

	################ 뽑기저축 ################ 
	@commands.command(name=commandSetting_jungsan[48][0], aliases=commandSetting_jungsan[48][1:])
	async def bank_ladder_save_money(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]):
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[48][0]} [순번] [금액] [인원]** 양식으로 입력 해주세요")
		
		input_sell_price_data : list = args.split()
		len_input_sell_price_data = len(input_sell_price_data)

		if len_input_sell_price_data != 3:
			return await ctx.send(f"**{commandSetting_jungsan[48][0]} [순번] [금액] [인원]** 양식으로 입력 해주세요")
		
		try:
			input_sell_price_data[0] = int(input_sell_price_data[0])
			input_sell_price_data[1] = int(input_sell_price_data[1])
			input_sell_price_data[2] = int(input_sell_price_data[2])
		except ValueError:
			return await ctx.send(f"**[순번]** 및 **[금액]**은 숫자로 입력 해주세요")

		jungsan_document : dict = self.jungsan_db.find_one({"$and" : [{"$or":[{"toggle_ID" : str(ctx.author.id)}, {"regist_ID" : str(ctx.author.id)}]}, {"_id":int(input_sell_price_data[0])}, {"itemstatus":"미판매"}]})
		if not jungsan_document:
			return await ctx.send(f"{ctx.author.mention}님! 등록하신 정산 내역이 **[ 미판매 ]** 중이 아니거나 없습니다. **[ {commandSetting_jungsan[13]}/{commandSetting_jungsan[16]} ]** 명령을 통해 확인해주세요")
		
		if input_sell_price_data[2] < 1:
			return await ctx.send(f"{ctx.author.mention}님! 추첨인원이 0보다 작거나 같습니다. 재입력 해주세요")
		
		ladder_check : bool = False

		if len(jungsan_document["before_jungsan_ID"]) > input_sell_price_data[2]:
			result_ladder = random.sample(jungsan_document["before_jungsan_ID"], input_sell_price_data[2])
			await ctx.send(f"**[ {', '.join(jungsan_document['before_jungsan_ID'])} ]** 중 **[ {', '.join(result_ladder)} ]** 당첨! 해당 인원의 계좌로 저축합니다.")
			ladder_check = True
		else:
			return await ctx.send(f"{ctx.author.mention}님! 추첨인원이 총 인원과 같거나 많습니다. 재입력 해주세요")
		
		after_tax_price : int = int(input_sell_price_data[1]*(1-(basicSetting_jungsan[7]/100)))
		result_each_price = int(after_tax_price//input_sell_price_data[2])   

		participant_list : list = result_ladder

		self.member_db.update_many({"game_ID":{"$in":participant_list}}, {"$inc":{"account":result_each_price}})

		insert_data : dict = {}
		insert_data = {
					"itemstatus":"분배완료",
					"price":after_tax_price,
					"each_price":result_each_price,
					"before_jungsan_ID":[],
					"after_jungsan_ID":participant_list,
					"bank_money_insert":True,
					"ladder_check":ladder_check
					}

		result = self.jungsan_db.update_one({"_id":input_sell_price_data[0]}, {"$set":insert_data}, upsert = False)
		if result.raw_result["nModified"] < 1 and "upserted" not in result.raw_result:
			return await ctx.send(f"{ctx.author.mention}, 은행 저축 실패.")		

		return await ctx.send(f"**[ 순번 : {input_sell_price_data[0]} ]**   💰판매금 **[ {after_tax_price} ]**(세율 {basicSetting_jungsan[7]}% 적용)\n**{participant_list}**계좌로 인당 **💰 [ {result_each_price} ]** 은행 저축 완료!")

	################ 입금 #################
	@is_manager() 
	@commands.command(name=commandSetting_jungsan[30][0], aliases=commandSetting_jungsan[30][1:])
	async def bank_deposit_money(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")
			
		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[30][0]} [금액] [아이디] [아이디]...** 양식으로 입력 해주세요")
		
		input_bank_deposit_data : list = args.split()
		len_input_sell_price_data : int = len(input_bank_deposit_data)

		if len_input_sell_price_data < 2:
			return await ctx.send(f"**{commandSetting_jungsan[30][0]} [금액] [아이디] [아이디]...** 양식으로 입력 해주세요")

		try:
			input_bank_deposit_data[0] = int(input_bank_deposit_data[0])
		except ValueError:
			return await ctx.send(f"**[금액]**은 숫자로 입력 해주세요")

		check_member_data : list = []
		check_member_list : list = []
		wrong_input_id : list = []

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			check_member_list.append(game_id['game_ID'])

		for game_id in input_bank_deposit_data[1:]:
			if game_id not in check_member_list:
				wrong_input_id.append(game_id)

		if len(wrong_input_id) > 0:
			return await ctx.send(f"```입금자 [{', '.join(wrong_input_id)}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")	

		result_update = self.member_db.update_many({"game_ID":{"$in":input_bank_deposit_data[1:]}}, {"$inc":{"account":input_bank_deposit_data[0]}})
		if result_update.modified_count != len(input_bank_deposit_data[1:]):
			return await ctx.send(f"```은행 입금 실패. 정확한 [아이디]를 입력 후 다시 시도 해보세요!```")

		return await ctx.send(f"```ml\n{input_bank_deposit_data[1:]}님 💰[{input_bank_deposit_data[0]}] 은행 입금 완료!.```")

	################ 출금 #################
	@is_manager() 
	@commands.command(name=commandSetting_jungsan[31][0], aliases=commandSetting_jungsan[31][1:])
	async def bank_withdraw_money(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")
			
		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[31][0]} [금액] [아이디] [아이디]...** 양식으로 입력 해주세요")
		
		input_bank_withdraw_data : list = args.split()
		len_input_bank_withdraw_data : int = len(input_bank_withdraw_data)

		if len_input_bank_withdraw_data < 2:
			return await ctx.send(f"**{commandSetting_jungsan[31][0]} [금액] [아이디] [아이디]...** 양식으로 입력 해주세요")

		try:
			input_bank_withdraw_data[0] = int(input_bank_withdraw_data[0])
		except ValueError:
			return await ctx.send(f"**[금액]**은 숫자로 입력 해주세요")

		check_member_data : list = []
		check_member_list : list = []
		wrong_input_id : list = []

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			check_member_list.append(game_id['game_ID'])

		for game_id in input_bank_withdraw_data[1:]:
			if game_id not in check_member_list:
				wrong_input_id.append(game_id)

		if len(wrong_input_id) > 0:
			return await ctx.send(f"```출금자 [{', '.join(wrong_input_id)}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")	

		result_update = self.member_db.update_many({"game_ID":{"$in":input_bank_withdraw_data[1:]}}, {"$inc":{"account":-input_bank_withdraw_data[0]}})

		if result_update.modified_count != len(input_bank_withdraw_data[1:]):
			return await ctx.send(f"```은행 출금 실패. 정확한 [아이디]를 입력 후 다시 시도 해보세요!```")

		return await ctx.send(f"```ml\n{input_bank_withdraw_data[1:]}님 💰[{input_bank_withdraw_data[0]}] 은행 출금 완료!.```")

	################ 혈비입금 #################
	@is_manager() 
	@commands.command(name=commandSetting_jungsan[32][0], aliases=commandSetting_jungsan[32][1:])
	async def guild_support_money_save(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")
			
		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[32][0]} [금액]** 양식으로 입력 해주세요")

		try:
			args = int(args)
		except ValueError:
			return await ctx.send(f"**[금액]**은 숫자로 입력 해주세요")

		result_guild_update : dict = self.guild_db.update_one({"_id":"guild"}, {"$inc":{"guild_money":args}}, upsert = True)
		if result_guild_update.raw_result["nModified"] < 1 and "upserted" not in result_guild_update.raw_result:
			return await ctx.send(f"```혈비 입금 실패!```")
		insert_log_data = {
					"in_out_check":True,  # True : 입금, False : 출금
					"log_date":datetime.datetime.now(),
					"money":args,
					"member_list":[],
					"reason":""
		}
		result_guild_log = self.guild_db_log.insert_one(insert_log_data)

		total_guild_money : dict = self.guild_db.find_one({"_id":"guild"})

		embed = discord.Embed(
				title = f"💰  혈비 입금 완료",
				description = f"",
				color=0x00ff00
				)
		embed.add_field(name = f"**입금**", value = f"**```fix\n{args}```**")
		embed.add_field(name = f"**혈비**", value = f"**```fix\n{total_guild_money['guild_money']}```**")
		return await ctx.send(embed = embed)

	################ 혈비출금 #################
	@is_manager() 
	@commands.command(name=commandSetting_jungsan[49][0], aliases=commandSetting_jungsan[49][1:])
	async def guild_support_money_withdraw(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")
			
		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[49][0]} [금액]** 양식으로 입력 해주세요")

		guild_support_money_withdraw_data : list = args.split(" *")
		if len(guild_support_money_withdraw_data) != 2:
			return await ctx.send(f"**{commandSetting_jungsan[49][0]} [금액] *[사유]** 양식으로 입력 해주세요")

		try:
			guild_support_money_withdraw_data[0] = int(guild_support_money_withdraw_data[0])
		except ValueError:
			return await ctx.send(f"**[금액]**은 숫자로 입력 해주세요")

		result_guild_update : dict = self.guild_db.update_one({"_id":"guild"}, {"$inc":{"guild_money":-guild_support_money_withdraw_data[0]}}, upsert = True)
		if result_guild_update.raw_result["nModified"] < 1 and "upserted" not in result_guild_update.raw_result:
			return await ctx.send(f"```혈비 출금 실패!```")
		insert_log_data = {
					"in_out_check":False,  # True : 입금, False : 출금
					"log_date":datetime.datetime.now(),
					"money":guild_support_money_withdraw_data[0],
					"member_list":[],
					"reason":guild_support_money_withdraw_data[1]
		}
		result_guild_log = self.guild_db_log.insert_one(insert_log_data)

		total_guild_money : dict = self.guild_db.find_one({"_id":"guild"})

		embed = discord.Embed(
				title = f"💰  혈비 출금 완료",
				description = f"",
				color=0x00ff00
				)
		embed.add_field(name = f"**출금**", value = f"**```fix\n{guild_support_money_withdraw_data[0]}```**")
		embed.add_field(name = f"**혈비**", value = f"**```fix\n{total_guild_money['guild_money']}```**")
		return await ctx.send(embed = embed)

	################ 혈비지원 #################
	@is_manager() 
	@commands.command(name=commandSetting_jungsan[33][0], aliases=commandSetting_jungsan[33][1:])
	async def guild_support_money(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		guild_data : dict = self.guild_db.find_one({"_id":"guild"})

		if not guild_data:
			return await ctx.send(f"등록된 혈비가 없습니다!")
			
		if not args:
			return await ctx.send(f"**{commandSetting_jungsan[33][0]} [금액] [아이디1] [아이디2] ... *[사유]** 양식으로 입력 해주세요")
		
		input_guild_support_money_data : list = args.split(" *")
		if len(input_guild_support_money_data) != 2:
			return await ctx.send(f"**{commandSetting_jungsan[33][0]} [금액] [아이디] [아이디2] ... *[사유]** 양식으로 입력 해주세요")

		input_guild_support_money_ID_data : list = input_guild_support_money_data[0].split(" ")

		try:
			input_guild_support_money_ID_data[0] = int(input_guild_support_money_ID_data[0])
		except ValueError:
			return await ctx.send(f"**[금액]**은 숫자로 입력 해주세요")

		check_member_data : list = []
		check_member_list : list = []
		wrong_input_id : list = []

		check_member_data = list(self.member_db.find())
		for game_id in check_member_data:
			check_member_list.append(game_id['game_ID'])

		for game_id in input_guild_support_money_ID_data[1:]:
			if game_id not in check_member_list:
				wrong_input_id.append(game_id)

		if len(wrong_input_id) > 0:
			return await ctx.send(f"```지원자 [{', '.join(wrong_input_id)}](은)는 혈원으로 등록되지 않은 아이디 입니다.```")	

		result_update = self.member_db.update_many({"game_ID":{"$in":input_guild_support_money_ID_data[1:]}}, {"$inc":{"account":input_guild_support_money_ID_data[0]}})

		if result_update.modified_count != len(input_guild_support_money_ID_data[1:]):
			return await ctx.send(f"```혈비 지원 실패. 정확한 [아이디]를 입력 후 다시 시도 해보세요!```")
		insert_log_data = {
					"in_out_check":False, # True : 입금, False : 출금
					"log_date":datetime.datetime.now(),
					"money":str(input_guild_support_money_ID_data[0]*len(input_guild_support_money_ID_data[1:])),
					"member_list":input_guild_support_money_ID_data[1:],
					"reason":input_guild_support_money_data[1]
		}
		result_guild_log = self.guild_db_log.insert_one(insert_log_data)

		total_support_money : int = len(input_guild_support_money_ID_data[1:]) * input_guild_support_money_ID_data[0]

		result_guild_update = self.guild_db.update_one({"_id":"guild"}, {"$inc":{"guild_money":-total_support_money}}, upsert = False)
		if result_guild_update.raw_result["nModified"] < 1 and "upserted" not in result_guild_update.raw_result:
			return await ctx.send(f"```혈비 출금 실패!```")

		embed = discord.Embed(
				title = f"🤑 혈비 지원 완료",
				description = f"```css\n[{input_guild_support_money_data[1]}] 사유로 💰[{input_guild_support_money_ID_data[0]}]씩 혈비에서 지원했습니다.```",
				color=0x00ff00
				)
		embed.add_field(name = f"**👥  명단**", value = f"**```fix\n{', '.join(input_guild_support_money_ID_data[1:])}```**")
		embed.add_field(name = f"**💰  지원금**", value = f"**```fix\n{input_guild_support_money_ID_data[0]}```**")
		return await ctx.send(embed = embed)

	################ 창고검색 #################
	@commands.command(name=commandSetting_jungsan[44][0], aliases=commandSetting_jungsan[44][1:])
	async def guild_inventory_search(self, ctx, *, args : str = None):
		if ctx.message.channel.id != int(basicSetting_jungsan[6]) or basicSetting_jungsan[6] == "":
			return

		member_data : dict = self.member_db.find_one({"_id":ctx.author.id})

		if not member_data:
			return await ctx.send(f"{ctx.author.mention}님은 혈원으로 등록되어 있지 않습니다!")

		if args:
			return await ctx.send(f"**{commandSetting_jungsan[44][0]}** 만 입력 해주세요!")

		pipeline = [
				    {"$match": {"itemstatus":"미판매"}},  # 조건
				    {"$group": {"_id": "$item", "count": {"$sum":1}}}  # 요런식으로 변환해준다.
				]

		item_counts = self.jungsan_db.aggregate(pipeline)

		sorted_item_counts : dict = sorted(item_counts, key=lambda item_counts:item_counts['count'], reverse = True)
		len_sorted_item_counts = len(sorted_item_counts)
		#print(sorted_item_counts)

		embed_list : list = []
		embed_index : int = 0
		embed_cnt : int = 0

		embed = discord.Embed(title = '', description = f'📦  `창고 내역`', color = 0x00ff00)

		embed_list.append(embed)

		if len_sorted_item_counts > 0 :
			for item_data in sorted_item_counts:
				embed_cnt += 1
				if embed_cnt > 24 :
					embed_cnt = 0
					embed_index += 1
					tmp_embed = discord.Embed(
						title = "",
						description = "",
						color=0x00ff00
						)
					embed_list.append(tmp_embed)
				embed_list[embed_index].add_field(name = item_data['_id'], value = f"```{item_data['count']}```")
			embed.set_footer(text = f"전체 아이템 종류  :  {len_sorted_item_counts}개")
			if len(embed_list) > 1:
				for embed_data in embed_list:
					await asyncio.sleep(0.1)
					await ctx.send(embed = embed_data)
				return
			else:
				return await ctx.send(embed=embed, tts=False)
		else :
			embed.add_field(name = '\u200b\n', value = '창고가 비었습니다.\n\u200b')
			return await ctx.send(embed=embed, tts=False)

class bossCog(commands.Cog): 
	def __init__(self, bot):
		self.bot = bot	

	################ 보탐봇 입장 ################ 	
	@commands.has_permissions(manage_messages=True)
	@commands.command(name=command[0][0], aliases=command[0][1:])
	async def join_(ctx):
		global basicSetting
		global chflg
		global voice_client1

		if basicSetting[7] == "":
			channel = ctx.message.channel.id #메세지가 들어온 채널 ID

			print ('[ ', basicSetting[7], ' ]')
			print ('] ', ctx.message.channel.name, ' [')

			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith("textchannel ="):
					inputData_textCH[i] = 'textchannel = ' + str(channel) + '\r'
					basicSetting[7] = channel
					#print ('======', inputData_text[i])
			
			result_textCH = '\n'.join(inputData_textCH)
			
			#print (result_textCH)
			
			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

			await ctx.send(f"< 텍스트채널 [{ctx.message.channel.name}] 접속완료 >\n< 음성채널 접속 후 [{command[5][0]}] 명령을 사용 하세요 >", tts=False)
			
			print('< 텍스트채널 [' + self.get_channel(basicSetting[7]).name + '] 접속완료>')
			if basicSetting[6] != "":
				voice_client1 = await self.get_channel(basicSetting[6]).connect(reconnect=True)
				print('< 음성채널 [' + self.get_channel(basicSetting[6]).name + '] 접속완료>')
			if basicSetting[8] != "":
				if str(basicSetting[8]) in channel_id:
					print('< 사다리채널 [' + self.get_channel(int(basicSetting[8])).name + '] 접속완료 >')
				else:
					basicSetting[8] = ""
					print(f"사다리채널 ID 오류! [{command[28][0]} 사다리] 명령으로 재설정 바랍니다.")
			if basicSetting[11] != "":
				if str(basicSetting[11]) in channel_id:
					print('< 정산채널 [' + self.get_channel(int(basicSetting[11])).name + '] 접속완료>')
				else:
					basicSetting[11] = ""
					print(f"정산채널 ID 오류! [{command[28][0]} 정산] 명령으로 재설정 바랍니다.")
			if basicSetting[18] != "":
				if str(basicSetting[18]) in channel_id:
					print('< 척살채널 [' + self.get_channel(int(basicSetting[18])).name + '] 접속완료>')
				else:
					basicSetting[18] = ""
					print(f"척살채널 ID 오류! [{command[28][0]} 척살] 명령으로 재설정 바랍니다.")
			if basicSetting[19] != "":
				if str(basicSetting[19]) in channel_id:
					print('< 경주채널 [' + self.get_channel(int(basicSetting[19])).name + '] 접속완료>')
				else:
					basicSetting[19] = ""
					print(f"경주채널 ID 오류! [{command[28][0]} 경주] 명령으로 재설정 바랍니다.")
			if basicSetting[20] != "":
				if str(basicSetting[20]) in channel_id:
					print('< 아이템채널 [' + self.get_channel(int(basicSetting[20])).name + '] 접속완료>')
				else:
					basicSetting[20] = ""
					print(f"아이템채널 ID 오류! [{command[28][0]} 아이템] 명령으로 재설정 바랍니다.")
			if int(basicSetting[13]) != 0 :
				print('< 보탐봇 재시작 시간 ' + endTime.strftime('%Y-%m-%d ') + endTime.strftime('%H:%M:%S') + ' >')
				print('< 보탐봇 재시작 주기 ' + basicSetting[13] + '일 >')
			else :
				print('< 보탐봇 재시작 설정안됨 >')

			chflg = 1
		else:
			for guild in client.guilds:
				for text_channel in guild.text_channels:
					if basicSetting[7] == text_channel.id:
						curr_guild_info = guild

			emoji_list : list = ["⭕", "❌"]
			guild_error_message = await ctx.send(f"이미 **[{curr_guild_info.name}]** 서버 **[{setting_channel_name}]** 채널이 명령어 채널로 설정되어 있습니다.\n해당 채널로 명령어 채널을 변경 하시려면 ⭕ 그대로 사용하시려면 ❌ 를 눌러주세요.\n(10초이내 미입력시 기존 설정 그대로 설정됩니다.)", tts=False)

			for emoji in emoji_list:
				await guild_error_message.add_reaction(emoji)

			def reaction_check(reaction, user):
				return (reaction.message.id == guild_error_message.id) and (user.id == ctx.author.id) and (str(reaction) in emoji_list)
			try:
				reaction, user = await client.wait_for('reaction_add', check = reaction_check, timeout = 10)
			except asyncio.TimeoutError:
				return await ctx.send(f"시간이 초과됐습니다. **[{curr_guild_info.name}]** 서버 **[{setting_channel_name}]** 채널에서 사용해주세요!")

			if str(reaction) == "⭕":
				await voice_client1.disconnect()
				basicSetting[6] = ""
				basicSetting[7] = int(ctx.message.channel.id)

				print ('[ ', basicSetting[7], ' ]')
				print ('] ', ctx.message.channel.name, ' [')

				inidata_textCH = repo.get_contents("test_setting.ini")
				file_data_textCH = base64.b64decode(inidata_textCH.content)
				file_data_textCH = file_data_textCH.decode('utf-8')
				inputData_textCH = file_data_textCH.split('\n')
				
				for i in range(len(inputData_textCH)):
					if inputData_textCH[i].startswith("textchannel ="):
						inputData_textCH[i] = 'textchannel = ' + str(basicSetting[7]) + '\r'
				
				result_textCH = '\n'.join(inputData_textCH)
				
				contents = repo.get_contents("test_setting.ini")
				repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

				return await ctx.send(f"명령어 채널이 **[{ctx.author.guild.name}]** 서버 **[{ctx.message.channel.name}]** 채널로 새로 설정되었습니다.\n< 음성채널 접속 후 [{command[5][0]}] 명령을 사용 하세요 >")
			else:
				return await ctx.send(f"명령어 채널 설정이 취소되었습니다.\n**[{curr_guild_info.name}]** 서버 **[{setting_channel_name}]** 채널에서 사용해주세요!")

	################ 보탐봇 메뉴 출력 ################ 	
	@commands.command(name=command[1][0], aliases=command[1][1:])
	async def menu_(self, ctx):
		if ctx.message.channel.id == basicSetting[7]:
			command_list = ''
			command_list += ','.join(command[2]) + '\n'     #!설정확인
			command_list += ','.join(command[3]) + '\n'     #!채널확인
			command_list += ','.join(command[4]) + ' [채널명]\n'     #!채널이동
			command_list += ','.join(command[5]) + ' ※ 관리자만 실행 가능\n'     #!소환
			command_list += ','.join(command[6]) + '\n'     #!불러오기
			command_list += ','.join(command[7]) + '\n'     #!초기화
			command_list += ','.join(command[8]) + '\n'     #!명치
			command_list += ','.join(command[9]) + '\n'     #!재시작
			command_list += ','.join(command[10]) + '\n'     #!미예약
			command_list += ','.join(command[11]) + ' [인원] [금액]\n'     #!분배
			command_list += ','.join(command[12]) + ' [뽑을인원수] [아이디1] [아이디2]...\n'     #!사다리
			command_list += ','.join(command[27]) + ' [아이디1] [아이디2]...(최대 12명)\n'     #!경주
			command_list += ','.join(command[13]) + ' [아이디]\n'     #!정산
			command_list += ','.join(command[14]) + ' 또는 ' + ','.join(command[14]) + ' 0000, 00:00\n'     #!보스일괄
			command_list += ','.join(command[15]) + '\n'     #!q
			command_list += ','.join(command[16]) + ' [할말]\n'     #!v
			command_list += ','.join(command[17]) + '\n'     #!리젠
			command_list += ','.join(command[18]) + '\n'     #!현재시간
			command_list += ','.join(command[24]) + '\n'     #!킬초기화
			command_list += ','.join(command[25]) + '\n'     #!킬횟수 확인
			command_list += ','.join(command[25]) + ' [아이디]\n'     #!킬
			command_list += ','.join(command[26]) + ' [아이디]\n'     #!킬삭제
			command_list += ','.join(command[33]) + ' [아이디] 또는 ' + ','.join(command[33]) + ' [아이디] [횟수]\n'     #!킬차감
			command_list += ','.join(command[29]) + '\n'     #!아이템 목록 초기화
			command_list += ','.join(command[30]) + '\n'     #!아이템 목록 확인
			command_list += ','.join(command[30]) + ' [아이템] 또는 ' + ','.join(command[30]) + ' [아이템] [개수]\n'     #!아이템 목록 입력
			command_list += ','.join(command[31]) + ' [아이템]\n'     #!아이템 목록에서 삭제
			command_list += ','.join(command[32]) + ' [아이템] 또는 ' + ','.join(command[32]) + ' [아이템] [개수]\n'     #!아이템 차감
			command_list += ','.join(command[19]) + '\n'     #!공지
			command_list += ','.join(command[19]) + ' [공지내용]\n'     #!공지
			command_list += ','.join(command[20]) + '\n'     #!공지삭제
			command_list += ','.join(command[21]) + ' [할말]\n'     #!상태
			command_list += ','.join(command[28]) + ' 사다리, 정산, 척살, 경주, 아이템\n'     #!채널설정
			command_list += ','.join(command[34]) + ' ※ 관리자만 실행 가능\n\n'     #서버나가기
			command_list += ','.join(command[22]) + '\n'     #보스탐
			command_list += ','.join(command[23]) + '\n'     #!보스탐
			command_list += '[보스명]컷 또는 [보스명]컷 0000, 00:00\n'  
			command_list += '[보스명] 컷 또는 [보스명] 컷 0000, 00:00\n'   
			command_list += '[보스명]멍 또는 [보스명]멍 0000, 00:00\n'     
			command_list += '[보스명]예상 또는 [보스명]예상 0000, 00:00\n' 
			command_list += '[보스명]삭제\n'     
			command_list += '[보스명]메모 [할말]\n'
			embed = discord.Embed(
					title = "----- 명령어 -----",
					description= '```' + command_list + '```',
					color=0xff00ff
					)
			embed.add_field(
					name="----- 추가기능 -----",
					value= '```- [보스명]컷/멍/예상  [할말] : 보스시간 입력 후 빈칸 두번!! 메모 가능\n- [보스명]컷 명령어는 초성으로 입력가능합니다.\n  ex)' + bossData[0][0] + '컷 => ' + convertToInitialLetters(bossData[0][0] +'컷') + ', ' + bossData[0][0] + ' 컷 => ' + convertToInitialLetters(bossData[0][0] +' 컷') + '```'
					)
			await ctx.send( embed=embed, tts=False)
		else:
			return

	################ 보탐봇 기본 설정확인 ################ 
	@commands.command(name=command[2][0], aliases=command[2][1:])
	async def setting_(ctx):	
		#print (ctx.message.channel.id)
		if ctx.message.channel.id == basicSetting[7]:
			setting_val = '보탐봇버전 : Server Ver. 18 (2020. 7. 4.)\n'
			setting_val += '음성채널 : ' + self.get_channel(basicSetting[6]).name + '\n'
			setting_val += '텍스트채널 : ' + self.get_channel(basicSetting[7]).name +'\n'
			if basicSetting[8] != "" :
				setting_val += '사다리채널 : ' + self.get_channel(int(basicSetting[8])).name + '\n'
			if basicSetting[11] != "" :
				setting_val += '정산채널 : ' + self.get_channel(int(basicSetting[11])).name + '\n'
			if basicSetting[18] != "" :
				setting_val += '척살채널 : ' + self.get_channel(int(basicSetting[18])).name + '\n'
			if basicSetting[19] != "" :
				setting_val += '경주채널 : ' + self.get_channel(int(basicSetting[19])).name + '\n'
			if basicSetting[20] != "" :
				setting_val += '아이템채널 : ' + self.get_channel(int(basicSetting[20])).name + '\n'
			setting_val += '보스젠알림시간1 : ' + basicSetting[1] + ' 분 전\n'
			setting_val += '보스젠알림시간2 : ' + basicSetting[3] + ' 분 전\n'
			setting_val += '보스멍확인시간 : ' + basicSetting[2] + ' 분 후\n'
			embed = discord.Embed(
					title = "----- 설정내용 -----",
					description= f'```{setting_val}```',
					color=0xff00ff
					)
			embed.add_field(
					name="----- Special Thanks to. -----",
					value= '```총무님, 옹님```'
					)
			await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 서버 채널 확인 ################ 
	@commands.command(name=command[3][0], aliases=command[3][1:])
	async def chChk_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			channel_name, channel_id, channel_voice_name, channel_voice_id = await get_guild_channel_info()

			ch_information = []
			cnt = 0
			ch_information.append("")

			ch_voice_information = []
			cntV = 0
			ch_voice_information.append("")

			for guild in client.guilds:
				ch_information[cnt] = f"{ch_information[cnt]}👑  {guild.name}  👑\n"
				for i in range(len(channel_name)):
					for text_channel in guild.text_channels:
						if channel_id[i] == str(text_channel.id):
							if len(ch_information[cnt]) > 900 :
								ch_information.append("")
								cnt += 1
							ch_information[cnt] = f"{ch_information[cnt]}[{channel_id[i]}] {channel_name[i]}\n"

				ch_voice_information[cntV] = f"{ch_voice_information[cntV]}👑  {guild.name}  👑\n"
				for i in range(len(channel_voice_name)):
					for voice_channel in guild.voice_channels:
						if channel_voice_id[i] == str(voice_channel.id):
							if len(ch_voice_information[cntV]) > 900 :
								ch_voice_information.append("")
								cntV += 1
							ch_voice_information[cntV] = f"{ch_voice_information[cntV]}[{channel_voice_id[i]}] {channel_voice_name[i]}\n"
					
			######################

			if len(ch_information) == 1 and len(ch_voice_information) == 1:
				embed = discord.Embed(
					title = "----- 채널 정보 -----",
					description= '',
					color=0xff00ff
					)
				embed.add_field(
					name="< 택스트 채널 >",
					value= '```' + ch_information[0] + '```',
					inline = False
					)
				embed.add_field(
					name="< 보이스 채널 >",
					value= '```' + ch_voice_information[0] + '```',
					inline = False
					)

				await ctx.send( embed=embed, tts=False)
			else :
				embed = discord.Embed(
					title = "----- 채널 정보 -----\n< 택스트 채널 >",
					description= '```' + ch_information[0] + '```',
					color=0xff00ff
					)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(ch_information)-1):
					embed = discord.Embed(
						title = '',
						description= '```' + ch_information[i+1] + '```',
						color=0xff00ff
						)
					await ctx.send( embed=embed, tts=False)
				embed = discord.Embed(
					title = "< 음성 채널 >",
					description= '```' + ch_voice_information[0] + '```',
					color=0xff00ff
					)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(ch_voice_information)-1):
					embed = discord.Embed(
						title = '',
						description= '```' + ch_voice_information[i+1] + '```',
						color=0xff00ff
						)
					await ctx.send( embed=embed, tts=False)
		else:
			return

	################ 텍스트채널이동 ################ 
	@commands.command(name=command[4][0], aliases=command[4][1:])
	async def chMove_(ctx):
		global basicSetting
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			for i in range(len(channel_name)):
				if  channel_name[i] == msg:
					channel = int(channel_id[i])
					
			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith('textchannel ='):
					inputData_textCH[i] = 'textchannel = ' + str(channel) + '\r'
					basicSetting[7] = int(channel)
			
			result_textCH = '\n'.join(inputData_textCH)

			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)
			
			await ctx.send( f"명령어 채널이 < {ctx.message.channel.name} >에서 < {self.get_channel(channel).name} > 로 이동되었습니다.", tts=False)
			await self.get_channel(channel).send( f"< {self.get_channel(channel).name} 이동완료 >", tts=False)
		else:
			return

	################ 보탐봇 음성채널 소환 ################ 
	@commands.has_permissions(manage_messages=True)
	@commands.command(name=command[5][0], aliases=command[5][1:])
	async def connectVoice_(ctx):
		global voice_client1
		global basicSetting
		if ctx.message.channel.id == basicSetting[7]:
			if ctx.voice_client is None:
				if ctx.author.voice:
					voice_client1 = await ctx.author.voice.channel.connect(reconnect = True)
				else:
					await ctx.send('음성채널에 먼저 들어가주세요.', tts=False)
					return
			else:
				if ctx.voice_client.is_playing():
					ctx.voice_client.stop()

				await ctx.voice_client.move_to(ctx.author.voice.channel)

			voice_channel = ctx.author.voice.channel

			print ('< ', basicSetting[6], ' >')
			print ('> ', self.get_channel(voice_channel.id).name, ' <')

			if basicSetting[6] == "":
				inidata_voiceCH = repo.get_contents("test_setting.ini")
				file_data_voiceCH = base64.b64decode(inidata_voiceCH.content)
				file_data_voiceCH = file_data_voiceCH.decode('utf-8')
				inputData_voiceCH = file_data_voiceCH.split('\n')

				for i in range(len(inputData_voiceCH)):
					if inputData_voiceCH[i].startswith('voicechannel ='):
						inputData_voiceCH[i] = 'voicechannel = ' + str(voice_channel.id) + '\r'
						basicSetting[6] = int(voice_channel.id)

				result_voiceCH = '\n'.join(inputData_voiceCH)

				contents = repo.get_contents("test_setting.ini")
				repo.update_file(contents.path, "test_setting", result_voiceCH, contents.sha)

			elif basicSetting[6] != int(voice_channel.id):
				inidata_voiceCH = repo.get_contents("test_setting.ini")
				file_data_voiceCH = base64.b64decode(inidata_voiceCH.content)
				file_data_voiceCH = file_data_voiceCH.decode('utf-8')
				inputData_voiceCH = file_data_voiceCH.split('\n')

				for i in range(len(inputData_voiceCH)):
					if inputData_voiceCH[i].startswith('voicechannel ='):
						inputData_voiceCH[i] = 'voicechannel = ' + str(voice_channel.id) + '\r'
						basicSetting[6] = int(voice_channel.id)

				result_voiceCH = '\n'.join(inputData_voiceCH)

				contents = repo.get_contents("test_setting.ini")
				repo.update_file(contents.path, "test_setting", result_voiceCH, contents.sha)

			await ctx.send('< 음성채널 [' + self.get_channel(voice_channel.id).name + '] 접속완료>', tts=False)
		else:
			return


	################ my_bot.db에 저장된 보스타임 불러오기 ################
	@commands.command(name=command[6][0], aliases=command[6][1:])
	async def loadDB_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			await dbLoad()

			if LoadChk == 0:
				await ctx.send('<불러오기 완료>', tts=False)
			else:
				await ctx.send('<보스타임 정보가 없습니다.>', tts=False)
		else:
			return

	################ 저장된 정보 초기화 ################
	@commands.command(name=command[7][0], aliases=command[7][1:])
	async def initVal_(ctx):
		global basicSetting
		global bossData
		global fixed_bossData

		global bossTime
		global tmp_bossTime
		global fixed_bossTime

		global bossTimeString
		global bossDateString
		global tmp_bossTimeString
		global tmp_bossDateString

		global bossFlag
		global bossFlag0
		global fixed_bossFlag
		global fixed_bossFlag0
		global bossMungFlag
		global bossMungCnt

		global FixedBossDateData
		global indexFixedBossname
			
		if ctx.message.channel.id == basicSetting[7]:
			basicSetting = []
			bossData = []
			fixed_bossData = []

			bossTime = []
			tmp_bossTime = []
			fixed_bossTime = []

			bossTimeString = []
			bossDateString = []
			tmp_bossTimeString = []
			tmp_bossDateString = []

			bossFlag = []
			bossFlag0 = []
			fixed_bossFlag = []
			fixed_bossFlag0 = []
			bossMungFlag = []
			bossMungCnt = []

			FixedBossDateData = []
			indexFixedBossname = []
			
			init()

			await dbSave()

			await ctx.send('< 초기화 완료 >', tts=False)
			print ("< 초기화 완료 >")
		else:
			return


	################ 명존쎄 ################ 
	@commands.command(name=command[8][0], aliases=command[8][1:])
	async def mungchi_(ctx):
		global basicSetting
		global bossTimeString
		global bossDateString
		global bossFlag
		global bossFlag0
		global bossMungFlag

		if ctx.message.channel.id == basicSetting[7]:
			await ctx.send( '< 보탐봇 명치 맞고 숨 고르기 중! 잠시만요! >', tts=False)
			await dbSave()
			print("명치!")
			await voice_client1.disconnect()
			#client.clear()
			raise SystemExit
		else:
			return

	################ 보탐봇 재시작 ################ 
	@commands.command(name=command[9][0], aliases=command[9][1:])
	async def restart_(ctx):
		global basicSetting
		global bossTimeString
		global bossDateString

		if ctx.message.channel.id == basicSetting[7]:
			if basicSetting[2] != '0':
				for i in range(bossNum):
					if bossMungFlag[i] == True:
						bossTimeString[i] = tmp_bossTime[i].strftime('%H:%M:%S')
						bossDateString[i] = tmp_bossTime[i].strftime('%Y-%m-%d')
			await dbSave()
			await data_list_Save("kill_list.ini", "-----척살명단-----", kill_Data)
			await data_list_Save("item_list.ini", "-----아이템목록-----", item_Data)
			await voice_client1.disconnect()
			#await FixedBossDateSave()
			#await self.get_channel(channel).send('<보탐봇 재시작 중... 갑자기 인사해도 놀라지마세요!>', tts=False)
			print("보탐봇강제재시작!")
			await asyncio.sleep(2)

			inidata_restart = repo_restart.get_contents("restart.txt")
			file_data_restart = base64.b64decode(inidata_restart.content)
			file_data_restart = file_data_restart.decode('utf-8')
			inputData_restart = file_data_restart.split('\n')

			if len(inputData_restart) < 3:	
				contents12 = repo_restart.get_contents("restart.txt")
				repo_restart.update_file(contents12.path, "restart_0", "restart\nrestart\nrestrat\n", contents12.sha)
			else:
				contents12 = repo_restart.get_contents("restart.txt")
				repo_restart.update_file(contents12.path, "restart_1", "", contents12.sha)
		else:
			return

	################ 미예약 보스타임 출력 ################ 
	@commands.command(name=command[10][0], aliases=command[10][1:])
	async def nocheckBoss_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			tmp_boss_information = []
			tmp_cnt = 0
			tmp_boss_information.append('')
			
			for i in range(bossNum):
				if bossTimeString[i] == '99:99:99' and bossMungFlag[i] != True :
					if len(tmp_boss_information[tmp_cnt]) > 1800 :
						tmp_boss_information.append('')
						tmp_cnt += 1
					tmp_boss_information[tmp_cnt] = tmp_boss_information[tmp_cnt] + bossData[i][0] + ','

			if len(tmp_boss_information) == 1:
				if len(tmp_boss_information[0]) != 0:
					tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 미예약 보스 -----",
						description= tmp_boss_information[0],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)
			else:
				if len(tmp_boss_information[0]) != 0:
					if len(tmp_boss_information) == 1 :
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
					else:
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
					title = "----- 미예약 보스 -----",
					description= tmp_boss_information[0],
					color=0x0000ff
					)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(tmp_boss_information)-1):
					if len(tmp_boss_information[i+1]) != 0:
						if i == len(tmp_boss_information)-2:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1][:len(tmp_boss_information[i+1])-1] + "\n```"
						else:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1] + "\n```"							
					else :
						tmp_boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= tmp_boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)
		else:
			return

	################ 분배 결과 출력 ################ 
	@commands.command(name=command[11][0], aliases=command[11][1:])
	async def bunbae_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			separate_money = []
			separate_money = msg.split(" ")
			num_sep = floor(int(separate_money[0]))
			cal_tax1 = floor(float(separate_money[1])*0.05)
			
			real_money = floor(floor(float(separate_money[1])) - cal_tax1)
			cal_tax2 = floor(real_money/num_sep) - floor(float(floor(real_money/num_sep))*0.95)
			if num_sep == 0 :
				await ctx.send('```분배 인원이 0입니다. 재입력 해주세요.```', tts=False)
			else :
				embed = discord.Embed(
					title = "----- 분배결과! -----",
					description= '```1차 세금 : ' + str(cal_tax1) + '\n1차 수령액 : ' + str(real_money) + '\n분배자 거래소등록금액 : ' + str(floor(real_money/num_sep)) + '\n2차 세금 : ' + str(cal_tax2) + '\n인당 실수령액 : ' + str(floor(float(floor(real_money/num_sep))*0.95)) + '```',
					color=0xff00ff
					)
				await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 사다리 결과 출력 ################ 
	@commands.command(name=command[12][0], aliases=command[12][1:])
	async def ladder_(ctx):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[8]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			ladder = []
			ladder = msg.split(" ")
			try:
				num_cong = int(ladder[0])
				del(ladder[0])
			except ValueError:
				return await ctx.send('```뽑을 인원은 숫자로 입력바랍니다\nex)!사다리 1 가 나 다 ...```')
			await LadderFunc(num_cong, ladder, ctx)
		else:
			return

	################ 정산확인 ################ 
	@commands.command(name=command[13][0], aliases=command[13][1:])
	async def jungsan_(ctx):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[11]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			if basicSetting[10] !="" and basicSetting[12] !="" and basicSetting[14] !="" and basicSetting[15] !="" and basicSetting[16] !=""  :
				SearchID = msg
				gc = gspread.authorize(credentials)
				wks = gc.open(basicSetting[12]).worksheet(basicSetting[14])

				wks.update_acell(basicSetting[15], SearchID)

				result = wks.acell(basicSetting[16]).value

				embed = discord.Embed(
						description= '```' + SearchID + ' 님이 받을 다이야는 ' + result + ' 다이야 입니다.```',
						color=0xff00ff
						)
				await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 보스타임 일괄 설정 ################
	@commands.command(name=command[14][0], aliases=command[14][1:])
	async def allBossInput_(ctx):
		global basicSetting
		global bossData
		global fixed_bossData

		global bossTime
		global tmp_bossTime

		global fixed_bossTime

		global bossTimeString
		global bossDateString
		global tmp_bossTimeString
		global tmp_bossDateString

		global bossFlag
		global bossFlag0
		global bossMungFlag
		global bossMungCnt
		
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			for i in range(bossNum):
				tmp_msg = msg
				if len(tmp_msg) > 3 :
					if tmp_msg.find(':') != -1 :
						chkpos = tmp_msg.find(':')
						hours1 = tmp_msg[chkpos-2:chkpos]
						minutes1 = tmp_msg[chkpos+1:chkpos+3]
						now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
						tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
						tmp_now = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
					else:
						chkpos = len(tmp_msg)-2
						hours1 = tmp_msg[chkpos-2:chkpos]
						minutes1 = tmp_msg[chkpos:chkpos+2]
						now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
						tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
						tmp_now = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
				else:
					now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
					tmp_now = now2
					
				bossFlag[i] = False
				bossFlag0[i] = False
				bossMungFlag[i] = False
				bossMungCnt[i] = 1

				if tmp_now > now2 :
					tmp_now = tmp_now + datetime.timedelta(days=int(-1))
					
				if tmp_now < now2 : 
					deltaTime = datetime.timedelta(hours = int(bossData[i][1]), minutes = int(bossData[i][5]))
					while now2 > tmp_now :
						tmp_now = tmp_now + deltaTime
						bossMungCnt[i] = bossMungCnt[i] + 1
					now2 = tmp_now
					bossMungCnt[i] = bossMungCnt[i] - 1
				else :
					now2 = now2 + datetime.timedelta(hours = int(bossData[i][1]), minutes = int(bossData[i][5]))
							
				tmp_bossTime[i] = bossTime[i] = nextTime = now2
				tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
				tmp_bossDateString[i] = bossDateString[i] = nextTime.strftime('%Y-%m-%d')

			await dbSave()
			await dbLoad()
			await dbSave()
			
			await ctx.send('<보스 일괄 입력 완료>', tts=False)
			print ("<보스 일괄 입력 완료>")
		else:
			return


	################ 가장 근접한 보스타임 출력 ################ 
	@commands.command(name=command[15][0], aliases=command[15][1:])
	async def nearTimeBoss_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			checkTime = datetime.datetime.now() + datetime.timedelta(days=1, hours = int(basicSetting[0]))
			
			datelist = []
			datelist2 = []
			ouput_bossData = []
			aa = []
			sorted_datelist = []

			for i in range(bossNum):
				if bossMungFlag[i] != True and bossTimeString[i] != '99:99:99' :
					datelist2.append(bossTime[i])

			for i in range(fixed_bossNum):
				if fixed_bossTime[i] < datetime.datetime.now() + datetime.timedelta(hours=int(basicSetting[0])+3):
					datelist2.append(fixed_bossTime[i])

			datelist = list(set(datelist2))

			for i in range(bossNum):
				if bossMungFlag[i] != True :
					aa.append(bossData[i][0])		                 #output_bossData[0] : 보스명
					aa.append(bossTime[i])                           #output_bossData[1] : 시간
					aa.append(bossTime[i].strftime('%H:%M:%S'))      #output_bossData[2] : 시간(00:00:00)
					ouput_bossData.append(aa)
				aa = []

			for i in range(fixed_bossNum):
				aa.append(fixed_bossData[i][0])                      #output_bossData[0] : 보스명
				aa.append(fixed_bossTime[i])                         #output_bossData[1] : 시간
				aa.append(fixed_bossTime[i].strftime('%H:%M:%S'))    #output_bossData[2] : 시간(00:00:00)
				ouput_bossData.append(aa)
				aa = []

			tmp_sorted_datelist = sorted(datelist)

			for i in range(len(tmp_sorted_datelist)):
				if checkTime > tmp_sorted_datelist[i]:
					sorted_datelist.append(tmp_sorted_datelist[i])
			
			if len(sorted_datelist) == 0:
				await ctx.send( '<보스타임 정보가 없습니다.>', tts=False)
			else : 
				result_lefttime = ''
				
				if len(sorted_datelist) > int(basicSetting[9]):
					for j in range(int(basicSetting[9])):
						for i in range(len(ouput_bossData)):
							if sorted_datelist[j] == ouput_bossData[i][1]:
								leftTime = ouput_bossData[i][1] - (datetime.datetime.now()  + datetime.timedelta(hours = int(basicSetting[0])))

								total_seconds = int(leftTime.total_seconds())
								hours, remainder = divmod(total_seconds,60*60)
								minutes, seconds = divmod(remainder,60)

								result_lefttime += '다음 ' + ouput_bossData[i][0] + '탐까지 %02d:%02d:%02d 남았습니다. ' % (hours,minutes,seconds) + '[' +  ouput_bossData[i][2] + ']\n'
				else :
					for j in range(len(sorted_datelist)):
						for i in range(len(ouput_bossData)):						
							if sorted_datelist[j] == ouput_bossData[i][1]:
								leftTime = ouput_bossData[i][1] - (datetime.datetime.now()  + datetime.timedelta(hours = int(basicSetting[0])))

								total_seconds = int(leftTime.total_seconds())
								hours, remainder = divmod(total_seconds,60*60)
								minutes, seconds = divmod(remainder,60)

								result_lefttime += '다음 ' + ouput_bossData[i][0] + '탐까지 %02d:%02d:%02d 남았습니다. ' % (hours,minutes,seconds) + '[' +  ouput_bossData[i][2] + ']\n'
				embed = discord.Embed(
					description= result_lefttime,
					color=0xff0000
					)
				await ctx.send( embed=embed, tts=False)
		else:
			return

	################ 음성파일 생성 후 재생 ################ 			
	@commands.command(name=command[16][0], aliases=command[16][1:])
	async def playText_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			sayMessage = msg
			await MakeSound(ctx.message.author.display_name +'님이, ' + sayMessage, './sound/say')
			await ctx.send("```< " + ctx.author.display_name + " >님이 \"" + sayMessage + "\"```", tts=False)
			await PlaySound(voice_client1, './sound/say.wav')
		else:
			return

	################ 리젠시간 출력 ################
	@commands.command(name=command[17][0], aliases=command[17][1:])
	async def regenTime_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			await ctx.send(embed=regenembed, tts=False)
		else:
			return
			
	################ 현재시간 확인 ################ 
	@commands.command(name=command[18][0], aliases=command[18][1:])
	async def currentTime_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			curruntTime = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
			embed = discord.Embed(
				title = '현재시간은 ' + curruntTime.strftime('%H') + '시 ' + curruntTime.strftime('%M') + '분 ' + curruntTime.strftime('%S')+ '초 입니다.',
				color=0xff00ff
				)
			await ctx.send( embed=embed, tts=False)
		else:
			return

	################ 공지 등록/확인 ################ 
	@commands.command(name=command[19][0], aliases=command[19][1:])
	async def notice_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content.split(" ")
			if len(msg) > 1:
				sayMessage = " ".join(msg[1:])
				contents = repo.get_contents("notice.ini")
				repo.update_file(contents.path, "notice 등록", sayMessage, contents.sha)
				await ctx.send( '< 공지 등록완료 >', tts=False)
			else:
				notice_initdata = repo.get_contents("notice.ini")
				notice = base64.b64decode(notice_initdata.content)
				notice = notice.decode('utf-8')
				if notice != '' :
					embed = discord.Embed(
							description= str(notice),
							color=0xff00ff
							)
				else :
					embed = discord.Embed(
							description= '```등록된 공지가 없습니다.```',
							color=0xff00ff
							)
				await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 공지 삭제 ################ 
	@commands.command(name=command[20][0], aliases=command[20][1:])
	async def noticeDel_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			contents = repo.get_contents("notice.ini")
			repo.update_file(contents.path, "notice 삭제", '', contents.sha)
			await ctx.send( '< 공지 삭제완료 >', tts=False)
		else:
			return

	################ 봇 상태메세지 변경 ################ 
	@commands.command(name=command[21][0], aliases=command[21][1:])
	async def botStatus_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			sayMessage = msg
			await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=sayMessage, type=1), afk = False)
			await ctx.send( '< 상태메세지 변경완료 >', tts=False)
		else:
			return

	################ 보스타임 출력 ################ 
	@commands.command(name=command[22][0], aliases=command[22][1:])
	async def bossTime_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			datelist = []
			datelist2 = []
			ouput_bossData = []
			aa = []
			
			for i in range(bossNum):
				if bossMungFlag[i] == True :
					datelist2.append(tmp_bossTime[i])
				else :
					datelist2.append(bossTime[i])

			for i in range(fixed_bossNum):
				if fixed_bossTime[i] < datetime.datetime.now() + datetime.timedelta(hours=int(basicSetting[0])+3):
					datelist2.append(fixed_bossTime[i])

			datelist = list(set(datelist2))

			tmp_boss_information = []
			tmp_cnt = 0
			tmp_boss_information.append('')

			for i in range(bossNum):
				if bossTimeString[i] == '99:99:99' and bossMungFlag[i] != True :
					if len(tmp_boss_information[tmp_cnt]) > 1000 :
						tmp_boss_information.append('')
						tmp_cnt += 1
					tmp_boss_information[tmp_cnt] = tmp_boss_information[tmp_cnt] + bossData[i][0] + ','
				else :
					aa.append(bossData[i][0])		                     #output_bossData[0] : 보스명
					if bossMungFlag[i] == True :
						aa.append(tmp_bossTime[i])                       #output_bossData[1] : 시간
						aa.append(tmp_bossTime[i].strftime('%H:%M:%S'))  #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(tmp_bossTime[i].strftime('%H:%M'))  
						aa.append('-')	                                 #output_bossData[3] : -
					else :
						aa.append(bossTime[i])                           #output_bossData[1] : 시간
						aa.append(bossTime[i].strftime('%H:%M:%S'))      #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(bossTime[i].strftime('%H:%M'))  
						aa.append('+')	                                 #output_bossData[3] : +
					aa.append(bossData[i][2])                            #output_bossData[4] : 멍/미입력 보스
					aa.append(bossMungCnt[i])	                         #output_bossData[5] : 멍/미입력횟수
					aa.append(bossData[i][6])	                         #output_bossData[6] : 메세지
					ouput_bossData.append(aa)
					aa = []

			for i in range(fixed_bossNum):
				aa.append(fixed_bossData[i][0])                      #output_bossData[0] : 보스명
				aa.append(fixed_bossTime[i])                         #output_bossData[1] : 시간
				aa.append(fixed_bossTime[i].strftime('%H:%M:%S'))    #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(fixed_bossTime[i].strftime('%H:%M'))
				aa.append('@')                                       #output_bossData[3] : @
				aa.append(0)                                         #output_bossData[4] : 멍/미입력 보스
				aa.append(0)                                         #output_bossData[5] : 멍/미입력횟수
				aa.append("")                                        #output_bossData[6] : 메세지
				ouput_bossData.append(aa)
				aa = []

			boss_information = []
			cnt = 0
			boss_information.append('')

			for timestring in sorted(datelist):
				if len(boss_information[cnt]) > 1800 :
					boss_information.append('')
					cnt += 1
				for i in range(len(ouput_bossData)):
					if timestring == ouput_bossData[i][1]:
						if ouput_bossData[i][4] == '0' :
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (미 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'
						else : 
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (멍 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'

			if len(boss_information) == 1 and len(tmp_boss_information) == 1:
				###########################
				if len(boss_information[0]) != 0:
					boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
				else :
					boss_information[0] = '``` ```'

				if len(tmp_boss_information[0]) != 0:
					tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 보스탐 정보 -----",
						description= boss_information[0],
						color=0x0000ff
						)
				embed.add_field(
						name="----- 미예약 보스 -----",
						value= tmp_boss_information[0],
						inline = False
						)				
				await ctx.send( embed=embed, tts=False)
			else : 
				###########################일반보스출력
				if len(boss_information[0]) != 0:
					boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
				else :
					boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 보스탐 정보 -----",
						description= boss_information[0],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(boss_information)-1):
					if len(boss_information[i+1]) != 0:
						boss_information[i+1] = "```diff\n" + boss_information[i+1] + "\n```"
					else :
						boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)
				###########################미예약보스출력
				if len(tmp_boss_information[0]) != 0:
					if len(tmp_boss_information) == 1 :
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
					else:
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
					title = "----- 미예약 보스 -----",
					description= tmp_boss_information[0],
					color=0x0000ff
					)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(tmp_boss_information)-1):
					if len(tmp_boss_information[i+1]) != 0:
						if i == len(tmp_boss_information)-2:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1][:len(tmp_boss_information[i+1])-1] + "\n```"
						else:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1] + "\n```"							
					else :
						tmp_boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= tmp_boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)

			await dbSave()
			await data_list_Save("kill_list.ini", "-----척살명단-----", kill_Data)
			await data_list_Save("item_list.ini", "-----아이템목록-----", item_Data)
		else:
			return

	################ 보스타임 출력 ################ 
	@commands.command(name="ㅄㅌ", aliases=command[22][1:])
	async def bossTime_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			datelist = []
			datelist2 = []
			ouput_bossData = []
			aa = []
			
			for i in range(bossNum):
				if bossMungFlag[i] == True :
					datelist2.append(tmp_bossTime[i])
				else :
					datelist2.append(bossTime[i])

			for i in range(fixed_bossNum):
				if fixed_bossTime[i] < datetime.datetime.now() + datetime.timedelta(hours=int(basicSetting[0])+3):
					datelist2.append(fixed_bossTime[i])

			datelist = list(set(datelist2))

			tmp_boss_information = []
			tmp_cnt = 0
			tmp_boss_information.append('')

			for i in range(bossNum):
				if bossTimeString[i] == '99:99:99' and bossMungFlag[i] != True :
					if len(tmp_boss_information[tmp_cnt]) > 1000 :
						tmp_boss_information.append('')
						tmp_cnt += 1
					tmp_boss_information[tmp_cnt] = tmp_boss_information[tmp_cnt] + bossData[i][0] + ','
				else :
					aa.append(bossData[i][0])		                     #output_bossData[0] : 보스명
					if bossMungFlag[i] == True :
						aa.append(tmp_bossTime[i])                       #output_bossData[1] : 시간
						aa.append(tmp_bossTime[i].strftime('%H:%M:%S'))  #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(tmp_bossTime[i].strftime('%H:%M'))  
						aa.append('-')	                                 #output_bossData[3] : -
					else :
						aa.append(bossTime[i])                           #output_bossData[1] : 시간
						aa.append(bossTime[i].strftime('%H:%M:%S'))      #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(bossTime[i].strftime('%H:%M'))  
						aa.append('+')	                                 #output_bossData[3] : +
					aa.append(bossData[i][2])                            #output_bossData[4] : 멍/미입력 보스
					aa.append(bossMungCnt[i])	                         #output_bossData[5] : 멍/미입력횟수
					aa.append(bossData[i][6])	                         #output_bossData[6] : 메세지
					ouput_bossData.append(aa)
					aa = []

			for i in range(fixed_bossNum):
				aa.append(fixed_bossData[i][0])                      #output_bossData[0] : 보스명
				aa.append(fixed_bossTime[i])                         #output_bossData[1] : 시간
				aa.append(fixed_bossTime[i].strftime('%H:%M:%S'))    #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(fixed_bossTime[i].strftime('%H:%M'))
				aa.append('@')                                       #output_bossData[3] : @
				aa.append(0)                                         #output_bossData[4] : 멍/미입력 보스
				aa.append(0)                                         #output_bossData[5] : 멍/미입력횟수
				aa.append("")                                        #output_bossData[6] : 메세지
				ouput_bossData.append(aa)
				aa = []

			boss_information = []
			cnt = 0
			boss_information.append('')

			for timestring in sorted(datelist):
				if len(boss_information[cnt]) > 1800 :
					boss_information.append('')
					cnt += 1
				for i in range(len(ouput_bossData)):
					if timestring == ouput_bossData[i][1]:
						if ouput_bossData[i][4] == '0' :
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (미 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'
						else : 
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (멍 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'

			if len(boss_information) == 1 and len(tmp_boss_information) == 1:
				###########################
				if len(boss_information[0]) != 0:
					boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
				else :
					boss_information[0] = '``` ```'

				if len(tmp_boss_information[0]) != 0:
					tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 보스탐 정보 -----",
						description= boss_information[0],
						color=0x0000ff
						)
				embed.add_field(
						name="----- 미예약 보스 -----",
						value= tmp_boss_information[0],
						inline = False
						)				
				await ctx.send( embed=embed, tts=False)
			else : 
				###########################일반보스출력
				if len(boss_information[0]) != 0:
					boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
				else :
					boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 보스탐 정보 -----",
						description= boss_information[0],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(boss_information)-1):
					if len(boss_information[i+1]) != 0:
						boss_information[i+1] = "```diff\n" + boss_information[i+1] + "\n```"
					else :
						boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)
				###########################미예약보스출력
				if len(tmp_boss_information[0]) != 0:
					if len(tmp_boss_information) == 1 :
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
					else:
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
					title = "----- 미예약 보스 -----",
					description= tmp_boss_information[0],
					color=0x0000ff
					)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(tmp_boss_information)-1):
					if len(tmp_boss_information[i+1]) != 0:
						if i == len(tmp_boss_information)-2:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1][:len(tmp_boss_information[i+1])-1] + "\n```"
						else:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1] + "\n```"							
					else :
						tmp_boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= tmp_boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)

			await dbSave()
			await data_list_Save("kill_list.ini", "-----척살명단-----", kill_Data)
			await data_list_Save("item_list.ini", "-----아이템목록-----", item_Data)
		else:
			return

	################ 보스타임 출력 ################ 
	@commands.command(name="ㅂㅅㅌ", aliases=command[22][1:])
	async def bossTime_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			datelist = []
			datelist2 = []
			ouput_bossData = []
			aa = []
			
			for i in range(bossNum):
				if bossMungFlag[i] == True :
					datelist2.append(tmp_bossTime[i])
				else :
					datelist2.append(bossTime[i])

			for i in range(fixed_bossNum):
				if fixed_bossTime[i] < datetime.datetime.now() + datetime.timedelta(hours=int(basicSetting[0])+3):
					datelist2.append(fixed_bossTime[i])

			datelist = list(set(datelist2))

			tmp_boss_information = []
			tmp_cnt = 0
			tmp_boss_information.append('')

			for i in range(bossNum):
				if bossTimeString[i] == '99:99:99' and bossMungFlag[i] != True :
					if len(tmp_boss_information[tmp_cnt]) > 1000 :
						tmp_boss_information.append('')
						tmp_cnt += 1
					tmp_boss_information[tmp_cnt] = tmp_boss_information[tmp_cnt] + bossData[i][0] + ','
				else :
					aa.append(bossData[i][0])		                     #output_bossData[0] : 보스명
					if bossMungFlag[i] == True :
						aa.append(tmp_bossTime[i])                       #output_bossData[1] : 시간
						aa.append(tmp_bossTime[i].strftime('%H:%M:%S'))  #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(tmp_bossTime[i].strftime('%H:%M'))  
						aa.append('-')	                                 #output_bossData[3] : -
					else :
						aa.append(bossTime[i])                           #output_bossData[1] : 시간
						aa.append(bossTime[i].strftime('%H:%M:%S'))      #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(bossTime[i].strftime('%H:%M'))  
						aa.append('+')	                                 #output_bossData[3] : +
					aa.append(bossData[i][2])                            #output_bossData[4] : 멍/미입력 보스
					aa.append(bossMungCnt[i])	                         #output_bossData[5] : 멍/미입력횟수
					aa.append(bossData[i][6])	                         #output_bossData[6] : 메세지
					ouput_bossData.append(aa)
					aa = []

			for i in range(fixed_bossNum):
				aa.append(fixed_bossData[i][0])                      #output_bossData[0] : 보스명
				aa.append(fixed_bossTime[i])                         #output_bossData[1] : 시간
				aa.append(fixed_bossTime[i].strftime('%H:%M:%S'))    #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(fixed_bossTime[i].strftime('%H:%M'))
				aa.append('@')                                       #output_bossData[3] : @
				aa.append(0)                                         #output_bossData[4] : 멍/미입력 보스
				aa.append(0)                                         #output_bossData[5] : 멍/미입력횟수
				aa.append("")                                        #output_bossData[6] : 메세지
				ouput_bossData.append(aa)
				aa = []

			boss_information = []
			cnt = 0
			boss_information.append('')

			for timestring in sorted(datelist):
				if len(boss_information[cnt]) > 1800 :
					boss_information.append('')
					cnt += 1
				for i in range(len(ouput_bossData)):
					if timestring == ouput_bossData[i][1]:
						if ouput_bossData[i][4] == '0' :
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (미 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'
						else : 
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (멍 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'

			if len(boss_information) == 1 and len(tmp_boss_information) == 1:
				###########################
				if len(boss_information[0]) != 0:
					boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
				else :
					boss_information[0] = '``` ```'

				if len(tmp_boss_information[0]) != 0:
					tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 보스탐 정보 -----",
						description= boss_information[0],
						color=0x0000ff
						)
				embed.add_field(
						name="----- 미예약 보스 -----",
						value= tmp_boss_information[0],
						inline = False
						)				
				await ctx.send( embed=embed, tts=False)
			else : 
				###########################일반보스출력
				if len(boss_information[0]) != 0:
					boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
				else :
					boss_information[0] = '``` ```'

				embed = discord.Embed(
						title = "----- 보스탐 정보 -----",
						description= boss_information[0],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(boss_information)-1):
					if len(boss_information[i+1]) != 0:
						boss_information[i+1] = "```diff\n" + boss_information[i+1] + "\n```"
					else :
						boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)
				###########################미예약보스출력
				if len(tmp_boss_information[0]) != 0:
					if len(tmp_boss_information) == 1 :
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
					else:
						tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0] + "\n```"
				else :
					tmp_boss_information[0] = '``` ```'

				embed = discord.Embed(
					title = "----- 미예약 보스 -----",
					description= tmp_boss_information[0],
					color=0x0000ff
					)
				await ctx.send( embed=embed, tts=False)
				for i in range(len(tmp_boss_information)-1):
					if len(tmp_boss_information[i+1]) != 0:
						if i == len(tmp_boss_information)-2:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1][:len(tmp_boss_information[i+1])-1] + "\n```"
						else:
							tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1] + "\n```"							
					else :
						tmp_boss_information[i+1] = '``` ```'

					embed = discord.Embed(
							title = '',
							description= tmp_boss_information[i+1],
							color=0x0000ff
							)
					await ctx.send( embed=embed, tts=False)

			await dbSave()
			await data_list_Save("kill_list.ini", "-----척살명단-----", kill_Data)
			await data_list_Save("item_list.ini", "-----아이템목록-----", item_Data)
		else:
			return

	################ 보스타임 출력(고정보스포함) ################ 
	@commands.command(name=command[23][0], aliases=command[23][1:])
	async def bossTime_fixed_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			datelist = []
			datelist2 = []
			ouput_bossData = []
			aa = []
			fixed_datelist = []
			
			for i in range(bossNum):
				if bossMungFlag[i] == True :
					datelist2.append(tmp_bossTime[i])
				else :
					datelist2.append(bossTime[i])

			datelist = list(set(datelist2))

			tmp_boss_information = []
			tmp_cnt = 0
			tmp_boss_information.append('')

			for i in range(bossNum):
				if bossTimeString[i] == '99:99:99' and bossMungFlag[i] != True :
					if len(tmp_boss_information[tmp_cnt]) > 1800 :
						tmp_boss_information.append('')
						tmp_cnt += 1
					tmp_boss_information[tmp_cnt] = tmp_boss_information[tmp_cnt] + bossData[i][0] + ','
				else :
					aa.append(bossData[i][0])		                     #output_bossData[0] : 보스명
					if bossMungFlag[i] == True :
						aa.append(tmp_bossTime[i])                       #output_bossData[1] : 시간
						aa.append(tmp_bossTime[i].strftime('%H:%M:%S'))  #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(tmp_bossTime[i].strftime('%H:%M'))
						aa.append('-')	                                 #output_bossData[3] : -
					else :
						aa.append(bossTime[i])                           #output_bossData[1] : 시간
						aa.append(bossTime[i].strftime('%H:%M:%S'))      #output_bossData[2] : 시간(00:00:00) -> 초빼기 : aa.append(bossTime[i].strftime('%H:%M'))
						aa.append('+')	                                 #output_bossData[3] : +
					aa.append(bossData[i][2])                            #output_bossData[4] : 멍/미입력 보스
					aa.append(bossMungCnt[i])	                         #output_bossData[5] : 멍/미입력횟수
					aa.append(bossData[i][6])	                         #output_bossData[6] : 메세지
					ouput_bossData.append(aa)
					aa = []

			for i in range(fixed_bossNum):
				fixed_datelist.append(fixed_bossTime[i])

			fixed_datelist = list(set(fixed_datelist))

			fixedboss_information = []
			cntF = 0
			fixedboss_information.append('')
					
			for timestring1 in sorted(fixed_datelist):
				if len(fixedboss_information[cntF]) > 1800 :
					fixedboss_information.append('')
					cntF += 1
				for i in range(fixed_bossNum):
					if timestring1 == fixed_bossTime[i]:
						if (datetime.datetime.now() + datetime.timedelta(hours=int(basicSetting[0]))).strftime('%Y-%m-%d') == fixed_bossTime[i].strftime('%Y-%m-%d'):
							tmp_timeSTR = fixed_bossTime[i].strftime('%H:%M:%S') #초빼기 : tmp_timeSTR = fixed_bossTime[i].strftime('%H:%M')
						else:
							tmp_timeSTR = '[' + fixed_bossTime[i].strftime('%Y-%m-%d') + '] ' + fixed_bossTime[i].strftime('%H:%M:%S') #초빼기 : tmp_timeSTR = '[' + fixed_bossTime[i].strftime('%Y-%m-%d') + '] ' + fixed_bossTime[i].strftime('%H:%M')
						fixedboss_information[cntF] = fixedboss_information[cntF] + tmp_timeSTR + ' : ' + fixed_bossData[i][0] + '\n'

			boss_information = []
			cnt = 0
			boss_information.append('')

			for timestring in sorted(datelist):
				if len(boss_information[cnt]) > 1800 :
					boss_information.append('')
					cnt += 1
				for i in range(len(ouput_bossData)):
					if timestring == ouput_bossData[i][1]:
						if ouput_bossData[i][4] == '0' :
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (미 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'
						else : 
							if ouput_bossData[i][5] == 0 :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' ' + ouput_bossData[i][6] + '\n'
							else :
								boss_information[cnt] = boss_information[cnt] + ouput_bossData[i][3] + ' ' + ouput_bossData[i][2] + ' : ' + ouput_bossData[i][0] + ' (멍 ' + str(ouput_bossData[i][5]) + '회)' + ' ' + ouput_bossData[i][6] + '\n'

			###########################고정보스출력
			if len(fixedboss_information[0]) != 0:
				fixedboss_information[0] = "```diff\n" + fixedboss_information[0] + "\n```"
			else :
				fixedboss_information[0] = '``` ```'
	
			embed = discord.Embed(
					title = "----- 고 정 보 스 -----",
					description= fixedboss_information[0],
					color=0x0000ff
					)
			await ctx.send( embed=embed, tts=False)
			for i in range(len(fixedboss_information)-1):
				if len(fixedboss_information[i+1]) != 0:
					fixedboss_information[i+1] = "```diff\n" + fixedboss_information[i+1] + "\n```"
				else :
					fixedboss_information[i+1] = '``` ```'

				embed = discord.Embed(
						title = '',
						description= fixedboss_information[i+1],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)

			###########################일반보스출력
			if len(boss_information[0]) != 0:
				boss_information[0] = "```diff\n" + boss_information[0] + "\n```"
			else :
				boss_information[0] = '``` ```'

			embed = discord.Embed(
					title = "----- 보스탐 정보 -----",
					description= boss_information[0],
					color=0x0000ff
					)
			await ctx.send( embed=embed, tts=False)
			for i in range(len(boss_information)-1):
				if len(boss_information[i+1]) != 0:
					boss_information[i+1] = "```diff\n" + boss_information[i+1] + "\n```"
				else :
					boss_information[i+1] = '``` ```'

				embed = discord.Embed(
						title = '',
						description= boss_information[i+1],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)

			###########################미예약보스출력
			if len(tmp_boss_information[0]) != 0:
				if len(tmp_boss_information) == 1 :
					tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0][:len(tmp_boss_information[0])-1] + "\n```"
				else:
					tmp_boss_information[0] = "```fix\n" + tmp_boss_information[0] + "\n```"
			else :
				tmp_boss_information[0] = '``` ```'

			embed = discord.Embed(
				title = "----- 미예약 보스 -----",
				description= tmp_boss_information[0],
				color=0x0000ff
				)
			await ctx.send( embed=embed, tts=False)
			for i in range(len(tmp_boss_information)-1):
				if len(tmp_boss_information[i+1]) != 0:
					if i == len(tmp_boss_information)-2:
						tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1][:len(tmp_boss_information[i+1])-1] + "\n```"
					else:
						tmp_boss_information[i+1] = "```fix\n" + tmp_boss_information[i+1] + "\n```"
				else :
					tmp_boss_information[i+1] = '``` ```'

				embed = discord.Embed(
						title = '',
						description= tmp_boss_information[i+1],
						color=0x0000ff
						)
				await ctx.send( embed=embed, tts=False)

			await dbSave()
			await data_list_Save("kill_list.ini", "-----척살명단-----", kill_Data)
			await data_list_Save("item_list.ini", "-----아이템목록-----", item_Data)
		else:
			return

	################ 킬초기화 ################ 
	@commands.command(name=command[24][0], aliases=command[24][1:])
	async def killInit_(ctx):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[18]:
			global kill_Data

			kill_Data = {}
			
			await init_data_list('kill_list.ini', '-----척살명단-----')
			return await ctx.send( '< 킬 목록 초기화완료 >', tts=False)
		else:
			return

	################ 킬명단 확인 및 추가################ 
	@commands.command(name=command[25][0], aliases=command[25][1:]) 
	async def killList_(ctx, *, args : str = None):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[18]:
			global kill_Data

			if not args:
				kill_output = ''
				for key, value in kill_Data.items():
					kill_output += ':skull_crossbones: ' + str(key) + ' : ' + str(value) + '번 따히!\n'

				if kill_output != '' :
					embed = discord.Embed(
							description= str(kill_output),
							color=0xff00ff
							)
				else :
					embed = discord.Embed(
							description= '등록된 킬 목록이 없습니다. 분발하세요!',
							color=0xff00ff
							)
				return await ctx.send(embed=embed, tts=False)

			if args in kill_Data:
				kill_Data[args] += 1
			else:
				kill_Data[args] = 1
					
			embed = discord.Embed(
					description= ':skull_crossbones: ' + args + ' 따히! [' + str(kill_Data[args]) + '번]\n',
					color=0xff00ff
					)
			return await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 킬삭제 ################ 
	@commands.command(name=command[26][0], aliases=command[26][1:])
	async def killDel_(ctx, *, args : str = None):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[18]:
			global kill_Data
			
			if not args:
				return await ctx.send( '```제대로 된 아이디를 입력해주세요!\n```', tts=False)
			
			if args in kill_Data:
				del kill_Data[args]
				return await ctx.send( ':angel: ' + args + ' 삭제완료!', tts=False)
			else :				
				return await ctx.send( '```킬 목록에 등록되어 있지 않습니다!\n```', tts=False)
		else:
			return

	################ 킬 차감 ################ 
	@commands.command(name=command[33][0], aliases=command[33][1:]) 
	async def killSubtract_(ctx, *, args : str = None):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[18]:
			global kill_Data

			if not args:
				return await ctx.send(f'{command[33][0]} [아이디] 혹은 {command[33][0]} [아이디] [횟수] 양식에 맞춰 입력해주세요!', tts = False)

			input_data = args.split()
			
			if len(input_data) == 1:
				kill_name = args
				count = 1
			elif len(input_data) == 2:
				kill_name = input_data[0]
				try:
					count = int(input_data[1])
				except ValueError:
					return await ctx.send(f'[횟수]는 숫자로 입력바랍니다')
			else:
				return await ctx.send(f'{command[33][0]} [아이디] 혹은 {command[33][0]} [아이디] [횟수] 양식에 맞춰 입력해주세요!', tts = False)

			if kill_name in kill_Data:
				if kill_Data[kill_name] < int(count):
					return await ctx.send( f"등록된 킬 횟수[{str(kill_Data[kill_name])}번]보다 차감 횟수[{str(count)}번]가 많습니다. 킬 횟수에 맞게 재입력 바랍니다.", tts=False)
				else:
					kill_Data[kill_name] -= int(count)
			else:
				return await ctx.send( '```킬 목록에 등록되어 있지 않습니다!\n```', tts=False)
					
			embed = discord.Embed(
					description= f':angel: [{kill_name}] [{str(count)}번] 차감 완료! [잔여 : {str(kill_Data[kill_name])}번]\n',
					color=0xff00ff
					)
			
			if kill_Data[kill_name] == 0:
				del kill_Data[kill_name]

			return await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 경주 ################ 
	@commands.command(name=command[27][0], aliases=command[27][1:])
	async def race_(ctx):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[19]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			race_info = []
			fr = []
			racing_field = []
			str_racing_field = []
			cur_pos = []
			race_val = []
			random_pos = []
			racing_result = []
			output = ':camera: :camera: :camera: 신나는 레이싱! :camera: :camera: :camera:\n'
			#racing_unit = [':giraffe:', ':elephant:', ':tiger2:', ':hippopotamus:', ':crocodile:',':leopard:',':ox:', ':sheep:', ':pig2:',':dromedary_camel:',':dragon:',':rabbit2:'] #동물스킨
			#racing_unit = [':red_car:', ':taxi:', ':bus:', ':trolleybus:', ':race_car:', ':police_car:', ':ambulance:', ':fire_engine:', ':minibus:', ':truck:', ':articulated_lorry:', ':tractor:', ':scooter:', ':manual_wheelchair:', ':motor_scooter:', ':auto_rickshaw:', ':blue_car:', ':bike:', ':helicopter:', ':steam_locomotive:']  #탈것스킨
			#random.shuffle(racing_unit) 
			racing_member = msg.split(" ")

			racing_unit = []

			emoji = discord.Emoji
			emoji = ctx.message.guild.emojis

			for j in range(len(tmp_racing_unit)):
				racing_unit.append(':' + tmp_racing_unit[j] + ':')
				for i in range(len(emoji)):
					if emoji[i].name == tmp_racing_unit[j].strip(":"):
						racing_unit[j] = '<:' + tmp_racing_unit[j] + ':' + str(emoji[i].id) + '>'

			random.shuffle(racing_unit)

			field_size = 60
			tmp_race_tab = 35 - len(racing_member)
			if len(racing_member) <= 1:
				await ctx.send('레이스 인원이 2명보다 작습니다.')
				return
			elif len(racing_member) >= 13:
				await ctx.send('레이스 인원이 12명 초과입니다.')
				return
			else :
				race_val = random.sample(range(tmp_race_tab, tmp_race_tab+len(racing_member)), len(racing_member))
				random.shuffle(race_val)
				for i in range(len(racing_member)):
					fr.append(racing_member[i])
					fr.append(racing_unit[i])
					fr.append(race_val[i])
					race_info.append(fr)
					fr = []
					for i in range(field_size):
						fr.append(" ")
					racing_field.append(fr)
					fr = []

				for i in range(len(racing_member)):
					racing_field[i][0] = "|"
					racing_field[i][field_size-2] = race_info[i][1]
					if len(race_info[i][0]) > 5:
						racing_field[i][field_size-1] = "| " + race_info[i][0][:5] + '..'
					else:
						racing_field[i][field_size-1] = "| " + race_info[i][0]
					str_racing_field.append("".join(racing_field[i]))
					cur_pos.append(field_size-2)
				
				for i in range(len(racing_member)):
					output +=  str_racing_field[i] + '\n'

				result_race = await ctx.send(output + ':traffic_light: 3초 후 경주가 시작됩니다!')
				await asyncio.sleep(1)
				await result_race.edit(content = output + ':traffic_light: 2초 후 경주가 시작됩니다!')
				await asyncio.sleep(1)
				await result_race.edit(content = output + ':traffic_light: 1초 후 경주가 시작됩니다!')
				await asyncio.sleep(1)
				await result_race.edit(content = output + ':checkered_flag:  경주 시작!')								

				for i in range(len(racing_member)):
					test = random.sample(range(2,field_size-2), race_info[i][2])
					while len(test) != tmp_race_tab + len(racing_member)-1 :
						test.append(1)
					test.append(1)
					test.sort(reverse=True)
					random_pos.append(test)

				for j in range(len(random_pos[0])):
					if j%2 == 0:
						output =  ':camera: :camera_with_flash: :camera: 신나는 레이싱! :camera_with_flash: :camera: :camera_with_flash:\n'
					else :
						output =  ':camera_with_flash: :camera: :camera_with_flash: 신나는 레이싱! :camera: :camera_with_flash: :camera:\n'
					str_racing_field = []
					for i in range(len(racing_member)):
						temp_pos = cur_pos[i]
						racing_field[i][random_pos[i][j]], racing_field[i][temp_pos] = racing_field[i][temp_pos], racing_field[i][random_pos[i][j]]
						cur_pos[i] = random_pos[i][j]
						str_racing_field.append("".join(racing_field[i]))

					await asyncio.sleep(1) 

					for i in range(len(racing_member)):
						output +=  str_racing_field[i] + '\n'
					
					await result_race.edit(content = output + ':checkered_flag:  경주 시작!')
				
				for i in range(len(racing_field)):
					fr.append(race_info[i][0])
					fr.append((race_info[i][2]) - tmp_race_tab + 1)
					racing_result.append(fr)
					fr = []

				result = sorted(racing_result, key=lambda x: x[1])

				result_str = ''
				for i in range(len(result)):
					if result[i][1] == 1:
						result[i][1] = ':first_place:'
					elif result[i][1] == 2:
						result[i][1] = ':second_place:'
					elif result[i][1] == 3:
						result[i][1] = ':third_place:'
					elif result[i][1] == 4:
						result[i][1] = ':four:'
					elif result[i][1] == 5:
						result[i][1] = ':five:'
					elif result[i][1] == 6:
						result[i][1] = ':six:'
					elif result[i][1] == 7:
						result[i][1] = ':seven:'
					elif result[i][1] == 8:
						result[i][1] = ':eight:'
					elif result[i][1] == 9:
						result[i][1] = ':nine:'
					elif result[i][1] == 10:
						result[i][1] = ':keycap_ten:'
					else:
						result[i][1] = ':x:'
					result_str += result[i][1] + "  " + result[i][0] + "  "
					
				#print(result)
				await asyncio.sleep(1)
				return await result_race.edit(content = output + ':tada: 경주 종료!\n' + result_str)
		else:
			return

	################ 보탐봇 입장 ################ 	
	@commands.command(name=command[28][0], aliases=command[28][1:])
	async def set_channel_(ctx):
		global basicSetting

		msg = ctx.message.content[len(ctx.invoked_with)+1:]
		channel = ctx.message.channel.id #메세지가 들어온 채널 ID

		if msg == '사다리' : #사다리 채널 설정
			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith('ladderchannel'):
					inputData_textCH[i] = 'ladderchannel = ' + str(channel) + '\r'
					basicSetting[8] = channel
			result_textCH = '\n'.join(inputData_textCH)

			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

			print(f'< 사다리채널 [{ctx.message.channel.name}] 설정완료 >')
			return await ctx.send(f'< 사다리채널 [{ctx.message.channel.name}] 설정완료 >', tts=False)
		elif msg == '정산' :
			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith('jungsanchannel'):
					inputData_textCH[i] = 'jungsanchannel = ' + str(channel) + '\r'
					basicSetting[11] = channel
			result_textCH = '\n'.join(inputData_textCH)

			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

			print(f'< 정산채널 [{ctx.message.channel.name}] 설정완료 >')
			return await ctx.send(f'< 정산채널 [{ctx.message.channel.name}] 설정완료 >', tts=False)			
		elif msg == '척살' :
			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith('killchannel'):
					inputData_textCH[i] = 'killchannel = ' + str(channel) + '\r'
					basicSetting[18] = channel
			result_textCH = '\n'.join(inputData_textCH)

			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

			print(f'< 척살채널 [{ctx.message.channel.name}] 설정완료 >')
			return await ctx.send(f'< 척살채널 [{ctx.message.channel.name}] 설정완료 >', tts=False)
		elif msg == '경주' :
			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith('racingchannel'):
					inputData_textCH[i] = 'racingchannel = ' + str(channel) + '\r'
					basicSetting[19] = channel
			result_textCH = '\n'.join(inputData_textCH)

			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

			print(f'< 경주채널 [{ctx.message.channel.name}] 설정완료 >')
			return await ctx.send(f'< 경주채널 [{ctx.message.channel.name}] 설정완료 >', tts=False)
		elif msg == '아이템' :
			inidata_textCH = repo.get_contents("test_setting.ini")
			file_data_textCH = base64.b64decode(inidata_textCH.content)
			file_data_textCH = file_data_textCH.decode('utf-8')
			inputData_textCH = file_data_textCH.split('\n')
			
			for i in range(len(inputData_textCH)):
				if inputData_textCH[i].startswith('itemchannel'):
					inputData_textCH[i] = 'itemchannel = ' + str(channel) + '\r'
					basicSetting[20] = channel
			result_textCH = '\n'.join(inputData_textCH)

			contents = repo.get_contents("test_setting.ini")
			repo.update_file(contents.path, "test_setting", result_textCH, contents.sha)

			print(f'< 아이템채널 [{ctx.message.channel.name}] 설정완료 >')
			return await ctx.send(f'< 아이템채널 [{ctx.message.channel.name}] 설정완료 >', tts=False)
		else :
			return await ctx.send(f'```올바른 명령어를 입력해주세요.```', tts=False)

	################ 아이템초기화 확인 ################ 
	@commands.command(name=command[29][0], aliases=command[29][1:])
	async def itemInit_(ctx):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[20]:
			global item_Data

			item_Data = {}

			await init_data_list('item_list.ini', '-----아이템 목록-----')
			return await ctx.send( '< 아이템 목록 초기화완료 >', tts=False)
		else:
			return

	################ 아이템 목록 확인 및 추가 ################ 
	@commands.command(name=command[30][0], aliases=command[30][1:]) 
	async def itemList_(ctx, *, args : str = None):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[20]:
			global item_Data
			
			if not args:
				sorted_item_list = sorted(item_Data.items(), key=lambda x: x[0])

				embed_list : list = []
				embed_index : int = 0
				embed_cnt : int = 0
				embed = discord.Embed(title = '', description = f'`{client.user.name}\'s 창고`', color = 0x00ff00)
				
				embed_list.append(embed)

				if len(sorted_item_list) > 0 :
					for item_id, count in sorted_item_list:
						embed_cnt += 1
						if embed_cnt > 24 :
							embed_cnt = 0
							embed_index += 1
							tmp_embed = discord.Embed(
								title = "",
								description = "",
								color=0x00ff00
								)
							embed_list.append(tmp_embed)
						embed_list[embed_index].add_field(name = item_id, value = count)
					embed_list[len(embed_list)-1].set_footer(text = f"전체 아이템 종류  :  {len(item_Data)}개")
					if len(embed_list) > 1:
						for embed_data in embed_list:
							await asyncio.sleep(0.1)
							await ctx.send(embed = embed_data)
						return
					else:
						return await ctx.send(embed=embed, tts=False)
				else :
					embed.add_field(name = '\u200b\n', value = '창고가 비었습니다.\n\u200b')
					return await ctx.send(embed=embed, tts=False)

			input_data = args.split()
			
			if len(input_data) == 1:
				item_name = args
				count = 1
			elif len(input_data) == 2:
				item_name = input_data[0]
				try:
					count = int(input_data[1])
				except ValueError:
					return await ctx.send(f'아이템 [개수]는 숫자로 입력바랍니다')
			else:
				return await ctx.send(f'{command[30][0]} [아이템명] 혹은 {command[30][0]} [아이템명] [개수] 양식에 맞춰 입력해주세요!', tts = False)	

			if item_name in item_Data:
				item_Data[item_name] += int(count)
			else:
				item_Data[item_name] = int(count)
					
			embed = discord.Embed(
					description= f':inbox_tray: **[{item_name}] [{str(count)}개]** 등록 완료! [잔여 : {str(item_Data[item_name])}개]\n',
					color=0xff00ff
					)
			return await ctx.send(embed=embed, tts=False)

		else:
			return

	################ 아이템 삭제 ################ 
	@commands.command(name=command[31][0], aliases=command[31][1:])
	async def itemDel_(ctx, *, args : str = None):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[20]:
			global item_Data

			if not args:
				return await ctx.send( f'{command[31][0]} [아이템명] 양식에 맞춰 입력해주세요!', tts = False)

			if args in item_Data:
				del item_Data[args]
				embed = discord.Embed(
					description= ':outbox_tray: ' + args + ' 삭제완료!',
					color=0xff00ff
					)
				return await ctx.send(embed=embed, tts=False)
			else :				
				return await ctx.send( '```아이템 목록에 등록되어 있지 않습니다!\n```', tts=False)
		else:
			return

	################ 아이템 차감 ################ 
	@commands.command(name=command[32][0], aliases=command[32][1:]) 
	async def itemSubtract_(ctx, *, args : str = None):
		if ctx.message.channel.id == basicSetting[7] or ctx.message.channel.id == basicSetting[20]:
			global item_Data

			if not args:
				return await ctx.send(f'{command[32][0]} [아이템명] 혹은 {command[32][0]} [아이템명] [개수] 양식에 맞춰 입력해주세요!', tts = False)

			input_data = args.split()
			
			if len(input_data) == 1:
				item_name = args
				count = 1
			elif len(input_data) == 2:
				item_name = input_data[0]
				try:
					count = int(input_data[1])
				except ValueError:
					return await ctx.send(f'아이템 [개수]는 숫자로 입력바랍니다')
			else:
				return await ctx.send(f'{command[32][0]} [아이템명] 혹은 {command[32][0]} [아이템명] [개수] 양식에 맞춰 입력해주세요!', tts = False)	

			if item_name in item_Data:
				if item_Data[item_name] < int(count):
					return await ctx.send( f"등록된 아이템 개수[{str(item_Data[item_name])}개]보다 차감 개수[{str(count)}개]가 많습니다. 등록 개수에 맞게 재입력 바랍니다.", tts=False)
				else:
					item_Data[item_name] -= int(count)
			else:
				return await ctx.send( '```아이템 목록에 등록되어 있지 않습니다!\n```', tts=False)
					
			embed = discord.Embed(
					description= f':outbox_tray: **[{item_name}] [{str(count)}개]** 차감 완료! [잔여 : {str(item_Data[item_name])}개]\n',
					color=0xff00ff
					)
			
			if item_Data[item_name] == 0:
				del item_Data[item_name]

			return await ctx.send(embed=embed, tts=False)
		else:
			return

	################ 서버 나가기 ################ 		
	@commands.has_permissions(manage_messages=True)
	@commands.command(name=command[34][0], aliases=command[34][1:])
	async def leaveGuild_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			guild_list : str = ""
			guild_name : str = ""

			for i, gulid_name in enumerate(client.guilds):
				guild_list += f"`{i+1}.` {gulid_name}\n"

			embed = discord.Embed(
				title = "----- 서버 목록 -----",
				description = guild_list,
				color=0x00ff00
				)
			await ctx.send(embed = embed)

			try:
				await ctx.send(f"```떠나고 싶은 서버의 [숫자]를 입력하여 선택해 주세요```")
				message_result : discord.Message = await client.wait_for("message", timeout = 10, check=(lambda message: message.channel == ctx.message.channel and message.author == ctx.message.author))
			except asyncio.TimeoutError:
				return await ctx.send(f"```서버 선택 시간이 초과됐습니다! 필요시 명령어를 재입력해 주세요```")
				
			try:
				guild_name = client.guilds[int(message_result.content)-1].name
				await client.get_guild(client.guilds[int(message_result.content)-1].id).leave()
				return await ctx.send(f"```[{guild_name}] 서버에서 떠났습니다.!```")
			except ValueError:
				return			

	################ ?????????????? ################ 
	@commands.command(name='!오빠')
	async def brother1_(ctx):
		await PlaySound(voice_client1, './sound/오빠.mp3')

	@commands.command(name='!언니')
	async def sister_(ctx):
		await PlaySound(voice_client1, './sound/언니.mp3')

	@commands.command(name='!형')
	async def brother2_(ctx):
		await PlaySound(voice_client1, './sound/형.mp3')
	
	@commands.command(name='!TJ', aliases=['!tj'])
	async def TJ_(ctx):
		resultTJ = random.randrange(1,9)
		await PlaySound(voice_client1, './sound/TJ' + str(resultTJ) +'.mp3')


	@client.event
	async def on_command_error(ctx, error):
		if isinstance(error, CommandNotFound):
			return
		elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
			return
		elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
			return await ctx.send(f"**[{ctx.message.content}]** 명령을 사용할 권한이 없습니다.!")
		raise error

	# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
	@client.event
	async def on_message(msg):
		await client.wait_until_ready()
		if msg.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
			return None #동작하지 않고 무시합니다.

		ori_msg = msg

		global channel
		
		global basicSetting
		global bossData
		global fixed_bossData

		global bossNum
		global fixed_bossNum
		global chkvoicechannel
		global chkrelogin

		global bossTime
		global tmp_bossTime

		global fixed_bossTime

		global bossTimeString
		global bossDateString
		global tmp_bossTimeString
		global tmp_bossDateString

		global bossFlag
		global bossFlag0
		global bossMungFlag
		global bossMungCnt
		
		global voice_client1
		
		global channel_info
		global channel_name
		global channel_id
		global channel_voice_name
		global channel_voice_id
		global channel_type
		
		global chflg
		global LoadChk
		
		global indexFixedBossname
		global FixedBossDateData
		
		global gc #정산
		global credentials	#정산

		global regenembed
		global command
		global kill_Data
		
		id = msg.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
		
		if chflg == 1 :
			if self.get_channel(basicSetting[7]).id == msg.channel.id:
				channel = basicSetting[7]
				message = msg

				hello = message.content

				for i in range(bossNum):
					################ 보스 컷처리 ################ 
					if message.content.startswith(bossData[i][0] +'컷') or message.content.startswith(convertToInitialLetters(bossData[i][0] +'컷')) or message.content.startswith(bossData[i][0] +' 컷') or message.content.startswith(convertToInitialLetters(bossData[i][0] +' 컷')):
						if hello.find('  ') != -1 :
							bossData[i][6] = hello[hello.find('  ')+2:]
							hello = hello[:hello.find('  ')]
						else:
							bossData[i][6] = ''
							
						tmp_msg = bossData[i][0] +'컷'
						if len(hello) > len(tmp_msg) + 3 :
							if hello.find(':') != -1 :
								chkpos = hello.find(':')
								hours1 = hello[chkpos-2:chkpos]
								minutes1 = hello[chkpos+1:chkpos+3]
								now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
							else:
								chkpos = len(hello)-2
								hours1 = hello[chkpos-2:chkpos]
								minutes1 = hello[chkpos:chkpos+2]
								now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
						else:
							now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
							tmp_now = now2

						bossFlag[i] = False
						bossFlag0[i] = False
						bossMungFlag[i] = False
						bossMungCnt[i] = 0

						if tmp_now > now2 :
							tmp_now = tmp_now + datetime.timedelta(days=int(-1))
							
						if tmp_now < now2 : 
							deltaTime = datetime.timedelta(hours = int(bossData[i][1]), minutes = int(bossData[i][5]))
							while now2 > tmp_now :
								tmp_now = tmp_now + deltaTime
								bossMungCnt[i] = bossMungCnt[i] + 1
							now2 = tmp_now
							bossMungCnt[i] = bossMungCnt[i] - 1
						else :
							now2 = now2 + datetime.timedelta(hours = int(bossData[i][1]), minutes = int(bossData[i][5]))
									
						tmp_bossTime[i] = bossTime[i] = nextTime = now2
						tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
						tmp_bossDateString[i] = bossDateString[i] = nextTime.strftime('%Y-%m-%d')
						embed = discord.Embed(
								description= '```다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.```',
								color=0xff0000
								)
						await self.get_channel(channel).send(embed=embed, tts=False)

					################ 보스 멍 처리 ################ 

					if message.content.startswith(bossData[i][0] +'멍') or message.content.startswith(bossData[i][0] +' 멍'):
						if hello.find('  ') != -1 :
							bossData[i][6] = hello[hello.find('  ')+2:]
							hello = hello[:hello.find('  ')]
						else:
							bossData[i][6] = ''
							
						tmp_msg = bossData[i][0] +'멍'
						tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))

						if len(hello) > len(tmp_msg) + 3 :
							temptime = tmp_now
							if hello.find(':') != -1 :
								chkpos = hello.find(':')
								hours1 = hello[chkpos-2:chkpos] 
								minutes1 = hello[chkpos+1:chkpos+3]					
								temptime = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
							else:
								chkpos = len(hello)-2
								hours1 = hello[chkpos-2:chkpos]
								minutes1 = hello[chkpos:chkpos+2]					
								temptime = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
							
							bossMungCnt[i] = 0
							bossFlag[i] = False
							bossFlag0[i] = False
							bossMungFlag[i] = False

							if temptime > tmp_now :
								temptime = temptime + datetime.timedelta(days=int(-1))

							if temptime < tmp_now :
								deltaTime = datetime.timedelta(hours = int(bossData[i][1]), minutes = int(bossData[i][5]))
								while temptime < tmp_now :
									temptime = temptime + deltaTime
									bossMungCnt[i] = bossMungCnt[i] + 1

							tmp_bossTime[i] = bossTime[i] = temptime				

							tmp_bossTimeString[i] = bossTimeString[i] = temptime.strftime('%H:%M:%S')
							tmp_bossDateString[i] = bossDateString[i] = temptime.strftime('%Y-%m-%d')
							embed = discord.Embed(
									description= '```다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.```',
									color=0xff0000
									)
							await self.get_channel(channel).send(embed=embed, tts=False)
						else:
							if tmp_bossTime[i] < tmp_now :

								nextTime = tmp_bossTime[i] + datetime.timedelta(hours = int(bossData[i][1]), minutes = int(bossData[i][5]))

								bossFlag[i] = False
								bossFlag0[i] = False
								bossMungFlag[i] = False
								bossMungCnt[i] = bossMungCnt[i] + 1

								tmp_bossTime[i] = bossTime[i] = nextTime				

								tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
								tmp_bossDateString[i] = bossDateString[i] = nextTime.strftime('%Y-%m-%d')
								embed = discord.Embed(
										description= '```다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.```',
										color=0xff0000
										)
								await self.get_channel(channel).send(embed=embed, tts=False)
							else:
								await self.get_channel(channel).send('```' + bossData[i][0] + '탐이 아직 안됐습니다. 다음 ' + bossData[i][0] + '탐 [' + tmp_bossTimeString[i] + '] 입니다```', tts=False)

						
				################ 예상 보스 타임 입력 ################ 

					if message.content.startswith(bossData[i][0] +'예상')  or message.content.startswith(bossData[i][0] +' 예상'):
						if hello.find('  ') != -1 :
							bossData[i][6] = hello[hello.find('  ')+2:]
							hello = hello[:hello.find('  ')]
						else:
							bossData[i][6] = ''
							
						tmp_msg = bossData[i][0] +'예상'
						if len(hello) > len(tmp_msg) + 4 :
							if hello.find(':') != -1 :
								chkpos = hello.find(':')
								hours1 = hello[chkpos-2:chkpos]
								minutes1 = hello[chkpos+1:chkpos+3]
								now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
							else:
								chkpos = len(hello)-2
								hours1 = hello[chkpos-2:chkpos]
								minutes1 = hello[chkpos:chkpos+2]
								now2 = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = datetime.datetime.now() + datetime.timedelta(hours = int(basicSetting[0]))
								tmp_now = tmp_now.replace(hour=int(hours1), minute=int(minutes1))
							
							bossFlag[i] = False
							bossFlag0[i] = False
							bossMungFlag[i] = False
							bossMungCnt[i] = 0

							if tmp_now < now2 :
								tmp_now = tmp_now + datetime.timedelta(days=int(1))

							tmp_bossTime[i] = bossTime[i] = nextTime = tmp_now
							tmp_bossTimeString[i] = bossTimeString[i] = nextTime.strftime('%H:%M:%S')
							tmp_bossDateString[i] = bossDateString[i] = nextTime.strftime('%Y-%m-%d')
							embed = discord.Embed(
									description= '```다음 ' + bossData[i][0] + ' ' + bossTimeString[i] + '입니다.```',
									color=0xff0000
									)
							await self.get_channel(channel).send(embed=embed, tts=False)
						else:
							await self.get_channel(channel).send('```' + bossData[i][0] +' 예상 시간을 입력해주세요.```', tts=False)
							
					################ 보스타임 삭제 ################
						
					if message.content == bossData[i][0] +'삭제' or message.content == bossData[i][0] +' 삭제':
						bossTime[i] = datetime.datetime.now()+datetime.timedelta(days=365, hours = int(basicSetting[0]))
						tmp_bossTime[i] =  datetime.datetime.now()+datetime.timedelta(days=365, hours = int(basicSetting[0]))
						bossTimeString[i] = '99:99:99'
						bossDateString[i] = '9999-99-99'
						tmp_bossTimeString[i] = '99:99:99'
						tmp_bossDateString[i] = '9999-99-99'
						bossFlag[i] = False
						bossFlag0[i] = False
						bossMungFlag[i] = False
						bossMungCnt[i] = 0
						await self.get_channel(channel).send('<' + bossData[i][0] + ' 삭제완료>', tts=False)
						await dbSave()
						print ('<' + bossData[i][0] + ' 삭제완료>')
					
					################ 보스별 메모 ################ 

					if message.content.startswith(bossData[i][0] +'메모 '):
						
						tmp_msg = bossData[i][0] +'메모 '
						
						bossData[i][6] = hello[len(tmp_msg):]
						await self.get_channel(channel).send('< ' + bossData[i][0] + ' [ ' + bossData[i][6] + ' ] 메모등록 완료>', tts=False)
						
					if message.content.startswith(bossData[i][0] +'메모삭제'):
						
						bossData[i][6] = ''
						await self.get_channel(channel).send('< ' + bossData[i][0] + ' 메모삭제 완료>', tts=False)

		await client.process_commands(ori_msg)

	#client.loop.create_task(task())

	#try:
	#	client.loop.run_until_complete(client.start(access_token))
	#except SystemExit:
	#	handle_exit()
	#except KeyboardInterrupt:
	#	handle_exit()
	#client.loop.close()
	#print("Program ended")
	#break

	#print("Bot restarting")
	#client = discord.Client(loop=client.loop)
	#client = commands.Bot(command_prefix="", help_command = None, description='일상디코봇')

ilsang_distribution_bot : IlsangDistributionBot = IlsangDistributionBot()
ilsang_distribution_bot.add_cog(settingCog(ilsang_distribution_bot))
ilsang_distribution_bot.add_cog(adminCog(ilsang_distribution_bot))
ilsang_distribution_bot.add_cog(memberCog(ilsang_distribution_bot))
ilsang_distribution_bot.add_cog(manageCog(ilsang_distribution_bot))
ilsang_distribution_bot.add_cog(bankCog(ilsang_distribution_bot))
ilsang_distribution_bot.add_cog(bossCog(ilsang_distribution_bot))
ilsang_distribution_bot.run()
