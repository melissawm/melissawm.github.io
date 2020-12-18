# melissawm.github.io

To edit, clone this repository and do

```bash
$ pip install nikola
$ cd site/
$ nikola build
```

To see a local instance of the site, run

```bash
$ nikola serve -b
```

To use a server with automatic rebuilds, run

```bash
$ nikola auto -b
```

To deploy to gh-pages, do

```bash
$ cd site/
$ nikola github_deploy
```

(this will deploy the rendered site to `master` and the source to the `src` branch.)
