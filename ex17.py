from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

# output.close()
input.close()


# cat command display contents of file. It can also do many other things. It's an old command that "conCATenates" files together, but mostly it's just an easy way to print a file to the screen.

# windows alternative to 'cat' is 'type' command

# Non-ASCII character '\xe2' ...  error will come when you have copied and pasted the code and some weird character is present.
