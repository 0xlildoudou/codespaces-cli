import os
from codespaces_cli.core.cli import cli

def check_env():
    env_vars = ['GITHUB_TOKEN']

    for env_var in env_vars:
        try:
            os.environ[env_var]
            return True
        except:
            print(f'{env_var} environement variable not set')
            return False

def main(): 
    if check_env():
        cli()
    else:
        exit(1)


if __name__ == '__main__':
    main()