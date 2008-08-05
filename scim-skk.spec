%define version	0.5.3
%define cvs	20070802
%if %cvs
%define release	%mkrel 0.%cvs.2
%else
%define release	%mkrel 3
%endif

%define scim_version 1.4.2

Name:		scim-skk
Summary:	SCIM IMEngine module for skk
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL+
URL:		http://sourceforge.jp/projects/scim-imengine/
%if %cvs
Source0:	%{name}-%{cvs}.tar.bz2
%else
Source0:	http://prdownloads.sourceforge.jp/scim-imengine/18121/%{name}-%{version}.tar.gz
%endif
Patch0:		scim-skk-gcc4.3.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	scim-client = %{scim_api}
Requires:	skkdic
BuildRequires:	scim-devel >= %{scim_version}
BuildRequires:	automake, libltdl-devel
Obsoletes:	%{mklibname scim-skk 0}

%description
Scim-skk is an SCIM IMEngine module for skk.
It supports Japanese input.

%prep
%if %cvs
%setup -q -n %name
%else
%setup -q
%endif
%patch0 -p0

%build
%if %cvs
autoreconf -i
%endif

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/scim-1.0/1.4.0/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README README.ja
%{_datadir}/scim/icons/*
%{_datadir}/scim/SKK/style/*.sty
%{_libdir}/scim-1.0/1.4.0/IMEngine/*.so
%{_libdir}/scim-1.0/1.4.0/SetupUI/*.so
