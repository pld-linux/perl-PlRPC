%include	/usr/lib/rpm/macros.perl
Summary:	PlRPC perl module
Summary(pl):	Modu� perla PlRPC
Name:		perl-PlRPC
Version:	0.2017
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPC/PlRPC-%{version}.tar.gz
# Source0-md5:	e70f33f0f8c30ee5547865c15b811b7d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Net-Daemon
BuildRequires:	perl-Storable
BuildRequires:	perl-Compress-Zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PlRPC (Perl RPC) is a package for implementing servers and clients
that are written in Perl entirely.

%description -l pl
PlRPC (Perl RPC) to pakiet s�u��cy do tworzenia serwer�w i klient�w
wy��cznie w perlu.

%prep
%setup -q -n PlRPC-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/RPC/PlClient.pm
%{perl_vendorlib}/RPC/PlServer.pm
%{perl_vendorlib}/RPC/PlServer
%{_mandir}/man3/R*
