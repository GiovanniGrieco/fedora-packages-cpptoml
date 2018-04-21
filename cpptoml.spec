%define prjname cpptoml
%define prjversion 0.4.0

Name: %{prjname}
Version: %{prjversion}
Release: 0%{?dist}
Summary: cpptoml is a header-only library for parsing TOML

License: MIT
URL:     https://github.com/skystrife/%{prjname}
Source0: https://github.com/skystrife/%{prjname}/archive/toml-v%{prjversion}.tar.gz
BuildArch: noarch
BuildRequires: cmake

%description
cpptoml is a header-only library for parsing TOML.
TOML aims to be a minimal configuration file format
that is easy to read due to obvious semantics.
TOML is designed to map unambiguously to a hash table.
TOML should be easy to parse into data structures in
a wide variety of languages.

%prep
%autosetup -n %{prjname}-toml-v%{version}

%build
%cmake .
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/usr/include/
%{__install} -m 0644 include/cpptoml.h $RPM_BUILD_ROOT/usr/include/cpptoml.h

%clean

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_includedir}/cpptoml.h

%changelog
* Fri Apr 20 2018 Giovanni Grieco <corsaro@fedoraproject.org> - 0.4.0
- Made package available for personal COPR repo.
