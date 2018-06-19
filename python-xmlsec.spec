%global srcname xmlsec

Name:           python-%{srcname}
Version:        1.3.3
Release:        2%{?dist}
Summary:        Python bindings for the XML Security Library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  libxml2-devel >= 2.9.1
BuildRequires:  xmlsec1-devel >= 1.2.18
BuildRequires:  libtool-ltdl-devel


%description
%{summary}.


%package -n python2-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires: %{py2_dist lxml}
BuildRequires: %{py2_dist pkgconfig}
BuildRequires: %{py2_dist pytest}
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.18
Requires: xmlsec1-openssl
Requires: %{py2_dist lxml}
Requires: %{py2_dist pkgconfig}


%description -n python2-%{srcname}
%{summary}.


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: %{py3_dist lxml}
BuildRequires: %{py3_dist pkgconfig}
BuildRequires: %{py3_dist pytest}
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.18
Requires: xmlsec1-openssl
Requires: %{py3_dist lxml}
Requires: %{py3_dist pkgconfig}


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


# Tests aren't available


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/xmlsec*.so
%{python2_sitearch}/xmlsec-%{version}-*.egg-info


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/xmlsec*.so
%{python3_sitearch}/xmlsec-%{version}-*.egg-info


%changelog
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.3-1
- Initial package.
