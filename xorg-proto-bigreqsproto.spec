Summary:	BigReqs extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia BigReqs
Name:		xorg-proto-bigreqsproto
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-%{version}.tar.bz2
# Source0-md5:	6f6c24436c2b3ab235eb14a85b9aaacf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BigReqs extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia BigReqs.

%package devel
Summary:	BigReqs extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia BigReqs
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel

%description devel
BigReqs extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia BigReqs.

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
%doc COPYING ChangeLog README specs/*.{html,css}
%{_includedir}/X11/extensions/bigreqs*.h
%{_pkgconfigdir}/bigreqsproto.pc
