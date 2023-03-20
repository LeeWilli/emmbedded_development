Make a directory named 'hw2'，and any related files should be placed in it and have to be named with head of 'hw2'，such as 'hw2.sh', and etc. As a result, the file named 'hw2.sh' should be \~/hw2/hw2.sh （‘~' represend the root directory of you account).

1. Clone the repository for the class [website](https://github.com/LeeWilli/emmbedded_development).
    1. Explore the version history by visualizing it as a graph.
    2. Who was the last person to modify README.md? (Hint: use git log with an argument).
    3. What was the commit message associated with the last modification to the collections: line of _config.yml? (Hint: use git blame and git show).

2. Modify one of cloned files. What happens when you do git stash? What do you see when running git log --all --oneline? Run git stash pop to undo what you did with git stash. In what scenario might this be useful?

3. Fork the repository for the class [website](https://github.com/LeeWilli/emmbedded_development), find a typo or some other improvement you can make, and submit a pull request on GitHub (you may want to look at [this](https://github.com/firstcontributions/first-contributions)).
There are two improvements:
    1. Like many command line tools, Git provides a configuration file (or dotfile) called ~/.gitconfig. Create an alias in ~/.gitconfig so that when you run git graph, you get the output of git log --all --graph --decorate --oneline. Information about git aliases can be found [here](https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias).
    2. You can define global ignore patterns in ~/.gitignore_global after running git config --global core.excludesfile ~/.gitignore_global. Do this, and set up your global gitignore file to ignore OS-specific or editor-specific temporary files, like .DS_Store.
