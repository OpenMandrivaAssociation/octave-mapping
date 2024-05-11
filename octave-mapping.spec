%global octpkg mapping

Summary:	Add a simple mapping and GIS .shp and raster support in Octave
Name:		octave-mapping
Version:	1.4.2
Release:	7
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/mapping/
Source0:	https://downloads.sourceforge.net/octave/mapping-%{version}.tar.gz

BuildRequires:  octave-devel >= 5.2.0
BuildRequires:  octave-io >= 2.2.7
BuildRequires:  octave-geometry >= 4.0.0
BuildRequires:	pkgconfig(gdal)

Requires:	octave(api) = %{octave_api}
Requires:  	octave-io >= 2.2.7
Requires:  	octave-geometry >= 4.0.0

Requires(post): octave
Requires(postun): octave

%description
Simple mapping and GIS .shp .dxf and raster file functions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

