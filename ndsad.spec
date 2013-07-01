Summary: Captures traffic information and translates it into Cisco NetFlow format
Name: ndsad
Version: 1.33
Release: %mkrel 5
Source: http://puzzle.dl.sourceforge.net/sourceforge/ndsad/ndsad-%{version}.tgz
Source1: ndsad.init
Patch0: ndsad.conf.patch
License: GPL
URL: http://www.netup.biz
Group: Monitoring
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires: libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The NetUP ndsad utility captures IP-traffic from network interfaces and
export NetFlow v.5. Data is gathered from libpcap library on Unix and
from winpcap on Windows. Also you are able to use tee/divert sockets on
FreeBSD and ULOG on Linux for data source.

%prep
%setup -q
%patch0 -p0

%build
./preconf
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
install -c -m 0755 -s ndsad $RPM_BUILD_ROOT%{_sbindir}/ndsad
install -c -m 0700 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/ndsad
install -c -m 0644 ndsad.conf $RPM_BUILD_ROOT%{_sysconfdir}/ndsad.conf
install -c -m 0644 ndsad.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/ndsad.conf.5

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service ndsad

%preun
%_preun_service ndsad

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README
%attr(755,root,root) %{_sbindir}/ndsad
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/ndsad.conf
%attr(644,root,root) %{_mandir}/man5/ndsad.conf.5.*
%attr(700,root,root) %{_sysconfdir}/rc.d/init.d/ndsad



%changelog
* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.33-5mdv2009.1
+ Revision: 298298
- rebuilt against libpcap-1.0.0

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.33-4mdv2009.0
+ Revision: 253696
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.33-2mdv2008.1
+ Revision: 140994
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 21:58:39 (55197)
- adjust buildrequires

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/09/06 21:50:29 (55191)
Import ndsad

* Wed Mar 01 2006 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 1.33-1mdk
- first package

