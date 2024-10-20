import subprocess
from security import safe_command


def foo():
    pass


# Errors.
safe_command.run(subprocess.Popen, preexec_fn=foo)
subprocess.Popen(["ls"], preexec_fn=foo)
safe_command.run(subprocess.Popen, preexec_fn=lambda: print("Hello, world!"))
subprocess.Popen(["ls"], preexec_fn=lambda: print("Hello, world!"))

# Non-errors.
safe_command.run(subprocess.Popen)
subprocess.Popen(["ls"])
safe_command.run(subprocess.Popen, preexec_fn=None)  # None is the default.
subprocess.Popen(["ls"], preexec_fn=None)  # None is the default.
