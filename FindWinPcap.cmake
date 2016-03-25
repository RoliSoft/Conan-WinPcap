#
#  WinPcap Developer's Pack CMake Package Finder
#
#    WINPCAP_FOUND - Found the WDK
#    WINPCAP_INCLUDE_DIR - The WDK include directory
#    WINPCAP_LIBRARY - Libraries to be linked with
#

find_path(WINPCAP_INCLUDE_DIR "pcap.h" PATHS "include")
find_library(WINPCAP_LIBRARY NAMES "wpcap" PATHS "lib")

include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WinPcap DEFAULT_MSG WINPCAP_INCLUDE_DIR WINPCAP_LIBRARY)

mark_as_advanced(WINPCAP_INCLUDE_DIR WINPCAP_LIBRARY)