# Doesn't work because of test cases intentionally containing
# bits that can't be compiled (invalid-encoding.py)
%define _python_bytecompile_errors_terminate_build 0

%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
#USED LATEST GIT: 03.04.2020 to fix 
#conflicting requests - nothing provides (python3.8dist(wrapt) >= 1.11 with python3.8dist(wrapt) < 1.12) needed by python-astroid-2.3.3-4.noarch
Version:	2.4.2
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/PyCQA/astroid
Source0:	https://github.com/PyCQA/astroid/archive/astroid-astrodi-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
 
%description 
A common base representation of python source code for pylint
and other projects

%prep
%setup -qn %{module}-%{module}-%{version}
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST
# Drop python2 dep
rm -rf %{buildroot}%{py_sitedir}/astroid/tests/testdata/python2
rm -rf %{buildroot}%{py_sitedir}/astroid/tests/testdata/python3/data/*py2.5*egg*

rm -rf %{buildroot}%{python3_sitelib}/astroid/tests

%files
%{py_sitedir}/astroid
%{py_sitedir}/astroid*.egg-info
%{python_sitelib}/tests/*
