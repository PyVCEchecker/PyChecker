import subprocess
import json



thing = subprocess.Popen('python overit.py gooey-seed-ui', stdout=subprocess.PIPE)
out, err = thing.communicate()
print(thing.returncode)
print(out)
print(err)

print(json.loads(out.decode('utf-8'))['--load'])
