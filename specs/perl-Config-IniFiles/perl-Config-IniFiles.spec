# $Id$
# Authority: dag

%define real_name Config-IniFiles

Summary: Module for reading .ini-style configuration files
Name: perl-Config-IniFiles
Version: 2.38
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-IniFiles/

Source: http://www.cpan.org/modules/by-module/Config/Config-IniFiles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503


%description
Module for reading .ini-style configuration files.


%prep
%setup -n %{real_name}-%{version} 


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*


%changelog
* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 2.38-1
- Initial package. (using DAR)
