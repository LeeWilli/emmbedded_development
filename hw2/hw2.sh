git clone  https://github.com/wangxuzuo/hw2.git

git log --all --graph --decorate

git checkout  README.md
git log

git blame _config.yml
git show [commit ID]

echo “test01” >> testStash.txt
git stash 
git stash pop

git config --global alias.gitgraph  'git log --all --graph --decorate --oneline'

touch .gitignore_global
echo “.DS_Store” >>”.gitignore_global”
git config --global core.excludesfile ~/.gitignore_global


