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

The scripts looks for config.ini. This one needs to contain your OpenAI API key in the following format: 
```
[config]
api_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
