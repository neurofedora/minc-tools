%global upver 2-3-00

Name:           minc-tools
Version:        2.3.00
Release:        1%{?dist}
Summary:        Basic minc-tools from former minc repository

License:        MIT
URL:            https://github.com/BIC-MNI/minc-tools
Source0:        https://github.com/BIC-MNI/minc-tools/archive/%{name}-%{upver}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libminc-devel
BuildRequires:  bison flex

%description
This package is a collection of tools that work on MINC format
images.

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
* Sat Nov 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.3.00-1
- Initial package
