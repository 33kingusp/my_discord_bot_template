import json
import discord
import message_events
import reaction_events
import private_events
import guild_events
import group_events

client = discord.Client()   # dicord botを使用
config = None               # token情報などのコンフィグ
current_channel = None      # botが稼働しているチャンネル

# Discordに接続したとき
@client.event
async def on_connect():
    print('on_connect')

# Discordから切断したとき
@client.event
async def on_disconnect():
    print('on_disconnect')

# ログインしたとき
@client.event
async def on_ready():
	print('on_ready')

# セッションを再開したとき
@client.event
async def on_resumed():
    print("on_resumed")

# コンフィグの読み込み
def open_config():
    with open('../config.json', 'r') as fp:
        conf = json.load(fp)
    return conf

# メインメソッド
def main():
    global config
    config = open_config()

    message_events.init(client)
    reaction_events.init(client)
    private_events.init(client)
    guild_events.init(client)
    group_events.init(client)

    client.run(config["bot_token"])

    exit(0)

if __name__ == "__main__":
    main()