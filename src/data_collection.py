""" Collects commit data for a single user. """
from pydriller import RepositoryMining
import pprint


# indicate path for repository by pluggin in the URL of repo (must be public)
repo_path = "https://github.com/GatorCogitate/cogitate_tool"


def collect_commits_user_email_key(repo):
    # TODO: edit the method to take in the URL for the repo
    """ Creates a dictionary of commit objects for a single user. """
    # holds email of repo members as keys, contents of commit object as values
    author_dict = {}

    # loop to turn the each Commits object into the values of the dictionary `author_dict`
    for commit in RepositoryMining(repo).traverse_commits():
        if commit.author.email not in author_dict.keys():
            author_dict[commit.author.email] = [commit]
        else:
            author_dict[commit.author.email].append(commit)
    return author_dict


def collect_commits_hash(repo):

    commit_list = []

    for commit in RepositoryMining("..").traverse_commits():

        # print(commit)
        print(commit.in_main_branch)
        # commit_list.append(
        # {"hash":commit.hash,
        # "author_msg":commit.msg,
        # "author_name":commit.author.name,
        # "author_email":commit.author.email,
        # "author_date":commit.author_date,
        # "in_main_branch":commit.in_main_branch,
        # # "merge":commit.merge,
        # # # "change_type":commit.modifications.change_type,
        # # "added":commit.modifications.added,
        # # "removed":commit.modifications.removed,
        # # "nloc":commit.modifications.nloc,
        # # "complexity":commit.modifications.complexity,
        # # "methods":commit.modifications.methods,
        # })

    return commit_list


print(collect_commits_hash(repo_path))