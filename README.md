# Virus & Worm: Ethical Demonstration

## Prerequisites:

- For the virus, depending on the operating system used, you can customize the subprocess.open line.
  For Kali Linux, qterminale is usable, and for other Linux distributions, it requires downloading qterminale.

- For the worm, just be cautious about the choice of the copy path. By default, it copies to the current directory.

- Run main.py (for my work in general).

## Operation:

### I. Virus:

The virus implemented here is not harmful, but it is possible to go further and cause damage.
This virus ensures copying its own code and placing it in other files ending with .py or .pyw.
Also, this virus opens terminals; by default, it's twice, but you can set your own number, even infinite 
(but be cautious, as it can damage your computer, it's better to test it in a virtual machine).

### II. Worm:

The worm has some similar functionality to the virus, which is replication.
In essence, the worm creates hidden files by taking the names of existing files and pasting its own code.
Be careful to have many files in the current directory or to execute the ver script multiple times, 
as it can cause storage damage. Note that here as well, the possibility of going further is always conceivable, 
for example, using SSH for the worm.

## Issues Encountered:

In this bonus project, I did not encounter any specific problems to mention.
The separation of three scripts implies the non-functioning of the program.
However, if you wish, you can execute the virus on one hand and the worm on the other to test.


