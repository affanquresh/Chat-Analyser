#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Qt6::QDarwinContactsPermissionPlugin" for configuration "Release"
set_property(TARGET Qt6::QDarwinContactsPermissionPlugin APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(Qt6::QDarwinContactsPermissionPlugin PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX;OBJCXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/qt6/plugins/permissions/libqdarwincontactspermission.a"
  )

list(APPEND _cmake_import_check_targets Qt6::QDarwinContactsPermissionPlugin )
list(APPEND _cmake_import_check_files_for_Qt6::QDarwinContactsPermissionPlugin "${_IMPORT_PREFIX}/lib/qt6/plugins/permissions/libqdarwincontactspermission.a" )

# Import target "Qt6::QDarwinContactsPermissionPlugin_init" for configuration "Release"
set_property(TARGET Qt6::QDarwinContactsPermissionPlugin_init APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(Qt6::QDarwinContactsPermissionPlugin_init PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELEASE ""
  IMPORTED_OBJECTS_RELEASE "${_IMPORT_PREFIX}/lib/qt6/plugins/permissions/objects-Release/QDarwinContactsPermissionPlugin_init/Unity/unity_0_cxx.cxx.o"
  )

list(APPEND _cmake_import_check_targets Qt6::QDarwinContactsPermissionPlugin_init )
list(APPEND _cmake_import_check_files_for_Qt6::QDarwinContactsPermissionPlugin_init "${_IMPORT_PREFIX}/lib/qt6/plugins/permissions/objects-Release/QDarwinContactsPermissionPlugin_init/Unity/unity_0_cxx.cxx.o" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
