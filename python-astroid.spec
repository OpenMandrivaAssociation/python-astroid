# Doesn't work because of test cases intentionally containing
# bits that can't be compiled (invalid-encoding.py)
%define _python_bytecompile_errors_terminate_build 0

%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
Version:	2.1.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/PyCQA/astroid
Source0:	https://pypi.io/packages/source/a/astroid/astroid-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
A common base representation of python source code for pylint
and other projects

%prep
%setup -qn %{module}-%{module}-%{version}
  
%build
%__%py_build

%install 
%__%py_install --record=FILE_LIST
# Drop python2 dep
rm -rf %{buildroot}%{py_puresitedir}/astroid/tests/testdata/python2
rm -rf %{buildroot}%{py_puresitedir}/astroid/tests/testdata/python3/data/*py2.5*egg*

%files
%{py_puresitedir}/astroid
%{py_puresitedir}/astroid*.egg-info
