# Created by pyp2rpm-3.3.5
%global pypi_name flaky


Name:           python-%{pypi_name}
Version:        3.7.0
Release:        1
Summary:        Plugin for nose or pytest that automatically reruns flaky tests
Group:          Development/Python
License:        Apache Software License, Version 2.0, http://www.apache.org/licenses/LICENSE-2.0
URL:            https://github.com/box/flaky
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

#BuildRequires:  python3dist(tox)

%description
Flaky is a plugin for nose or pytest that automatically reruns flaky
tests.Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of removing
those tests or marking them to skip, they can be automatically retried

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

