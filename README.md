# pdk-semver

---

Pretty print versions for project and artifacts.<br>
Make version more or less informative depending on the audience.

```text
$ pdk-semver -s all --rinfo-value some.info
internal  3.2.2-rev.3.some.info.git.b674019
  public  3.2.2-rev.3.some.info
 baserev  3.2.2-rev.3
    base  3.2.2
```

Main features are:
 * Automatic versioning based on git content and CI variables
 * Unique build versions. Version includes nearest tag,
   number of commits and commit hash
 * Artifact and release info. Add artifact details, like CPU, platform, client etc.
 * Easy customization. Every component can be overridden with `--COMP-value`
   option, like `--rinfo-value`

The version format is:

![base](https://img.shields.io/badge/base-3.2.2-darkgreen)
![rev](https://img.shields.io/badge/rev-rev.4-darkgreen)
![rinfo](https://img.shields.io/badge/rinfo-aarch64.gcc.12.1-darkgreen)
![binfo](https://img.shields.io/badge/binfo-git.abcde1234-darkgreen)

## Use Cases

### CI and Shallow clones
CI servers usually do shallow (partial) clone, so `pdk-semver` can't get tag and
commit counter. What can we do?
 * adjust CI clone depth to the tagging frequency
 * keep tag name in a text file, but commit counter still be off
 * unshallow, bring more commits

### Working with docker images

### Working with buildroot

## Installation

```sh
pip install pdk-semver
```

## Development
See [development](docs/devel.md) doc

[pkg-link]: https://pypi.python.org/pypi/pdk-semver/
[pkg-version]: https://img.shields.io/pypi/v/pdk-semver?logo=pypi&logoColor=aaaaaa&color=blue
[pkg-license]: https://img.shields.io/pypi/l/pdk-semver?logoColor=aaaaaa&color=blue
[pkg-pyversions]: https://img.shields.io/pypi/pyversions/pdk-semver?logo=python&logoColor=aaaaaa&color=blue
