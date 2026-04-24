# Python Package Management (A Guide for Node.js Developers)

If you are coming from a JavaScript/Node.js background, Python's package management ecosystem has similar concepts but uses different tools and terminologies. This guide explains how Python handles dependencies and compares it directly to Node.js concepts.

## 1. `package.json` Equivalent

In Node.js, `package.json` stores your project metadata, scripts, and a list of your dependencies. 
In Python, there are a few ways this is handled depending on the complexity of your project:

* **`requirements.txt` (Simple Projects):** This is the most common and basic way to list dependencies. It's simply a text file with one package per line. However, it doesn't store project metadata (like author, version) or scripts.
* **`pyproject.toml` (Modern Standard):** This is the modern equivalent of `package.json`. It is a configuration file that stores project metadata, build system requirements, and dependencies. Tools like Poetry, Flit, and modern `pip` use this.
* **`setup.py` / `setup.cfg` (Legacy):** Older projects use these files to define project metadata and dependencies. They are slowly being phased out in favor of `pyproject.toml`.

## 2. `package-lock.json` Equivalent

In Node.js, `package-lock.json` locks the exact versions of all dependencies (and sub-dependencies) to ensure deterministic builds across different environments.
In Python:

* **`requirements.txt` (via `pip freeze`):** While `requirements.txt` can be used just to list top-level packages (like `requests`), developers often use the command `pip freeze > requirements.txt` to output *every* installed package and its exact version (e.g., `requests==2.31.0`). In this usage, it acts just like a lock file.
* **`poetry.lock` / `Pipfile.lock`:** If you use advanced package managers like Poetry or Pipenv (which are very similar to `npm` or `yarn`), they automatically generate a dedicated `.lock` file to lock down exact versions.

## 3. `node_modules` Equivalent

In Node.js, dependencies are installed locally in the `node_modules` folder inside your project directory.
In Python, by default, packages are installed **globally** on your system. To avoid version conflicts between different projects, Python uses **Virtual Environments (`venv`)**.

* **Virtual Environment (`venv`):** This is an isolated environment for your project. When activated, any packages you install will go into a local folder (usually named `venv` or `.env` inside your project), acting exactly like `node_modules`.

**How to use it:**
```bash
# Create a virtual environment named "venv"
python3 -m venv venv

# Activate it (Linux/Mac)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate
```

## 4. `npm install` Equivalent

In Node.js, `npm` is the default package manager.
In Python, **`pip`** (Pip Installs Packages) is the default package manager.

| Node.js Command | Python Equivalent | Explanation |
| :--- | :--- | :--- |
| `npm install <package>` | `pip install <package>` | Installs a package (e.g., `pip install requests`). |
| `npm install` | `pip install -r requirements.txt` | Installs all dependencies listed in the file. |
| `npm uninstall <package>` | `pip uninstall <package>` | Removes a package. |
| `npm list` | `pip list` | Shows all installed packages. |

## Modern All-in-One Tools

If you want an experience that is almost exactly like `npm` or `yarn` (handling virtual environments, locking, and metadata all at once), you should look into modern Python tools:

1. **Poetry:** Uses `pyproject.toml` and `poetry.lock`. It automatically creates virtual environments and provides commands like `poetry add <package>` (like `npm install <package>`).
2. **Pipenv:** Uses `Pipfile` and `Pipfile.lock`. Brings `npm`-like workflow to Python.
