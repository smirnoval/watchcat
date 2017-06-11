# watchcat

Python library to monitor changes in files.

### Using

```python
python3 args.py *<files>
```
where:
files -- list of files and dirs for watching.

### Examples

```python
python3 args.py 1.txt tests
```
watchcat will monitor the file 1.txt and all files in the folder tests and all nested subfolders.
