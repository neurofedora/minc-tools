%global upver 2-3-00

Name:           minc-tools
Version:        2.3.00
Release:        2%{?dist}
Summary:        Collection of tools that work on MINC format images

License:        MIT
URL:            https://github.com/BIC-MNI/minc-tools
Source0:        https://github.com/BIC-MNI/minc-tools/archive/%{name}-%{upver}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libminc-devel
BuildRequires:  bison flex
# mincview uses display command from ImageMagick
Requires:       /usr/bin/display

%description
This package is a collection of tools that work on MINC format
images.

* rawtominc, minctoraw, mincextract - format conversion
* mincheader, mincdiff, mincinfo, minchistory - file information
* mincedit, minc_modify_header - header manipulation
* mincresample - arbitrary volume resampling
* mincreshape - extraction of volume sub-cubes, image flipping, dimension
  re-ordering, type conversion
* mincconcat - concatenating or interleaving images from multiple files
* mincmath - perform simple math on files
* minccalc - perform more complicated math on files through an expression
* mincaverage - average minc files
* mincstats - calculate statistics across voxels of a file
* minclookup - lookup table operations for arbitrary re-mappings of intensities
* worldtovoxel, voxeltoworld - coordinate conversion
* xfmconcat, xfminvert - generalized transformation utilities
* mincview - simple image display using xv or ImageMagick
* mincpik - generate picture from slice through volume

%prep
%autosetup -n %{name}-%{name}-%{upver}
# we're installing mans to /usr/share/man instead of /usr/man
sed -i -e '/^INSTALL_MAN_PAGES/s/\${CMAKE_INSTALL_PREFIX}\/man/\${CMAKE_INSTALL_PREFIX}\/share\/man/' \
  progs/CMakeLists.txt conversion/CMakeLists.txt
rm -rf build/
mkdir -p build/

%build
pushd build/
  %cmake ../
  %make_build
popd

%install
pushd build/
  %make_install
popd

# Those are perl script, fix shebang to generate autodependency
sed -i -e '1s/^#!.*$/#!/usr/bin/perl' %{buildroot}%{_bindir}/minc{history,pik}

%check
pushd build/
  ctest -VV
popd

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*.1*

%changelog
* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.3.00-2
- Fix dependencies
- More description

* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.3.00-1
- Initial package
