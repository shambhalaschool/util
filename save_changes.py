import os
import zipfile

from git import Repo

import config as CONFIG

FILE_EXTENSIONS = (".ev3", ".nxt")

def save_changes(from_dir, to_dir):
    print("Extracting project files from {} to {}\n".format(from_dir, to_dir))
    files = os.listdir(from_dir)
    project_files = [f for f in files if f.endswith(FILE_EXTENSIONS)]

    for project in project_files:
        full_path = os.path.join(from_dir, project)
        with zipfile.ZipFile(full_path, "r") as zipped_project:
            zipped_project.extractall(os.path.join(to_dir, project))
    

    repo = Repo(to_dir)
    if not repo.is_dirty() and not repo.untracked_files:
        print("Not seeing any changes, aborting")
        return

    print("Adding untracked files to Git\n")
    repo.index.add(repo.untracked_files)

    import pdb; pdb.set_trace()
    print("I see these changes:")
    for diff in repo.index.diff(None):
        print("{} - {}".format(diff.change_type, diff.a_path))
    
    message = input("Please describe them: ")


    

    print('\nCommitting "{}"'.format(message))
    repo.index.commit(message)

    print("Synchronizing...")
    # repo.remotes.origin.pull()
    # repo.remotes.origin.push()
    
    

if __name__ == "__main__":
    save_changes(CONFIG.mindstorms_dir, CONFIG.git_dir)