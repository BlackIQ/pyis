# Here is how I do things:

```bash
uv add --dev build twine pytest # Install things
uv run pytest -v # Run tests
rm -rf dist build *.egg-info # Clean old outputs
uv build # Create package
uv run twine check dist/* # Check publish files
uv run twine upload dist/* # Upload to Pypi
```
