tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."
x = "\'"
fat_cat = """
    I'll do a list:
    \t* Cat food
    \t* %rFishies%s
    \t* Cat\bnip\n\t* Grass\b
    
    """ % (x, x)
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# NOTE %r prints it the way its written in the file. %s prints it the way you'd like to see it
# NOTE \b at the end does not do anything.
