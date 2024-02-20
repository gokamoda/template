

## Clone
```
git clone git@github.com:gokamoda/template.git
```

```
mv template {project-name}
```

```
cd template
```

```
sed -i '' 's/template/{project-name}/g' pyproject.toml
```

```
mv template {project-name}
```

```
poetry install
```

```
. .venv/bin/activate
```

```
poetry run python {project-name}/main.py
```


flake8, pylint
```
source check.sh
```

isort, black
```
source clean.sh
```
