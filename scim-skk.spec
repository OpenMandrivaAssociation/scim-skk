%define version 0.5.2
%define release %mkrel 4.20060803.1

%define scim_version 1.4.2

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-skk
Summary:	Scim-skk is an SCIM IMEngine module for skk
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://sourceforge.jp/projects/scim-imengine/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:		scim >= %{scim_version}
Requires:		skkdic
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake1.8, libltdl-devel

%description
Scim-skk is an SCIM IMEngine module for skk.
It supports Japanese input.


%package -n %{libname}
Summary:	Scim-skk library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
scim-skk library.


%prep
%setup -q -n %name
cp /usr/share/automake-1.9/mkinstalldirs .

%build
# force to regenerate ltmain.sh
set -x
aclocal-1.9 -I m4
autoheader
libtoolize -c --automake 
automake --add-missing --copy --include-deps
autoconf

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README README.ja
%{_datadir}/scim/icons/*
%{_datadir}/scim/SKK/style/*.sty

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/IMEngine/*.so
%{_libdir}/scim-1.0/SetupUI/*.so


