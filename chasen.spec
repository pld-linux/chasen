Summary:	Japanese Morphological Analysis System, ChaSen
Summary(pl):	System analizy morfologii japońskiej ChaSen
Name:		chasen
Version:	2.2.8
Release:	2
Epoch:		0
License:	freeware
Group:		Applications/Text
Source0:	http://chasen.aist-nara.ac.jp/stable/chasen/%{name}-%{version}.tar.gz
# Source0-md5:	492fce8f554d7d2ff720a8b5453ac624
Patch0:		%{name}-nolibs.patch
URL:		http://chasen.aist-nara.ac.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Japanese Morphological Analysis System.

%description -l pl
System analizy morfologii japońskiej ChaSen.

%package devel
Summary:	Header files for ChaSen developers
Summary(pl):	Pliki nagłówkowe dla programistów używających systemu ChaSen
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files for ChaSen developers.

%description devel -l pl
Pliki nagłówkowe dla deweloperów używających systemu ChaSen.

%package static
Summary:	Static ChaSen library
Summary(pl):	Biblioteka statyczna ChaSen
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static ChaSen library.

%description static -l pl
Biblioteka statyczna ChaSen.

%prep
%setup -q
%patch -p1

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

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/* .
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README manual.pdf
%lang(ja) %doc NEWS-ja README-ja manual-j.pdf
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/%{name}
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chasen-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libchasen.la
%{_includedir}/chasen.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libchasen.a
