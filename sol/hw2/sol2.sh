# 1.1 Explore the version history by visualizing it as a graph.
git log --all --graph --decorate

# 1.2 Who was the last person to modify README.md? (Hint: use git log with an argument).
git log README.md

# 1.3 What was the commit message associated with the last modification to the website: line of hw2.md? (Hint: use git blame and git show).
git blame README.md | grep website

git show 7588c472

# 2. Modify one of cloned files. What happens when you do git stash? What do you see when running git log --all --oneline? Run git stash pop to undo what you did with git stash. In what scenario might this be useful?
git stash

git log --all --oneline

git stash pop

# 3.1

[alias]
   graph = log --all --graph --decorate --oneline

# 3.2

 git config --global core.excludesfile ~/.gitignore .DS_Store
