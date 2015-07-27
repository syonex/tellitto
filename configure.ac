## this gets processed by "autoreconf --install" to create configure.in

# at least this version of auto tools? - 2.59 is on centos 5.x
AC_PREREQ(2.59)

AC_INIT([tellitto], [1.1], [software@syonex.com])

# utilities go here
AC_CONFIG_AUX_DIR([build-aux])

## foreign means nota GNU package, so no NEWS, README, COPYING, etc. needed
## AM_INIT_AUTOMAKE([-Wall -Werror])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])

# Checks for programs.
# automake 1.12 seems to require this, but automake 1.11 doesn't recognize it
# m4_pattern_allow([AM_PROG_AR])
# AM_PROG_AR
# m4_ifdef([AM_PROG_AR], [AM_PROG_AR])
# AC_PROG_CC
# AM_PROG_CC_C_O
# AC_PROG_RANLIB

# Checks for libraries.

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.



AC_CONFIG_FILES([
    Makefile
    tellitto/Makefile
])

AC_OUTPUT
