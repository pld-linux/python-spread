
%define		module	SpreadModule

Summary:	Python extension module wrapping the C API for Spread, an open source group communications package
Name:		python-%{module}
Version:	1.5
Release:	0.1
License:	PSF
Group:		Development/Languages/Python
Source0:	http://www.zope.org/Members/tim_one/spread/SpreadModule-1.5/SpreadModule-1.5.tgz
# Source0-md5:	4c953e0f9f08635fb47dd04a23e222dc
URL:		http://www.zope.org/Members/tim_one/spread/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	spread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python extension module wrapping the C API for Spread, an open source group
communications package.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO* doc.txt
%attr(755,root,root) %{py_sitedir}/*.so
