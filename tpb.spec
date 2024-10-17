%define	name	tpb
%define	version	0.6.4
%define release	9

Name:		%{name}
Summary:	Program to use the IBM ThinkPad(tm) special keys
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
URL:		https://www.nongnu.org/tpb/
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-8mdv2011.0
+ Revision: 615235
- the mass rebuild of 2010.1 packages

* Tue Dec 15 2009 Frederic Crozat <fcrozat@mandriva.com> 0.6.4-7mdv2010.1
+ Revision: 478998
- Add udev rules to allow non-root user to use tpb (Mdv bug #55660)

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.6.4-6mdv2010.0
+ Revision: 434430
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-5mdv2009.0
+ Revision: 242861
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 04 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.4-3mdv2008.0
+ Revision: 78881
- rebuild
- Import tpb



* Sat Jul 15 2006 Michael Reinsch <mreinsch@mandriva.org> 0.6.4-2mdv2007.0
- no need to patch /etc/modules any more, kernel 2.4 is no longer supported
- do need to patch /etc/security/console.perms any more, configuration for
  /dev/nvram is already present since several releases (now in 
  /etc/security/console.perms.d/50-mandriva.perms)
- no longer bzip2ed patch

* Wed Jan 04 2006 Lenny Cartier <lenny@mandriva.com> 0.6.4-1mdk
- 0.6.4

* Mon Aug 23 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.6.3-1mdk
- 0.6.3
- update patch

* Wed Mar 24 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.6.0-2mdk
- increase polltime to reduce CPU usage under 2.6 kernels (#9193) 
  (thanks to Michael Reinsch)

* Sun Dec 14 2003 Per ?yvind Karlsen <peroyvind@linux-mandrake.com> 0.6.0-1mdk
- 0.6.0
- fix buildrequires (lib64..)

* Mon Jun 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5.1-1mdk
- 0.5.1

* Wed Feb 19 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.2-2mdk
- from Michael Reinsch <mr@uue.org> :
	- add nvram entry to console.perms if required
	- launch it from xinit.d
	- provide a nicer default config

* Tue Feb 18 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.4.2-1mdk
- from Michael Reinsch <mr@uue.org> :
	- add nvram entries to modules.conf if required
	- first mandrake spec file
