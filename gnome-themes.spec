Summary:	Default themes for Gnome2 enviroment
Summary(pl):	motywy dla ¶rodowiska Gnome2
Name:		gnome-themes
Version:	2.1.99
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk2-engines
BuildRequires:	libglade2-devel
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
%configure

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
