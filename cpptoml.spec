Name:          cpptoml
Version:       0.4.0
Release:       1%{?dist}
Summary:       A header-only library for parsing TOML
Group:         Applications/Development
URL:           https://github.com/skystrife/cpptoml
Source0:       https://github.com/skystrife/cpptoml/archive/toml-v%{version}.tar.gz
License:       MIT
BuildRequires: cmake, gcc-c++

%description
%{summary}.

%package devel
Summary:       Development files for %{name}

%description devel
This package contains libraries and header files for developing applications that use %{name}.

%global debug_package %{nil}

%prep
%autosetup -n cpptoml-toml-v%{version}

%build
cmake .
make

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

mkdir -p %{buildroot}%{_bindir}
install -m 0755 cpptoml-parser %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_includedir}/
install -m 0644 include/cpptoml.h %{buildroot}%{_includedir}/

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

%changelog
* Sat Apr 28 2018 Giovanni Grieco <giovanni.grc96@gmail.com> 0.4.0-1
- package ported to Fedora
* Sun Mar 22 2015 Davide Madrisan <davide.madrisan@gmail.com> 0.4.0-1mamba
- package created by autospec
