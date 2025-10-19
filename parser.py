import os
import shutil
from ml import fileTools as ft

from config import config

def file(path) : 
    if not os.path.exists(path) :
        raise Exception("File " + path + " does not exist.")
    res = ""
    res = "\n\nContent of " + path + " :\n"
    res += ft.read(path) + "\n\n"
    return res

def _dir(path) : 
    if not os.path.exists(path) :
        raise Exception("Dir " + path + " does not exist.")
    if not os.path.isdir(path) :
        raise Exception("Dir " + path + " is a file.")

    ls = os.listdir(path)
    res = "\n\nFiles list in " + path + " :\n"
    for f in ls : 
        res += f + "\n"
    res += "\n\n"
    return res

def source_code(dirpath): 
    if not os.path.exists(dirpath) :
        raise Exception("Dir " + dirpath + " does not exist.")
    if not os.path.isdir(dirpath) :
        raise Exception("Dir " + dirpath + " is a file.")
    extensions = ["py", "js", "java", "c", "cpp", "go", "css", "html", "h", "hpp", "rs", "sh", "bash", "zsh", "php", "lua", "ts", "swift", "kt", "r", "mm", "m", "scala"]

    _files = ft.byExtensions(dirpath, extensions)
    for root, dirs, filesls in os.walk(dirpath):
        for _file in filesls : 
            filepath = os.path.join(root, _file)
            ext = ft.ext(filepath)
            if ext != "": continue
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('#!'):
                        _files.append(filepath)
            except:
                pass  # Can't read the file, skip it
    res = "\n\nSource code in " + dirpath + " :\n"
    for f in _files : 
        res += file(f)
    res += "\n\n"
    return res

#separators separated by a space : func
#usage : 
#:file:/my/file/path:file:
rules = {
        ":file: :f:": file,
        ":dir: :d:": _dir,
        ":src: :s:": source_code,
}

def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

def printRules(dum) :
    for r in rules : 
        print(r + " : " + str(rules[r]))

def parsed(user_input): 
    res = user_input
    for var in config.variables : 
        res = res.replace("$" + var, config.variables[var])
    for r in rules : 
        for k in r.split(" ") :
            tmp = res.split(k)
            for i in range(len(tmp)): 
                if is_odd(i):
                    tmp[i] = rules[r](tmp[i])
            res = "".join(tmp)

    return res


