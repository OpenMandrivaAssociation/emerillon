%define		url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		emerillon
Version:	0.1.90
Release:	%mkrel 1
Summary:	A map viewer for GNOME
Group:		Graphical desktop/GNOME
License:	GPLv2+ and LGPLv2+
URL:		http://projects.gnome.org/emerillon/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(champlain-gtk-0.12) >= 0.11.0
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(geoclue) >= 0.11.1
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
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/girepository-1.0/Emerillon-0.2.typelib
%{_datadir}/applications/%{name}.desktop
%{_datadir}/GConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.gnome.emerillon.gschema.xml

%files devel
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/Emerillon-0.2.gir
%{_includedir}/%{name}*/
%{_libdir}/pkgconfig/%{name}.pc

%files vala
%defattr(-,root,root)
%{_datadir}/vala/vapi/%{name}.*
