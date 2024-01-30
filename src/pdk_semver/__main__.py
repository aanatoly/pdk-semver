"""
Pretty print package version.

The full version style has these components:
[base]-[revision].[release info].[build info]

You can override components via command line options.

EPILOG:
Examples:
Print version in default style, e.g. internal
  $ pdk-semver
  3.2.2-rev.3.git.b674019

Print version in default style, with release info "arch.aarch64"
  $ pdk-semver --rinfo-value arch.aarch64
  3.2.2-rev.3.arch.aarch64.git.b674019

Print all styles
  $ pdk-semver -s all --rinfo-value some.info
  internal 3.2.2-rev.3.some.info.git.b674019
    public 3.2.2-rev.3.some.info
   baserev 3.2.2-rev.3
      base 3.2.2
    latest 3.2
"""


import logging
import sys

import pydevkit.log.config  # noqa: F401
from pydevkit.argparse import ArgumentParser
from pydevkit.shell import Shell

from . import __version__
from .ver import Version

log = logging.getLogger(__name__)


class GitVals:
    @staticmethod
    def supported(path):
        sh = Shell()
        sh["dir"] = path
        sh["git"] = 'git -C "%(dir)s"' % sh
        sh("%(git)s rev-parse --git-dir >& /dev/null")

    @staticmethod
    def get_vals(adir, aref) -> dict:
        sh = Shell()
        sh["dir"] = adir
        sh["ref"] = aref
        sh["git"] = 'git -C "%(dir)s"' % sh
        rc = {}
        # find closest tag
        val = sh.inp("%(git)s describe --abbrev=0 %(ref)s 2>/dev/null | cat")
        rc["base_value"] = val if val else "0.1.0"
        if val:
            val += ".."
        sh["tag"] = val
        val = int(sh.inp("%(git)s rev-list %(tag)s%(ref)s --count"))
        rc["rev_value"] = val
        val = sh.inp("%(git)s rev-parse --short %(ref)s")
        rc["binfo_value"] = ["git", val]
        return rc


def get_vc_vals(path, ref) -> dict:
    for cls in [GitVals]:
        try:
            cls.supported(path)
            log.debug("git repo found at '%s", path)
            return cls.get_vals(path, ref)
        except Exception:
            pass
    log.warning("no version control found at '%s", path)
    return {}


def get_cmd_vals(args) -> dict:
    vals = {}
    for k, v in vars(args).items():
        pfx = k.split("_", 1)[0]
        if pfx in ["rinfo"]:
            vals[k] = v
    return vals


def get_args():
    p = ArgumentParser(help=__doc__, version=__version__, usage="short")
    p.add_argument(
        "-C", help="path to git repo", dest="path", metavar="path", default="."
    )
    p.add_argument(
        "-r", help="git revision ref", dest="ref", metavar="ref", default="HEAD"
    )
    styles = [*list(Version.Styles.keys()), "all"]
    p.add_argument(
        "-s",
        help="style, one of %(choices)s",
        dest="style",
        metavar="name",
        default="internal",
        choices=styles,
    )
    p.add_argument(
        "--rinfo-value", help="release info component", metavar="txt", default=""
    )

    return p.parse_known_args()


def main():
    args, unknown_args = get_args()
    if unknown_args:
        log.warning("Unknown arguments: %s", unknown_args)
        sys.exit(1)

    ver = Version()
    cmd_vals = get_cmd_vals(args)
    git_vals = get_vc_vals(args.path, args.ref)
    if args.style != "all":
        print(ver.fmt(Version.Styles[args.style], git_vals, cmd_vals))
        return

    for k, v in Version.Styles.items():
        print("%8s" % k, ver.fmt(v, git_vals, cmd_vals))


if __name__ == "__main__":
    main()
