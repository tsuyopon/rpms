# $Id$
# Authority: dries
# Upstream: Jeff Weisberg <jaw+pause$tcp4me,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chart-Strip

Summary: Draw strip chart type graphs
Name: perl-Chart-Strip
Version: 1.01
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chart-Strip/

Source: http://www.cpan.org/modules/by-module/Chart/Chart-Strip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module you can draw strip chart type graphs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Chart/
%{perl_vendorlib}/Chart/Strip.pm

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
