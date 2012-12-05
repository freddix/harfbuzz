Summary:	HarfBuzz - internationalized text shaping library
Name:		harfbuzz
Version:	0.9.8
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/harfbuzz/release/%{name}-%{version}.tar.bz2
# Source0-md5:	13b569f0acedbdb6ffe1fb8fbb4914cc
URL:		http://www.freedesktop.org/wiki/HarfBuzz
BuildRequires:	cairo-devel
BuildRequires:	freetype-devel
BuildRequires:	glib-devel
#BuildRequires:	graphite2-devel
BuildRequires:	icu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Internationalized OpenType text layout and rendering library.

%package devel
Summary:	Header files for HarfBuzz library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for HarfBuzz library.

%package apidocs
Summary:	HarfBuzz API documentation
Group:		Documentation

%description apidocs
API and internal documentation for HarfBuzz library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# missing
cat >> $RPM_BUILD_ROOT%{_pkgconfigdir}/harfbuzz.pc <<EOF
Requires.private: glib-2.0 gobject-2.0 icu-le icu-uc freetype2
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/hb-ot-shape-closure
%attr(755,root,root) %{_bindir}/hb-shape
%attr(755,root,root) %{_bindir}/hb-view
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz.so.0
%attr(755,root,root) %{_libdir}/libharfbuzz.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz.so
%{_libdir}/*.la
%{_includedir}/harfbuzz
%{_pkgconfigdir}/harfbuzz.pc

