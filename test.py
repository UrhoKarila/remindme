import os, re

def GetLinesFromFile(name):
	f = open(name, 'r')
	vals = f.read()
	vals = vals.splitlines()
	f.close()
	return vals

#Testing reading from file for variables
values = GetLinesFromFile("test.txt")
enter_words = GetLinesFromFile("enter_words.txt")
exit_words = GetLinesFromFile("exit_words.txt")
test_commands = GetLinesFromFile("test_commands.txt")


print values

print "\nurhoebeling@gmail.com found in file? "
print 'urhoebeling@gmail.com' in values

print 'enter_words: ' + repr(str(enter_words))
print 'exit_words: ' + repr(str(exit_words))
print 'building regex...'
location_regex = '.*when i ('+ '|'.join(enter_words) + '|' + '|'.join(exit_words)+').*\'(.*)\'.*'
predicate_regex = '.*to (.*)when|$'

print "location_regex is: ---\n" + repr(location_regex) + '\n---'
print "predicate_regex is: ---\n" + repr(predicate_regex) + '\n---'

for command in test_commands:
	matches = re.match( location_regex, command, re.I)
	if(matches):
		print '\ncommand is ' + matches.group(0)
		print '---\ndirection (imprecise) = ' + matches.group(1) + '\n---'
		direction = 'null'
		if(matches.group(1) in enter_words):
			direction = 'enter'
		if(matches.group(1) in exit_words):
			direction = 'exit'
		print "Direction evaluates to " + direction
		print "---\n Location is: " + matches.group(2) + "\n---"
		print '////////'

		predicate = re.match( predicate_regex, command, re.I )
		if(predicate):
			print "Action requested is:\n\t" + predicate.group(1) + '\n################'
		else:
			print "Failed to match action \n####################"

	else:
		print "!!!!!!!!!!\nFailed to match location_regex " + repr(location_regex) + "\n" + command + "\n!!!!!!!!!!\n"