%define		url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		emerillon
Version:	0.1.90
Release:	3
Summary:	A map viewer for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv2+ and LGPLv2+
URL:		http://projects.gnome.org/emerillon/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	pkgconfig(geoclue)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(champlain-gtk-0.12)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(rest-0.7)

%description
Emerillon is a map viewer for GNOME that has an extensible plugin architecture
and Telepathy integration to enable app and location sharing and display of 
friends locations.

%package devel
Summary:	Development package for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Files for developing plugins for %{name}.

%package vala
Summary:	Vala Development package for %{name}
Group:		Development/Other
Requires:	%{name}-devel = %{version}-%{release}

%description vala
Files for vala development with %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-schemas-compile \
	--enable-introspection
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/girepository-1.0/Emerillon-0.2.typelib
%{_datadir}/applications/%{name}.desktop
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.gnome.emerillon.gschema.xml

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/Emerillon-0.2.gir
%{_includedir}/%{name}*/
%{_libdir}/pkgconfig/%{name}.pc

%files vala
%{_datadir}/vala/vapi/%{name}.*



%changelog
* Fri Jun 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.90-2
+ Revision: 805911
- rebuild for clutter libs

* Thu Feb 23 2012 Andrey Bondrov <abondrov@mandriva.org> 0.1.90-1
+ Revision: 779300
- imported package emerillon

