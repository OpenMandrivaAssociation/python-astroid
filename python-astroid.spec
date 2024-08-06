%undefine _debugsource_packages

# Doesn't work because of test cases intentionally containing
# bits that can't be compiled (invalid-encoding.py)
%define _python_bytecompile_errors_terminate_build 0

%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
Version:	3.3.0
Release:	1
Group:		Development/Python
License:	Python
Url:		https://github.com/PyCQA/astroid
Source0:	https://files.pythonhosted.org/packages/source/a/astroid/astroid-%{version}.tar.gz
#Patch0:   https://patch-diff.githubusercontent.com/raw/PyCQA/astroid/pull/801.patch
BuildArch:	noarch 
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(pip)
 
%description 
A common base representation of python source code for pylint
and other projects

%prep
%autosetup -p1 -n %{module}-%{version}
  
%build
%py_build

%install 
%py_install

%files
%{py_sitedir}/astroid
%{py_sitedir}/astroid*.*-info
#{python_sitelib}/tests/*
