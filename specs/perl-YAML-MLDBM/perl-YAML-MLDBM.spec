# $Id$

# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define real_name YAML-MLDBM
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Use tied hash databases with Python and Ruby
Name: perl-YAML-MLDBM
Version: 0.10
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-MLDBM/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-MLDBM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is similar to MLDBM except that it stores data internally as
YAML, instead of Data::Dumper or Storable. By doing this, you can create
tied hash DBM databases that can be used seamlessly in Python or Ruby
applications. That's because those languages also have YAML and DBM
modules. As other languages get YAML support, you should be able to use
YAML::MLDBM with them as well.

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
%{perl_vendorlib}/YAML/MLDBM.pm
%{perl_vendorlib}/MLDBM/*/YAML.pm

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
