#
%define		git_version	2.19.91
#
Summary:	Default themes for GNOME enviroment
Summary(pl.UTF-8):	Domyślne motywy dla środowiska GNOME
Name:		gnome-themes
Version:	2.20.0
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	862b436d77ff4dcf14849524d33c296c
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gtk2-engines >= 1:2.12.0
BuildRequires:	icon-naming-utils >= 0.8.2
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gtk2-engines >= 1:2.12.0
Conflicts:	crux-engine
Conflicts:	crux-theme
Obsoletes:	gnome-themes-Clarius
Obsoletes:	gnome-themes-Flat-Blue
Obsoletes:	gnome-themes-Traditional
Obsoletes:	gnome-themes-Grand-Canyon
Obsoletes:	gnome-themes-Ocean-Dream
Obsoletes:	gnome-themes-Sandwish
Obsoletes:	gnome-themes-Sandy
Obsoletes:	gnome-themes-Simple
Obsoletes:	gnome-themes-Smokey
Obsoletes:	gnome-themes-Smokey-Blue
Obsoletes:	gnome-themes-Smokey-Red
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME enviroment.

%description -l pl.UTF-8
Domyślne motywy dla środowiska GNOME.

%package Clearlooks
Summary:	Clearlooks theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw Clearlooks dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Clearlooks
Clearlooks theme for GNOME enviroment.

%description Clearlooks -l pl.UTF-8
Motyw Clearlooks dla środowiska GNOME.

%package ClearlooksClassic
Summary:	ClearlooksClassic theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw ClearlooksClassic dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description ClearlooksClassic
ClearlooksClassic theme for GNOME enviroment.

%description ClearlooksClassic -l pl.UTF-8
Motyw ClearlooksClassic dla środowiska GNOME.

%package Crux
Summary:	Crux theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw Crux dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Crux
Crux theme for GNOME enviroment.

%description Crux -l pl.UTF-8
Motyw Crux dla środowiska GNOME.

%package Glider
Summary:	Glider theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw Glider dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Glider
Glider theme for GNOME enviroment.

%description Glider -l pl.UTF-8
Motyw Glider dla środowiska GNOME.

%package Glossy
Summary:	Glossy theme for GNOME environment
Summary(pl.UTF-8):	Motyw Glossy dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Glossy
Glossy theme for GNOME environment.

%description Glossy -l pl.UTF-8
Motyw Glossy dla środowiska GNOME.

%package HighContrast
Summary:	HighContrast theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw HighContrast dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrast
HighContrast theme for GNOME enviroment.

%description HighContrast -l pl.UTF-8
Motyw HighContrast dla środowiska GNOME.

%package HighContrast-SVG
Summary:	HighContrast SVG theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw HighContrast SVG dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrast-SVG
HighContrast theme for GNOME enviroment (svg version).

%description HighContrast-SVG -l pl.UTF-8
Motyw HighContrast dla środowiska GNOME (wersja SVG).

%package HighContrastInverse
Summary:	HighContrastInverse theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw HighContrastInverse dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrintInverse = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrastInverse
HighContrastInverse theme for GNOME enviroment.

%description HighContrastInverse -l pl.UTF-8
Motyw HighContrastInverse dla środowiska GNOME.

%package HighContrastLargePrint
Summary:	HighContrastLargePrint theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw HighContrastLargePrint dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrast = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrastLargePrint
HighContrastLargePrint theme for GNOME enviroment.

%description HighContrastLargePrint -l pl.UTF-8
Motyw HighContrastLargePrint dla środowiska GNOME.

%package HighContrastLargePrintInverse
Summary:	HighContrastLargePrintInverse theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw HighContrastLargePrintInverse dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrastLargePrintInverse
HighContrastLargePrintInverse theme for GNOME enviroment.

%description HighContrastLargePrintInverse -l pl.UTF-8
Motyw HighContrastLargePrintInverse dla środowiska GNOME.

%package Inverted
Summary:	Inverted theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw Inverted dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Inverted
Inverted theme for GNOME enviroment.

%description Inverted -l pl.UTF-8
Motyw Inverted dla środowiska GNOME.

%package LargePrint
Summary:	LargePrint theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw LargePrint dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description LargePrint
LargePrint theme for GNOME enviroment.

%description LargePrint -l pl.UTF-8
Motyw LargePrint dla środowiska GNOME.

%package LowContrast
Summary:	LowContrast theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw LowContrast dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-LowContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description LowContrast
LowContrast theme for GNOME enviroment.

%description LowContrast -l pl.UTF-8
Motyw LowContrast dla środowiska GNOME.

%package LowContrastLargePrint
Summary:	LowContrastLargePrint theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw LowContrastLargePrint dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description LowContrastLargePrint
LowContrastLargePrint theme for GNOME enviroment.

%description LowContrastLargePrint -l pl.UTF-8
Motyw LowContrastLargePrint dla środowiska GNOME.

%package Mist
Summary:	Mist theme for GNOME enviroment
Summary(pl.UTF-8):	Motyw Mist dla środowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description Mist
Mist theme for GNOME enviroment.

%description Mist -l pl.UTF-8
Motyw Mist dla środowiska GNOME.

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

CD=`pwd`
cd $RPM_BUILD_ROOT%{_iconsdir}
for dir in *
do
        gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
done
cd $CD

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

%files ClearlooksClassic
%defattr(644,root,root,755)
%{_datadir}/themes/ClearlooksClassic

%files Crux
%defattr(644,root,root,755)
%{_datadir}/themes/Crux/index.theme
%{_iconsdir}/Crux

%files Glider
%defattr(644,root,root,755)
%{_datadir}/themes/Glider

%files Glossy
%defattr(644,root,root,755)
%{_datadir}/themes/Glossy

%files HighContrast
%defattr(644,root,root,755)
%{_datadir}/themes/HighContrast
%{_iconsdir}/HighContrast

%files HighContrast-SVG
%defattr(644,root,root,755)
%{_iconsdir}/HighContrast-SVG

%files HighContrastInverse
%defattr(644,root,root,755)
%{_datadir}/themes/HighContrastInverse
%{_iconsdir}/HighContrastInverse

%files HighContrastLargePrint
%defattr(644,root,root,755)
%{_datadir}/themes/HighContrastLargePrint
%{_iconsdir}/HighContrastLargePrint

%files HighContrastLargePrintInverse
%defattr(644,root,root,755)
%{_datadir}/themes/HighContrastLargePrintInverse
%{_iconsdir}/HighContrastLargePrintInverse

%files Inverted
%defattr(644,root,root,755)
%{_datadir}/themes/Inverted

%files LargePrint
%defattr(644,root,root,755)
%{_datadir}/themes/LargePrint
%{_iconsdir}/LargePrint

%files LowContrast
%defattr(644,root,root,755)
%{_datadir}/themes/LowContrast
%{_iconsdir}/LowContrast

%files LowContrastLargePrint
%defattr(644,root,root,755)
%{_datadir}/themes/LowContrastLargePrint
%{_iconsdir}/LowContrastLargePrint

%files Mist
%defattr(644,root,root,755)
%{_datadir}/themes/Mist/index.theme
%{_datadir}/themes/Mist/metacity-1
%{_iconsdir}/Mist
