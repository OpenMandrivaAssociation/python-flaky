Name:		python-flaky
Version:	3.8.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/f/flaky/flaky-%{version}.tar.gz
Summary:	Plugin for pytest that automatically reruns flaky tests.
URL:		https://pypi.org/project/flaky/
License:	Apache Software License, Version 2.0, http://www.apache.org/licenses/LICENSE-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Plugin for pytest that automatically reruns flaky tests.

%prep
%autosetup -p1 -n flaky-%{version}

%files
%{py_sitedir}/flaky
%{py_sitedir}/flaky-*.*-info
