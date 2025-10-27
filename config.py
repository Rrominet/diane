from ml import fileTools as ft
from ml import log
import os
import random
import json
pdir = os.path.dirname(os.path.abspath(__file__)) + os.sep + "data"

class Config : 
    def __init__(self) :
        self.model = ""
        self.context = ""
        self.apiKey = ""
        self.textEditor = ""
        self.greeting = "Hey ! What do we do today ?"
        self.variables = {}

        if os.path.exists("/usr/bin/python3"): 
            self.py = "/usr/bin/python3"
        elif os.path.exists("/usr/bin/python"): 
            self.py = "/usr/bin/python"
        elif os.path.exists("/usr/local/bin/python3"): 
            self.py = "/usr/local/bin/python3"
        elif os.path.exists("/usr/local/bin/python"): 
            self.py = "/usr/local/bin/python"
        else : 
            self.py = "python3"

        if not os.path.exists(pdir) :
            os.mkdir(pdir)

    def readModel(self) : 
        filepath = os.path.join(pdir, "model")
        if not os.path.exists(filepath) :
            log.print ("Error : No model file found", "red") 
            self.askModel()
            return
        data = ft.read(filepath)
        self.model = data.split("\n")[0]

    def readTextEditor(self) : 
        filepath = os.path.join(pdir, "text-editor")
        if not os.path.exists(filepath) :
            log.print ("Info : No text-editor file found - using the default one nano", "grey") 
            self.textEditor = "nano"
            return
        data = ft.read(filepath)
        self.textEditor = data

    def askModel(self) : 
        model = input ("Enter the Claude model you want to use : ")
        ft.write(model, os.path.join(pdir, "model"))
        self.model = model

    def editContext(self): 
        print (self.textEditor + " \"" + os.path.join(pdir, "context") + "\"")
        os.system(self.textEditor + " \"" + os.path.join(pdir, "context") + "\"")

    def readContext(self) : 
        filepath = os.path.join(pdir, "context")
        if (not os.path.exists(filepath)) :
            log.print ("Info : No context file found", "grey")
        data = ft.read(filepath)
        self.context = data

    def readApiKey(self) : 
        filepath = os.path.join(pdir, "api-keys")
        if not os.path.exists(filepath) :
            log.print ("Error : No api-keys file found", "red")
            self.askApiKey()
            return
        data = ft.read(filepath)
        tmp = data.split("\n")
        if len(tmp) < 2 :
            self.apiKey = tmp[0]
        else :
            self.apiKey = tmp[1]

    def askApiKey(self) : 
        key = input ("Enter your Anthropic API key : ")
        ft.write(key, os.path.join(pdir, "api-keys"))
        self.apiKey = key

    def loadGreeting(self) : 
        filepath = os.path.join(pdir, "greetings")
        if (not os.path.exists(filepath)) :
            return
        data = ft.read(filepath)
        ls = data.split("\n")
        idx = random.randint(0, len(ls) - 1)
        self.greeting = ls[idx]

    def loadVariables(self): 
        filepath = os.path.join(pdir, "variables")
        if not os.path.exists(filepath) :
            log.print ("Info : No variables file found", "grey") 
            return
        data = ft.read(filepath)
        try: 
            self.variables = json.loads(data)
        except:
            log.print("Error : impossible to parse the variable file", "red")

    def load(self): 
        self.readModel()
        self.readContext()
        self.readApiKey()
        self.loadGreeting()
        self.loadVariables()
        self.readTextEditor()

    def log(self): 
        log.print("Model : " + self.model, "grey")
        log.print("API key : " + self.apiKey, "grey") 
        log.print("Text editor : " + self.textEditor, "grey")


config = Config()
config.load()

def askModel(dum) : 
    config.askModel()

def askApiKey(dum) : 
    config.askApiKey()

def _log(dum) : 
    config.log()

def editContext(dum) : 
    config.editContext()
