# 做题准备

以自己的账户登录树莓派系统，并修改密码。账户名是学号，初始密码:123，可以用实现了ssh的软件如XSHELL，PUTTY等登录，也可用命令行方式：
ssh 学号@1.116.217.137 -p 6001，建议使用MobaXterm。

在自己账户目录下创建子目录hw1，所有要检查的文件都放在这个目录下，文件名字以数字开头，如1.py等，这时文件的路径应该是： \~/hw1/1.py 
（'~'表示你的账户所在根目录，如pi账户，那么完整路径就是/home/pi/hw1/1.py）。1表示第1题，后面可以跟字符串，如1_hello.py，也可以不跟。

# 题目

1.	用linux指令实现下列功能，所有指令放在一个脚本文件中，并验证能够正确执行.验证方法是使用bash 1.sh，观察结果是否输出正确，这里假设你的脚本文件名称是1.sh。功能需求如下（需要有一定英文基础），

    1.  You want to create a one-line file without having to use an editor.
    2.  You want to create a new directory by using the Terminal.
    3.  You want to delete a file or directory using the Terminal.
    4.  You need to change the permissions of a file.
    5.  Sometimes Python libraries and another software are hosted on the GitHub website or other online Git repository(https://github.com/LeeWilli/emmbedded_development.git). You need to be able to fetch them onto your Raspberry Pi.
    6.  You want to find a file that you know is on the system somewhere.
    7.  You want to quickly create a file with some text or record a directory listing into a file.
    8.  You have a number of text files, and you want to join them into one big file.
    9.  You want to use the output of one Linux command as the input to another command.
    10. You want to run a command, but you don’t want the output filling up your screen.
    11. You want to create aliases (shortcuts) to commands that you use frequently.

2. Read man ls and write an ls command that lists files in the following manner

    - Includes all files, including hidden files
    - Sizes are listed in human readable format (e.g. 454M instead of 454279954)
    - Files are ordered by recency
    - Output is colorized
    - A sample output would look like this
```shell
     -rw-r--r--   1 user group 1.1M Jan 14 09:53 baz
     drwxr-xr-x   5 user group  160 Jan 14 09:53 .
     -rw-r--r--   1 user group  514 Jan 14 06:42 bar
     -rw-r--r--   1 user group 106M Jan 13 12:12 foo
     drwx------+ 47 user group 1.5K Jan 12 18:08 ..
```

3. As we covered in the lecture `find`’s `-exec` can be very powerful for performing operations over the files we are searching for. However, what if we want to do something with all the files, like creating a zip file? As you have seen so far commands will take input from both arguments and STDIN. When piping commands, we are connecting STDOUT to STDIN, but some commands like `tar` take inputs from arguments. To bridge this disconnect there’s the `xargs` command which will execute a command using STDIN as arguments. For example `ls | xargs rm` will delete the files in the current directory.
Your task is to write a command that recursively finds all HTML files in the folder and makes a zip with them. Note that your command should work even if the files have spaces (hint: check -d flag for xargs).

4. (Advanced) Write a command or script to recursively find the most recently modified file in a directory. More generally, can you list all files by recency?

