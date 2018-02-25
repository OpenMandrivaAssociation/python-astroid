%define module	astroid
  
Summary:	Base representation of python source code for pylint and others
Name:		python-astroid
Version:	1.6.1
Release:	1
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

%files
%{py_sitedir}/astroid
%{py_sitedir}/astroid*.egg-info
