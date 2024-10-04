# pdk-semver

![pkg-version]
![pkg-license]

Pretty print project's versions in different styles<br>

```text
$ pdk-semver -s all --extra some.info
internal  3.2.2-rev.3.some.info.git.b674019
  public  3.2.2-rev.3.some.info
    base  3.2.2-some.info

$ pdk-semver
3.2.2-rev.3.git.b674019
```

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
