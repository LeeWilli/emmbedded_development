Make a directory named 'hw2'， and any related files should be placed in it and have to be named with a head of 'p1'， such as 'p1.sh', etc. 'p1' represents problem 1 of this homework. As a result, the path of 'p1.sh' should be ~/hw2/p1.sh （‘~' represents the root directory of your account).

Clone the repository for the class website.

Explore the version history by visualizing it as a graph.
Who was the last person to modify README.md? (Hint: use git log with an argument).
What was the commit message associated with the last modification to the website: line of hw2.md? (Hint: use git blame and git show).
Modify one of cloned files. What happens when you do git stash? What do you see when running git log --all --oneline? Run git stash pop to undo what you did with git stash. In what scenario might this be useful?

Fork the repository for the class website, find a typo or some other improvement you can make, and submit a pull request on GitHub (you may want to look at this). There are two improvements:

Like many command line tools, Git provides a configuration file (or dotfile) called ~/.gitconfig. Create an alias in ~/.gitconfig so that when you run git graph, you get the output of git log --all --graph --decorate --oneline. Information about git aliases can be found here.
You can define global ignore patterns in ~/.gitignore_global after running git config --global core.excludesfile ~/.gitignore_global. Do this, and set up your global gitignore file to ignore OS-specific or editor-specific temporary files, like .DS_Store.
Apply core bash scripting concepts to build a simple file viewer CLI tool

