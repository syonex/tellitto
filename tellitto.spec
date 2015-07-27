Name: tellitto
Version: 1.1
Release: 1
License: 2012 by SYONEX, All Rights Reserved.
Packager: software@syonex.com
Vendor: SYONEX
Source0: tellitto-1.1.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Summary: tellitto
Group: Applications


%description 
tellitto - notify people via pager SMS etc.
built at FreshBooks


%prep
%setup -q

%build
autoreconf
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}


%files
%attr(0755,root,root) "/usr/sbin/tellitto"
%attr(0644,root,root) "/usr/share/man/man8/tellitto.8.gz"
