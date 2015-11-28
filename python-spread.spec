
%define		module	SpreadModule

Summary:	Python wrapper the C API for Spread, an open source group communications package
Summary(pl.UTF-8):	Pythonowy wrapper do API C Spreada - pakietu komunikacji grupowej z otwartymi źródłami
Name:		python-spread
Version:	1.5
Release:	2
License:	PSF
Group:		Development/Languages/Python
Source0:	http://www.zope.org/Members/tim_one/spread/SpreadModule-1.5/SpreadModule-%{version}.tgz
# Source0-md5:	4c953e0f9f08635fb47dd04a23e222dc
URL:		http://www.zope.org/Members/tim_one/spread/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	spread-devel >= 3.17.3-0.2
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python extension module wrapping the C API for Spread, an open source
group communications package.

%description -l pl.UTF-8
Moduł rozszerzenia Pythona obudowujący API C dla Spreada - pakietu
komunikacji grupowej z otwartymi źródłami.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO* doc.txt
%attr(755,root,root) %{py_sitedir}/*.so
