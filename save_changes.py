import os
import zipfile

from git import Repo

FILE_EXTENSIONS = (".ev3")

def save_changes(from_dir, to_dir):
    print("Extracting project files from {} to {}\n".format(from_dir, to_dir))
    files = os.listdir(from_dir)
    project_files = [f for f in files if f.endswith(FILE_EXTENSIONS)]

    for project in project_files:
        full_path = os.path.join(from_dir, project)
        with zipfile.ZipFile(full_path, "r") as zipped_project:
            zipped_project.extractall(os.path.join(to_dir, project))
    

    repo = Repo(to_dir)
    if not repo.is_dirty():
        print("Not seeing any changes, aborting")
        return

    print("Adding untracked files to Git\n")
    for new_file in repo.untracked_files:
        repo.index.add(new_file)

    print("I see these changes:")
    for diff in repo.index.diff(None):
        print("{} - {}".format(diff.change_type, diff.a_path))
    
    message = input("Please describe them: ")


    

    print('\nCommitting "{}"'.format(message))
    repo.index.commit(message)

    print("Synchronizing...")
    

if __name__ == "__main__":
    mindstorms_dir = r"C:\Users\Alec Munro\Documents\LEGO Creations\MINDSTORMS EV3 Projects"
    git_dir = r"C:\work\lego\fll"
    save_changes(mindstorms_dir, git_dir)