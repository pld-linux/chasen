# TODO: it should be reviewed by ac/am specialist and generally
#		by more experienced PLD developers.
# 		I stole spec from:
# http://sacral.c.u-tokyo.ac.jp/~hasimoto/Pineapple/0.2/testing/SPECS/chasen.spec
Summary:	Japanese Morphological Analysis System, ChaSen
Summary(pl):	System analizy morfologii japoñskiej, ChaSen
Name:		chasen
Version:	2.2.8
Release:	1
Epoch:		0
License:	freeware
Group:		Applications/Text
Source0:	http://chasen.aist-nara.ac.jp/stable/chasen/%{name}-%{version}.tar.gz
# Source0-md5:	492fce8f554d7d2ff720a8b5453ac624
URL:		http://chasen.aist-nara.ac.jp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Japanese Morphological Analysis System.

%description -l pl
System analizy morfologii japoñskiej, ChaSen

%package devel
Summary:	Libraries and header files for ChaSen developers.
Summary(pl):	Biblioteki i pliki nag³ówkowe dla deweloperów ChaSen.
Group:	Development/Libraries

%package static
Summary:	Static ChaSen library.
Summary(pl):	Biblioteka statyczna ChaSen.
Group:	Development/Libraries

%description devel
Libraries and header files for ChaSen developers.

%description devel -l pl
Biblioteki i pliki nag³ówkowe dla deweloperów ChaSen.

%description static
Static ChaSen library.

%description static -l pl
Biblioteka statyczna ChaSen.

%prep
%setup -q

%build
%{__aclocal}
%{__autoheader}
%{__libtoolize}
%{__automake}
%{__autoconf}
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

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS* README* manual*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%attr(755,root,root) %{_libdir}/*.so*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%{_includedir}/%{name}.h
%attr(755,root,root) %{_libdir}/libchasen.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libchasen.a
