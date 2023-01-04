# askAI
A Python script that allows the user to chat with an AI using OpenAI's API. For as long as the script is running, the AI will remember the conversation your having. 

## Example output: 
![image](https://user-images.githubusercontent.com/60260940/210553358-aade3dda-0090-41a8-a840-73d9f10ebce4.png)


## Command
- /quit will terminate the script
- CTRL+C will terminate the script

## Requirements
The script requires the following modules to be installed: 
- openai 
- random
- os
- configparser

The scripts looks for your OpenAI API key in config.ini, location as it is located. The file needs to have the have the following format: 
```
[config]
api_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Getting an OpenAI API key: 

Register on OpenAP's webpage: https://beta.openai.com/signup

After signing up, navigate to view API keys in the menu
1. Click on the menu "Personal" in the top right corner: 
2. Click view API keys
3. Create new secrey key

![image](https://user-images.githubusercontent.com/60260940/210555274-841d5021-d0ba-4b51-9d5a-c383325eb346.png)

4. Copy the key and paste it in config.ini
