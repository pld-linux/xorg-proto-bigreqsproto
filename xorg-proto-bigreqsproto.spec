Summary:	BigReqs protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu BigReqs i pomocnicze
Name:		xorg-proto-bigreqsproto
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/bigreqsproto-%{version}.tar.bz2
# Source0-md5:	d30c5dbf19ca6dffcd9788227ecff8c5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BigReqs protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu BigReqs i pomocnicze.

%package devel
Summary:	BigReqs protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu BigReqs i pomocnicze
Group:		X11/Development/Libraries
# just for dirs
Requires:	xorg-proto-xproto-devel

%description devel
BigReqs protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu BigReqs i pomocnicze.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/bigreqsproto.pc
