from git import Repo
import subprocess
import os


def libs_gitpy(path_dir, repo_name, git_url):
    full_url = f'{git_url}/{repo_name}.git'
    full_path = f'{path_dir}\\{repo_name}'
    print(f'Cloning repo: {repo_name} into {path_dir}')
    Repo.clone_from(full_url, full_path)


def subproc(path_dir, repo_name, git_url):
    os.chdir(path_dir)
    print(f'Cloning repo: {repo_name} into {path_dir}')
    proc = subprocess.Popen(['git', 'clone', f'{git_url}/{repo_name}.git'], stdout=subprocess.PIPE)
    proc.stdout.read()


if __name__ == '__main__':
    # print_hi()
    path = r"D:\GitHub_backup"
    # repos = ('powershell_scripts', 'fixversions', 'pytnon_projects', 'xls_macros', 'django-ckeditor',
    #          'shared_repository', 'sites_template', 'docker-training', 'diplom_radik', 'vagrant_training',
    #          'DocumentsVault', 'comandline_scripts', 'Accounting', 'kubernetes-traning', 'pipeline', 'jobs_groovy',
    #          'groovy_calculator', 'helloworld_maven', 'helloworld_ant', 'ansible-examples', 'hello-war')
    repos = ('hello-war',)
    url = 'https://github.com/Dispirit'
    for repo in repos:
        subproc(path, repo, url)
        # libs_gitpy(path, repo, url)
