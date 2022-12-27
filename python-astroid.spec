# Doesn't work because of test cases intentionally containing
# bits that can't be compiled (invalid-encoding.py)
%define _python_bytecompile_errors_terminate_build 0

%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
Version:	2.12.13
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/PyCQA/astroid
Source0:	https://files.pythonhosted.org/packages/source/a/astroid/astroid-%{version}.tar.gz
#Patch0:   https://patch-diff.githubusercontent.com/raw/PyCQA/astroid/pull/801.patch
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(pip)
 
%description 
A common base representation of python source code for pylint
and other projects

%prep
%setup -qn %{module}-%{version}
%autopatch -p1
  
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
#{python_sitelib}/tests/*
