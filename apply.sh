#!/bin/sh


git add --all | echo

sleep 1
git commit -m $1 | echo


sleep 1

git push hykim master
