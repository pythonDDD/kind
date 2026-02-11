# @title 優しい言葉BOT Ver1.1 (変数格納版)
import google.generativeai as genai

# APIキーを設定
GEMINI_API_KEY = "AIzaSyCNwsYw22CzwWext1R2D6tLJhV3b9XoR4E"

# 次のセルで使うための変数を空で用意しておく
message = ""

def generate_healing_message():
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-flash-latest')

        print("--- 生成中... ---")
        prompt = "心が疲れた人に贈る、140文字以内の短く優しい癒やしの言葉を1つ生成してください。"
        response = model.generate_content(prompt)

        if response.text:
            return response.text.strip()
        else:
            return "（メッセージの生成に失敗しました）"

    except Exception as e:
        print(f"\n❌ エラーが発生しました:\n{e}")
        return ""

# 関数を実行して、結果をグローバル変数の message に入れる
message = generate_healing_message() + "\n#優しい言葉"

if message:
    print("\n【生成結果を message に格納しました】")
    print(message)

# 例えば、さらに加工して使うこともできます
print(f"\n文字数は {len(message)} 文字です。")

# twitter-----------------------------------------------------------
import tweepy
import random

# Twitter API認証情報
api_key = 'eruL9ovXYrZjErDxdVV43wdPC'
api_key_secret = 'as59ntnBiKzGkPal0VvxTYThiuBG1A4A3LQ8zpkqX6d9q1ApfP'
access_token = '2007277067545796608-lw7UvTbH4sFUWQQYGUz4J61vAorwfX'
access_token_secret = 'qJSAOwzOsFAg5FDS6jeLkw764JZm5UMm65q4G7hWlzeYN'


#Twitter Developer Portalから取得したキーを設定
ck = api_key
cs = api_key_secret
at = access_token
ats = access_token_secret


# Twitter API credentials
consumer_key = ck
consumer_secret = cs
access_token = at
access_token_secret = ats

# Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret)



# 確認用（コンソールに出力して内容をチェック）
print("ツイート予定の内容:")
print(message)

# 4. 画像アップロードとツイート実行
#image_paths = ["btc.png", "btc1.png"]
# リスト内包表記でメディアIDを取得
# media_ids = [api.media_upload(filename=path).media_id for path in image_paths]

# ツイート送信
client.create_tweet(text=message)#, media_ids=media_ids[:2])
