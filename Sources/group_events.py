# だれかがグループチャンネルに参加したとき
async def on_group_join(channel, user):
    print('on_group_join : ', channel, user)

# だれかがグループチャンネルから脱退したとき
async def on_group_remove(channel, user):
    print('on_group_remove : ', channel, user)

def init(client):
    client.on_group_join =  on_group_join
    client.on_group_remove =  on_group_remove
    return