import requests
import hashlib
import uuid

def get_player_uuid(username):
    online_uuid = get_premium_uuid(username)
    offline_uuid = offline_player_uuid(username)
    return online_uuid, offline_uuid

def get_premium_uuid(username):
    try:
        response = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
        if response.status_code == 200:
            return response.json().get('id')
    except Exception as e:
        pass
    return None

def print_uuids(username, online_uuid, offline_uuid):
    print(f'Username: {username}')
    if online_uuid is not None:
        print(f'Premium UUID: {online_uuid}')
    else:
        print(f'Premium UUID: None')
    print(f'Cracked/Offline UUID: {offline_uuid}')

def get_uuid_from_user():
    return input("Enter Minecraft username: ").strip()

def uuid_command(username):
    try:
        online_uuid, offline_uuid = get_player_uuid(username)
        print_uuids(username, online_uuid, offline_uuid)
    except KeyboardInterrupt:
        print('\nOperation interrupted.')
    except Exception as e:
        print(f"An error occurred: {e}")

def offline_player_uuid(username):
    data = hashlib.md5(("OfflinePlayer:" + username).encode('utf-8')).digest()
    data = bytearray(data)
    data[6] = data[6] & 0x0f | 0x30
    data[8] = data[8] & 0x3f | 0x80
    return str(uuid.UUID(bytes=bytes(data)))

if __name__ == "__main__":
    username = get_uuid_from_user()
    uuid_command(username)
