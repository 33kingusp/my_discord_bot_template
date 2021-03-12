# サーバのチャンネルが作成されたとき
async def on_guild_channel_create(channel):
    print('on_guild_channel_create : ', channel)

# サーバのチャンネルが削除されたとき
async def on_guild_channel_delete(channel):
    print('on_guild_channel_delete : ', channel)

# サーバのチャンネルが更新されたとき
async def on_guild_channel_update(channel):
    print('on_guild_channel_update : ', channel)

# サーバのメッセージがピン留めされたりはずされたりしたとき
async def on_guild_pins_update(channel, last_pin):
    print('on_guild_pins_update : ', channel, last_pin)

# サーバの連携サービスが更新されたとき
async def on_guild_integrations_update(guild):
    print('on_guild_integrations_update : ', guild)

# メンバが参加したとき
async def on_member_join(member):
    print('on_member_join : ', member)

# メンバが退出したとき
async def on_member_remove(member):
    print('on_member_remove : ', member)

# メンバーがプロフィールを編集したとき
async def on_member_update(before, after):
    print('on_member_update : ', before, after)

# ユーザがプロフィールを編集したとき
async def on_user_update(before, after):
    print('on_user_update : ', before, after)

# botがサーバを作成した、または参加したとき
async def on_guild_join(guild):
    print('on_guild_join : ', guild)

# botがサーバから削除されたとき
async def on_guild_remove(guild):
    print('on_guild_remove : ', guild)

# サーバが更新されたとき
async def on_guild_update(before, after):
    print('on_guild_update : ', before, after)

# サーバのロールが作成されたとき
async def on_guild_role_create(role):
    print('on_guild_role_create : ', role)

# サーバのロールが削除されたとき
async def on_guild_role_delete(role):
    print('on_guild_role_delete : ', role)

# サーバのロールが更新されたとき
async def on_guild_role_update(before, after):
    print('on_guild_role_update : ', before, after)

# サーバの絵文字が更新されたとき
async def on_guild_emojis_update(guild, before, after):
    print('on_guild_emojis_update : ', guild, before, after)

# サーバが利用可能になったとき
async def on_guild_available(guild):
    print('on_guild_available : ', guild)

# サーバが利用不可能になったとき
async def on_guild_unavailable(guild):
    print('on_guild_unavailable : ', guild)

# メンバがボイス状態を更新したとき
# ボイスチャンネルに参加・退出・マイクやスピーカーをミュートしたとき
async def on_voice_state_update(member, before, after):
    print('on_voice_state_update : ', member, before, after)

# メンバがBANされたとき
async def on_member_ban(guild, user):
    print('on_member_ban : ',  guild, user)

# メンバがBANを解除されたとき
async def on_member_unban(guild, user):
    print('on_member_unban : ',  guild, user)

# 招待が作成されたとき
async def on_invate_create(invite):
    print('on_invate_create', invite)

# 招待が削除されたとき
async def on_invate_delete(invite):
    print('on_invate_delete', invite)

def init(client):
    client.on_guild_channel_create = on_guild_channel_create
    client.on_guild_channel_delete = on_guild_channel_delete
    client.on_guild_channel_update = on_guild_channel_update
    client.on_guild_pins_update = on_guild_pins_update
    client.on_guild_integrations_update = on_guild_integrations_update
    client.on_guild_join = on_guild_join
    client.on_guild_remove = on_guild_remove
    client.on_guild_update = on_guild_update
    client.on_guild_role_create = on_guild_role_create
    client.on_guild_role_delete = on_guild_role_delete
    client.on_guild_role_update = on_guild_role_update
    client.on_guild_emojis_update = on_guild_emojis_update
    client.on_guild_available = on_guild_available
    client.on_guild_unavailable = on_guild_unavailable
    client.on_voice_state_update = on_voice_state_update
    client.on_member_ban = on_member_ban
    client.on_member_unban = on_member_unban
    client.on_invate_create = on_invate_create
    client.on_invate_delete = on_invate_delete
    return
