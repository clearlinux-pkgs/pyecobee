#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyecobee
Version  : 31f950ee3a104c4ab5bdd7cb788b3d06076ccced
Release  : 14
URL      : https://github.com/sfanous/Pyecobee/archive/31f950ee3a104c4ab5bdd7cb788b3d06076ccced.tar.gz
Source0  : https://github.com/sfanous/Pyecobee/archive/31f950ee3a104c4ab5bdd7cb788b3d06076ccced.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: pyecobee-license = %{version}-%{release}
Requires: pyecobee-python = %{version}-%{release}
Requires: pyecobee-python3 = %{version}-%{release}
Requires: pytz
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pytz
BuildRequires : requests
BuildRequires : six
Patch1: 0001-Updated-runtime-object-from-API-page.patch

%description
Pyecobee: A Python implementation of the `ecobee API <https://www.ecobee.com/home/developer/api/introduction/index.shtml>`_
===========================================================================================================================

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
%setup -q -n Pyecobee-31f950ee3a104c4ab5bdd7cb788b3d06076ccced
cd %{_builddir}/Pyecobee-31f950ee3a104c4ab5bdd7cb788b3d06076ccced
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583206440
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyecobee
cp %{_builddir}/Pyecobee-31f950ee3a104c4ab5bdd7cb788b3d06076ccced/LICENSE %{buildroot}/usr/share/package-licenses/pyecobee/ac588e21dd3076fd0d39cf9633b8e319a30a223d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyecobee/ac588e21dd3076fd0d39cf9633b8e319a30a223d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
