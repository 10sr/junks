#----------------------------------------------------------
# yum install -y rpmdevtools tar wget
# yum install -y bzip2-devel expat-devel openssl-devel readline-devel sqlite-devel zlib-devel libffi-devel
# yum groupinstall -y "Development Tools"
# useradd rpmbuilder
# su - rpmbuilder
# rpmdev-setuptree || mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
# wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz -O rpmbuild/SOURCES/Python-3.7.7.tgz
# cd rpmbuild/SPECS/
# rpmdev-newspec python37
# vim python37.spec
# rpmbuild -bb --clean python37.spec
#----------------------------------------------------------
#--- GLOBAL-MODIFIABLE CONFIGS ---
#----------------------------------------------------------
%define _topdir             %(echo $HOME)/rpmbuild
%define _smp_mflags         -j3
%define __arch_install_post /usr/lib/rpm/check-buildroot
%define debug_package       %{nil}
%define _unpackaged_files_terminate_build 0
%global _python_bytecompile_errors_terminate_build 0

#----------------------------------------------------------
#--- USER-MODIFIABLE CONFIGS ---
#----------------------------------------------------------
%define name        Python
%define binsuffix   37
%define version     3.7.7
%define libvers     3.7
%define vendor      10sr
%define release     %{vendor}%{?dist}
%define __prefix    /usr/local

#----------------------------------------------------------
#--- SUMMARY ---
#----------------------------------------------------------
Summary: An interpreted, interactive, object-oriented programming language.
Name: %{name}%{binsuffix}
Version: %{version}
Release: %{release}
Vendor: %{vendor}
License: PSF
Group: Development/Languages
Source: https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: glibc-devel
BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: openssl-devel
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: zlib-devel
Prefix: %{__prefix}

%description
Python

%changelog
* Sun Apr 21 2020 10sr <10sr> [3.7.7-1]
- Update to Python 3.7.7
* Sun May 18 2014 mykysyk <mykysyk> [3.7.3-1]
- Initial RPM releas

#----------------------------------------------------------
#--- PREP ---
#----------------------------------------------------------
%prep
%setup -n Python-%{version}

#----------------------------------------------------------
#--- BUILD ---
#----------------------------------------------------------
%build

#--- CONFIGURE
./configure \
    --enable-shared \
    --enable-ipv6 \
    --prefix=%{__prefix}

#--- MAKE
make %{?_smp_mflags}

#----------------------------------------------------------
#--- INSTALL ---
#----------------------------------------------------------
%install

[ -d "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

#--- MAKE INSTALL
make install DESTDIR=$RPM_BUILD_ROOT

rm -f  $RPM_BUILD_ROOT%{__prefix}/bin/2to3*
rm -f  $RPM_BUILD_ROOT%{__prefix}/bin/idle*
rm -f  $RPM_BUILD_ROOT%{__prefix}/bin/pydoc*
rm -f  $RPM_BUILD_ROOT%{__prefix}/bin/easy_install*
rm -rf $RPM_BUILD_ROOT%{__prefix}/lib/pkgconfig
find   $RPM_BUILD_ROOT -type f -print0 |
       xargs -0 grep -l /usr/local/bin/python |
       while read file
       do
          sed -i 's|^#!.*python|#!/usr/bin/env python'"%{libvers}"'|'  $file
       done

mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo "%{__prefix}/lib" > $RPM_BUILD_ROOT/etc/ld.so.conf.d/python%{libvers}.conf

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------
#--- FILES ---
#----------------------------------------------------------
%files
%defattr(-,root,root)
%{__prefix}/bin/python*
%{__prefix}/lib/python%{libvers}/*
%{__prefix}/lib/libpython*
%{__prefix}/include/python%{libvers}m/*.h
%{__prefix}/include/python%{libvers}m/internal/*.h
%{__prefix}/share/man/man1/*
%config(noreplace) /etc/ld.so.conf.d/python%{libvers}.conf
