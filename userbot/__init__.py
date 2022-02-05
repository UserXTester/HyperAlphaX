# Abundant

# Copyright (C) 2020 by AlphaXProject @Github, 
#
# This file is part of https://t.me/AlphaXProject  project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://t.me/AlphaXProject  >
#
# All rights reserved.
#
# Created by : https://t.me/AlphaXProject 
# Support by : https://t.me/AliansiAlphaX 


import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import HNDLR, BOT_TOKEN, BOT_HNDLR, ALIVE_NAME, ALIVE_LOGO, BOTLOG_CHATID, HASH_CHAT, REPO_LINK, STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, HEROKU_API_KEY, UPSTREAM_REPO, UPSTREAM_REPO_BRANCH, UPSTREAM_REPO_URL, HEROKU_APP_NAME
from Config import STRING, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8, STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30, STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40, STRING41, STRING42, STRING43, STRING44, STRING45, STRING46, STRING47, STRING48, STRING49, STRING50, STRING51, STRING52, STRING53, STRING54, STRING55, STRING56, STRING57, STRING58, STRING59, STRING60, STRING61, STRING62, STRING63, STRING64, STRING65, STRING66, STRING67, STRING68, STRING69, STRING70, STRING71, STRING72, STRING73, STRING74, STRING75, STRING76, STRING77, STRING78, STRING79, STRING80, STRING81, STRING82, STRING83, STRING84, STRING85, STRING86, STRING87, STRING88, STRING89, STRING90, STRING91, STRING92, STRING93, STRING94, STRING95, STRING96, STRING97, STRING98, STRING99, STRING100
import asyncio
import telethon.utils

from telethon.tl.types import InputPeerUser, ChatBannedRights
from telethon.tl.functions.channels import (
    InviteToChannelRequest,
    EditBannedRequest,
    GetFullChannelRequest,
    LeaveChannelRequest)
from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)

from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID, RABSEN
import git
import heroku3
from asyncio import sleep

import html

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError

from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,
                                          UsernameOccupiedError)

from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

from telethon.tl.functions.photos import (DeletePhotosRequest,
                                          GetUserPhotosRequest,
                                          UploadProfilePhotoRequest)

from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
import time
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.errors import rpcbaseerrors
import requests
from userbot.utils.tools import edit_or_reply as eor



a = API_ID
b = API_HASH

istri = STRING
istri2 = STRING2
istri3 = STRING3
istri4 = STRING4
istri5 = STRING5
istri6 = STRING6
istri7 = STRING7
istri8 = STRING8
istri9 = STRING9
istri10 = STRING10
istri11 = STRING11
istri12 = STRING12
istri13 = STRING13
istri14 = STRING14
istri15 = STRING15
istri16 = STRING16
istri17 = STRING17
istri18 = STRING18
istri19 = STRING19
istri20 = STRING20
istri21 = STRING21
istri22 = STRING22
istri23 = STRING23
istri24 = STRING24
istri25 = STRING25
istri26 = STRING26
istri27 = STRING27
istri28 = STRING28
istri29 = STRING29
istri30 = STRING30
istri31 = STRING31
istri32 = STRING32
istri33 = STRING33
istri34 = STRING34
istri35 = STRING35
istri36 = STRING36
istri37 = STRING37
istri38 = STRING38
istri39 = STRING39
istri40 = STRING40
istri41 = STRING41
istri42 = STRING42
istri43 = STRING43
istri44 = STRING44
istri45 = STRING45
istri46 = STRING46
istri47 = STRING47
istri48 = STRING48
istri49 = STRING49
istri50 = STRING50
istri51 = STRING51
istri52 = STRING52
istri53 = STRING53
istri54 = STRING54
istri55 = STRING55
istri56 = STRING56
istri57 = STRING57
istri58 = STRING58
istri59 = STRING59
istri60 = STRING60
istri61 = STRING61
istri62 = STRING62
istri63 = STRING63
istri64 = STRING64
istri65 = STRING65
istri66 = STRING66
istri67 = STRING67
istri68 = STRING68
istri69 = STRING69
istri70 = STRING70
istri71 = STRING71
istri72 = STRING72
istri73 = STRING73
istri74 = STRING74
istri75 = STRING75
istri76 = STRING76
istri77 = STRING77
istri78 = STRING78
istri79 = STRING79
istri80 = STRING80
istri81 = STRING81
istri82 = STRING82
istri83 = STRING83
istri84 = STRING84
istri85 = STRING85
istri86 = STRING86
istri87 = STRING87
istri88 = STRING88
istri89 = STRING89
istri90 = STRING90
istri91 = STRING91
istri92 = STRING92
istri93 = STRING93
istri94 = STRING94
istri95 = STRING95
istri96 = STRING96
istri97 = STRING97
istri98 = STRING98
istri99 = STRING99
istri100 = STRING100
res_time = 11
ren_time = 16

fibot = BOT_TOKEN # bot api
ubversi = f"Alpha3.2.1 [A14.3]" #versi
LOG_GROUP = HASH_CHAT  # HASH LINK GROUP
A_LOGO = ALIVE_LOGO
SENDMLOG = BOTLOG_CHATID  # ID LOG GROUP

bot1 = ""       # bot 1
bot2 = ""
bot3 = ""
bot4 = ""
bot5 = ""
bot6 = ""
bot7 = ""
bot8 = ""
bot9 = ""
bot10 = ""      # bot 10
bot11 = ""
bot12 = ""
bot13 = ""
bot14 = ""
bot15 = ""
bot16 = ""
bot17 = ""
bot18 = ""
bot19 = ""
bot20 = ""      # bot 20
bot21 = ""
bot22 = ""
bot23 = ""
bot24 = ""
bot25 = ""
bot26 = ""
bot27 = ""
bot28 = ""
bot29 = ""
bot30 = ""      # bot 30
bot31 = ""
bot32 = ""
bot33 = ""
bot34 = ""
bot35 = ""
bot36 = ""
bot37 = ""
bot38 = ""
bot39 = ""
bot40 = ""      # bot 40
bot41 = ""
bot42 = ""
bot43 = ""
bot44 = ""
bot45 = ""
bot46 = ""
bot47 = ""
bot48 = ""
bot49 = ""
bot50 = ""       #bot 50
bot51 = ""
bot52 = ""
bot53 = ""
bot54 = ""
bot55 = ""
bot56 = ""
bot57 = ""
bot58 = ""
bot59 = ""
bot60 = ""
bot61 = ""
bot62 = ""
bot63 = ""
bot64 = ""
bot65 = ""
bot66 = ""
bot67 = ""
bot68 = ""
bot69 = ""
bot70 = ""
bot71 = ""
bot72 = ""
bot73 = ""
bot74 = ""
bot75 = ""
bot76 = ""
bot77 = ""
bot78 = ""
bot79 = ""
bot80 = ""
bot81 = ""
bot82 = ""
bot83 = ""
bot84 = ""
bot85 = ""
bot86 = ""
bot87 = ""
bot88 = ""
bot89 = ""
bot90 = ""
bot91 = ""
bot92 = ""
bot93 = ""
bot94 = ""
bot95 = ""
bot96 = ""
bot97 = ""
bot98 = ""
bot99 = ""
bot100 = ""
xbot = ""


que = {}

SMEX_USERS = []

for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global bot1
    global bot2
    global bot3
    global bot4
    global bot5
    global bot6
    global bot7
    global bot8
    global bot9
    global bot10      # bot 10
    global bot11
    global bot12
    global bot13
    global bot14
    global bot15
    global bot16
    global bot17
    global bot18
    global bot19
    global bot20      # bot 20
    global bot21
    global bot22
    global bot23
    global bot24
    global bot25
    global bot26
    global bot27
    global bot28
    global bot29
    global bot30      # bot 30
    global bot31
    global bot32
    global bot33
    global bot34
    global bot35
    global bot36
    global bot37
    global bot38
    global bot39
    global bot40      # bot 40
    global bot41
    global bot42
    global bot43
    global bot44
    global bot45
    global bot46
    global bot47
    global bot48
    global bot49
    global bot50      # bot 50
    global bot51
    global bot52
    global bot53
    global bot54
    global bot55
    global bot56
    global bot57
    global bot58
    global bot59
    global bot60
    global bot61
    global bot62
    global bot63
    global bot64
    global bot65
    global bot66
    global bot67
    global bot68
    global bot69
    global bot70
    global bot71
    global bot72
    global bot73
    global bot74
    global bot75
    global bot76
    global bot77
    global bot78
    global bot79
    global bot80
    global bot81
    global bot82
    global bot83
    global bot84
    global bot85
    global bot86
    global bot87
    global bot88
    global bot89
    global bot90
    global bot91
    global bot92
    global bot93
    global bot94
    global bot95
    global bot96
    global bot97
    global bot98
    global bot99
    global bot100
    global xbot         # CLIENT BOT API
    global ubversi
    global LOG_GROUP    # GROUP LOG
    global A_LOGO
    global SENDMLOG     # LOG MESSAGE
    global res_time
    global ren_time 
 

    print(f"\n⏳ 「 ⚡️𝘿𝙇-𝙓𝟓𝟎 𝙐𝘽⚡️ 」 {ubversi} IS STARTING...\n")

    # booting start
    bsta = datetime.now()

    # var message
    sukses = 0
    failed = 0
    if istri:
        session_name = str(istri)            # ==============CLIENT 1=============
        print("String 1 Found")
        bot1 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 1")
            await bot1.start()
            botme = await bot1.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**01 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                await bot1.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot1(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot1.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        print("Task 3B")
                        pass
                except Exception as e:
                    print(e)
                    print("Task 3C")
                    pass
            try:
                print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot1(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            print("Task 5 = [Client 1] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        bot1 = TelegramClient(session_name, a, b)
        try:
            await bot1.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri2:
        session_name = str(istri2)       # ==============CLIENT 2=============
        print("String 2 Found")
        bot2 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 2")
            await bot2.start()
            botme = await bot2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**02 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group

                await bot2.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot2(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot2.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot2(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 2] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        bot2 = TelegramClient(session_name, a, b)
        try:
            await bot2.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri3:
        session_name = str(istri3)
        print("String 3 Found")
        bot3 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 3")
            await  bot3.start()
            botme = await bot3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**03 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot3.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot3(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot3.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot3(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # # print("Task 5 = [Client 3] is finish!")
            # sukses += 1

        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        bot3 = TelegramClient(session_name, a, b)
        try:
            await bot3.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri4:
        session_name = str(istri4)
        print("String 4 Found")
        bot4 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 4")
            await bot4.start()
            botme = await bot4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**04 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot4.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot4(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot4.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot4(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 4] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        bot4 = TelegramClient(session_name, a, b)
        try:
            await bot4.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri5:
        session_name = str(istri5)            # ==============CLIENT 5=============
        print("String 5 Found")
        bot5 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 5")
            await bot5.start()
            botme = await bot5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**05 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot5.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot5(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot5.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot5(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # # print("Task 5 = [Client 5] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        bot5 = TelegramClient(session_name, a, b)
        try:
            await bot5.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
                  
    if istri6:
        session_name = str(istri6)
        print("String 6 Found")
        bot6 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 6")
            await bot6.start()
            botme = await bot6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**06 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot6.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot6(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot6.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot6(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # # print("Task 5 = [Client 6] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        bot6 = TelegramClient(session_name, a, b)
        try:
            await bot6.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri7:
        session_name = str(istri7)
        print("String 7 Found")
        bot7 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 7")
            await bot7.start()
            botme = await bot7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**07 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot7.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot7(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot7.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot7(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 7] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bot7 = TelegramClient(session_name, a, b)
        try:
            await bot7.start()
        except Exception as e:
            pass
            failed += 1 # if session failed    
        
    
    if istri8:
        session_name = str(istri8)
        print("String 8 Found")
        bot8 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 8")
            await bot8.start()
            botme = await bot8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**08 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot8.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot8(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot8.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot8(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 8] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        bot8 = TelegramClient(session_name, a, b)
        try:
            await bot8.start()
        except Exception as e:
            pass
            failed += 1 # if session failed   
        
    if istri9:
        session_name = str(istri9)
        print("String 9 Found")
        bot9 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 9")
            await bot9.start()
            botme = await bot9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**09 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot9.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot9(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot9.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot9(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 9] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        bot9 = TelegramClient(session_name, a, b)
        try:
            await bot9.start()
        except Exception as e:
            pass
            failed += 1 # if session failed   
    
  
    if istri10:
        session_name = str(istri10)               # ==============CLIENT 10=============
        print("String 10 Found")
        bot10 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 10")
            await bot10.start()
            botme = await bot10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**10 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot10.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot10(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot10.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot10(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 10] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        bot10 = TelegramClient(session_name, a, b)
        try:
            await bot10.start()
        except Exception as e:
            pass
            failed += 1 # if session failed 
        
    
    if istri11:
        session_name = str(istri11)
        print("String 11 Found")
        bot11 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 11")
            await bot11.start()
            botme = await bot11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**11 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot11.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot11(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot11.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot11(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 11] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        bot11 = TelegramClient(session_name, a, b)
        try:
            await bot11.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri12:
        session_name = str(istri12)
        print("String 12 Found")
        bot12 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 12")
            await bot12.start()
            botme = await bot12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**12 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot12.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot12(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot12.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot12(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 12] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        bot12 = TelegramClient(session_name, a, b)
        try:
            await bot12.start()
        except Exception as e:
            pass
            failed += 1 # if session failed   
    
  
    if istri13:
        session_name = str(istri13)
        print("String 13  Found")
        bot13 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 13")
            await bot13.start()
            botme = await bot13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**13 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot13.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot13(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot13.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot13(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 13] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        bot13 = TelegramClient(session_name, a, b)
        try:
            await bot13.start()
        except Exception as e:
            pass 
            failed += 1 # if session failed
        
    
    if istri14:
        session_name = str(istri14)
        print("String 14 Found")
        bot14 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 14")
            await bot14.start()
            botme = await bot14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**14 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot14.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot14(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot14.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot14(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 14] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        bot14 = TelegramClient(session_name, a, b)
        try:
            await bot14.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri15:
        session_name = str(istri15)              # ==============CLIENT 15=============
        print("String 15 Found")
        bot15 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 15")
            await bot15.start()
            botme = await bot15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**15 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot15.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot15(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot15.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot15(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 15] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        bot15 = TelegramClient(session_name, a, b)
        try:
            await bot15.start()
        except Exception as e:
            pass
            failed += 1 # if session failed


    if istri16:
        session_name = str(istri16)
        print("String 16 Found")
        bot16 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 16")
            await bot16.start()
            botme = await bot16.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**16 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot16.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot16(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot16.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot16(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 16] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        bot16 = TelegramClient(session_name, a, b)
        try:
            await bot16.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri17:
        session_name = str(istri17)
        print("String 17 Found")
        bot17 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 17")
            await bot17.start()
            botme = await bot17.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**17 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot17.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot17(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot17.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot17(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 17] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        bot17 = TelegramClient(session_name, a, b)
        try:
            await bot17.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri18:
        session_name = str(istri18)
        print("String 18 Found")
        bot18 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 18")
            await bot18.start()
            botme = await bot18.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**18 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot18.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot18(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot18.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot18(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 18] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        bot18 = TelegramClient(session_name, a, b)
        try:
            await bot18.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri19:
        session_name = str(istri19)
        print("String 19 Found")
        bot19 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 19")
            await bot19.start()
            botme = await bot19.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**19 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot19.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot19(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot19.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot19(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 19] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        bot19 = TelegramClient(session_name, a, b)
        try:
            await bot19.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri20:
        session_name = str(istri20)           # ==============CLIENT 20=============
        print("String 20 Found")
        bot20 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 20")
            await bot20.start()
            botme = await bot20.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**20 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot20.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot20(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot20.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot20(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 20] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        bot20 = TelegramClient(session_name, a, b)
        try:
            await bot20.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    # random sleep
    print(f"Random Sleep Request {res_time}s - {ren_time}s") 
    await asyncio.sleep(random.randrange(res_time, ren_time))
   
    if istri21:
        session_name = str(istri21)
        print("String 21 Found")
        bot21 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 21")
            await bot21.start()
            botme = await bot21.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**21 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot21.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot21(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot21.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot21(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 21] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        bot21 = TelegramClient(session_name, a, b)
        try:
            await bot21.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri22:
        session_name = str(istri22)
        print("String 22 Found")
        bot22 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 22")
            await bot22.start()
            botme = await bot22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**22 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot22.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot22(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot22.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot22(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 22] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        bot22 = TelegramClient(session_name, a, b)
        try:
            await bot22.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri23:
        session_name = str(istri23)
        print("String 23 Found")
        bot23 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 23")
            await bot23.start()
            botme = await bot23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**23 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot23.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot23(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot23.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot23(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 23] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        bot23 = TelegramClient(session_name, a, b)
        try:
            await bot23.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri24:
        session_name = str(istri24)
        print("String 24 Found")
        bot24 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 24")
            await bot24.start()
            botme = await bot24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**24 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot24.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot24(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot24.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot24(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 24] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        bot24 = TelegramClient(session_name, a, b)
        try:
            await bot24.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri25:
        session_name = str(istri25)           # ==============CLIENT 25=============
        print("String 25 Found")
        bot25 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 25")
            await bot25.start()
            botme = await bot25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**25 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot25.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot25(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot25.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot25(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 25] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        bot25 = TelegramClient(session_name, a, b)
        try:
            await bot25.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri26: 
        session_name = str(istri26)
        print("String 26 Found")
        bot26 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 26")
            await bot26.start()
            botme = await bot26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**26 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot26.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot26(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot26.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot26(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 26] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        bot26 = TelegramClient(session_name, a, b)
        try:
            await bot26.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri27:
        session_name = str(istri27)
        print("String 27 Found")
        bot27 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 27")
            await bot27.start()
            botme = await bot27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**27 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot27.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot27(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot27.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot27(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 27] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        bot27 = TelegramClient(session_name, a, b)
        try:
            await bot27.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri28:
        session_name = str(istri28)
        print("String 28 Found")
        bot28 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 28")
            await bot28.start()
            botme = await bot28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**28 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot28.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot28(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot28.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot28(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 28] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        bot28 = TelegramClient(session_name, a, b)
        try:
            await bot28.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri29:
        session_name = str(istri29)
        print("String 29 Found")
        bot29 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 29")
            await bot29.start()
            botme = await bot29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**29 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot29.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot29(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot29.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot29(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 29] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        bot29 = TelegramClient(session_name, a, b)
        try:
            await bot29.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri30:
        session_name = str(istri30)       # ==============CLIENT 30=============
        print("String 30 Found")
        bot30 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 30")
            await bot30.start()
            botme = await bot30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**30 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot30.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot30(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot30.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot30(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 30] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        bot30 = TelegramClient(session_name, a, b)
        try:
            await bot30.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri31:
        session_name = str(istri31)
        print("String 31 Found")
        bot31 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 31")
            await bot31.start()
            botme = await bot31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**31 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot31.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot31(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot31.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot31(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 31] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "startup"
        bot31 = TelegramClient(session_name, a, b)
        try:
            await bot31.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
                  
    if istri32:
        session_name = str(istri32)
        print("String 32 Found")
        bot32 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 32")
            await bot32.start()
            botme = await bot32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**32 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot32.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot32(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot32.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot32(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 32] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "startup"
        bot32 = TelegramClient(session_name, a, b)
        try:
            await bot32.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri33:
        session_name = str(istri33)
        print("String 33 Found")
        bot33 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 33")
            await bot33.start()
            botme = await bot33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**33 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot33.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot33(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot33.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot33(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 33] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "startup"
        bot33 = TelegramClient(session_name, a, b)
        try:
            await bot33.start()
        except Exception as e:
            pass    
            failed += 1 # if session failed
        
    
    if istri34:
        session_name = str(istri34)
        print("String 34 Found")
        bot34 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 34")
            await bot34.start()
            botme = await bot34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**34 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot34.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot34(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot34.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot34(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 34] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "startup"
        bot34 = TelegramClient(session_name, a, b)
        try:
            await bot34.start()
        except Exception as e:
            pass   
            failed += 1 # if session failed
        
    if istri35:
        session_name = str(istri35)               # ==============CLIENT 35=============
        print("String 35 Found")
        bot35 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 35")
            await bot35.start()
            botme = await bot35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**35 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot35.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot35(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot35.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot35(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 35] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "startup"
        bot35 = TelegramClient(session_name, a, b)
        try:
            await bot35.start()
        except Exception as e:
            pass   
            failed += 1 # if session failed
    
  
    if istri36:
        session_name = str(istri36)
        print("String 36 Found")
        bot36 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 36")
            await bot36.start()
            botme = await bot36.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**36 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot36.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot36(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot36.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot36(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 36] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        pass
        session_name = "startup"
        bot36 = TelegramClient(session_name, a, b)
        try:
            await bot36.start()
        except Exception as e:
            pass 
            failed += 1 # if session failed
        
    
    if istri37:
        session_name = str(istri37)
        print("String 37 Found")
        bot37 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 37")
            await bot37.start()
            botme = await bot37.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**37 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot37.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot37(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot37.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot37(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 37] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        pass
        session_name = "startup"
        bot37 = TelegramClient(session_name, a, b)
        try:
            await bot37.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri38:
        session_name = str(istri38)
        print("String 38 Found")
        bot38 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 38")
            await bot38.start()
            botme = await bot38.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**38 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot38.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot38(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot38.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot38(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 38] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        pass
        session_name = "startup"
        bot38 = TelegramClient(session_name, a, b)
        try:
            await bot38.start()
        except Exception as e:
            pass   
            failed += 1 # if session failed
    
  
    if istri39:
        session_name = str(istri39)
        print("String 39  Found")
        bot39 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 39")
            await bot39.start()
            botme = await bot39.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**39 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot39.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot39(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot39.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot39(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 39] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        pass
        session_name = "startup"
        bot39 = TelegramClient(session_name, a, b)
        try:
            await bot39.start()
        except Exception as e:
            pass 
            failed += 1 # if session failed
        
    
    if istri40:
        session_name = str(istri40)               # ==============CLIENT 40=============
        print("String 40 Found")
        bot40 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 40")
            await bot40.start()
            botme = await bot40.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**40 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot40.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot40(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot40.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot40(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 40] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        pass
        session_name = "startup"
        bot40 = TelegramClient(session_name, a, b)
        try:
            await bot40.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
    
    # random sleep
    print(f"Random Sleep Request {res_time}s - {ren_time}s") 
    await asyncio.sleep(random.randrange(res_time, ren_time))
    
    if istri41:
        session_name = str(istri41)
        print("String 41 Found")
        bot41 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 41")
            await bot41.start()
            botme = await bot41.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**41 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot41.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot41(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot41.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot41(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 41] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 41 not Found")
        pass
        session_name = "startup"
        bot41 = TelegramClient(session_name, a, b)
        try:
            await bot41.start()
        except Exception as e:
            pass
            failed += 1 # if session failed


    if istri42:
        session_name = str(istri42)
        print("String 42 Found")
        bot42 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 42")
            await bot42.start()
            botme = await bot42.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**42 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot42.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot42(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    sukses += 1
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot42.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot42(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 42] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 42 not Found")
        session_name = "startup"
        bot42 = TelegramClient(session_name, a, b)
        try:
            await bot42.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri43:
        session_name = str(istri43)
        print("String 43 Found")
        bot43 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 43")
            await bot43.start()
            botme = await bot43.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**43 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot43.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot43(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot43.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot43(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 43] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 43 not Found")
        session_name = "startup"
        bot43 = TelegramClient(session_name, a, b)
        try:
            await bot43.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri44:
        session_name = str(istri44)
        print("String 44 Found")
        bot44 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 44")
            await bot44.start()
            botme = await bot44.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**44 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot44.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot44(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot44.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot44(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 44] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 44 not Found")
        session_name = "startup"
        bot44 = TelegramClient(session_name, a, b)
        try:
            await bot44.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri45:
        session_name = str(istri45)               # CLIENT 45
        print("String 45 Found")
        bot45 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 45")
            await bot45.start()
            botme = await bot45.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**45 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot45.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot45(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot45.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot45(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 45] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 45 not Found")
        session_name = "startup"
        bot45 = TelegramClient(session_name, a, b)
        try:
            await bot45.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri46:
        session_name = str(istri46)
        print("String 46 Found")
        bot46 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 46")
            await bot46.start()
            botme = await bot46.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**46 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot46.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot46(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot46.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot46(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 46] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 46 not Found")
        session_name = "startup"
        bot46 = TelegramClient(session_name, a, b)
        try:
            await bot46.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri47:
        session_name = str(istri47)                  # CLIENT 47
        print("String 47 Found")
        bot47 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 47")
            await bot47.start()
            botme = await bot47.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**47 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot47.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot47(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot47.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot47(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 47] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 47 not Found")
        session_name = "startup"
        bot47 = TelegramClient(session_name, a, b)
        try:
            await bot47.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri48:
        session_name = str(istri48)
        print("String 48 Found")
        bot48 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 48")
            await bot48.start()
            botme = await bot48.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**48 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot48.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot48(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot48.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot48(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 48] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 48 not Found")
        session_name = "startup"
        bot48 = TelegramClient(session_name, a, b)
        try:
            await bot48.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri49:
        session_name = str(istri49)
        print("String 49 Found")
        bot49 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 49")
            await bot49.start()
            botme = await bot49.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**49 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot49.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot49(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot49.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot49(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 49] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 49 not Found")
        session_name = "startup"
        bot49 = TelegramClient(session_name, a, b)
        try:
            await bot49.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri50:
        session_name = str(istri50)               # CLIENT 50
        print("String 50 Found")
        bot50 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 50")
            await bot50.start()
            botme = await bot50.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**50 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot50.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot50(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot50.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot50(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 50] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 50 not Found")
        session_name = "startup"
        bot50 = TelegramClient(session_name, a, b)
        try:
            await bot50.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

# ======================================50 ==================================

    if istri51:
        session_name = str(istri51)            # ==============CLIENT 51=============
        print("String 51 Found")
        bot51 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 51")
            await bot51.start()
            botme = await bot51.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**51 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                await bot51.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot51(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot51.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        print("Task 3B")
                        pass
                except Exception as e:
                    print(e)
                    print("Task 3C")
                    pass
            try:
                print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot51(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            print("Task 5 = [Client 51] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 51 not Found")
        session_name = "startup"
        bot51 = TelegramClient(session_name, a, b)
        try:
            await bot51.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri52:
        session_name = str(istri52)       # ==============CLIENT 52=============
        print("String 52 Found")
        bot52 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 52")
            await bot52.start()
            botme = await bot52.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**52 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group

                await bot52.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot52(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot52.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot52(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 52] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 52 not Found")
        pass
        session_name = "startup"
        bot52 = TelegramClient(session_name, a, b)
        try:
            await bot52.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri53:
        session_name = str(istri53)
        print("String 53 Found")
        bot53 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 53")
            await  bot53.start()
            botme = await bot53.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**53 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot53.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot53(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot53.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot53(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # # print("Task 5 = [Client 3] is finish!")
            # sukses += 1

        except Exception as e:
            print(e)
            pass
    else:
        print("Session 53 not Found")
        pass
        session_name = "startup"
        bot53 = TelegramClient(session_name, a, b)
        try:
            await bot53.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri54:
        session_name = str(istri54)
        print("String 54 Found")
        bot54 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 54")
            await bot54.start()
            botme = await bot54.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**54 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot54.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot54(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot54.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot54(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 54] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 54 not Found")
        pass
        session_name = "startup"
        bot54 = TelegramClient(session_name, a, b)
        try:
            await bot54.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri55:
        session_name = str(istri55)            # ==============CLIENT 55=============
        print("String 55 Found")
        bot55 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 55")
            await bot55.start()
            botme = await bot55.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**55 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot55.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot55(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot55.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot55(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # # print("Task 5 = [Client 5] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 55 not Found")
        pass
        session_name = "startup"
        bot55 = TelegramClient(session_name, a, b)
        try:
            await bot55.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
                  
    if istri56:
        session_name = str(istri56)
        print("String 56 Found")
        bot56 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 56")
            await bot56.start()
            botme = await bot56.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**56 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot56.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot56(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot56.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot56(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # # print("Task 5 = [Client 56] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 56 not Found")
        pass
        session_name = "startup"
        bot56 = TelegramClient(session_name, a, b)
        try:
            await bot56.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri57:
        session_name = str(istri57)
        print("String 57 Found")
        bot57 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 57")
            await bot57.start()
            botme = await bot57.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**57 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot57.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot57(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot57.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot57(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 57] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 57 not Found")
        pass
        session_name = "startup"
        bot57 = TelegramClient(session_name, a, b)
        try:
            await bot57.start()
        except Exception as e:
            pass
            failed += 1 # if session failed    
        
    
    if istri58:
        session_name = str(istri58)
        print("String 58 Found")
        bot58 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 58")
            await bot58.start()
            botme = await bot58.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**58 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot58.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot58(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot58.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot58(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 58] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 58 not Found")
        pass
        session_name = "startup"
        bot58 = TelegramClient(session_name, a, b)
        try:
            await bot58.start()
        except Exception as e:
            pass
            failed += 1 # if session failed   
        
    if istri59:
        session_name = str(istri59)
        print("String 59 Found")
        bot59 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 59")
            await bot59.start()
            botme = await bot59.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**59 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot59.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot59(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot59.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot59(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 59] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 59 not Found")
        pass
        session_name = "startup"
        bot59 = TelegramClient(session_name, a, b)
        try:
            await bot59.start()
        except Exception as e:
            pass
            failed += 1 # if session failed   
    
  
    if istri60:
        session_name = str(istri60)               # ==============CLIENT 60=============
        print("String 60 Found")
        bot60 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 60")
            await bot60.start()
            botme = await bot60.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**60 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot60.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot60(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot60.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot60(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 60] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 60 not Found")
        pass
        session_name = "startup"
        bot60 = TelegramClient(session_name, a, b)
        try:
            await bot60.start()
        except Exception as e:
            pass
            failed += 1 # if session failed 
        
    
    # random sleep
    print(f"Random Sleep Request {res_time}s - {ren_time}s") 
    await asyncio.sleep(random.randrange(res_time, ren_time))

    if istri61:
        session_name = str(istri61)
        print("String 61 Found")
        bot61 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 61")
            await bot61.start()
            botme = await bot61.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**61 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot61.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot61(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot61.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot61(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 61] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 61 not Found")
        pass
        session_name = "startup"
        bot61 = TelegramClient(session_name, a, b)
        try:
            await bot61.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri62:
        session_name = str(istri62)
        print("String 62 Found")
        bot62 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 62")
            await bot62.start()
            botme = await bot62.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**62 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot62.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot62(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot62.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot62(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 62] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 62 not Found")
        pass
        session_name = "startup"
        bot62 = TelegramClient(session_name, a, b)
        try:
            await bot62.start()
        except Exception as e:
            pass
            failed += 1 # if session failed   
    
  
    if istri63:
        session_name = str(istri63)
        print("String 63  Found")
        bot63 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 63")
            await bot63.start()
            botme = await bot63.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**63 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot63.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot63(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot63.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot63(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 63] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 63 not Found")
        pass
        session_name = "startup"
        bot63 = TelegramClient(session_name, a, b)
        try:
            await bot63.start()
        except Exception as e:
            pass 
            failed += 1 # if session failed
        
    
    if istri64:
        session_name = str(istri64)
        print("String 64 Found")
        bot64 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 64")
            await bot64.start()
            botme = await bot64.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**64 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot64.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot64(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot64.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot64(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 64] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 64 not Found")
        pass
        session_name = "startup"
        bot64 = TelegramClient(session_name, a, b)
        try:
            await bot64.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri65:
        session_name = str(istri65)              # ==============CLIENT 65=============
        print("String 65 Found")
        bot65 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 65")
            await bot65.start()
            botme = await bot65.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**65 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot65.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot65(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot65.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot65(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 65] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 65 not Found")
        pass
        session_name = "startup"
        bot65 = TelegramClient(session_name, a, b)
        try:
            await bot65.start()
        except Exception as e:
            pass
            failed += 1 # if session failed


    if istri66:
        session_name = str(istri66)
        print("String 66 Found")
        bot66 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 66")
            await bot66.start()
            botme = await bot66.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**66 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot66.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot66(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot66.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot66(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 66] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 66 not Found")
        session_name = "startup"
        bot66 = TelegramClient(session_name, a, b)
        try:
            await bot66.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri67:
        session_name = str(istri67)
        print("String 67 Found")
        bot67 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 67")
            await bot67.start()
            botme = await bot67.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**67 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot67.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot67(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot67.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot67(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 67] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 67 not Found")
        session_name = "startup"
        bot67 = TelegramClient(session_name, a, b)
        try:
            await bot67.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri68:
        session_name = str(istri68)
        print("String 68 Found")
        bot68 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 68")
            await bot68.start()
            botme = await bot68.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**68 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot68.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot68(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot68.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot68(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 68] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 68 not Found")
        session_name = "startup"
        bot68 = TelegramClient(session_name, a, b)
        try:
            await bot68.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri69:
        session_name = str(istri69)
        print("String 69 Found")
        bot69 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 69")
            await bot69.start()
            botme = await bot69.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**69 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot69.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot69(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot69.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot69(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 69] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 69 not Found")
        session_name = "startup"
        bot69 = TelegramClient(session_name, a, b)
        try:
            await bot69.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri70:
        session_name = str(istri70)           # ==============CLIENT 70=============
        print("String 70 Found")
        bot70 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 70")
            await bot70.start()
            botme = await bot70.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**70 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot70.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot70(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot70.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot70(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 70] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 70 not Found")
        session_name = "startup"
        bot70 = TelegramClient(session_name, a, b)
        try:
            await bot70.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri71:
        session_name = str(istri71)
        print("String 71 Found")
        bot71 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 71")
            await bot71.start()
            botme = await bot71.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**71 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot71.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot71(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot71.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot71(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 71] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 71 not Found")
        session_name = "startup"
        bot71 = TelegramClient(session_name, a, b)
        try:
            await bot71.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri72:
        session_name = str(istri72)
        print("String 72 Found")
        bot72 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 72")
            await bot72.start()
            botme = await bot72.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**72 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot72.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot72(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot72.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot72(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 72] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 72 not Found")
        session_name = "startup"
        bot72 = TelegramClient(session_name, a, b)
        try:
            await bot72.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri73:
        session_name = str(istri73)
        print("String 73 Found")
        bot73 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 73")
            await bot73.start()
            botme = await bot73.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**73 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot73.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot73(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot73.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot73(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 73] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 73 not Found")
        session_name = "startup"
        bot73 = TelegramClient(session_name, a, b)
        try:
            await bot73.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri74:
        session_name = str(istri74)
        print("String 74 Found")
        bot74 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 74")
            await bot74.start()
            botme = await bot74.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**74 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot74.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot74(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot74.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot74(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 74] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 74 not Found")
        session_name = "startup"
        bot74 = TelegramClient(session_name, a, b)
        try:
            await bot74.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri75:
        session_name = str(istri75)           # ==============CLIENT 75=============
        print("String 75 Found")
        bot75 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 75")
            await bot75.start()
            botme = await bot75.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**75 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot75.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot75(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot75.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot75(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 75] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 75 not Found")
        session_name = "startup"
        bot75 = TelegramClient(session_name, a, b)
        try:
            await bot75.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri76: 
        session_name = str(istri76)
        print("String 76 Found")
        bot76 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 76")
            await bot76.start()
            botme = await bot76.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**76 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot76.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot76(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot76.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot76(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 76] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 76 not Found")
        session_name = "startup"
        bot76 = TelegramClient(session_name, a, b)
        try:
            await bot76.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri77:
        session_name = str(istri77)
        print("String 77 Found")
        bot77 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 77")
            await bot77.start()
            botme = await bot77.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**77 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot77.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot77(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot77.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot77(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 77] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 77 not Found")
        session_name = "startup"
        bot77 = TelegramClient(session_name, a, b)
        try:
            await bot77.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri78:
        session_name = str(istri78)
        print("String 78 Found")
        bot78 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 78")
            await bot78.start()
            botme = await bot78.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**78 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot78.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot78(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot78.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot78(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 78] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 78 not Found")
        pass
        session_name = "startup"
        bot78 = TelegramClient(session_name, a, b)
        try:
            await bot78.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri79:
        session_name = str(istri79)
        print("String 79 Found")
        bot79 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 79")
            await bot79.start()
            botme = await bot79.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**79 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot79.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot79(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot79.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot79(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 79] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 79 not Found")
        pass
        session_name = "startup"
        bot79 = TelegramClient(session_name, a, b)
        try:
            await bot79.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri80:
        session_name = str(istri80)       # ==============CLIENT 80=============
        print("String 80 Found")
        bot80 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 80")
            await bot80.start()
            botme = await bot80.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**80 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot80.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot80(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot80.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot80(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 80] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 80 not Found")
        pass
        session_name = "startup"
        bot80 = TelegramClient(session_name, a, b)
        try:
            await bot80.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    # random sleep
    print(f"Random Sleep Request {res_time}s - {ren_time}s") 
    await asyncio.sleep(random.randrange(res_time, ren_time))

    if istri81:
        session_name = str(istri81)
        print("String 81 Found")
        bot81 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 81")
            await bot81.start()
            botme = await bot81.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**81 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot81.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot81(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot81.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot81(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 81] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 81 not Found")
        pass
        session_name = "startup"
        bot81 = TelegramClient(session_name, a, b)
        try:
            await bot81.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
                  
    if istri82:
        session_name = str(istri82)
        print("String 82 Found")
        bot82 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 82")
            await bot82.start()
            botme = await bot82.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**82 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot82.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot82(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot82.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot82(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 82] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 82 not Found")
        pass
        session_name = "startup"
        bot82 = TelegramClient(session_name, a, b)
        try:
            await bot82.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    if istri83:
        session_name = str(istri83)
        print("String 83 Found")
        bot83 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 83")
            await bot83.start()
            botme = await bot83.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**83 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot83.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot83(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot83.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot83(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 83] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 83 not Found")
        pass
        session_name = "startup"
        bot83 = TelegramClient(session_name, a, b)
        try:
            await bot83.start()
        except Exception as e:
            pass    
            failed += 1 # if session failed
        
    
    if istri84:
        session_name = str(istri84)
        print("String 84 Found")
        bot84 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 84")
            await bot84.start()
            botme = await bot84.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**84 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot84.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot84(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot84.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot84(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 84] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 84 not Found")
        pass
        session_name = "startup"
        bot84 = TelegramClient(session_name, a, b)
        try:
            await bot84.start()
        except Exception as e:
            pass   
            failed += 1 # if session failed
        
    if istri85:
        session_name = str(istri85)               # ==============CLIENT 85=============
        print("String 85 Found")
        bot85 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 85")
            await bot85.start()
            botme = await bot85.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**85 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot85.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot85(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot85.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot85(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 85] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 85 not Found")
        pass
        session_name = "startup"
        bot85 = TelegramClient(session_name, a, b)
        try:
            await bot85.start()
        except Exception as e:
            pass   
            failed += 1 # if session failed
    
  
    if istri86:
        session_name = str(istri86)
        print("String 86 Found")
        bot86 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 86")
            await bot86.start()
            botme = await bot86.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**86 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot86.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot86(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot86.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot86(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 86] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 86 not Found")
        pass
        session_name = "startup"
        bot86 = TelegramClient(session_name, a, b)
        try:
            await bot86.start()
        except Exception as e:
            pass 
            failed += 1 # if session failed
        
    
    if istri87:
        session_name = str(istri87)
        print("String 87 Found")
        bot87 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 87")
            await bot87.start()
            botme = await bot87.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**87 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot87.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot87(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot87.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot87(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 87] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 87 not Found")
        pass
        session_name = "startup"
        bot87 = TelegramClient(session_name, a, b)
        try:
            await bot87.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri88:
        session_name = str(istri88)
        print("String 88 Found")
        bot88 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 88")
            await bot88.start()
            botme = await bot88.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**88 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot88.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot88(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot88.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot88(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 88] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 88 not Found")
        pass
        session_name = "startup"
        bot88 = TelegramClient(session_name, a, b)
        try:
            await bot88.start()
        except Exception as e:
            pass   
            failed += 1 # if session failed
    
  
    if istri89:
        session_name = str(istri89)
        print("String 89  Found")
        bot89 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 89")
            await bot89.start()
            botme = await bot89.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**89 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot89.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot89(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot89.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot89(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 89] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 89 not Found")
        pass
        session_name = "startup"
        bot89 = TelegramClient(session_name, a, b)
        try:
            await bot89.start()
        except Exception as e:
            pass 
            failed += 1 # if session failed
        
    
    if istri90:
        session_name = str(istri90)               # ==============CLIENT 90=============
        print("String 90 Found")
        bot90 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 90")
            await bot90.start()
            botme = await bot90.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**90 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot90.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot90(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot90.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot90(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 90] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 90 not Found")
        pass
        session_name = "startup"
        bot90 = TelegramClient(session_name, a, b)
        try:
            await bot90.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
        
    
    if istri91:
        session_name = str(istri91)
        print("String 91 Found")
        bot91 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 91")
            await bot91.start()
            botme = await bot91.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**91 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot91.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot91(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot91.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot91(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 91] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 91 not Found")
        pass
        session_name = "startup"
        bot91 = TelegramClient(session_name, a, b)
        try:
            await bot91.start()
        except Exception as e:
            pass
            failed += 1 # if session failed


    if istri92:
        session_name = str(istri92)
        print("String 92 Found")
        bot92 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 92")
            await bot92.start()
            botme = await bot92.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**92 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot92.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot92(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    sukses += 1
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot92.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot92(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 92] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 92 not Found")
        session_name = "startup"
        bot92 = TelegramClient(session_name, a, b)
        try:
            await bot92.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri93:
        session_name = str(istri93)
        print("String 93 Found")
        bot93 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 93")
            await bot93.start()
            botme = await bot93.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**93 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot93.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot93(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot93.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot93(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 93] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 93 not Found")
        session_name = "startup"
        bot93 = TelegramClient(session_name, a, b)
        try:
            await bot93.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri94:
        session_name = str(istri94)
        print("String 94 Found")
        bot94 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 94")
            await bot94.start()
            botme = await bot94.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**94 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot94.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot94(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot94.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot94(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 94] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 94 not Found")
        session_name = "startup"
        bot94 = TelegramClient(session_name, a, b)
        try:
            await bot94.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri95:
        session_name = str(istri95)               # CLIENT 95
        print("String 95 Found")
        bot95 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 95")
            await bot95.start()
            botme = await bot95.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**95 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot95.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot95(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot95.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot95(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 95] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 95 not Found")
        session_name = "startup"
        bot95 = TelegramClient(session_name, a, b)
        try:
            await bot95.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri96:
        session_name = str(istri96)
        print("String 96 Found")
        bot96 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 96")
            await bot96.start()
            botme = await bot96.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**96 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot96.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot96(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot96.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot96(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 96] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 96 not Found")
        session_name = "startup"
        bot96 = TelegramClient(session_name, a, b)
        try:
            await bot96.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri97:
        session_name = str(istri97)                  # CLIENT 97
        print("String 97 Found")
        bot97 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 97")
            await bot97.start()
            botme = await bot97.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**97 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot97.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot97(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot97.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot97(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 97] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 97 not Found")
        session_name = "startup"
        bot97 = TelegramClient(session_name, a, b)
        try:
            await bot97.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri98:
        session_name = str(istri98)
        print("String 98 Found")
        bot98 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 98")
            await bot98.start()
            botme = await bot98.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**98 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot98.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot98(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot98.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot98(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 98] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 98 not Found")
        session_name = "startup"
        bot98 = TelegramClient(session_name, a, b)
        try:
            await bot98.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri99:
        session_name = str(istri99)
        print("String 99 Found")
        bot99 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 99")
            await bot99.start()
            botme = await bot99.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**99 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot99.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot99(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot99.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot99(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 99] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 99 not Found")
        session_name = "startup"
        bot99 = TelegramClient(session_name, a, b)
        try:
            await bot99.start()
        except Exception as e:
            pass
            failed += 1 # if session failed
   
    if istri100:
        session_name = str(istri100)               # CLIENT 100
        print("String 100 Found")
        bot100 = TelegramClient(StringSession(session_name), a, b)
        try:
            # # sukses += 1
            print("Booting Up The Client 100")
            await bot100.start()
            botme = await bot100.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            msxlog = f"""**100 - Userbot is Alive!**\nOwner : **{full_name}**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                await bot100.send_message(SENDMLOG, f"""{msxlog}""")
            except Exception as e:
                print(e)
                try:
                    # print("Task 2 = join LOG_GROUP kalo belom join") # Join ke log group
                    await bot100(functions.messages.ImportChatInviteRequest(hash=f"{LOG_GROUP}"))
                    try:
                        print("Task 3 = lalu send msg to LOG_GROUP") # Send pesan ke log group
                        await bot100.send_message(SENDMLOG, f"""{msxlog}""")
                    except Exception as e:
                        print(e)
                        pass
                except Exception as e:
                    print(e)
                    pass
            try:
                # print("Task 4 = join ke @AlphaXProject juga") # Join ke log group
                await bot100(functions.channels.JoinChannelRequest(channel="@AlphaXProject"))
                sukses += 1
            except Exception as e:
                    print(e)
                    pass
            # print("Task 5 = [Client 100] is finish!")
            # sukses += 1
            
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 100 not Found")
        session_name = "startup"
        bot100 = TelegramClient(session_name, a, b)
        try:
            await bot100.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

    # random sleep
    print(f"Random Sleep Request {res_time}s - {ren_time}s") 
    await asyncio.sleep(random.randrange(res_time, ren_time))

    # booting end
    bend = datetime.now()
    boot_box = (bsta-bend).microseconds / 1000
    
    # var bot token
    if fibot:
        session_name = str(fibot)           # CLIENT BOT API / TOKEN
        
        print("Token 1 Found")
        xbot = TelegramClient(session_name, a, b)
        try:
            # # sukses += 1
            total_client = 100 - failed
            print("Booting Up The Token 51")
            await xbot.start(bot_token=BOT_TOKEN)
            botme = await xbot.get_me()
            SMEX_USERS.append(botid)
            # user = await idk.get_me()
            # get mention name profile
            full_name = f"[{botme.first_name}](tg://user?id={botme.id})"
            # bot pinger
            start = datetime.now()
            try:
                # send process msg
                xbotm = await xbot.send_message(SENDMLOG,f"`processing..`")
            except Exception as e:
                print(e)
                pass
            
            end = datetime.now()
            ms = (end-start).microseconds / 1000
            
            
            # starting message for bot
            msxlog = f"""\n✥ **Hello master...**\n╔════════════════════╗\n\n ➠ **{ALIVE_NAME} is Alive!**\n\n◖════════════════════◗\n ➠ `Owner \t:` **{full_name}**\n ➠ `Total Clients \t:` {total_client}\n ➠ `Clients On \t:` {sukses}\n ➠ `Version \t:` `{ubversi}`\n ➠ `Branch \t:` `{UPSTREAM_REPO_BRANCH}`\n ➠ `Pinging \t:` **{ms}** `𝗺𝘀`\n ➠ `Booting \t:` **{boot_box}** `𝗺𝘀`\n╚════════════════════╝\n✥ **Powered by : @AlphaXProject**"""
            try:
                # print("Task 1 = send msg to LOG_GROUP") # Send pesan ke log group
                # edit mesg xbotm
                await xbotm.edit(f"""{msxlog}""")
            except Exception as e:
                print(e)
                pass
        except Exception as e:
            print(e)
            pass
    else:
        print("Token 1 not Found")
        session_name = "startup"
        xbot = TelegramClient(session_name, a, b)
        try:
            await xbot.start()
        except Exception as e:
            pass
            failed += 1 # if session failed

loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       
