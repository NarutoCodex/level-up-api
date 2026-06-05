# main.py (modified for multi-instance support)
# SCRIPT BY NARUTO(@narutocodexff) TELEGRAM CHANNEL (@narutocodexofc)
# MODIFIED: Added multi-instance support

import requests, os, json, binascii, time, urllib3, base64, datetime, re, socket, ssl, asyncio, aiohttp, random, traceback, shutil, sys, argparse
from protobuf_decoder.protobuf_decoder import Parser
from xDL import *
from autoup import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from Pb2 import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2
import google.protobuf.json_format as json_format
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Global variables - will be instance-specific
instances = {}  # Store all bot instances
instance_stop_flags = {}  # Stop flags per instance

class BotInstance:
    def __init__(self, instance_id, uid, password):
        self.instance_id = instance_id
        self.uid = uid
        self.password = password
        self.online_writer = None
        self.whisper_writer = None
        self.auto_start_running = False
        self.stop_auto = False
        self.auto_start_task = None
        self.bot_uid = None
        self.region = None
        self.login_url = None
        self.ob = None
        self.version = None
        self.Hr = {}
        self.running = True
        
    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{self.instance_id}] {msg}")
        
    def init_globals(self):
        self.login_url, self.ob, self.version = AuToUpDaTE()
        self.Hr = {
            'User-Agent': Uaa(),
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/x-www-form-urlencoded",
            'Expect': "100-continue",
            'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1",
            'ReleaseVersion': self.ob
        }

def rot13(text):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += c
    return result

LEVEL_UP = "PebjaK64 ( GT= @SSobgfNYY )"
print(rot13(LEVEL_UP))

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

async def SEndPacKeT(ChaT, OnLinE, TypE, PacKeT, instance):
    if TypE == 'ChaT' and ChaT:
        ChaT.write(PacKeT)
        await ChaT.drain()
    elif TypE == 'OnLine' and OnLinE:
        OnLinE.write(PacKeT)
        await OnLinE.drain()

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": await Ua(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"
    }
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("open_id"), data.get("access_token")
            return None, None

async def encrypted_proto(encoded_hex, instance):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload

async def EncRypTMajoRLoGin(open_id, access_token, instance):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = instance.version
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWAUOUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return await encrypted_proto(string, instance)

async def MajorLogin(payload, instance):
    url = f"{instance.login_url}MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=instance.Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def GetLoginData(base_url, payload, token, instance):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    instance.Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=instance.Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(data):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(data)
    return proto

async def DecRypTLoGinDaTa(data):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(data)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto

async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9:
        headers = '0000000'
    elif uid_length == 8:
        headers = '00000000'
    elif uid_length == 10:
        headers = '000000'
    elif uid_length == 7:
        headers = '000000000'
    else:
        headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"

async def join_teamcode_packet(team_code, key, iv, region):
    fields = {
        1: 4,
        2: {
            4: bytes.fromhex("01090a0b121920"),
            5: str(team_code),
            6: 6,
            8: 1,
            9: {2: 800, 6: 11, 8: "1.111.1", 9: 5, 10: 1}
        }
    }
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def start_auto_packet(key, iv, region):
    fields = {1: 9, 2: {1: 12480598706}}
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def leave_squad_packet(key, iv, region):
    fields = {1: 7, 2: {1: 12480598706}}
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)

async def auto_start_loop(team_code, uid, chat_id, chat_type, key, iv, region, instance):
    instance.auto_start_running = True
    start_spam_duration = 25
    wait_after_match = 2
    start_spam_delay = 0.1
    
    while not instance.stop_auto and instance.running:
        try:
            join_pkt = await join_teamcode_packet(team_code, key, iv, region)
            await SEndPacKeT(instance.whisper_writer, instance.online_writer, 'OnLine', join_pkt, instance)
            await asyncio.sleep(1)

            start_pkt = await start_auto_packet(key, iv, region)
            end_time = time.time() + start_spam_duration
            while time.time() < end_time and not instance.stop_auto and instance.running:
                await SEndPacKeT(instance.whisper_writer, instance.online_writer, 'OnLine', start_pkt, instance)
                await asyncio.sleep(start_spam_delay)

            if instance.stop_auto or not instance.running:
                break

            waited = 0
            while waited < wait_after_match and not instance.stop_auto and instance.running:
                await asyncio.sleep(1)
                waited += 1
            if instance.stop_auto or not instance.running:
                break

            leave_pkt = await leave_squad_packet(key, iv, region)
            await SEndPacKeT(instance.whisper_writer, instance.online_writer, 'OnLine', leave_pkt, instance)
            await asyncio.sleep(1)

        except Exception as e:
            instance.log(f"Auto error: {e}")
            break
    instance.auto_start_running = False

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, instance, max_retries=3):
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, "IN")
            await SEndPacKeT(instance.whisper_writer, instance.online_writer, 'ChaT', P, instance)
            return True
        except Exception:
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def TcPOnLine(ip, port, jwt_token, bot_uid, key, iv, AutHToKen, instance, reconnect_delay=0.5):
    while instance.running:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            instance.online_writer = writer
            writer.write(bytes.fromhex(AutHToKen))
            await writer.drain()
            while instance.running:
                data = await reader.read(9999)
                if not data:
                    break
            instance.online_writer.close()
            await instance.online_writer.wait_closed()
            instance.online_writer = None
        except Exception as e:
            instance.log(f"Online error: {e}")
            if instance.online_writer:
                instance.online_writer.close()
                await instance.online_writer.wait_closed()
                instance.online_writer = None
        if instance.running:
            await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region, instance, reconnect_delay=0.5):
    while instance.running:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            instance.whisper_writer = writer
            writer.write(bytes.fromhex(AutHToKen))
            await writer.drain()
            ready_event.set()

            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                pK = await AuthClan(clan_id, clan_compiled_data, key, iv)
                if instance.whisper_writer:
                    writer.write(pK)
                    await writer.drain()

            while instance.running:
                data = await reader.read(9999)
                if not data:
                    break

                if data.hex().startswith("120000"):
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        inPuTMsG = response.Data.msg.strip().lower()
                        instance.log(f"Msg from {uid}: {inPuTMsG}")

                        if inPuTMsG.strip().isdigit():
                            team_code = inPuTMsG.strip()
                            if instance.auto_start_running:
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]Auto start already running. Send 's' to stop first.", uid, chat_id, key, iv, instance)
                                continue
                            
                            instance.stop_auto = False
                            await safe_send_message(response.Data.chat_type, f"[B][C][00FF00]Auto start ON for team {team_code}\nSend 's' to stop.", uid, chat_id, key, iv, instance)
                            instance.auto_start_task = asyncio.create_task(auto_start_loop(team_code, uid, chat_id, response.Data.chat_type, key, iv, region, instance))

                        elif inPuTMsG.strip() == 's':
                            if instance.auto_start_running:
                                instance.stop_auto = True
                                if instance.auto_start_task and not instance.auto_start_task.done():
                                    instance.auto_start_task.cancel()
                                await safe_send_message(response.Data.chat_type, "[B][C][00FF00]Auto start stopped.", uid, chat_id, key, iv, instance)
                            else:
                                await safe_send_message(response.Data.chat_type, "[B][C][FF0000]Auto start is not running.", uid, chat_id, key, iv, instance)

                        elif inPuTMsG.strip() in ('/help', 'help', '/menu', 'menu'):
                            help_msg = (
                                "[B][C][00FF00]━━━━━━━━━━\n"
                                "      🤖 BOT COMMANDS 🤖\n"
                                "━━━━━━━━━━\n"
                                "[FFFFFF]Send Team Code  [00FF00]- Start auto level up\n"
                                "[FFFFFF]Send 's'           [00FF00]- Stop auto level up\n"
                                "[FFFFFF]/help             [00FF00]- Show this menu\n"
                                "━━━━━━━━━━\n"
                            )
                            await safe_send_message(response.Data.chat_type, help_msg, uid, chat_id, key, iv, instance)

                    except Exception as e:
                        instance.log(f"Decode error: {e}")

            instance.whisper_writer.close()
            await instance.whisper_writer.wait_closed()
            instance.whisper_writer = None
        except Exception as e:
            instance.log(f"Chat error: {e}")
            if instance.whisper_writer:
                instance.whisper_writer.close()
                await instance.whisper_writer.wait_closed()
                instance.whisper_writer = None
        if instance.running:
            await asyncio.sleep(reconnect_delay)

async def MaiiiinE(instance):
    instance.log(f"Starting bot with UID: {instance.uid}")
    instance.init_globals()

    open_id, access_token = await GeNeRaTeAccEss(instance.uid, instance.password)
    if not open_id:
        instance.log("❌ Failed to get open_id/access_token")
        return None

    payload = await EncRypTMajoRLoGin(open_id, access_token, instance)
    login_resp = await MajorLogin(payload, instance)
    if not login_resp:
        instance.log("❌ MajorLogin failed")
        return None
    auth = await DecRypTMajoRLoGin(login_resp)
    token = auth.token
    if not token:
        instance.log("❌ No token")
        return None

    url = auth.url
    instance.region = getattr(auth, 'region', 'IND')
    instance.bot_uid = str(auth.account_uid)
    key = auth.key
    iv = auth.iv
    timestamp = auth.timestamp

    login_data = await GetLoginData(url, payload, token, instance)
    if not login_data:
        instance.log("❌ GetLoginData failed")
        return None
    ports = await DecRypTLoGinDaTa(login_data)
    online_ip, online_port = ports.Online_IP_Port.split(":")
    chat_ip, chat_port = ports.AccountIP_Port.split(":")

    instance.log(f"✅ Bot ONLINE! UID: {instance.bot_uid}")
    instance.log(f"🌐 Online Server: {online_ip}:{online_port}")
    instance.log(f"💬 Chat Server: {chat_ip}:{chat_port}")
    instance.log(f"📍 Region: {instance.region}")

    auth_token = await xAuThSTarTuP(int(instance.bot_uid), token, int(timestamp), key, iv)

    ready = asyncio.Event()
    task1 = asyncio.create_task(TcPChaT(chat_ip, chat_port, auth_token, key, iv, ports, ready, instance.region, instance))
    task2 = asyncio.create_task(TcPOnLine(online_ip, online_port, token, instance.bot_uid, key, iv, auth_token, instance))

    instance.log("🤖 Bot is online and waiting for commands...")
    await asyncio.gather(task1, task2)

async def StarTinG(instance):
    while instance.running:
        try:
            await MaiiiinE(instance)
        except Exception as e:
            instance.log(f"Restarting due to error: {e}")
            traceback.print_exc()
            if instance.running:
                await asyncio.sleep(5)

# Function to start a new bot instance
async def start_bot_instance(instance_id, uid, password):
    if instance_id in instances:
        return {"error": "Instance already exists"}
    
    instance = BotInstance(instance_id, uid, password)
    instances[instance_id] = instance
    instance.running = True
    
    # Start bot in background
    asyncio.create_task(StarTinG(instance))
    
    return {"success": True, "instance_id": instance_id}

# Function to stop a bot instance
async def stop_bot_instance(instance_id):
    if instance_id not in instances:
        return {"error": "Instance not found"}
    
    instance = instances[instance_id]
    instance.running = False
    instance.stop_auto = True
    
    # Clean up
    if instance.online_writer:
        instance.online_writer.close()
    if instance.whisper_writer:
        instance.whisper_writer.close()
    
    del instances[instance_id]
    
    return {"success": True, "instance_id": instance_id}

# Function to get instance status
def get_instance_status(instance_id):
    if instance_id not in instances:
        return {"error": "Instance not found"}
    
    instance = instances[instance_id]
    return {
        "instance_id": instance.instance_id,
        "uid": instance.uid,
        "bot_uid": instance.bot_uid,
        "running": instance.running,
        "auto_start_running": instance.auto_start_running,
        "region": instance.region
    }

# Function to list all instances
def list_instances():
    return {
        "total": len(instances),
        "instances": [
            {
                "instance_id": i.instance_id,
                "uid": i.uid,
                "bot_uid": i.bot_uid,
                "running": i.running,
                "auto_start_running": i.auto_start_running
            }
            for i in instances.values()
        ]
    }