llc -filetype=obj output.ll -o output.o
gcc output.o -o output -ggdb
./output