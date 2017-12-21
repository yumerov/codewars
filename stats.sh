#!/usr/bin/env bash

echo "Done:"
done_total=0
for i in `seq 1 8`; do
    files=$(expr $(ls -l done/kyu-$i | wc -l) - 1)
    done_total=$(expr $done_total + $files)
    echo "  kyu $i: $files"
done
echo "  Total: $done_total"

echo "Todo:"
todo_total=0
for i in `seq 1 8`; do
    files=$(expr $(ls -l todo/kyu-$i | wc -l) - 1)
    todo_total=$(expr $todo_total + $files)
    echo "  kyu $i: $files"
done
echo "  Total: $todo_total"