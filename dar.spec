# Upstream: Dag Wieers <dag@wieers.com>
# Dists: rh90 rh80 rh73 rh62

Summary: Dag Apt Repository builder.
Name: dar
Version: 0.6.0
Release: 0
License: GPL
Group: Development/Tools
URL: http://dag.wieers.com/home-made/dar/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dag.wieers.com/home-made/dar/dar-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
Requires: apt, rpm-build
#Requires: soapbox, imprison, distcc, ccache

%description
DAR is a framework for building packages in clean build environments
(distributions). It consists of tools to create and manage these build
environments, to build packages for each build environment and to update
multiple Apt repositories. 

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README TODO
%config %{_sysconfdir}/dar/
%{_sbindir}/*
%{_libdir}/dar/
%{_datadir}/dar/

%changelog
* Mon Mar 01 2004 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Updated to release 0.5.0.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.4.7-0
- Updated to release 0.4.7.

* Wed Apr 02 2003 Dag Wieers <dag@wieers.com> - 0.4.6-0
- Updated to release 0.4.6.

* Thu Mar 20 2003 Dag Wieers <dag@wieers.com> - 0.4.5-0
- Updated to release 0.4.5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.4.4-0
- Updated to release 0.4.4.

* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
