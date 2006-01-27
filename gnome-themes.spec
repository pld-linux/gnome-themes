Summary:	Default themes for GNOME enviroment
Summary(pl):	Domy¶lne motywy dla ¶rodowiska GNOME
Name:		gnome-themes
Version:	2.13.2
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-themes/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	b2058ca2c8157edc7f5b097bbe9cc537
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk2-engines >= 1:2.6.5
BuildRequires:	libtool
BuildRequires:	intltool >= 0.28
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gtk2-engines >= 1:2.6.5
Conflicts:	crux-engine
Conflicts:	crux-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME enviroment.

%description -l pl
Domy¶lne motywy dla ¶rodowiska GNOME.

%package Clearlooks
Summary:	Clearlooks theme for GNOME enviroment
Summary(pl):	Motyw Clearlooks dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Clearlooks
Clearlooks theme for GNOME enviroment.

%description Clearlooks -l pl
Motyw Clearlooks dla ¶rodowiska GNOME.

%package Crux
Summary:	Crux theme for GNOME enviroment
Summary(pl):	Motyw Crux dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Crux
Crux theme for GNOME enviroment.

%description Crux -l pl
Motyw Crux dla ¶rodowiska GNOME.

%package Flat-Blue
Summary:	Flat-Blue theme for GNOME enviroment
Summary(pl):	Motyw Flat-Blue dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Flat-Blue
Flat-Blue theme for GNOME enviroment.

%description Flat-Blue -l pl
Motyw Flat-Blue dla ¶rodowiska GNOME.

%package Glider
Summary:	Glider theme for GNOME enviroment
Summary(pl):	Motyw Glider dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Glider
Glider theme for GNOME enviroment.

%description Glider -l pl
Motyw Glider dla ¶rodowiska GNOME.

%package Grand-Canyon
Summary:	Grand-Canyon theme for GNOME enviroment
Summary(pl):	Motyw Grand-Canyon dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Smokey = %{version}-%{release}
Requires:	%{name}-Smokey-Red = %{version}-%{release}

%description Grand-Canyon
Grand-Canyon theme for GNOME enviroment.

%description Grand-Canyon -l pl
Motyw Grand-Canyon dla ¶rodowiska GNOME.

%package HighContrast
Summary:	HighContrast theme for GNOME enviroment
Summary(pl):	Motyw HighContrast dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description HighContrast
HighContrast theme for GNOME enviroment.

%description HighContrast -l pl
Motyw HighContrast dla ¶rodowiska GNOME.

%package HighContrastInverse
Summary:	HighContrastInverse theme for GNOME enviroment
Summary(pl):	Motyw HighContrastInverse dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrintInverse = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description HighContrastInverse
HighContrastInverse theme for GNOME enviroment.

%description HighContrastInverse -l pl
Motyw HighContrastInverse dla ¶rodowiska GNOME.

%package HighContrastLargePrint
Summary:	HighContrastLargePrint theme for GNOME enviroment
Summary(pl):	Motyw HighContrastLargePrint dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrast = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description HighContrastLargePrint
HighContrastLargePrint theme for GNOME enviroment.

%description HighContrastLargePrint -l pl
Motyw HighContrastLargePrint dla ¶rodowiska GNOME.

%package HighContrastLargePrintInverse
Summary:	HighContrastLargePrintInverse theme for GNOME enviroment
Summary(pl):	Motyw HighContrastLargePrintInverse dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description HighContrastLargePrintInverse
HighContrastLargePrintInverse theme for GNOME enviroment.

%description HighContrastLargePrintInverse -l pl
Motyw HighContrastLargePrintInverse dla ¶rodowiska GNOME.

%package LargePrint
Summary:	LargePrint theme for GNOME enviroment
Summary(pl):	Motyw LargePrint dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description LargePrint
LargePrint theme for GNOME enviroment.

%description LargePrint -l pl
Motyw LargePrint dla ¶rodowiska GNOME.

%package LowContrast
Summary:	LowContrast theme for GNOME enviroment
Summary(pl):	Motyw LowContrast dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-LowContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description LowContrast
LowContrast theme for GNOME enviroment.

%description LowContrast -l pl
Motyw LowContrast dla ¶rodowiska GNOME.

%package LowContrastLargePrint
Summary:	LowContrastLargePrint theme for GNOME enviroment
Summary(pl):	Motyw LowContrastLargePrint dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description LowContrastLargePrint
LowContrastLargePrint theme for GNOME enviroment.

%description LowContrastLargePrint -l pl
Motyw LowContrastLargePrint dla ¶rodowiska GNOME.

%package Mist
Summary:	Mist theme for GNOME enviroment
Summary(pl):	Motyw Mist dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Flat-Blue = %{version}-%{release}

%description Mist
Mist theme for GNOME enviroment.

%description Mist -l pl
Motyw Mist dla ¶rodowiska GNOME.

%package Ocean-Dream
Summary:	Ocean-Dream theme for GNOME enviroment
Summary(pl):	Motyw Ocean-Dream dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Sandwish = %{version}-%{release}
Requires:	%{name}-Sandy = %{version}-%{release}

%description Ocean-Dream
Ocean-Dream theme for GNOME enviroment.

%description Ocean-Dream -l pl
Motyw Ocean-Dream dla ¶rodowiska GNOME.

%package Sandwish
Summary:	Sandwish theme for GNOME enviroment
Summary(pl):	Motyw Sandwish dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Sandwish
Sandwish theme for GNOME enviroment.

%description Sandwish -l pl
Motyw Sandwish dla ¶rodowiska GNOME.

%package Sandy
Summary:	Sandy theme for GNOME enviroment
Summary(pl):	Motyw Sandy dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Sandy
Sandy theme for GNOME enviroment.

%description Sandy -l pl
Motyw Sandy dla ¶rodowiska GNOME.

%package Simple
Summary:	Simple theme for GNOME enviroment
Summary(pl):	Motyw Simple dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Simple
Simple theme for GNOME enviroment.

%description Simple -l pl
Motyw Simple dla ¶rodowiska GNOME.

%package Smokey
Summary:	Smokey theme for GNOME enviroment
Summary(pl):	Motyw Smokey dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Smokey
Smokey theme for GNOME enviroment.

%description Smokey -l pl
Motyw Smokey dla ¶rodowiska GNOME.

%package Smokey-Blue
Summary:	Smokey-Blue theme for GNOME enviroment
Summary(pl):	Motyw Smokey-Blue dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Smokey = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Smokey-Blue
Smokey-Blue theme for GNOME enviroment.

%description Smokey-Blue -l pl
Motyw Smokey-Blue dla ¶rodowiska GNOME.

%package Smokey-Red
Summary:	Smokey-Red theme for GNOME enviroment
Summary(pl):	Motyw Smokey-Red dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Smokey-Red
Smokey-Red theme for GNOME enviroment.

%description Smokey-Red -l pl
Motyw Smokey-Red dla ¶rodowiska GNOME.

%package Traditional
Summary:	Traditional theme for GNOME enviroment
Summary(pl):	Motyw Traditional dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.10.0

%description Traditional
Traditional theme for GNOME enviroment.

%description Traditional -l pl
Motyw Traditional dla ¶rodowiska GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

# all libs are in gtk2-engines now
rm -rf $RPM_BUILD_ROOT%{_libdir}
# eazel-engine is in gtk2-engines too
rm -rf $RPM_BUILD_ROOT%{_datadir}/eazel-engine

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%files Clearlooks
%defattr(644,root,root,755)
%{_datadir}/themes/Clearlooks/*

%files Crux
%defattr(644,root,root,755)
%{_datadir}/icons/Crux
%{_datadir}/themes/Crux/index.theme

%files Flat-Blue
%defattr(644,root,root,755)
%{_datadir}/icons/Flat-Blue

%files Glider
%defattr(644,root,root,755)
%{_datadir}/themes/Glider

%files Grand-Canyon
%defattr(644,root,root,755)
%{_datadir}/themes/Grand-Canyon

%files HighContrast
%defattr(644,root,root,755)
%{_datadir}/icons/HighContrast
%{_datadir}/themes/HighContrast

%files HighContrastInverse
%defattr(644,root,root,755)
%{_datadir}/icons/HighContrastInverse
%{_datadir}/themes/HighContrastInverse

%files HighContrastLargePrint
%defattr(644,root,root,755)
%{_datadir}/icons/HighContrastLargePrint
%{_datadir}/themes/HighContrastLargePrint

%files HighContrastLargePrintInverse
%defattr(644,root,root,755)
%{_datadir}/icons/HighContrastLargePrintInverse
%{_datadir}/themes/HighContrastLargePrintInverse

%files LargePrint
%defattr(644,root,root,755)
%{_datadir}/icons/LargePrint
%{_datadir}/themes/LargePrint

%files LowContrast
%defattr(644,root,root,755)
%{_datadir}/icons/LowContrast
%{_datadir}/themes/LowContrast

%files LowContrastLargePrint
%defattr(644,root,root,755)
%{_datadir}/icons/LowContrastLargePrint
%{_datadir}/themes/LowContrastLargePrint

%files Mist
%defattr(644,root,root,755)
%{_datadir}/themes/Mist/metacity-1
%{_datadir}/themes/Mist/index.theme

%files Ocean-Dream
%defattr(644,root,root,755)
%{_datadir}/themes/Ocean-Dream

%files Sandwish
%defattr(644,root,root,755)
%{_datadir}/themes/Sandwish

%files Sandy
%defattr(644,root,root,755)
%{_datadir}/icons/Sandy

%files Simple
%defattr(644,root,root,755)
%{_datadir}/themes/Simple

%files Smokey
%defattr(644,root,root,755)
%{_datadir}/themes/Smokey

%files Smokey-Blue
%defattr(644,root,root,755)
%{_datadir}/icons/Smokey-Blue
%{_datadir}/themes/Smokey-Blue

%files Smokey-Red
%defattr(644,root,root,755)
%{_datadir}/icons/Smokey-Red

%files Traditional
%defattr(644,root,root,755)
%{_datadir}/themes/Traditional
