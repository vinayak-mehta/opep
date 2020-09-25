#!/usr/bin/env bash

git clone git@github.com:python/peps
cp peps/pep-*.rst .
ls *.rst | while read x; do name=$(echo "$x" | cut -d'.' -f1) && pandoc -s -o "$name.md" "$x"; done
rm *.rst
cp peps/pep-*.txt .
ls *.txt | while read x; do name=$(echo "$x" | cut -d'.' -f1) && pandoc -s -o "$name.md" "$x"; done
rm *.txt
rm -rf peps
