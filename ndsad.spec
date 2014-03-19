%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	NDSAD captures traffic information and translates it into Cisco NetFlow format
Name:		ndsad
Version:	1.33
Release:	6
License:	GPLv2+
Group:		Monitoring
Url:		http://www.netup.biz
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/ndsad/ndsad-%{version}.tgz
Source1:	ndsad.init
Patch0:		ndsad.conf.patch
BuildRequires:	pcap-devel
Requires(post,preun):	rpm-helper

%description
The NetUP ndsad utility captures IP-traffic from network interfaces and
export NetFlow v.5. Data is gathered from libpcap library on Unix and
from winpcap on Windows. Also you are able to use tee/divert sockets on
FreeBSD and ULOG on Linux for data source.

%files
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_sbindir}/ndsad
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/ndsad.conf
%attr(644,root,root) %{_mandir}/man5/ndsad.conf.5.*
%attr(700,root,root) %{_sysconfdir}/rc.d/init.d/ndsad

%post
%_post_service ndsad

%preun
%_preun_service ndsad

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
./preconf
%configure2_5x
%make

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
mkdir -p %{buildroot}%{_mandir}/man5
install -c -m 0755 -s ndsad %{buildroot}%{_sbindir}/ndsad
install -c -m 0700 %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/ndsad
install -c -m 0644 ndsad.conf %{buildroot}%{_sysconfdir}/ndsad.conf
install -c -m 0644 ndsad.conf.5 %{buildroot}%{_mandir}/man5/ndsad.conf.5

