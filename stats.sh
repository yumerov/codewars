#!/usr/bin/env bash
echo "Done:"

for i in `seq 1 8`; do
    files=$(expr $(ls -l done/kyu-$i | wc -l) - 1)
    echo "  kyu $i: $files"
done

echo "Todo: $(expr $(ls -l todo | wc -l) - 1)"
