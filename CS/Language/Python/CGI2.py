#!/home/yiddi/anaconda3/envs/tensorflow/bin/python3.6
import cgi

# The cgi module
# The cgi module contains a lot of declarations and does a lot of initializing in the background.
# Because of this Never use: from cgi import …
# Provides us with methods to get POST and GET requests from the web server.
# As well as a few other methods for parsing data.

# Using Form data
# The python cgi module handles POST and GET with the same method.
# cgi.FieldStorage() this method will return a FieldStorage object that allows us to get data from a submitted form.
# We can user the FieldStorage object like a python dictionary or we can use the getvalue() method. (I suggest not using this method as it will crash if there is more than one field with the same name. but for now it’s fine)
# Alternative methods are getfirst() and getlist() (Safe)

# Simple hello ‘insert name’ program
# Let’s create a simple script that grabs the entered name from POST and prints out hello to that name.
# Let’s just modify our hello.py file.
# Then lets add a check box to see if they are happy or sad or both,

# Notes
# When debugging you code you can use the cgitb module to output errors to the page.
# Import cgitbcgitb.enable()
# The cgitb.enable() can be modified so that the error messages are saved to a file rather than output to users of your script. This can be done with:cgitb.enable(display=0, logdir=“/path/”)
# cgi.escape() Try to always escape user input if you plan to use it!


print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1> Hello Program </h1>")

form = cgi.FieldStorage()

if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h1>Hello " + name + "! Thanks for using my script! </h1><br />")

if form.getvalue("happy"):
    print("<p> Yap! I'm happy too! </p>")

if form.getvalue("sad"):
    print("<p> Oh no! Why are you sad? </p>")

# 这个脚本是作为 post 的 action
print("<form method='post' action='CGI2.py'>")
print("<p>Name: <input type='text' name='name'/></p>")
print("<input type='checkbox' name='happy' /> Happy")
print("<input type='checkbox' name='sad' /> Sad")
print("<input type='submit' value='Submit' />")
print("</form>")
print("</body></html>")
