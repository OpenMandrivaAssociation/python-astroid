# Doesn't work because of test cases intentionally containing
# bits that can't be compiled (invalid-encoding.py)
%define _python_bytecompile_errors_terminate_build 0

%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
Version:	2.3.3
Release:	2
Group:		Development/Python
License:	Python
Url:		https://github.com/PyCQA/astroid
Source0:	https://github.com/PyCQA/astroid/archive/astroid-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
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

%files
%{py_sitedir}/astroid
%{py_sitedir}/astroid*.egg-info
