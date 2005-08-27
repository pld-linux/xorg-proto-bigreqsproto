Summary:	BigReqs protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u BigReqs i pomocnicze
Name:		xorg-proto-bigreqsproto
Version:	1.0
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/bigreqsproto-%{version}.tar.bz2
# Source0-md5:	c7a060b896a63b4f095aa6df39bd81b7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
BigReqs protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u BigReqs i pomocnicze.

%package devel
Summary:	BigReqs protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u BigReqs i pomocnicze
Group:		X11/Development/Libraries

%description devel
BigReqs protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u BigReqs i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/bigreqsproto.pc
