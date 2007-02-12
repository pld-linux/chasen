Summary:	Japanese Morphological Analysis System, ChaSen
Summary(pl.UTF-8):	System analizy morfologii japońskiej ChaSen
Name:		chasen
Version:	2.3.3
Release:	1
Epoch:		0
License:	Freeware
Group:		Applications/Text
Source0:	http://chasen.aist-nara.ac.jp/stable/chasen/%{name}-%{version}.tar.gz
# Source0-md5:	629e90d9490bac95606c38c2d344cc5f
Patch0:		%{name}-gcc4.patch
URL:		http://chasen.aist-nara.ac.jp/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRequires:	darts
BuildRequires:	iconv
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Japanese Morphological Analysis System.

%description -l pl.UTF-8
System analizy morfologii japońskiej ChaSen.

%package devel
Summary:	Header files for ChaSen developers
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających systemu ChaSen
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files for ChaSen developers.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla deweloperów używających systemu ChaSen.

%package static
Summary:	Static ChaSen library
Summary(pl.UTF-8):	Biblioteka statyczna ChaSen
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static ChaSen library.

%description static -l pl.UTF-8
Biblioteka statyczna ChaSen.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%lang(ja) %doc doc/manual-j.pdf
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chasen-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libchasen.la
%{_includedir}/chasen.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libchasen.a
