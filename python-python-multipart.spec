%define module python_multipart

Name:		python-python-multipart
Version:	0.0.20
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/python-multipart/python_multipart-%{version}.tar.gz
Summary:	A streaming multipart parser for Python
URL:		https://pypi.org/project/python-multipart/
License:	Apache-2.0
Group:		Development/Python

BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(pyyaml)

BuildArch:	noarch

%description
A streaming multipart parser for Python

%prep
%autosetup -p1 -n python_multipart-%{version}

%build
%py_build

%install
%py_install

%check
pytest tests/

%files
%{python3_sitelib}/%{module}-*.dist-info
%{python3_sitelib}/%{module}/*.py
%{python3_sitelib}/%{module}/*.typed
%{python3_sitelib}/%{module}/__pycache__/*.cpython-3*.pyc
%{python3_sitelib}/multipart/*.py
%{python3_sitelib}/multipart/__pycache__/*.cpython-3*.pyc
%doc README.md
%license LICENSE.txt