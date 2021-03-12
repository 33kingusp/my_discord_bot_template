# リアクションが追加されたとき
async def on_reaction_add(reaction, user):
    print('on_reaction_add : ', reaction, user)

# リアクションが追加されたとき
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_reaction_add(payload):
    print('on_raw_reaction_add : ', payload)

# リアクションが削除されたとき
async def on_reaction_remove(reaction, user):
    print('on_reaction_remove : ', reaction, user)

# リアクションが削除されたとき
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_reaction_remove(payload):
    print('on_raw_reaction_remove : ', payload)

# リアクションが全て削除されたとき
async def on_reaction_clear(message, reactions):
    print('on_reaction_clear : ', message, reactions)

# リアクションが全て削除されたとき
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_reaction_clear(payload):
    print('on_raw_reaction_clear : ', payload)

# Called when a message has a specific reaction removed from it.(わからん)
async def on_reaction_clear_emoji(reaction):
    print('on_reaction_clear_emoji : ', reaction)

# Called when a message has a specific reaction removed from it.(わからん)
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_reaction_clear_emoji(payload):
    print('on_raw_reaction_clear_emoji : ', payload)

# イベントの登録
def init(client):
    client.on_reaction_add = on_reaction_add
    client.on_raw_reaction_add = on_raw_reaction_add
    client.on_reaction_remove = on_reaction_remove
    client.on_raw_reaction_remove = on_raw_reaction_remove
    client.on_reaction_clear = on_reaction_clear
    client.on_raw_reaction_clear = on_raw_reaction_clear
    client.on_reaction_clear_emoji = on_reaction_clear_emoji
    client.on_raw_reaction_clear_emoji = on_raw_reaction_clear_emoji