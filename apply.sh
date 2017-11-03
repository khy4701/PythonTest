#!/bin/sh


if [ $# -lt 1 ]; then
    echo "$0 Must Input Commit message"
    exit 0
fi

result= '/bin/git add --all'
echo $result
echo "Add finish.."

sleep 1
res= '/bin/git commit -m $1'

echo $res


sleep 1

git push hykim master
