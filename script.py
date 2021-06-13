import io, os
from git.repo import Repo

COMMITS_TO_PRINT = 5

def print_commit(commit):
    """gitpython commit object, prints 40 char SHA-1 has for the commit 
    and all summary, authorname etc"""
    print('-----')
    print(str(commit.hexsha))
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary,
                                     commit.author.name,
                                     commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(),
                                              commit.size)))

def print_repository(repo):
    print('Repo description: {}'.format(repo.description))
    print('Repo active branch is {}'.format(repo.active_branch))
    for remote in repo.remotes:
        print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
    print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))

def read_data_by_commit_id(commit_id):
    """takes in commit id and reads data"""
    #targetfile = commit_id.tree/'analytics/views.py'
    targetfile = commit_id.tree/'requirements.txt'
    with io.BytesIO(targetfile.data_stream.read()) as f:
        print(f.read().decode('utf-8'))

# main
if __name__=="__main__":
    os.environ['GIT_REPO_NEW']='/Users/rshalem/Desktop/LibraryManagmentSystemAPI'
    repo_path = os.environ.get('GIT_REPO_NEW')
    repo = Repo(repo_path)
    commit = repo.commit('3e660b983d703f50b3213525af914bc7df432325')

    # check that repo is loaded correctly
    if not repo.bare:
        print('Repo at {} successfully loaded.'.format(repo_path))
        print_repository(repo)
        # create list of commits then print some of them to stdout
        commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
        for commit in commits:
            print_commit(commit)
            pass

        print('**********COMMIT DATA*******************')
        read_data_by_commit_id(commit)
    else:
        print('Could not load repository at {} :('.format(repo_path))