import os
from slack_bolt import App
from slack_sdk import WebClient
from mcp9600.temp import temp
# Start your app
if __name__ == “__main__“:
    temp()
    client = WebClient(os.environ[“SLACK_BOT_TOKEN”])
    response = client.chat_postMessage(
        channel=“#p1_nu_thermo”,
        text=“The current temperture is ” + str(mcp.temperture),
    )