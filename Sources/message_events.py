current_channel = None

# だれかがメッセージを入力し始めたとき
async def on_typing(cnannel, user, when):
    print('on_typing : ', cnannel, user, when)

# だれかが発言したとき
async def on_message(message):
    global current_channel
    print('on_message :', message)
    
    # botの発言には反応しない
	# 別のチャンネルでは反応しない
    if (message.author.bot) or (current_channel is None) or (current_channel != message.channel):
        return
    
    # print(message.author.id, message.content, message.attachments)

    # 送られてきたメッセージによる動作を記入
    return

# メッセージが削除されたとき
async def on_message_delete(message):
    print('on_message_delete : ', message)

# メッセージが一括削除されたとき
async def on_bulk_message_delete(messages):
    print('on_bulk_message_delete : ', messages)

# メッセージが削除されたとき
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_message_delete(payload):
    print('on_raw_message_delete : ', payload)

# メッセージが一括削除されたとき
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_bulk_message_delete(payload):
    print('on_raw_bulk_message_delete : ', payload)

# メッセージが編集されたとき
async def on_message_edit(before, after):
    print('on_message_edit : ', before, after)

# メッセージが編集されたとき
# 内部キャッシュの状態に関係なく呼び出される
async def on_raw_message_edit(payload):
    print('on_raw_message_edit : ', payload)

# イベントの登録
def init(client):
    client.on_typing = on_typing
    client.on_message = on_message
    client.on_message_delete = on_message_delete
    client.on_bulk_message_delete = on_bulk_message_delete
    client.on_raw_message_delete = on_raw_message_delete
    client.on_raw_bulk_message_delete = on_raw_bulk_message_delete
    client.on_message_edit = on_message_edit
    client.on_raw_message_edit = on_raw_message_edit
    return
    