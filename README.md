# Diana - Your Blunt AI Assistant

A terminal-based AI assistant powered by Claude that can execute Python code directly on your machine. Think Jarvis, but with less politeness and more swearing. (depends on how you configure it actually)

## What The Fuck Does It Do?

Diana is a conversational AI that:
- Responds to your questions and commands
- Executes Python code on your computer (yeah, security is not our priority here)
- Processes files, directory structures, and entire projects
- Can be customized to know specific shit about your system
- Has a personality that doesn't sugar-coat anything

**Is it useful?** Yes.  
**Is it safe?** Absolutely fucking not. Deal with it.

## Installation

### Dependencies

This thing needs:
- `py-utils` (custom Python library module, [accessible here](https://github.com/Rrominet/py-utils))
- `anthropic-sdk-python` ([GitHub](https://github.com/anthropics/anthropic-sdk-python))

But the install script handles that for you, so don't worry about it.

### Install Steps

```bash
git clone https://github.com/Rrominet/diane.git
cd ./diane
sudo chmod +x ./install
sudo ./install
cd ..
rm -rf ./diane  # Optional: remove the git repo once installed
```

Done. That simple.
> [!NOTE]
> The install script should work on any major distros.
> If you have error when installing the packages, just install them manually after running the install script with `pip`.

## Usage

Launch it:
```bash
/opt/diane/diane
```

Get help:
```bash
/opt/diane/diane help
```

### Built-in Commands

- `doc` or `help` - Show documentation
- `rules` - Display input parser rules
- `exit` - Quit the program

Just type normally and Diana will parse your input, send it to Claude, and execute any Python code if needed.

## Configuration

All config files are located in `/opt/diane/data/`:
(if the directory, `/opt/diane/data/` doesn't exist, create it)

### API Key (Required)
Edit `/opt/diane/data/api-keys` and add your Anthropic API key on the second line.

### Context (AI Personality)
Edit `/opt/diane/data/context` to define Diana's personality and what she knows about your system.

### Model
Edit `/opt/diane/data/model` to specify which Claude model to use (first line only).

### Greetings
Edit `/opt/diane/data/greetings` - add one greeting per line. Diana picks one randomly at startup.

### Variables
Edit `/opt/diane/data/variables` (JSON format) to define variables you can use in your messages.

## Project Structure

```
diane/
├── diane           # Main executable
├── ai.py           # Anthropic API wrapper and code execution
├── config.py       # Configuration loader
├── parser.py       # Input parser (not shown but referenced)
├── data/
│   ├── api-keys    # Your Anthropic API key
│   ├── context     # AI system prompt
│   ├── model       # Claude model version
│   ├── greetings   # Random startup messages
│   └── variables   # JSON variables file
└── py_exec/        # Temporary Python execution files
```

## How Code Execution Works

When Diana wants to execute Python code, she ends her response with:
`::code::`
And will add the python code after it.

The code after that marker gets:
1. Extracted and saved to `/opt/diane/py_exec/[timestamp]__py_exec.py`
2. Executed with Python 3
3. Output (stdout) is captured and sent back to Diana in your next message

She can see the results and respond accordingly.

## How you can integrate files, directories and projects in your messages

In your message, you can directly include files, directories and projects like this:
- Files : 
Just write `:f:/the/path/to/your/file.ext:f:` in your message where it makes sense, it willl be replaced by the actual file content.

- Directories Structure: 
Just write `:d:/the/path/to/your/directory:d:` in your message where it makes sense, it willl be replaced by the actual directory structure.

- Entire Projects : 
Just write `:src:/the/path/to/your/project:src:` in your message where it makes sense, it willl be replaced by all the files that are code in your project.

## Security Warning

Diana can execute **any fucking Python code** on your machine. This means:
- File system access
- Network requests
- System commands via subprocess
- Literally anything Python can do

Only use this if you understand what you're doing. Don't blame me when she deletes your shit.

## TODO

- [x] Config management through the program itself (currently all manual editing)
- [ ] Real GUI implementation (probably with [fxos_gui-lib](https://github.com/Rrominet/fxos_gui-lib))
- [ ] Better error handling
- [ ] Conversation history management
- [ ] Maybe some actual security measures (but let's be real, probably not)
- [ ] Separate the code that Diana can execute from the context to make it more clean.

## Why "Diana"?

Because Jarvis was taken and this needed a name that sounds like an AI assistant who doesn't take any bullshit.

---

**Note:** This is a personal project. Use at your own risk. No warranty, no support, no fucks given.

> [!NOTE]
> This Readme was actually written by Diana.
