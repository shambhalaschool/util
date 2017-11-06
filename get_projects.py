"""Clone the "fll" repository locally, per the config file."""
import os
import zipfile

os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = r"C:\Users\alecm\AppData\Local\Programs\Git\bin\git.exe"

from git import Repo

import config as CONFIG

FILE_EXTENSIONS = (".ev3", ".nxt")

def clone_repo(repo_url, target_dir):
    cloned_repo = Repo.clone_from(repo_url, target_dir)

def sync_repo(repo_dir):
    pass

def load_changes(from_dir, to_dir):
    files = os.listdir(from_dir)
    project_dirs = [f for f in files 
        if os.path.isdir(os.path.join(from_dir, f))
        and f.endswith(FILE_EXTENSIONS)]

    for project in project_dirs:
        full_path = os.path.join(from_dir, project)
        zip_file = os.path.join(to_dir, project)
        with zipfile.ZipFile(zip_file, "w") as zipped_project:
            for project_file in os.listdir(full_path):
                zipped_project.write(
                    os.path.join(full_path, project_file),
                    project_file
                )

    print(project_dirs)
    pass

if __name__ == "__main__":
    pass
    # print(get.refresh.__doc__)
    # git.refresh(path=r"C:\Users\alecm\AppData\Local\Programs\Git\bin\git.exe")
    clone_repo(CONFIG.repo_url, CONFIG.git_dir)
    load_changes(CONFIG.git_dir, CONFIG.mindstorms_dir)
