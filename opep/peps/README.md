## How are these .md files generated?

These Markdown files are generated using `pandoc`. On Ubuntu, you can install it using:

```
$ sudo apt install pandoc
```

And then:

```
$ git clone git@github.com:python/peps
$ cp *.rst .
$ ls *.rst | while read x; do name=$(echo "$x" | cut -d'.' -f1) && pandoc -s -o "$name.md" "$x"; done
$ rm *.rst
$ cp *.txt .
$ ls *.txt | while read x; do name=$(echo "$x" | cut -d'.' -f1) && pandoc -s -o "$name.md" "$x"; done
$ rm *.txt
$ rm -rf peps
```
