# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Google
%define		pnam	ProtocolBuffers
%include	/usr/lib/rpm/macros.perl
Summary:	Google::ProtocolBuffers - simple interface to Google Protocol Buffers
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f328b874b291018225201713054b3465
URL:		http://search.cpan.org/dist/Google-ProtocolBuffers/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Google Protocol Buffers is a data serialization format. It is binary
(and hence compact and fast for serialization) and as extendable as
XML; its nearest analogues are Thrift and ASN.1. There are official
mappings for C++, Java and Python languages; this library is a mapping
for Perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT -name .DS_Store | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/%{pdir}
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man3/*
