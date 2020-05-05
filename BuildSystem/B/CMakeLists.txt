project(main)
cmake_minimum_required(VERSION 3.13)

set(SOURCE_EXE main.cpp)

set(HEADER main.h)

include_directories(../)

add_executable(main ${SOURCE_EXE} ${HEADER})

