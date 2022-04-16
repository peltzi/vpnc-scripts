Name:		vpnc-scripts
Version:	0.1~git20220305
Release:	1

Summary:	Routing setup script for vpnc and openconnect
Group:		Productivity/Networking/Other
BuildArch:	noarch
Requires:	iproute
Requires:	which
# Compatibility with Fedora package
Provides:	vpnc-script = %{version}

License:	GPL-2.0-or-later
URL:		https://gitlab.com/openconnect/vpnc-scripts/
Source:		https://gitlab.com/openconnect/vpnc-scripts/-/archive/master/vpnc-scripts-%{version}.tar.gz

%description
This script sets up routing for VPN connectivity, when invoked by vpnc
or openconnect.

%prep
%setup -q

%build

%install
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/vpnc
install -m 0755 vpnc-script \
    %{buildroot}%{_sysconfdir}/vpnc/vpnc-script
install -m 0755 vpnc-script-sshd \
    %{buildroot}%{_sysconfdir}/vpnc/vpnc-script-sshd

%files
%dir %{_sysconfdir}/vpnc
%{_sysconfdir}/vpnc/vpnc-script
%{_sysconfdir}/vpnc/vpnc-script-sshd

%changelog
* Sat Apr 16 2022 OpenConnect Team <openconnect-devel@lists.infradead.org> - 0.1~git20220305
- Import from Fedora

