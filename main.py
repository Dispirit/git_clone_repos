from git import Repo  # pip install gitpython
import subprocess
import os
import requests
import getpass


def libs_gitpy(path_dir, repo_name, git_url):
    full_url = f'{git_url}/{repo_name}.git'
    full_path = f'{path_dir}\\{repo_name}'
    print(f'Cloning repo: {repo_name} into {path_dir}')
    Repo.clone_from(full_url, full_path)


def cloning_repo(path_dir, repo_name, git_url):
    os.chdir(path_dir)
    print(f'Cloning repo: {repo_name} into {path_dir}')
    proc = subprocess.Popen(['git', 'clone', f'{git_url}/{repo_name}.git'], stdout=subprocess.PIPE)
    proc.stdout.read()


def pulling_repo(path_dir, repo_name):
    repo_dir = f"{path_dir}/{repo_name}"
    os.chdir(repo_dir)
    print(f'Pull repo: {repo_name} from {repo_dir}\n')
    proc = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
    proc.stdout.read()


def check_directory(path, name_dir):
    exist_flag = os.path.isdir(f'{path}/{name_dir}')
    return exist_flag


def get_repos(user_name, git_login, git_password, target_path, git_url):
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(f'https://api.github.com/users/{user_name}/repos',
                            headers=headers,
                            auth=(f'{git_login}', f'{git_password}'))
    repos_result = response.json()
    for repo_name in repos_result:
        repo = repo_name.get("name")
        print(f"Repo {repo} was found")
        flag = check_directory(target_path, repo)
        if not flag:
            cloning_repo(target_path, repo, git_url)
            # libs_gitpy(path, repo, url)
        else:
            print(f"Repo '{repo}' exists")
            pulling_repo(target_path, repo)


if __name__ == '__main__':
    user = input("Enter your login: ")
    password = getpass.getpass(prompt="Enter your password: ")
    git_user_name = input("Enter your git profile name: ")
    path = r"D:\GitHub_backup"
    url = f'https://github.com/{git_user_name}'
    get_repos(f"{git_user_name}", f"{user}", password, path, url)
