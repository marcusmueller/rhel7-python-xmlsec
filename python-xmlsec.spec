%global srcname xmlsec

Name:           python-%{srcname}
Version:        1.3.13
Release:        1%{?dist}
Summary:        Python bindings for the XML Security Library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libxml2-devel >= 2.9.1
BuildRequires:  xmlsec1-devel >= 1.2.18
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  libtool-ltdl-devel


%description
%{summary}.


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: libxml2-devel >= 2.9.1
BuildRequires: python36-lxml
BuildRequires: pkgconfig
BuildRequires: python36-pkgconfig
BuildRequires: python36-pytest
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.18
Requires: xmlsec1-openssl
Requires: python36-lxml
Requires: python36-pkgconfig


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info
sed -i 's/build_requires.*//' setup.cfg
sed -i 's/requires.*//' setup.cfg
sed -i 's/^setup_reqs.*/setup_reqs = []/' setup.py

%build
# /usr/bin/python3 setup.py build '--executable=/usr/bin/python3 -s' --no-deps
%py3_build


%install
%py3_install


# Tests aren't available


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/xmlsec*.so
%{python3_sitearch}/xmlsec-*.egg-info
%{python3_sitearch}/xmlsec/*.pyi
%{python3_sitearch}/xmlsec/py.typed


%changelog
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.3-1
- Initial package.
