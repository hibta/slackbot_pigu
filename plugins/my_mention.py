# coding: utf-8

# モジュールのインポート
from slackbot.bot import respond_to
from slackbot.bot import listen_to

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？
#
# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない


# ---------------挨拶系---------------


# "おはよう"を返す
@respond_to("おはよう")
@respond_to("お早う")
def ohayou(message):
    message.reply("おはよ〜")


# "こんにちは"を返す
@respond_to("こんにちは")
@respond_to("こんにちわ")
def konnichiha(message):
    message.reply("こんにちは〜")


# "こんばんは"を返す
@respond_to("こんばんは")
@respond_to("こんばんわ")
def konbanha(message):
    message.reply("こんばんわ〜")


# "おやすみ"を返す
@respond_to("おやすみ")
@respond_to("お休み")
def oyasumi(message):
    message.reply("お休み〜")


# ------------リアクション系------------


# "いいね"という投稿にグッドのリアクションを付ける
@listen_to("いいね")
@listen_to("good")
@listen_to("Good")
def iine(message):
    message.react('+1')


# ---------------反応系---------------


# "あの"を含む投稿に反応
@listen_to('あの')
def listen_func(message):
    message.reply('？')
