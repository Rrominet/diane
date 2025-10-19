import sys
import os
import datetime
import subprocess
from ml import fileTools as ft

pdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(pdir + os.sep + "anthropic-sdk-python/src")

import anthropic
from config import config

client = anthropic.Anthropic(api_key=config.apiKey)
messages = []
last_code_result = ""

def send(to_send, model=config.model, context=config.context, max_tokens=8128) : 
    global messages
    if last_code_result != "" :
        to_send += "\n\nFYI: Your Last python code result was:\n" + last_code_result

    if(to_send == "") :
        return "", ""

    messages.append({"role": "user", "content": to_send})
    try : 
        response = client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=context,
                messages = messages
            )
    except Exception as e :
        print(e)
        return "", ""
    text = response.content[0].text
    tmp = text.split("::code::")  
    text = tmp[0]
    code = ""
    if (len(tmp) > 1) :
        code = tmp[1]
    if (text != "") :
        messages.append({"role": "assistant", "content": text})
    return text, code

def executePython(code): 
    global last_code_result
    if not os.path.isdir(pdir + os.sep + "py_exec"):
        os.mkdir(pdir + os.sep + "py_exec")
    pyfile = pdir + os.sep + "py_exec" + os.sep + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "__py_exec.py"
    ft.write(code, pyfile)
    pc = subprocess.run([config.py, pyfile], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    last_code_result = pc.stdout.decode("utf-8")
    if (pc.returncode != 0) : 
        print("Error: " + pc.stderr.decode("utf-8"))
    else :
        return last_code_result


