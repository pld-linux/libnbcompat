Summary:	NetBSD compat library 
Name:		libnbcompat
Version:	2005Q1
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	7c7fafd5d5c732d7ce0a735a940bcfc3
Patch0:		%{name}-install.patch
URL:		http://www.netbsd.org/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetBSD compatibility library

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
%{_includedir}/nbcompat.h
%dir %{_includedir}/nbcompat
%{_includedir}/nbcompat/*
