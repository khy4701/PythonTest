#!/bin/sh


if [ $# -lt 1 ]; then
    echo "$0 Must Input Commit message"
    exit 0
fi

result= `git add --all | echo`
echo $result
echo "Add finish.."

sleep 1
res= `git commit -m $1 | echo`

echo $res


sleep 1

git push hykim master
