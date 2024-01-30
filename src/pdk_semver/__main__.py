"""
Demonstrates pydevkit features.

EPILOG:
Example 1:
```
PYDEVKIT_LOG_HANDLER=app ./script --log-level=debug
```

Example 2:
```
./script --log-level=debug --log-handler=json
```
"""


import logging
import sys
import threading

import pydevkit.log.config  # noqa: F401
from pydevkit.argparse import ArgumentParser
from pydevkit.conf import conf_get
from pydevkit.log import prettify
from pydevkit.shell import Shell
from pydevkit.term import term_get

from . import __version__

log = logging.getLogger(__name__)


def get_args():
    p = ArgumentParser(help=__doc__, version=__version__)
    p.add_argument("--file", help="file to check")

    return p.parse_known_args()


def main():
    args, unknown_args = get_args()
    if unknown_args:
        log.warning("Unknown arguments: %s", unknown_args)
        sys.exit(1)
    threading.current_thread().name = "main"

    print(">> Test logging")
    kwargs = {"extra": {"ip": "10.0.0.1"}}
    for a in ["debug", "info", "warning", "error", "critical"]:
        fn = getattr(log, a)
        fn("%s msg", a)
        fn("%s msg", a, extra=kwargs)
    log.debug("kwargs\n%s", prettify(kwargs))

    print(">> Test terminal colors")
    term = term_get()
    print("try %sred%s string" % (term.red, term.normal))

    print(">> Test conf")
    print("conf: log level %s" % conf_get("level"))

    print(">> Test shell")
    sh = Shell()
    sh("echo hello, world")


if __name__ == "__main__":
    main()
