

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
poetry run python {project-name}/main.py