# $Id: perl-IP-Country.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG-GD

Summary: Perl SVG-GD module
Name: perl-SVG-GD
Version: 0.07
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/RONAN/SVG-GD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl SVG-GD module.

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

### Clean up buildroot (noarch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

### Clean up buildroot (arch)
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*

%changelog
* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
