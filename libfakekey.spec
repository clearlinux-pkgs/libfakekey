#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libfakekey
Version  : 0.3
Release  : 3
URL      : https://git.yoctoproject.org/cgit/cgit.cgi/libfakekey/snapshot/libfakekey-0.3.tar.bz2
Source0  : https://git.yoctoproject.org/cgit/cgit.cgi/libfakekey/snapshot/libfakekey-0.3.tar.bz2
Summary  : X Virtual Keyboard Library
Group    : Development/Tools
License  : GPL-2.0
Requires: libfakekey-lib = %{version}-%{release}
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xtst)

%description


%package dev
Summary: dev components for the libfakekey package.
Group: Development
Requires: libfakekey-lib = %{version}-%{release}
Provides: libfakekey-devel = %{version}-%{release}
Requires: libfakekey = %{version}-%{release}

%description dev
dev components for the libfakekey package.


%package lib
Summary: lib components for the libfakekey package.
Group: Libraries

%description lib
lib components for the libfakekey package.


%prep
%setup -q -n libfakekey-0.3
cd %{_builddir}/libfakekey-0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624658734
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1624658734
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/fakekey/fakekey.h
/usr/lib64/libfakekey.so
/usr/lib64/pkgconfig/libfakekey.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfakekey.so.0
/usr/lib64/libfakekey.so.0.0.1
