import argparse
from codespaces_cli.core.github import *
from rich.console import Console

console = Console()

def parser():
    p = argparse.ArgumentParser(
        description='Codespaces CLI help:'
    )
    p.add_argument('action',default=['start','stop','delete','info','list'], help='Action to a codespaces')
    p.add_argument('-n', help='Name of the codespace')
    p.add_argument('-p','--project',help='Project name (ex: 0xlildoudou/codespaces-cli)')

    return p.parse_args()

def cli():
    args = parser()

    if args.action:

        if args.action == 'create':
            with console.status(f"[bold green]{args.action} codespace...") as status:
                    if create_codespace(console, args.project):
                        exit(0)
                    else:
                        print('Error delete codespace')
                        exit(1)
        else:
            try:
                codespace_name = args.n
            except:
                print('Missing name of the codespace')
                exit(1)
            match args.action:

                case 'start':
                    with console.status(f"[bold green]{args.action} codespace...") as status:
                        if start_codespace(console, codespace_name):
                            exit(0)
                        else:
                            print('Error starting')
                            exit(1)

                case 'stop':
                    with console.status(f"[bold green]{args.action} codespace...") as status:
                        if stop_codespace(console, codespace_name):
                            exit(0)
                        else:
                            print('Error stopping')
                            exit(1)

                case 'info':
                    if info_codespace(codespace_name):
                        exit(0)
                    else:
                        print('Error getting infos')
                        exit(1)

                case 'delete':
                    with console.status(f"[bold green]{args.action} codespace...") as status:
                        if delete_codespace(console, codespace_name):
                            exit(0)
                        else:
                            print('Error delete codespace')
                            exit(1)
                case 'list':
                    get_list(console)
                    exit(0)