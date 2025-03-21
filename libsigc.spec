%define pkgname libsigc++

%define api_version 3.0
%define major 0
%define libname %mklibname sigc++ %api_version %major
%define libnamedev %mklibname -d sigc++ %api_version

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		%{pkgname}
Summary:	The Typesafe Signal Framework for C++
Version:	3.6.0
Release:	4
License:	LGPLv3+
Group:		System/Libraries
URL:		https://libsigc.sourceforge.net/
Source0:	https://download.gnome.org/sources/%{pkgname}/%{url_ver}/%{pkgname}-%{version}.tar.xz

BuildRequires: meson
BuildRequires: mm-common

%description
Callback system for use in widget libraries, abstract interfaces, and
general programming.

This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally part
of the Gtk-- widget set, %{pkgname} is now a separate library to provide for
more general use. It is the most complete library of its kind with the
ablity to connect an abstract callback to a class method, function, or
function object. It contains adaptor classes for connection of dissimilar
callbacks and has an ease of use unmatched by other C++ callback
libraries.

Package gtkmm, which is a c++ binding to the famous gtk+ library, uses
%{pkgname}.


%package -n %{libname}
Summary:	The Typesafe Signal Framework for C++
Group:		System/Libraries
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description -n %{libname}
Callback system for use in widget libraries, abstract interfaces, and
general programming.

This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally part
of the Gtk-- widget set, %{pkgname} is now a separate library to provide for
more general use. It is the most complete library of its kind with the
ablity to connect an abstract callback to a class method, function, or
function object. It contains adaptor classes for connection of dissimilar
callbacks and has an ease of use unmatched by other C++ callback
libraries.

Package gtkmm, which is a c++ binding to the famous gtk+ library, uses
%{pkgname}.


%package -n %{libnamedev}
Summary:	Development tools for the Typesafe Signal Framework for C++
Group:		Development/C++
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Provides:	sigc++%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{libnamedev}
This package contains the headers and static libraries of %{pkgname},
which are needed when developing or compiling applications which use
%{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

find %buildroot -name '*.la' -delete

%files -n %{libname}
%doc COPYING NEWS README.md
%{_libdir}/libsigc-%{api_version}.so.%{major}{,.*}

%files -n %{libnamedev}
%doc ChangeLog
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api_version}
