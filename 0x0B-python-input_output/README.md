# 0x0B. Python - Input/Output
## Mandatory Tasks
### 0. Read file
Write a function that reads a text file (```UTF8```) and prints it to the stdout:
 - Prototype: ```def read_file(filename=""):```
 - You must use the ```with ``` statement
 - You don't need to manage ```file permission``` or ```file doesn't exist``` exceptions.
 - You are now allowed to import any module
```
guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$
```
<strong>No test cases needed</strong>
<br>
<strong>Repo:</strong>
 - GitHub repository: ```alx-higher_level_programming```
 - Directory: ```0x0B-python-input_out```
 - File: ```0-read_file.py```

