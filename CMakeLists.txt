project(STILL)
cmake_minimum_required(VERSION 2.8)

# Generate compile_commands,json
set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE INTERNAL "")

find_package(LLVM REQUIRED)
find_package(Clang REQUIRED)

set(CMAKE_CXX_FLAGS "-g3 -O0 -fno-rtti ${LLVM_COMPILE_FLAGS}")

include_directories(${LLVM_INCLUDE_DIRS})
include_directories(${CLANG_INCLUDE_DIRS})

set(LLVM_LINK_COMPONENTS
  FrontendOpenMP
  Support
  )

add_executable(still
  main.cpp
  )

target_link_libraries(still
  PRIVATE
  clangAST
  clangASTMatchers
  clangBasic
  clangFrontend
  clangTooling
  clangToolingRefactoring
  )
