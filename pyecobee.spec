#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyecobee
Version  : 1.2.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/80/da/e9c94a250d344058938a25c6d62f4e25c9eafee00c92f748c00e41aa9363/pyecobee-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/da/e9c94a250d344058938a25c6d62f4e25c9eafee00c92f748c00e41aa9363/pyecobee-1.2.1.tar.gz
Summary  : A Python implementation of the ecobee API
Group    : Development/Tools
License  : MIT
Requires: pyecobee-license = %{version}-%{release}
Requires: pyecobee-python = %{version}-%{release}
Requires: pyecobee-python3 = %{version}-%{release}
Requires: enum34
Requires: pytz
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : enum34
BuildRequires : pytz
BuildRequires : requests
BuildRequires : six
Patch1: build.patch

%description
===========================================================================================================================
        
        Introduction
        ============
        Pyecobee is a simple, elegant, and object oriented implementation of the ecobee API in Python. It is compatible with Python 2.6/2.7/3.3/3.4/3.5/3.6

%package license
Summary: license components for the pyecobee package.
Group: Default

%description license
license components for the pyecobee package.


%package python
Summary: python components for the pyecobee package.
Group: Default
Requires: pyecobee-python3 = %{version}-%{release}

%description python
python components for the pyecobee package.


%package python3
Summary: python3 components for the pyecobee package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyecobee package.


%prep
%setup -q -n pyecobee-1.2.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546121427
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyecobee
cp LICENSE %{buildroot}/usr/share/package-licenses/pyecobee/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyecobee/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
