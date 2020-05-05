project(lib)

cmake_minimum_required(VERSION 3.13)

set(SOURCE_LIB lib.cpp)

add_library(lib STATIC ${SOURCE_LIB})

target_include_directories(lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

