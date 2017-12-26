#!/usr/bin/env bash

count () {
    ls -l $1/kyu-$2 | wc -l
}

echo "Done:"
done_total=0
for i in `seq 1 8`; do
    files=$(count done $i)
    done_total=$(expr $done_total + $files)
    echo "  kyu $i: $files"
done
echo "  Total: $done_total"

echo "Todo:"
todo_total=0
for i in `seq 1 8`; do
    files=$(count todo $i)
    todo_total=$(expr $todo_total + $files)
    echo "  kyu $i: $files"
done
echo "  Total: $todo_total"