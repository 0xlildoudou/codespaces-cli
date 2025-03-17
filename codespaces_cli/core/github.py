import requests, os
from codespaces_cli.core.output import *
from time import sleep
from colorama import Fore
from rich import print_json

class Github:
    base_url = 'https://api.github.com'
    base_header = {
        'Authorization':f'token {os.environ["GITHUB_TOKEN"]}',
        'Accept':'application/vnd.github.v3+json'
    }

    base_user = f'{base_url}/user'
    base_codespaces = f'{base_user}/codespaces'
    base_repos = f'{base_url}/repos'

def get_repo(project):
    r = requests.get(
        url=f'{Github.base_repos}/{project}',
        headers=Github.base_header
    )

    return r.json()

def get_list(console):
    r = requests.get(
        url=Github.base_codespaces,
        headers=Github.base_header
    )
    
    _output = []
    for codespace in r.json()['codespaces']:
        _output.append({
            'NAME':codespace['name'],
            'REPOSITORY':codespace['repository']['full_name'],
            'STATE': codespace['state'],
            'CREATED':codespace['created_at'],
            'LAST USED':codespace['last_used_at']
        })

    render_tab(console,_output)

def codespace_info(name):
    r = requests.get(
            url=f"{Github.base_codespaces}/{name}",
            headers=Github.base_header
        )
    
    return r.json()

def stop_codespace(console,name):
    r = requests.post(
        url=f"{Github.base_codespaces}/{name}/stop",
        headers=Github.base_header
    )

    state = "Available"

    console.log(f'stopping {name}')
    while state != 'Shutdown':
        state = codespace_info(name)['state']
        sleep(1)

    console.log(f'Codespace {name} stopped')
    return True

def start_codespace(console,name):
    r = requests.post(
        url=f"{Github.base_codespaces}/{name}/start",
        headers=Github.base_header
    )

    state = "Shutdown"

    console.log(f'starting {name}')
    while state != 'Available':
        state = codespace_info(name)['state']
        sleep(1)

    url = r.json()['web_url']
    console.log(f'Codespace url: {url}')
    return True

def delete_codespace(console,name):
    state = codespace_info(name)['state']

    if state != 'Shutdown':
        if stop_codespace(console,name):
            state = codespace_info(name)['state']
        else:
            print('Error stopping')
            exit(1)

    r = requests.delete(
        url=f"{Github.base_codespaces}/{name}",
        headers=Github.base_header
    )

    if r.status_code == 202:
        console.log(f'Codespace {name} successfuly deleted')
        return True
    else:
        console.log(f'Codespace {name} error: HTTP/{r.status_code}')
        console.log(f'{r.json()}')
        return False

def info_codespace(name):
    print_json(data=codespace_info(name))

def create_codespace(console,project):
    _id = get_repo(project)['id']

    r = requests.post(
        url=Github.base_codespaces,
        headers=Github.base_header,
        json={
            "repository_id": _id
        }
    )
    state = "Shutdown"
    name = r.json()['name']
    
    console.log(f'starting {name}')
    while state != 'Available':
        state = codespace_info(name)['state']
        sleep(1)

    console.log(f'Created {name}')
    console.log(f'Url : {r.json()['web_url']}')
    return True