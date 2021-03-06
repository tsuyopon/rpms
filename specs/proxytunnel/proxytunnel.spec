# $Id$
# Authority: dag
# Upstream: <proxytunnel-users$lists,sourceforge,net>

Summary: Punching holes in HTTP(S) proxy's
Name: proxytunnel
Version: 1.9.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://proxytunnel.sourceforge.net/

Source: http://dl.sf.net/proxytunnel/proxytunnel-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
ProxyTunnel is a program that connects stdin and stdout to a server somewhere
on the network, through a standard HTTPS proxy. We mostly use it to tunnel
SSH sessions through HTTP(S) proxies, allowing us to do many things that
wouldn't be possible without ProxyTunnel.

Proxytunnel can create tunnels using HTTP and HTTPS proxies, can work as a
back-end driver for an OpenSSH client, and create SSH connections through
HTTP(S) proxies and can work as a stand-alone application, listening on a
port for connections, and then tunneling these connections to a specified
destination.

If you want to make effective use of ProxyTunnel, the proxy server you are
going to be tunneling through must support HTTP CONNECT command and must
allow you to connect to destination machine and host, with or without HTTP
proxy authentication.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -I/usr/kerberos/include"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS INSTALL KNOWN_ISSUES LICENSE.txt README TODO
%doc %{_mandir}/man1/proxytunnel.1*
%{_bindir}/proxytunnel

%changelog
* Tue Mar 04 2008 Dag Wieers <dag@wieers.com> - 1.9.0-1
- Updated to release 1.9.0.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 1.8.0-1
- Updated to release 1.8.0.

* Fri Mar 16 2007 Dag Wieers <dag@wieers.com> - 1.7.0-1
- Updated to release 1.7.0.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 1.6.3-1
- Updated to release 1.6.3.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.0-3
- Source url fixed.

* Sun Mar 19 2006 Dag Wieers <dag@wieers.com> - 1.6.0-2
- Added SSL and setproctitle support.

* Fri Mar 03 2006 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 1.6.0-0.rc1
- Updated to release 1.6.0-rc1.

* Fri Dec 23 2005 Dag Wieers <dag@wieers.com> - 1.5.0-1
- Initial package. (using DAR)
