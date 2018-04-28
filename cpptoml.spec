Name:          cpptoml
Version:       20180428git2051836
Release:       2%{?dist}
Summary:       A header-only library for parsing TOML
Group:         Applications/Development
URL:           https://github.com/skystrife/cpptoml
Source0:       https://github.com/skystrife/cpptoml/archive/2051836a96a25e5a2d5283be7f633a157848f15e.tar.gz
License:       MIT
BuildRequires: cmake, gcc-c++, doxygen

%description
%{summary}.

%package devel
Summary: Development files for %{name}

%description devel
This package contains libraries and header files for developing applications that use %{name}.

%package doc
Summary: Documentation for %{name}

%description doc
This package contains documentation files for developing applications that use %{name}.

%global debug_package %{nil}

%prep
%autosetup -n cpptoml-2051836a96a25e5a2d5283be7f633a157848f15e

%build
cmake .
make
make doc

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

mkdir -p %{buildroot}%{_bindir}
install -m 0755 cpptoml-parser %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_includedir}/
install -m 0644 include/cpptoml.h %{buildroot}%{_includedir}/

mkdir -p %{buildroot}%{_pkgdocdir}/
find doc/html/* -type f -exec install -Dm 0644 "{}" %{buildroot}%{_pkgdocdir} \;

mkdir -p %{buildroot}%{_pkgdocdir}/search
find doc/html/search/* -type f -exec install -Dm 0644 "{}" %{buildroot}%{_pkgdocdir}/search \;

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%{_bindir}/cpptoml-parser
%doc LICENSE

%files devel
%defattr(-,root,root)
%{_includedir}/cpptoml.h
%doc README.md

%files doc
%defattr(-,root,root)
%doc %{_pkgdocdir}/*

%changelog
* Sat Apr 28 2018 Giovanni Grieco <giovanni.grc96@gmail.com> git2051836-1
- latest snapshot from git
- added doc package
* Sat Apr 28 2018 Giovanni Grieco <giovanni.grc96@gmail.com> 0.4.0-1
- package ported to Fedora
* Sun Mar 22 2015 Davide Madrisan <davide.madrisan@gmail.com> 0.4.0-1mamba
- package created by autospec
