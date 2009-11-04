#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working syslog)
#
%include	/usr/lib/rpm/macros.perl
Summary:	PlRPC perl module
Summary(pl.UTF-8):	Moduł Perla PlRPC
Name:		perl-PlRPC
Version:	0.2020
Release:	1
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/RPC/PlRPC-%{version}.tar.gz
# Source0-md5:	5361e137e56d037c5e796926ecb5300b
URL:		http://search.cpan.org/dist/PlRPC/
%if %{with tests}
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-Net-Daemon
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-perldoc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PlRPC (Perl RPC) is a package for implementing servers and clients
that are written in Perl entirely.

%description -l pl.UTF-8
PlRPC (Perl RPC) to pakiet służący do tworzenia serwerów i klientów
wyłącznie w Perlu.

%prep
%setup -q -n PlRPC

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

# do we package Bundle::* modules or not?
# or maybe as subpackage
%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/RPC/PlClient.pm
%{perl_vendorlib}/RPC/PlServer.pm
%{perl_vendorlib}/RPC/PlServer
%{perl_vendorlib}/RPC/PlClient
%{_mandir}/man3/R*
