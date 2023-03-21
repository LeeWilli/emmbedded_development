#1
git clone  https://github.com/wangxuzuo/hw2.git
#1.a
git log --all --graph --decorate
#1.b
git checkout  README.md
git log
#1.c
git blame hw2.md
#结果
#5bca7590 (LeeWilli 2020-10-14 23:32:39 +0800 1)
#ec48329b (LeeWilli 2020-10-14 23:32:02 +0800 2)
git show 5bca7590

#2
echo “test01” >> testStash.txt
git stash 
git stash pop
#3 a
git config --global alias.gitgraph  'git log --all --graph --decorate --oneline'
#3.b
touch .gitignore_global
echo “.DS_Store” >>”.gitignore_global”
git config --global core.excludesfile ~/.gitignore_global


