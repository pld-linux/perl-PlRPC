%include	/usr/lib/rpm/macros.perl
Summary:	PlRPC perl module
Summary(pl):	Modu³ perla PlRPC
Name:		perl-PlRPC
Version:	0.2012
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/RPC/PlRPC-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Net-Daemon
BuildRequires:	perl-Storable
BuildRequires:	perl-Compress-Zlib
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PlRPC (Perl RPC) is a package for implementing servers and clients
that are written in Perl entirely.

%description -l pl
PlRPC (Perl RPC) to pakiet s³u¿±cy do tworzenia serwerów i klientów
wy³±cznie w perlu.

%prep
%setup -q -n PlRPC-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/RPC/PlServer
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Bundle/PlRPC.pm
%{perl_sitelib}/RPC/PlClient.pm
%{perl_sitelib}/RPC/PlServer.pm
%{perl_sitelib}/RPC/PlServer
%{perl_sitearch}/auto/RPC/PlServer

%{_mandir}/man3/*
