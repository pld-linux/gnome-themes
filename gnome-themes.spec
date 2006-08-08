#
%define		git_version	2.15.91
#
Summary:	Default themes for GNOME enviroment
Summary(pl):	Domy¶lne motywy dla ¶rodowiska GNOME
Name:		gnome-themes
Version:	2.15.91
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-themes/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	681693616f195486af282f6433d27b7c
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gtk2-engines >= 1:2.7.7
BuildRequires:	icon-naming-utils >= 0.8.0
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	gtk2-engines >= 1:2.7.6
Conflicts:	crux-engine
Conflicts:	crux-theme
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

%description -l pl
Domy¶lne motywy dla ¶rodowiska GNOME.

%package Clarius
Summary:	Clarius theme for GNOME enviroment
Summary(pl):	Motyw Clarius dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= 2.15.90

%description Clarius
Clarius theme for GNOME enviroment.

%description Clarius -l pl
Motyw Clarius dla ¶rodowiska GNOME.

%package Clearlooks
Summary:	Clearlooks theme for GNOME enviroment
Summary(pl):	Motyw Clearlooks dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Clearlooks
Clearlooks theme for GNOME enviroment.

%description Clearlooks -l pl
Motyw Clearlooks dla ¶rodowiska GNOME.

%package Crux
Summary:	Crux theme for GNOME enviroment
Summary(pl):	Motyw Crux dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Crux
Crux theme for GNOME enviroment.

%description Crux -l pl
Motyw Crux dla ¶rodowiska GNOME.

%package Glider
Summary:	Glider theme for GNOME enviroment
Summary(pl):	Motyw Glider dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description Glider
Glider theme for GNOME enviroment.

%description Glider -l pl
Motyw Glider dla ¶rodowiska GNOME.

%package HighContrast
Summary:	HighContrast theme for GNOME enviroment
Summary(pl):	Motyw HighContrast dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrint = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrast
HighContrast theme for GNOME enviroment.

%description HighContrast -l pl
Motyw HighContrast dla ¶rodowiska GNOME.

%package HighContrast-SVG
Summary:	HighContrast SVG theme for GNOME enviroment
Summary(pl):	Motyw HighContrast SVG dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrast-SVG
HighContrast theme for GNOME enviroment (svg version).

%description HighContrast-SVG -l pl
Motyw HighContrast dla ¶rodowiska GNOME (wersja SVG).

%package HighContrastInverse
Summary:	HighContrastInverse theme for GNOME enviroment
Summary(pl):	Motyw HighContrastInverse dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-HighContrastLargePrintInverse = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

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
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrastLargePrint
HighContrastLargePrint theme for GNOME enviroment.

%description HighContrastLargePrint -l pl
Motyw HighContrastLargePrint dla ¶rodowiska GNOME.

%package HighContrastLargePrintInverse
Summary:	HighContrastLargePrintInverse theme for GNOME enviroment
Summary(pl):	Motyw HighContrastLargePrintInverse dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

%description HighContrastLargePrintInverse
HighContrastLargePrintInverse theme for GNOME enviroment.

%description HighContrastLargePrintInverse -l pl
Motyw HighContrastLargePrintInverse dla ¶rodowiska GNOME.

%package LargePrint
Summary:	LargePrint theme for GNOME enviroment
Summary(pl):	Motyw LargePrint dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

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
Requires:	gnome-icon-theme >= %{git_version}

%description LowContrast
LowContrast theme for GNOME enviroment.

%description LowContrast -l pl
Motyw LowContrast dla ¶rodowiska GNOME.

%package LowContrastLargePrint
Summary:	LowContrastLargePrint theme for GNOME enviroment
Summary(pl):	Motyw LowContrastLargePrint dla ¶rodowiska GNOME
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-icon-theme >= %{git_version}

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

for dir in Crux HighContrast HighContrast-SVG HighContrastInverse \
	HighContrastLargePrint HighContrastLargePrintInverse LargePrint \
	LowContrast LowContrastLargePrint
do
        gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/$dir
done

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ug

%find_lang %{name}

# all libs are in gtk2-engines now
rm -rf $RPM_BUILD_ROOT%{_libdir}
# eazel-engine is in gtk2-engines too
rm -rf $RPM_BUILD_ROOT%{_datadir}/eazel-engine

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%files Clarius
%defattr(644,root,root,755)
%{_datadir}/themes/Clarius

%files Clearlooks
%defattr(644,root,root,755)
%{_datadir}/themes/Clearlooks/*

%files Crux
%defattr(644,root,root,755)
%{_datadir}/themes/Crux/index.theme
%{_iconsdir}/Crux

%files Glider
%defattr(644,root,root,755)
%{_datadir}/themes/Glider

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
