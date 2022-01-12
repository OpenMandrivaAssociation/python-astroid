# Doesn't work because of test cases intentionally containing
# bits that can't be compiled (invalid-encoding.py)
%define _python_bytecompile_errors_terminate_build 0

%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
Version:	2.9.3
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/PyCQA/astroid
Source0:	https://files.pythonhosted.org/packages/2d/be/33923f5dee9f7119abbaa688833b0c71c2ef4b66af3b06ffc64fc8c341ae/astroid-2.9.3.tar.gz
#Patch0:   https://patch-diff.githubusercontent.com/raw/PyCQA/astroid/pull/801.patch
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
 
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
