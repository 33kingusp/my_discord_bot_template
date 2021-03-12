# プライベートチャンネルが作成されたとき
async def on_private_channel_create(channel):
    print('on_private_channel_create : ', channel)

# プライベートチャンネルが削除されたとき
async def on_private_channel_delete(channel):
    print('on_private_channel_delete : ', channel)

# プライベートグループDMが更新されたとき
async def on_private_channel_update(channel):
    print('on_private_channel_update : ', channel)

# プライベートチャンネルのメッセージがピン留めされたりはずされたりしたとき
async def on_private_channel_pins_update(channel, last_pin):
    print('on_private_channel_pins_update : ', channel, last_pin)

def init(client):
    client.on_private_channel_create = on_private_channel_create
    client.on_private_channel_delete = on_private_channel_delete
    client.on_private_channel_update = on_private_channel_update
    client.on_private_channel_pins_update = on_private_channel_pins_update
    return