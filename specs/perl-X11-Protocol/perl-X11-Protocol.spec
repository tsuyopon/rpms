# $Id$

# Authority: dries
# Upstream: Stephen McCamant <smcc$csua,berkeley,edu>

%define real_name X11-Protocol
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl module for the X Window System Protocol
Name: perl-X11-Protocol
Version: 0.53
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/X11-Protocol/

Source: http://search.cpan.org/CPAN/authors/id/S/SM/SMCCAM/X11-Protocol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This is a module for the X Window System Protocol.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/X11/*.pm
%{perl_vendorlib}/X11/Protocol
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Initial package.
