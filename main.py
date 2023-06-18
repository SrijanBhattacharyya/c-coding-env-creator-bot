import os, sys, time, json, setup, stat

setup.setup (os.path.abspath (__file__))

mainDir = os.path.dirname (os.path.abspath (__file__))


def get_env_path (flag_only: bool = False) -> (str|None):
    args = sys.argv [1::]

    if args == []: help ()

    if flag_only:
        for arg in args:
            if arg [0] == '-':
                return arg

    else:
        for arg in args:
            if arg [0] != '-':
                if "/" not in arg:
                    arg = os.path.join (os.getcwd (), arg)

                return arg


def check_flag (cmd: str) -> None:
    if cmd == '-t' or cmd == '-test':
        time.sleep (10)
        os.system (f"rm -r '{env_path}'")
        print (f"\033[1;31m[+] Removed '{get_env_path ()}' successfully.\033[0m")

    if cmd == '-h' or cmd == 'help':
        help ()


def mk_code_env () -> None:
    if os.path.exists (env_path):
        print (f"\033[1;31m[-] PathAlreadyExistsError: Can't create venv '{env_path}': File already exists.\033[0m")
        exit ()

    else: os.makedirs (env_path)


def check_if_created () -> bool:
    return os.path.exists (env_path)


def get_default_code  (mainDir: os.path) -> dict:
    default_cfg_files_dir = os.path.join (mainDir, "defaults")
    list_dir = os.listdir (default_cfg_files_dir)
    data = {}

    os.chdir (default_cfg_files_dir)

    for elem in list_dir:
        with open (elem, "r") as data_file:
            if "code-workspace" in elem:
                elem = os.path.join (".vscode", elem)

            if ".json" in elem:
                data [elem] = json.load (data_file)

            else:
                data [elem] = data_file.readlines ()

    return data


def mod_cfg (data: dict):
    # modifying the code-workspace file for the new venv
    cfg = data [".vscode/code-workspace.json"]

    cfg ["folders"]["path"]                             = env_path
    cfg ["settings"]["terminal.integrated.cwd"]         = env_path

    cfg = data ["settings.json"]

    cfg ["App-Settings"]["project_name"] = os.path.split (env_path)[1]

    return data


def config_code_env (data: dict) -> None:
    cmd = f"gcc -o output program.c"

    os.chdir (env_path)

    for file_path in data.keys ():
        file = file_path

        try:
            os.makedirs (os.path.dirname (file_path))
            file = os.path.join (os.path.dirname (file_path), f"{os.path.split (env_path)[1]}.code-workspace")

        except FileNotFoundError:
            pass

        with open (file, "w") as f:
            if ".json" in file_path:
                json.dump (data [file_path], f, indent = 4)

            else:
                f.writelines (data [file_path])

        if '.sh' in file_path:
            os.chmod('compiler.sh', stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

    os.system (cmd)


def help ():
    h = '''syntax: cbot -flag path-to-env

FLAGS:
  -h, -help        help
  -t, -test        test

Made by Srijan Bhattacharyya.'''

    print (h)
    exit ()


def main ():
    global env_path, data
    env_path = get_env_path ()
    data = mod_cfg (get_default_code (mainDir))

    mk_code_env ()

    if check_if_created ():
        config_code_env (data)

    print (f'\033[1;32m[+] Venv created successfully.\033[0m')
    print (f"\033[1;33mPath to venv: {env_path}\033[0m")

    check_flag (get_env_path (True))


if __name__ == "__main__":
    try:
        main ()

    except Exception as e:
        print (f'\033[1;31m[-] {e}\033[0m')
