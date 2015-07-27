## this gets processed by "autoreconf --install" to create Makefile.in

SUBDIRS=	tellitto

rpm: all
	env RPMDIR=/tmp epm_cover -a `uname -i` tellitto

EXTRA_DIST = tellitto.spec \
	tellitto/tellitto tellitto/tellitto.8 tellitto/tellitto.cfg \
	COPYRIGHT README

