%global octpkg mapping

Summary:	Add a simple mapping and GIS .shp and raster support in Octave
Name:		octave-%{octpkg}
Version:	1.4.2
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	octave-geometry >= 4.0.0
BuildRequires:	octave-io >= 2.2.7
BuildRequires:	pkgconfig(gdal)

Requires:	octave(api) = %{octave_api}
Requires:	octave-geometry >= 4.0.0
Requires:	octave-io >= 2.2.7

Requires(post): octave
Requires(postun): octave

%description
Simple mapping and GIS .shp and raster file functions.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

