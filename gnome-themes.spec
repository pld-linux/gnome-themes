Summary:	Default themes for GNOME2 enviroment
Summary(pl):	Domy¶lne motywy dla ¶rodowiska GNOME2
Name:		gnome-themes
Version:	2.8.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	f40cd7f3d6af3bb1aeab09ca84c146dc
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
Domy¶lne motywy dla ¶rodowiska GNOME2.

%package Crux
Summary:	Crux theme for GNOME 2 enviroment
Summary(pl):	Motyw Crux dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Crux
Crux theme for GNOME 2 enviroment.

%description Crux -l pl
Motyw Crux dla ¶rodowiska GNOME 2.

%package Flat-Blue
Summary:	Flat-Blue theme for GNOME 2 enviroment
Summary(pl):	Motyw Flat-Blue dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Flat-Blue
Flat-Blue theme for GNOME 2 enviroment.

%description Flat-Blue -l pl
Motyw Flat-Blue dla ¶rodowiska GNOME 2.

%package Glider
Summary:	Glider theme for GNOME 2 enviroment
Summary(pl):	Motyw Glider dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90
Requires:	gtk2-theme-engine-Smooth = %{version}-%{release}

%description Glider
Glider theme for GNOME 2 enviroment.

%description Glider -l pl
Motyw Glider dla ¶rodowiska GNOME 2.

%package Grand-Canyon
Summary:	Grand-Canyon theme for GNOME 2 enviroment
Summary(pl):	Motyw Grand-Canyon dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Smokey = %{version}-%{release}
Requires:	%{name}-Smokey-Red = %{version}-%{release}

%description Grand-Canyon
Grand-Canyon theme for GNOME 2 enviroment.

%description Grand-Canyon -l pl
Motyw Grand-Canyon dla ¶rodowiska GNOME 2.

%package HighContrast
Summary:	HighContrast theme for GNOME 2 enviroment
Summary(pl):	Motyw HighContrast dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description HighContrast
HighContrast theme for GNOME 2 enviroment.

%description HighContrast -l pl
Motyw HighContrast dla ¶rodowiska GNOME 2.

%package HighContrastInverse
Summary:	HighContrastInverse theme for GNOME 2 enviroment
Summary(pl):	Motyw HighContrastInverse dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrintInverse = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description HighContrastInverse
HighContrastInverse theme for GNOME 2 enviroment.

%description HighContrastInverse -l pl
Motyw HighContrastInverse dla ¶rodowiska GNOME 2.

%package HighContrastLargePrint
Summary:	HighContrastLargePrint theme for GNOME 2 enviroment
Summary(pl):	Motyw HighContrastLargePrint dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrast = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description HighContrastLargePrint
HighContrastLargePrint theme for GNOME 2 enviroment.

%description HighContrastLargePrint -l pl
Motyw HighContrastLargePrint dla ¶rodowiska GNOME 2.

%package HighContrastLargePrintInverse
Summary:	HighContrastLargePrintInverse theme for GNOME 2 enviroment
Summary(pl):	Motyw HighContrastLargePrintInverse dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description HighContrastLargePrintInverse
HighContrastLargePrintInverse theme for GNOME 2 enviroment.

%description HighContrastLargePrintInverse -l pl
Motyw HighContrastLargePrintInverse dla ¶rodowiska GNOME 2.

%package LargePrint
Summary:	LargePrint theme for GNOME 2 enviroment
Summary(pl):	Motyw LargePrint dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description LargePrint
LargePrint theme for GNOME 2 enviroment.

%description LargePrint -l pl
Motyw LargePrint dla ¶rodowiska GNOME 2.

%package LighthouseBlue
Summary:	LighthouseBlue theme for GNOME 2 enviroment
Summary(pl):	Motyw LighthouseBlue dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description LighthouseBlue
LighthouseBlue theme for GNOME 2 enviroment.

%description LighthouseBlue -l pl
Motyw LighthouseBlue dla ¶rodowiska GNOME 2.

%package LowContrast
Summary:	LowContrast theme for GNOME 2 enviroment
Summary(pl):	Motyw LowContrast dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-LowContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description LowContrast
LowContrast theme for GNOME 2 enviroment.

%description LowContrast -l pl
Motyw LowContrast dla ¶rodowiska GNOME 2.

%package LowContrastLargePrint
Summary:	LowContrastLargePrint theme for GNOME 2 enviroment
Summary(pl):	Motyw LowContrastLargePrint dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description LowContrastLargePrint
LowContrastLargePrint theme for GNOME 2 enviroment.

%description LowContrastLargePrint -l pl
Motyw LowContrastLargePrint dla ¶rodowiska GNOME 2.

%package Mist
Summary:	Mist theme for GNOME 2 enviroment
Summary(pl):	Motyw Mist dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Flat-Blue = %{version}-%{release}

%description Mist
Mist theme for GNOME 2 enviroment.

%description Mist -l pl
Motyw Mist dla ¶rodowiska GNOME 2.

%package Ocean-Dream
Summary:	Ocean-Dream theme for GNOME 2 enviroment
Summary(pl):	Motyw Ocean-Dream dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-LighthouseBlue = %{version}-%{release}
Requires:	%{name}-Sandwish = %{version}-%{release}
Requires:	%{name}-Sandy = %{version}-%{release}

%description Ocean-Dream
Ocean-Dream theme for GNOME 2 enviroment.

%description Ocean-Dream -l pl
Motyw Ocean-Dream dla ¶rodowiska GNOME 2.

%package Sandwish
Summary:	Sandwish theme for GNOME 2 enviroment
Summary(pl):	Motyw Sandwish dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Sandwish
Sandwish theme for GNOME 2 enviroment.

%description Sandwish -l pl
Motyw Sandwish dla ¶rodowiska GNOME 2.

%package Sandy
Summary:	Sandy theme for GNOME 2 enviroment
Summary(pl):	Motyw Sandy dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Sandy
Sandy theme for GNOME 2 enviroment.

%description Sandy -l pl
Motyw Sandy dla ¶rodowiska GNOME 2.

%package Simple
Summary:	Simple theme for GNOME 2 enviroment
Summary(pl):	Motyw Simple dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Simple
Simple theme for GNOME 2 enviroment.

%description Simple -l pl
Motyw Simple dla ¶rodowiska GNOME 2.

%package Smokey
Summary:	Smokey theme for GNOME 2 enviroment
Summary(pl):	Motyw Smokey dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Smokey
Smokey theme for GNOME 2 enviroment.

%description Smokey -l pl
Motyw Smokey dla ¶rodowiska GNOME 2.

%package Smokey-Blue
Summary:	Smokey-Blue theme for GNOME 2 enviroment
Summary(pl):	Motyw Smokey-Blue dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Smokey = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Smokey-Blue
Smokey-Blue theme for GNOME 2 enviroment.

%description Smokey-Blue -l pl
Motyw Smokey-Blue dla ¶rodowiska GNOME 2.

%package Smokey-Red
Summary:	Smokey-Red theme for GNOME 2 enviroment
Summary(pl):	Motyw Smokey-Red dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Smokey-Red
Smokey-Red theme for GNOME 2 enviroment.

%description Smokey-Red -l pl
Motyw Smokey-Red dla ¶rodowiska GNOME 2.

%package ThinIce
Summary:	ThinIce theme for GNOME 2 enviroment
Summary(pl):	Motyw ThinIce dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description ThinIce
ThinIce theme for GNOME 2 enviroment.

%description ThinIce -l pl
Motyw ThinIce dla ¶rodowiska GNOME 2.

%package Traditional
Summary:	Traditional theme for GNOME 2 enviroment
Summary(pl):	Motyw Traditional dla ¶rodowiska GNOME 2
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.7.90

%description Traditional
Traditional theme for GNOME 2 enviroment.

%description Traditional -l pl
Motyw Traditional dla ¶rodowiska GNOME 2.

%package -n gtk2-theme-engine-Smooth
Summary:        GTK+2 Smooth theme engine
Summary(pl):    Silnik Smooth dla GTK+2
Group:          Themes

%description -n gtk2-theme-engine-Smooth
GTK+2 Smooth theme engine.

%description -n gtk2-theme-engine-Smooth -l pl
Silnik Smooth dla GTK+2.

%prep
%setup -q

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

# no *.la for gtk engine modules
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/lib*.so
%exclude %{_libdir}/gtk-2.0/2.*/engines/libsmooth.so
%{_datadir}/eazel-engine

%files Crux
%defattr(644,root,root,755)
%{_datadir}/icons/Crux
%{_datadir}/themes/Crux

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

%files LighthouseBlue
%defattr(644,root,root,755)
%{_datadir}/themes/LighthouseBlue

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
%{_datadir}/themes/Mist

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

%files ThinIce
%defattr(644,root,root,755)
%{_datadir}/themes/ThinIce

%files Traditional
%defattr(644,root,root,755)
%{_datadir}/themes/Traditional

%files -n gtk2-theme-engine-Smooth
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/libsmooth.so
