import commands

def _(cmd):
	return commands.getoutput(cmd)

def lambda_handler(event, context):
	print _('cat /etc/os-release')
	print _('id')
	print _('cat /proc/cpuinfo | grep -e processor -e Xeon')
	print _('cat /proc/meminfo | grep -e MemTotal')
	print _('ENV')