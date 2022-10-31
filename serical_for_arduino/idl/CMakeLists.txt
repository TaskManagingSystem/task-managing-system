set(IDL_FILES "" )

if(WIN32)
  set(SCRIPT_FILE ${PROJECT_SOURCE_DIR}/idlcompile.bat)
  set(DELETE_FILE ${PROJECT_SOURCE_DIR}/delete.bat)
else()
    set(SCRIPT_FILE ${PROJECT_SOURCE_DIR}/idlcompile.sh)
endif()

if(EXISTS ${SCRIPT_FILE})
  configure_file(${SCRIPT_FILE} ${CMAKE_BINARY_DIR}/ COPYONLY)
  install(PROGRAMS ${SCRIPT_FILE} DESTINATION "${INSTALL_PREFIX}"
          COMPONENT component)
  if(UNIX)
    add_custom_target(idlcompile ALL sh ${CMAKE_BINARY_DIR}/idlcompile.sh
      WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )
  else()
    add_custom_target(idlcompile ALL ${CMAKE_BINARY_DIR}/idlcompile.bat
      WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )
  endif()
endif()

if(WIN32)
  if(EXISTS ${DELETE_FILE})
    configure_file(${DELETE_FILE} ${CMAKE_BINARY_DIR}/ COPYONLY)
    install(PROGRAMS ${DELETE_FILE} DESTINATION "${INSTALL_PREFIX}"
            COMPONENT component)
  endif()
endif()
