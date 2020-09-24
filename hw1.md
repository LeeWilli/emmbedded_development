1.	以自己的账户登录树莓派系统，并修改密码。账户名是学号，初始密码:123，可以用实现了ssh的软件如XSHELL，PUTTY等登录，也可用命令行方式：
ssh 学号@129.211.169.165 -p 6000

2.	在自己账户目录下创建子目录hw0，所有要检查的文件都放在这个目录下，文件名字以hw0开头，如hw0_1.sh等，这时文件的路径应该是：~/hw0/hw0_1.sh（‘~'表示你的账户所在更目录，如pi账户，那么完整路径就是/home/pi/hw0/ho0_1.sh。

3.	用linux指令实现下列功能，所有指令放在一个脚本文件中，并验证能够正确执行.验证方法是使用bash hw0_1.sh，观察结果是否输出正确，这里假设你的脚本文件名称是hw0_1.sh。功能需求如下，
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
    
