Summary:	Default themes for GNOME2 enviroment
Summary(pl):	Domy�lne motywy dla �rodowiska GNOME2
Name:		gnome-themes
Version:	2.7.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	09c3caaefdb785da62dba2e14c5f0df4
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk2-engines >= 2.2.0-3
BuildRequires:	libtool
BuildRequires:	intltool >= 0.28
Requires:	gtk2-engines >= 2.2.0-3
Conflicts:	crux-engine
Conflicts:	crux-theme
Conflicts:	gtk2-theme-engine-ThinIce
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME2 enviroment.

%description -l pl
Domy�lne motywy dla �rodowiska GNOME2.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
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

%find_lang %{name}

# no *.la for gtk engine modules
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/lib*.so
%{_datadir}/eazel-engine
%{_datadir}/icons/*
%{_datadir}/themes/*
