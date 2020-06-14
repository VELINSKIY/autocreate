import sys
import os
from github import Github


project_name = str(sys.argv[1])
path = 'SOME\\PATH'
user = Github('Github_Login', 'Github_Password').get_user()
    

def create():
    print('navigating to the path...')
    os.chdir(path)
    
    print('creating new folder...')
    os.mkdir(str(project_name))
    
    new_path = str('{}\\{}').format(path, project_name)
    os.chdir(new_path)
    print('navigating to the local folder... ', new_path)

    cmd = 'git init'
    os.system(cmd)

    repo = user.create_repo(project_name)
    print('creating new repo... ', project_name)
    
    repo_url = 'https://github.com/USERNAME/{}.git'.format(project_name)
    print('git remote add ', repo_url)
    cmd = f'git remote add origin {repo_url}'
    os.system(cmd)
    
    new_path = str('{}\\{}').format(path, project_name)
    os.chdir(new_path)
    print('navigating to the local repo... ', new_path)
    
    project = project_name + '.py'
    
    with open(project, 'w'):
        print(f'opening {project} VS Code...')
        cmd = 'code .'
        os.system(cmd)
    
    print('adding files...')
    cmd = f'git add .'
    os.system(cmd)
    
    print(f'\'{project_name}\' was created, Master')

    
if __name__ == "__main__":
    create()
