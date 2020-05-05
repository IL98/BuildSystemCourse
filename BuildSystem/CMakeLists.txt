
project(hello_world)

cmake_minimum_required(VERSION 3.13)

set(SCRIPT_DIR C)
set(PYTHON_SCRIPT preparing.py)

add_custom_command(
        PRE_BUILD
        OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/${SCRIPT_DIR}/index.h
        COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/${SCRIPT_DIR}/${PYTHON_SCRIPT}
        DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${SCRIPT_DIR}/${PYTHON_SCRIPT}
        COMMENT "GENERATING - index.h via python script"
        )

set(DOC_DIR doc)
set(DOC_OUTPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}/${DOC_DIR})

add_custom_command(
	PRE_BUILD
	OUTPUT ${DOC_OUTPUT_DIR}/html/doxygen.png
	DEPEND  ${CMAKE_CURRENT_SOURCE_DIR}/${DOC_DIR}/Doxyfile 
	COMMAND ENV_INPUT=${CMAKE_CURRENT_SOURCE_DIR} ENV_OUTPUT_DIR=${DOC_OUTPUT_DIR} doxygen ${CMAKE_CURRENT_SOURCE_DIR}/${DOC_DIR}/Doxyfile
	COMMENT "Generating documentation with Doxygen"
)

add_subdirectory(A)
add_subdirectory(B)

add_custom_target(doc ALL
	DEPENDS ${DOC_OUTPUT_DIR}/html/doxygen.png)

add_custom_target(run ALL
                       DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${SCRIPT_DIR}/index.h)	

add_dependencies(doc run)
add_dependencies(main doc)

target_link_libraries(main lib)

