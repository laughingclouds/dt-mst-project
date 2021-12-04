# dt-mst-project

group project for dt mst

## Installing

I have used Python 3.9.5 for this project. Normally it wouldn't have mattered much
but the smartass type hinting I did won't work for Python 3.8.z (and lower).
So please make sure you have version 3.9.5 (or higher) installed.

### Virtual Environment

We don't want our global scope to be polluted so let's set up a virtual environment.

Execute the following in your terminal/powershell/cmd

Windows

```bash
py -m venv venv
```

Linux

```bash
python3 -m venv venv
```

This creates a virtual environment with the name `venv` in your project root. Make sure you don't delete your `.gitignore` (don't want to push venv to the repo).

#### Activate venv

To activate your venv, well, I forgot the commands for windows. Good luck.

Linux

```bash
source venv/bin/activate
```

### requirements.txt

To install the same versions of the packages used to complete this project, execute the following command (after activating the venv).

Windows

```bash
py -m pip install -r requirements.txt
```

Linux

```bash
pip install -r requirements.txt

```
