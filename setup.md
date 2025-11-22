# Creating a `.venv` with Python 3.13 on Windows Using VS Code

This guide walks you through creating a Python 3.13 virtual environment (`.venv`) on a Windows system using Visual Studio Code (VS Code).

## Prerequisites

- **Python 3.13** must be installed  
  👉 Download from: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
- **Ensure Python 3.13 is added to your PATH** during installation.
- VS Code must be installed  
  👉 Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Install the **Python extension** in VS Code (from the Extensions view)

---

## Step-by-Step Instructions

### 1. Open Your Project Folder in VS Code

1. Launch VS Code.
2. Click on `File` > `Open Folder...` and select or create your project folder.

---

### 2. Open a New Terminal

1. Go to the top menu and click `Terminal` > `New Terminal`.
2. A terminal will open at the bottom of VS Code (PowerShell or Command Prompt by default).

---

### 3. Confirm Python 3.13 is Available

In the terminal, check your Python version:

```bash
python --version
```

OR

```bash
python3.13 --version
```

You should see:

```
Python 3.13.x
```

If `python` does not point to version 3.13, use `python3.13` explicitly in the next steps.

---

### 4. Create the Virtual Environment

Use this command to create the virtual environment using Python 3.13:

```bash
python3.13 -m venv .venv
```

✅ This will create a `.venv` folder in your project directory containing your Python 3.13 environment.

---

### 5. Activate the Virtual Environment

- For **PowerShell**:

```powershell
.venv\Scripts\Activate.ps1
```

- For **Command Prompt**:

```cmd
.venv\Scripts\activate.bat
```

- For **Git Bash**:

```bash
source .venv/Scripts/activate
```

> You’ll know it's activated when you see `(.venv)` at the beginning of the terminal line.

### 5.5 Activation Permision

- **Important Considerations**:

Execution Policy: If you encounter an _error_ stating that scripts cannot be loaded or run, it is likely due to PowerShell's execution policy. To allow script execution, you may need to adjust the policy. You can do this by running PowerShell as an administrator and executing:

```bash

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### 6. Select Python 3.13 Interpreter in VS Code

1. Press `Ctrl+Shift+P` to open the Command Palette.
2. Type and select: `Python: Select Interpreter`.
3. Choose the one that shows `.venv` and Python 3.13, such as:

```
./.venv/Scripts/python.exe
```

---

### 7. (Optional) Create a `requirements.txt` File

Save your installed packages:

```bash
pip freeze > requirements.txt
```

Install packages later from this file:

```bash
pip install -r requirements.txt
```

---

## Deactivating the Virtual Environment

To deactivate the virtual environment:

```bash
deactivate
```

---

## Troubleshooting

- If activation fails in PowerShell, you may need to enable script execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating the environment again.

---

✅ You now have a Python 3.13 virtual environment ready in VS Code on Windows!
