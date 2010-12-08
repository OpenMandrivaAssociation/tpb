%define	name	tpb
%define	version	0.6.4
%define	release	%mkrel 8

Name:		%{name}
Summary:	Program to use the IBM ThinkPad(tm) special keys
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
URL:		http://www.nongnu.org/tpb/
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.xinit
Source2:	90-tpb.rules
Patch0:		%{name}rc.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	xosd-devel >= 2.0

%description
This program enables the IBM Thinkpad(tm) special keys. It is possible to bind
a program to the ThinkPad button. It has a on-screen display (OSD) to show
volume, mute and brightness of the LCD.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/X11/xinit.d
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/X11/xinit.d/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING README CREDITS ChangeLog doc/callback_example.sh
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/X11/xinit.d/tpb
%config(noreplace) %{_sysconfdir}/udev/rules.d/*.rules
%defattr(0644,root,root,0755)
%config(noreplace) %{_sysconfdir}/tpbrc
%{_mandir}/man1/*
