from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# ValueError: need more than 3 values to unpack   (on giving 3 arguments)
# ValueError: too many values to unpack           (on giving 5 arguments)
