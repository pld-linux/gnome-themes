Summary:	Default themes for Gnome2 enviroment
Summary(pl):	Domy¶lne motywy dla ¶rodowiska Gnome2
Name:		gnome-themes
Version:	2.2.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.2/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk2-engines >= 2.2.0
BuildRequires:	gtk2-theme-engine-ThinIce >= 2.0.2
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:  intltool >= 0.25
BuildRequires:  libgnomeui-devel >= 2.2.0.1
Conflicts:	crux-engine
Conflicts:	crux-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for Gnome2 enviroment.

%description -l pl
Domy¶lne motywy dla ¶rodowiska Gnome2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
    --enable-all-themes \
    --disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/lib*.so
%{_libdir}/gtk-2.0/2.*/engines/lib*.la
%{_datadir}/*
