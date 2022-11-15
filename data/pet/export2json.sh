#!/bin/sh
cd ../.. || exit
RootPath=$(pwd)
cd "$RootPath"/../PetDoc/Config/Excel || exit
git pull
sh ./2_Export-server.sh "$RootPath"