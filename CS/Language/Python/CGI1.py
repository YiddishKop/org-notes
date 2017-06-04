#!/home/yiddi/anaconda3/envs/tensorflow/bin/python3.6

# CGI Programming
# Python3 Advanced #7

# Preamble
# This tutorial is about web interfacing, Having a basic understanding of HTML and how it works will be very helpful.
# If you have done any PHP before this will be familiar however in python.

# What is CGI?
# CGI stands for Common Gateway Interface.
# CGI is the standard for programs to interface with HTTP servers. (Some other servers too)
# This means we can take information from things like Forms.
# CGI scripts generally go in a web server’s cgi-bin directory.

# What is CGI Programming?
# CGI programming is writing dynamically generating WebPages that respond to user input or WebPages that interact with software on the server.
# Things like Dropbox use python for it’s web interface.
# Setup
# To be able to get our CGI to work we need a web server we can play with.
# If you have your own web server and want to use that go ahead.
# If you don’t lets quickly set up and apache2 web server on our Ubuntu box.

# Setup
# To install Apache2 (which should be a standard package in almost all linux distro’s) we use:sudo apt-get install apache2
# Then we must set the web server permissions to allow cgi programs to execute.For simplicity we will allow cgi to execute in the root directory.

# Basic CGI python script
# Lets create a basic script that just prints out that it worked and print hello world 5 times.
# Lets call it hello.py

# Must have a line telling the web server where python is installed eg.
# #!/usr/bin/python

# We also have to change the file permissions so it can execute. chmod 755 hello.py

# ➜  Python git:(master) ✗ sudo chmod 755 CGI1.py
# ➜  Python git:(master) ✗ sudo cp CGI1.py /var/www/
# ➜  Python git:(master) ✗ sudo a2enmod cgi
# ==>
# AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
# Your MPM seems to be threaded. Selecting cgid instead of cgi.
# Module cgid already enabled

# ➜  Python git:(master) ✗ sudo service apache2 restart
# chrome input: 127.0.0.1/DGI1.py

# 一开始遇到错误，apache2 解析不出来我的html
# #！/home/yiddi/......./python3.6
# 这句必须放在 .py 文件开头第一行
print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1> It Works! </h1>")
for i in range(5):
    print("<h2> Hello world! " + str(i) + "</h2>")

print("</body></html>")
