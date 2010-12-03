%define version	0.5.3
%define cvs	20080207
%if %cvs
%define release	%mkrel 0.%cvs.3
%else
%define release	%mkrel 5
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
Patch1:		scim-skk-fix-linkage.patch
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
%patch1 -p0

%build
%if %cvs
./bootstrap
%endif

%configure2_5x --disable-rpath --disable-ltdl-install --without-included-ltdl
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%{_libdir}/scim-1.0/1.4.0/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README README.ja
%{_datadir}/scim/icons/*
%{_datadir}/scim/SKK/style/*.sty
%{_libdir}/scim-1.0/1.4.0/IMEngine/*.so
%{_libdir}/scim-1.0/1.4.0/SetupUI/*.so
