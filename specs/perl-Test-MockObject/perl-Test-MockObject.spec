# $Id$

# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define real_name Test-MockObject
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Highly polymorphic testing object
Name: perl-Test-MockObject
Version: 0.20
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-MockObject/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/Test-MockObject-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Test::MockObject is a highly polymorphic testing object, capable of looking
like all sorts of objects.  This makes white-box testing much easier, as you
can concentrate on what the code being tested sends to and receives from the
mocked object, instead of worrying about faking up your own data.  (Another
option is not to test difficult things.  Now you have no excuse.)


%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Test/MockObject.pm
%{perl_vendorlib}/Test/MockObject/*

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
