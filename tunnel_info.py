import json,requests,time,os

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    return res_json["tunnels"][0]["public_url"][6:]

def send_tunnel_info():
    tunnel = get_ngrok_url()
    bot_token = os.environ['BOT_TOKEN']
    api_url = "https://api.telegram.org/bot{}/sendMessage?chat_id=809977861&text=```{}```&parse_mode=MarkdownV2".format(bot_token,return)
    requests.get(api_url)

send_tunnel_info()

while True:
	time.sleep(1000)