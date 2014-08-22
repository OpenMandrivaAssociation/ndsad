%define debug_package %{nil}

Summary:	NDSAD captures traffic information and translates it into Cisco NetFlow format
Name:		ndsad
Version:	1.33
Release:	8
License:	GPLv2+
Group:		Monitoring
Url:		http://www.netup.biz
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/ndsad/ndsad-%{version}.tgz
Source1:	ndsad.service
Patch0:		ndsad.conf.patch
BuildRequires:	pcap-devel
Requires(post,preun):	rpm-helper
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd

%description
The NetUP ndsad utility captures IP-traffic from network interfaces and
export NetFlow v.5. Data is gathered from libpcap library on Unix and
from winpcap on Windows. Also you are able to use tee/divert sockets on
FreeBSD and ULOG on Linux for data source.

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_sbindir}/ndsad
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/ndsad.conf
%attr(644,root,root) %{_mandir}/man5/ndsad.conf.5.*
%{_unitdir}/ndsad.service

%post
%systemd_post ndsad.service

%preun
%systemd_preun ndsad.service

%postun
%systemd_postun_with_restart ndsad.service

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
install -d %{buildroot}%{_unitdir}
install -c -m 0755 -s ndsad %{buildroot}%{_sbindir}/ndsad
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_unitdir}/ndsad.service
install -c -m 0644 ndsad.conf %{buildroot}%{_sysconfdir}/ndsad.conf
install -c -m 0644 ndsad.conf.5 %{buildroot}%{_mandir}/man5/ndsad.conf.5

