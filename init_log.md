
```
pyenv local 3.10.5
```

```
mkdir repo-template
```

```
cd repo-template
```

```
poetry init -n
```

```
poetry poetry env use $(which python)
```

```
. .venv/bin/activate
```

change pyproject.toml to 3.10.5

```
poetry lock
```

```
poetry add requests
```
