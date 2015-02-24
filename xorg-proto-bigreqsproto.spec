Summary:	Big Requests extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Big Requests
Name:		xorg-proto-bigreqsproto
Version:	1.1.2
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-%{version}.tar.bz2
# Source0-md5:	1a05fb01fa1d5198894c931cf925c025
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Big Requests extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Big Requests.

%package devel
Summary:	Big Requests extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Big Requests
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel

%description devel
Big Requests extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Big Requests.

%prep
%setup -q -n bigreqsproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/bigreq.html
%{_includedir}/X11/extensions/bigreqs*.h
%{_pkgconfigdir}/bigreqsproto.pc
