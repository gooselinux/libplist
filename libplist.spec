%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           libplist
Version:        1.2
Release:        1%{?dist}
Summary:        Library for manipulating Apple Binary and XML Property Lists

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://matt.colyer.name/projects/iphone-linux/

Source0:        http://cloud.github.com/downloads/JonathanBeck/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: python-devel
BuildRequires: swig
BuildRequires: cmake

%description
libplist is a library for manipulating Apple Binary and XML Property Lists

%package devel
Summary: Development package for libplist
Group: Development/Libraries
Requires: libplist = %{version}-%{release}
Requires: pkgconfig

%description devel
%{name}, development headers and libraries.

%package python
Summary: Python package for libplist
Group: Development/Libraries
Requires: libplist = %{version}-%{release}
Requires: python

%description python
%{name}, python libraries and support

%prep
%setup -q

%build
export CMAKE_PREFIX_PATH=/usr
%{cmake} .

make %{?_smp_mflags}

%install
export CMAKE_PREFIX_PATH=/usr
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER README
%{_bindir}/plutil
%{_bindir}/plutil-%{version}
%{_libdir}/libplist.so.*
%{_libdir}/libplist++.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libplist.pc
%{_libdir}/pkgconfig/libplist++.pc
%{_libdir}/libplist.so
%{_libdir}/libplist++.so
%{_includedir}/plist

%files python
%defattr(-,root,root,-)
%{python_sitearch}/plist

%changelog
* Thu Feb 11 2010 Bastien Nocera <bnocera@redhat.com> 1.2-1
- Update to 1.2
Related: rhbz#563926

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.13-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Peter Robinson <pbrobinson@gmail.com> 0.13-1
- New upstream 0.13 release

* Mon May 11 2009 Peter Robinson <pbrobinson@gmail.com> 0.12-2
- Further review updates

* Sun May 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.12-1
- Update to official tarball release, some review fixes

* Sun May 10 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.0-0.1
- Initial package
