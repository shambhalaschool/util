"""Clone the "fll" repository locally, per the config file."""
import os

os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = r"C:\Users\alecm\AppData\Local\Programs\Git\bin\git.exe"

from git import Repo

import config as CONFIG

def clone_repo(repo_url, target_dir):
    cloned_repo = Repo.clone_from(repo_url, target_dir)
    import pdb; pdb.set_trace()

def sync_repo(repo_dir):
    pass

if __name__ == "__main__":
    pass
    # print(get.refresh.__doc__)
    # git.refresh(path=r"C:\Users\alecm\AppData\Local\Programs\Git\bin\git.exe")
    clone_repo(CONFIG.repo_url, CONFIG.git_dir)